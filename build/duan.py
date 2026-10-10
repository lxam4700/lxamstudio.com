#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh trang case study cho từng dự án: du-an-<slug>.html

Thêm dự án mới = thêm một dict vào PROJECTS rồi chạy lại file này.
Ảnh để trong site/assets, nên nén sang .webp bề ngang 1600-1800px.
"""

import os, json, datetime, html as H

# --- auto width/height cho ảnh, doc header anh bang pure python ---
import struct as _struct, os as _os
_DIM_CACHE = {}

def imgdim(src):
    """Tra ve chuoi ' width="W" height="H"' doc tu header file anh, rong neu khong doc duoc."""
    if src in _DIM_CACHE:
        return _DIM_CACHE[src]
    out = ""
    for base in (".", "..", _os.path.join(_os.path.dirname(__file__), "..")):
        path = _os.path.join(base, src)
        if _os.path.isfile(path):
            wh = _read_wh(path)
            if wh:
                out = ' width="%d" height="%d"' % wh
            break
    _DIM_CACHE[src] = out
    return out

def _read_wh(path):
    try:
        with open(path, "rb") as f:
            head = f.read(32)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                return _struct.unpack(">II", head[16:24])
            if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
                ck = head[12:16]
                if ck == b"VP8 ":
                    return (_struct.unpack("<H", head[26:28])[0] & 0x3FFF,
                            _struct.unpack("<H", head[28:30])[0] & 0x3FFF)
                if ck == b"VP8L":
                    b = _struct.unpack("<I", head[21:25])[0]
                    return ((b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1)
                if ck == b"VP8X":
                    w = head[24] | head[25] << 8 | head[26] << 16
                    h = head[27] | head[28] << 8 | head[29] << 16
                    return (w + 1, h + 1)
                return None
            if head[:2] == b"\xff\xd8":
                f.seek(2)
                while True:
                    b = f.read(1)
                    if not b:
                        return None
                    if b != b"\xff":
                        continue
                    while b == b"\xff":
                        b = f.read(1)
                    m = b[0]
                    if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
                        continue
                    ln = _struct.unpack(">H", f.read(2))[0]
                    if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                        d = f.read(5)
                        return (_struct.unpack(">H", d[3:5])[0],
                                _struct.unpack(">H", d[1:3])[0])
                    f.seek(ln - 2, 1)
    except Exception:
        return None
    return None
# --- het khoi auto width/height ---


SITE = "/home/claude/site"
YEAR = datetime.date.today().year

NAV = (
    '<a href="ve-chung-toi.html">Về chúng tôi</a>'
    '<a href="index.html#portfolio" class="is-active">Portfolio</a>'
    '<a href="blog.html">Blog</a>'
    '<a href="hoc-vien.html">Khu học viên</a>'
    '<a href="index.html#lienhe">Liên hệ</a>'
    '<a href="khoa-hoc.html">Khóa học</a>'
    '<a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>'
)
DRAWER = (
    '<a href="ve-chung-toi.html">Về chúng tôi</a>'
    '<a href="index.html#portfolio">Portfolio</a>'
    '<a href="cam-nang.html">Cẩm nang</a>'
    '<a href="blog.html">Blog</a>'
    '<a href="hoc-vien.html">Khu học viên</a>'
    '<a href="index.html#lienhe">Liên hệ</a>'
    '<a href="khoa-hoc.html">Khóa học</a>'
    '<a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>'
    '<a href="lo-trinh.html">Lộ trình &amp; học phí</a>'
)

# ------------------------------------------------------------------ DỮ LIỆU
PROJECTS = [
    {
        "slug": "vplas",
        "title": "VPLAS: TVC thiết bị plasma",
        "client": "VPLAS",
        "year": "2025",
        "role": "Concept · Modeling · Lighting · Animation · VFX · Hậu kỳ",
        "tools": "Blender · Premiere Pro",
        "deliver": "TVC chiếu màn LED 10,5 × 3 m · bộ ảnh sản phẩm",
        "desc": ("Dựng và làm TVC cho thiết bị plasma VPLAS: từ file CAD tới bản dựng 3D hoàn chỉnh, "
                 "10 phân cảnh, hiệu ứng tia plasma và bộ ảnh sản phẩm cho truyền thông."),
        "hero": "assets/vplas-exploded-view-blender.jpg",
        "hero_alt": "Ảnh tách rời linh kiện thiết bị plasma VPLAS dựng bằng Blender",
        "intro": (
            "VPLAS là thiết bị plasma cầm tay do một đơn vị Việt Nam sản xuất. Họ cần một TVC chiếu trên "
            "màn LED khổ lớn tại sự kiện ra mắt, cộng một bộ ảnh sản phẩm dùng cho truyền thông sau đó. "
            "Toàn bộ hình ảnh dựng 3D, không quay thực tế, vì lúc làm sản phẩm còn chưa lên dây chuyền."
        ),
        "challenge_h": "Bài toán",
        "challenge": [
            ("Chưa có sản phẩm thật để quay",
             "Chỉ có file CAD và vài ảnh mẫu thử. Mọi chi tiết bề mặt, khe hở, độ bo cạnh đều phải dựng lại "
             "cho đúng với thứ sẽ xuất xưởng. Sai một chi tiết là khách nhận ra ngay."),
            ("Màn LED 10,5 × 3 mét",
             "Tỉ lệ rất rộng và người xem đứng gần. Bố cục phải đọc được ở khoảng cách ba mét, "
             "còn chi tiết bề mặt phải chịu được độ phân giải lớn mà không vỡ."),
            ("Kim loại đánh bóng trên nền tối",
             "Chất liệu khó nhất để render sạch. Không có gì xung quanh để phản chiếu thì bề mặt sẽ "
             "chết màu, còn phản chiếu quá tay thì mất form."),
        ],
        "gallery": [
            ("assets/vplas-render-san-pham-blender.jpg",
             "Shot sản phẩm chính: thiết bị VPLAS bản bạc trên nền tối",
             "Shot chủ đạo",
             "Một nguồn sáng chính đặt chếch trên, hai mặt hắt trắng hai bên để giữ chuyển sáng dọc "
             "thân máy. Vệt sáng chạy dọc cạnh là thứ nói cho mắt biết đây là kim loại gia công chứ không phải nhựa."),
            ("assets/vplas-exploded-view-blender.jpg",
             "Shot tách rời toàn bộ linh kiện bên trong thiết bị VPLAS",
             "Tách lớp linh kiện",
             "Cảnh khó nhất về sắp xếp. Hơn ba mươi chi tiết phải bung ra theo đúng thứ tự lắp ráp, "
             "đủ thưa để đọc được nhưng vẫn nằm gọn trong khung. Bo mạch và các chi tiết nhỏ dựng riêng từng cái."),
            ("assets/vplas-lot-xac.webp",
             "Phân cảnh máy bản đen chuyển thành bản bạc",
             "Cảnh chuyển màu",
             "Yêu cầu của khách là “máy lột xác”. Xử lý bằng cách cho lớp vỏ đen tan dần theo một mặt cắt "
             "chạy dọc thân, để lộ bản bạc bên dưới. Chuyển động phải chậm vừa đủ để mắt kịp đọc."),
            ("assets/vplas-che-do-auto.webp",
             "Cận cảnh logo AUTO phát sáng cùng dải đèn LED 5 mức",
             "Chế độ AUTO",
             "Dải LED năm mức và logo AUTO là điểm bán hàng chính. Ánh sáng xanh đến từ chính dải đèn "
             "trong cảnh, không phải đèn ngoài, nhờ vậy vệt sáng đổ lên bề mặt kim loại mới đúng hướng."),
            ("assets/vplas-tia-plasma-can.webp",
             "Cận cảnh tia plasma phóng ra từ đầu kim của thiết bị",
             "Tia plasma",
             "Cao trào của TVC. Tia dựng bằng hệ thống hạt kết hợp phát sáng, chạy thử hàng chục lần mới "
             "ra được nhịp giật đúng kiểu phóng điện thật thay vì trông như tia sét hoạt hình."),
            ("assets/vplas-cong-sac-chi-tiet.webp",
             "Cận cảnh cổng sạc USB-C và đèn báo trên thân máy",
             "Chi tiết cổng sạc",
             "Shot chứng minh chất lượng gia công. Ở cỡ này mọi khe hở đều lộ, nên phần bo cạnh và "
             "khoảng cách giữa các chi tiết phải khớp bản vẽ kỹ thuật."),
            ("assets/vplas-ban-ve-kich-thuoc-3d.jpg",
             "Bản vẽ kích thước thiết bị VPLAS: 17,4 cm chiều dài, 2,9 cm bề ngang",
             "Bản vẽ kích thước",
             "Khách cần một hình thể hiện kích thước thật để đưa vào tài liệu bán hàng. "
             "Cùng file dựng, chỉ đổi góc máy và thêm lớp chú thích."),
            ("assets/vplas-hai-may.webp",
             "Hai phiên bản thiết bị VPLAS bạc và đen trong cảnh kết",
             "Cảnh kết",
             "Hai bản máy hạ xuống như tàu vũ trụ, ý tưởng đến từ chính kịch bản của khách. "
             "Tia plasma phát dần khi chạm đất, dẫn vào slogan."),
        ],
        "process_h": "Cách làm",
        "process": [
            ("01", "Đọc brief và chốt đường hình",
             "Khách gửi kịch bản kèm thông điệp từng cảnh. Việc đầu tiên là chốt bố cục và góc máy ở "
             "dạng khối xám, trước khi đụng tới chi tiết. Duyệt ở bước này mất một ngày, duyệt sau khi "
             "render xong mất một tuần."),
            ("02", "Dựng từ file CAD",
             "File STEP của khách nhập vào rồi dựng lại phần vỏ cho sạch topology. CAD cho đúng kích "
             "thước nhưng lưới không dùng trực tiếp để render được."),
            ("03", "Ánh sáng trước, vật liệu sau",
             "Toàn bộ cảnh dựng sáng khi vật thể còn là chất xám trung tính. Ánh sáng đúng ở trạng thái "
             "xám thì gần như chắc chắn đúng khi có vật liệu."),
            ("04", "Render tách lớp",
             "Mỗi cảnh xuất riêng sản phẩm, nền, bóng đổ, phản chiếu và lớp phát sáng. Khi khách yêu cầu "
             "chỉnh nền tối hơn thì sửa trong vài phút thay vì render lại vài tiếng."),
            ("05", "Dựng phim và hoàn thiện",
             "Ghép mười phân cảnh, chỉnh màu tổng thể, thêm nhạc và hiệu ứng âm thanh, xuất đúng tỉ lệ "
             "màn LED của địa điểm tổ chức."),
        ],
        "stats": [("10", "Phân cảnh"), ("30+", "Chi tiết dựng riêng"), ("10,5m", "Bề ngang màn LED")],
    },
    {
        "slug": "jhm-masonry-hanger",
        "title": "JHM Masonry Hanger: TVC kỹ thuật",
        "client": "Simpson Strong-Tie · bài dự tuyển 3D Artist",
        "year": "2026",
        "role": "Modeling · Vật liệu · Lighting · Animation · SFX · Dựng phim",
        "tools": "Blender · Premiere Pro",
        "deliver": "TVC 46 giây, 1920×1080",
        "desc": ("TVC kỹ thuật 46 giây cho móc treo JHM Masonry Hanger của Simpson Strong-Tie: dựng từ "
                 "file CAD, thép mạ kẽm, cánh tay robot và chú thích kỹ thuật."),
        "hero": "assets/jhm-khoi-kinh-ky-thuat.webp",
        "hero_alt": "Móc treo JHM Masonry Hanger trong khối kính kỹ thuật, dựng bằng Blender",
        "intro": (
            "JHM Masonry Hanger là móc treo thép dùng trong xây dựng, một chi tiết kim loại nhỏ, "
            "không màu mè, mà vẫn phải làm cho ra được cảm giác chắc chắn và chính xác. Đề bài: một TVC "
            "kỹ thuật dưới một phút, đủ để người kỹ sư nhìn hiểu sản phẩm làm bằng gì và lắp ra sao."
        ),
        "challenge_h": "Bài toán",
        "challenge": [
            ("Sản phẩm không có gì để khoe",
             "Một miếng thép gập. Không màu, không đèn, không chuyển động. Toàn bộ sức hấp dẫn phải đến "
             "từ ánh sáng, góc máy và nhịp dựng, chứ bản thân vật thể không tự gánh được khung hình."),
            ("Thép mạ kẽm rất khó render",
             "Bề mặt vừa phản chiếu vừa nhám, lại xám hoàn toàn. Làm bóng quá thì thành inox, làm mờ quá "
             "thì thành nhựa. Phải tìm đúng khoảng giữa, và giữ nguyên khoảng đó qua mọi cảnh."),
            ("Vừa phải đẹp vừa phải đúng kỹ thuật",
             "Khách là hãng vật tư xây dựng, người xem là kỹ sư. Lỗ bắt vít, độ dày tôn, vị trí gân tăng "
             "cứng đều phải khớp bản vẽ. Không được làm đẹp bằng cách sửa hình dáng sản phẩm."),
        ],
        "gallery": [
            ("assets/jhm-title-card.webp",
             "Cảnh mở đầu TVC JHM Masonry Hanger với chữ tiêu đề trên nền tối",
             "Cảnh mở",
             "Sân khấu tối, hai khối đèn hai bên, sàn lưới kỹ thuật. Sản phẩm chưa xuất hiện, "
             "để khoảng lặng ba giây cho người xem ổn định mắt trước khi vào nội dung."),
            ("assets/jhm-canh-tay-robot.webp",
             "Cánh tay robot đặt móc treo JHM xuống bệ trong TVC",
             "Cánh tay robot",
             "Cần một chuyển động để dẫn sản phẩm vào khung. Cánh tay robot vừa giải quyết việc đó, "
             "vừa gợi đúng ngữ cảnh công nghiệp mà không cần lời thoại nào."),
            ("assets/jhm-silhouette.webp",
             "Bóng ngược sáng của móc treo JHM làm nổi đường viền sản phẩm",
             "Ngược sáng",
             "Đặt nguồn sáng phía sau để lấy riêng đường viền. Với vật thể xám, đây là cách nhanh nhất "
             "cho người xem đọc được hình dáng trước khi đi vào chi tiết bề mặt."),
            ("assets/jhm-mat-truoc.webp",
             "Móc treo JHM nhìn chính diện, thấy rõ hai cánh và gân tăng cứng",
             "Chính diện",
             "Góc kỹ thuật thuần tuý: hai cánh, gân tăng cứng, mặt bích. Ánh sáng dịu lại để không có "
             "vệt chói nào che mất đường gập."),
            ("assets/jhm-chi-tiet-lo-bat.webp",
             "Cận cảnh mặt trên móc treo JHM với các lỗ bắt vít",
             "Cận mặt bích",
             "Ở cỡ này mọi thứ đều lộ: mép cắt, độ dày tôn, bo góc lỗ. Đây là shot chứng minh phần dựng "
             "hình bám đúng bản vẽ chứ không phải dựng phỏng chừng."),
            ("assets/jhm-chu-thich-lo-vua.webp",
             "Lớp chú thích kỹ thuật chỉ vào các lỗ giữ vữa trên móc treo JHM",
             "Lớp chú thích: lỗ giữ vữa",
             "Chú thích dựng ngay trong Blender chứ không dán ở hậu kỳ, nên đường chỉ bám đúng vị trí "
             "khi camera di chuyển. Đây là phần khiến TVC kỹ thuật khác với TVC quảng cáo thường."),
            ("assets/jhm-chu-thich-thep-ma-kem.webp",
             "Chú thích vật liệu thép mạ kẽm trên móc treo JHM Masonry Hanger",
             "Lớp chú thích: vật liệu",
             "Thông tin vật liệu là thứ kỹ sư tìm đầu tiên. Đặt nó ở giữa video, lúc người xem đã nhìn "
             "đủ hình dáng và bắt đầu hỏi “làm bằng gì”."),
            ("assets/jhm-khoi-kinh-ky-thuat.webp",
             "Móc treo JHM đặt trong khối kính kỹ thuật trong suốt",
             "Khối kính",
             "Cảnh kết. Đặt sản phẩm trong khối kính để gợi ý sự chuẩn xác, đồng thời là cái cớ hợp lý "
             "để thêm một lớp phản chiếu, thứ mà cảnh xám suốt 40 giây đang thiếu."),
        ],
        "process_h": "Cách làm",
        "process": [
            ("01", "Từ file CAD sang lưới render được",
             "Khách cấp file STEP và OBJ. CAD cho đúng kích thước nhưng lưới tam giác vụn, bo cạnh vỡ, nên "
             "phải dựng lại phần vỏ để bevel bắt sáng sạch."),
            ("02", "Chốt vật liệu trước khi dựng cảnh",
             "Làm riêng một file thử vật liệu, so nhiều mức nhám cạnh nhau dưới cùng một đèn. "
             "Chốt xong mới mang sang các cảnh, để thép trông giống nhau từ đầu tới cuối."),
            ("03", "Dựng sân khấu dùng chung",
             "Một sân khấu tối với sàn lưới và hai khối đèn, dùng lại cho mọi cảnh. Nhờ vậy các shot "
             "cắt vào nhau không bị lệch tông, và đỡ phải dựng sáng lại từ đầu."),
            ("04", "Chú thích dựng trong 3D",
             "Chữ và đường chỉ là vật thể thật trong cảnh, gắn vào điểm trên sản phẩm. Camera chạy thì "
             "chú thích chạy theo đúng phối cảnh. Dán ở hậu kỳ sẽ trôi."),
            ("05", "Dựng phim và âm thanh",
             "Ghép theo nhịp: mở chậm, giữa nhanh, kết chậm lại. Hiệu ứng âm thanh cánh tay robot và "
             "tiếng giao diện kỹ thuật đặt đúng khung hình để cú cắt có trọng lượng."),
        ],
        "stats": [("46s", "Thời lượng"), ("8", "Phân cảnh"), ("1080p", "Độ phân giải")],
    },
    {
        "slug": "chivas-18",
        "title": "Chivas Regal 18 × Touliver: Phối cảnh triển lãm",
        "client": "Chivas Regal 18 × Touliver",
        "year": "2025",
        "role": "Dựng 3D phối cảnh · Ánh sáng · Render duyệt",
        "tools": "Blender",
        "deliver": "Phối cảnh nội thất + mặt bằng isometric và top-down",
        "back": "du-an-event.html",
        "back_label": "Khu Event",
        "title_seo": "Chivas Regal 18 × Touliver: Phối cảnh 3D | LXAM",
        "desc": ("Phối cảnh 3D dựng trước cho triển lãm Chivas Regal 18 × Touliver “Transformed to Rise”: toàn cảnh sảnh, màn LED chính và ba bản mặt bằng để duyệt sớm."),
        "hero": "assets/chivas18-phoi-canh-tong-the-man-led.webp",
        "hero_alt": "Phối cảnh 3D sảnh triển lãm Chivas Regal 18 với màn LED lớn và các khối ghế xanh",
        "intro": (
            "Trước khi dựng một triển lãm thật, người ta phải nhìn thấy nó đã. Đây là bộ phối cảnh 3D "
            "dựng cho triển lãm Chivas Regal 18 \u00d7 Touliver, \u201cTransformed to Rise\u201d, "
            "khai mạc 18.03.2025 tại Trung tâm Nghệ thuật Đương đại Vincom. Toàn bộ là hình dựng, "
            "chưa có gì được thi công ở thời điểm render."
        ),
        "meta_rows": [
            ("Thương hiệu", "Chivas Regal 18 × Touliver"),
            ("Sự kiện", "“Transformed to Rise”, 18.03.2025"),
            ("Địa điểm", "Trung tâm Nghệ thuật Đương đại Vincom"),
            ("Vai trò", "Dựng 3D phối cảnh · Ánh sáng · Render duyệt"),
            ("Công cụ", "Blender"),
            ("Loại hình", "Phối cảnh duyệt trước thi công"),
        ],
        "challenge_h": "Bài toán",
        "chal_title": "Vì sao phải dựng trước",
        "challenge": [
            ("Duyệt bố cục khi phòng còn trống",
             "Sảnh triển lãm là một mặt bằng chữ thập, trần lưới sáng, tường trắng. Muốn biết bao nhiêu "
             "khối ghế là vừa, tranh treo cách nhau bao xa, phải đặt thử trong 3D chứ không đo trên giấy được."),
            ("Màn LED là điểm nhìn đầu tiên",
             "Bức tường LED chạy hết một mặt phòng, khách bước vào là thấy ngay. Phải dựng đúng tỉ lệ để "
             "biết dòng chữ và chân dung nằm ở tầm mắt, không bị khối ghế phía trước che."),
            ("Luồng đi phải thấy từ trên xuống",
             "Bố cục đẹp ở tầm mắt vẫn có thể tắc khi trăm người cùng đứng. Ba bản mặt bằng isometric và "
             "top-down là để nhìn ra chỗ nghẽn trước khi vật tư lên xe."),
        ],
        "shots_title": "Năm bản dựng",
        "gallery": [
            ("assets/chivas18-phoi-canh-tong-the-man-led.webp",
             "Phối cảnh 3D toàn cảnh sảnh triển lãm Chivas 18, màn LED bên trái và dãy tranh bên phải",
             "Toàn cảnh sảnh",
             "Góc nhìn của người vừa bước vào: màn LED chiếm trọn mảng tường trái, dãy tranh chạy dọc "
             "tường phải, khối ghế rải giữa sàn. Đây là bản dùng để chốt mật độ ghế."),
            ("assets/chivas18-man-led-chinh-dien.webp",
             "Phối cảnh chính diện màn LED triển lãm Chivas Regal 18 × Touliver",
             "Màn LED chính diện",
             "Dựng thẳng mặt để kiểm tra tỉ lệ nội dung trên màn: chân dung, dòng “Transformed to Rise” "
             "và hai dải hoa văn hai bên. Nhìn thẳng mới biết chữ có bị khối ghế cắt ngang không."),
            ("assets/chivas18-mat-bang-isometric-1.webp",
             "Mặt bằng isometric triển lãm Chivas 18 nhìn từ góc thứ nhất",
             "Mặt bằng isometric, góc 1",
             "Cắt trần, nhìn chéo xuống. Kiểu hình này dễ đọc hơn bản vẽ 2D với người không quen xem "
             "bản vẽ: thấy được cả vị trí lẫn chiều cao từng hạng mục."),
            ("assets/chivas18-mat-bang-isometric-2.webp",
             "Mặt bằng isometric triển lãm Chivas 18 nhìn từ góc đối diện",
             "Mặt bằng isometric, góc 2",
             "Cùng mặt bằng, xoay sang phía đối diện để lộ nhánh hành lang bên kia, phần bị khuất "
             "hoàn toàn ở góc thứ nhất."),
            ("assets/chivas18-mat-bang-tu-tren-xuong.webp",
             "Mặt bằng nhìn từ trên xuống của triển lãm Chivas 18",
             "Mặt bằng từ trên xuống",
             "Bản cuối để đo khoảng cách thật. Khối ghế rải theo cụm chứ không xếp hàng, chừa lối đi "
             "chéo từ cửa vào tới màn LED."),
        ],
        "process_h": "Cách làm",
        "proc_title": "Bốn bước",
        "process": [
            ("01", "Dựng vỏ phòng theo mặt bằng thật",
             "Tường, trần lưới sáng, cột và các nhánh hành lang dựng đúng kích thước trước. Mọi thứ "
             "đặt sau đó chỉ đáng tin nếu cái hộp này đúng."),
            ("02", "Đặt hạng mục rồi thử lại",
             "Màn LED, tranh, khối ghế, bục trưng bày. Đặt xong nhìn lại từ cửa vào, cái gì che cái gì "
             "thì dời, chứ không giữ vì đã dựng."),
            ("03", "Ánh sáng theo đèn có thật",
             "Trần lưới của địa điểm là nguồn sáng chính. Dựng đúng nó thì phối cảnh mới ra được cảm giác "
             "của phòng thật, thay vì một bản render sáng đều kiểu catalogue."),
            ("04", "Xuất hai nhóm hình cho hai người xem",
             "Phối cảnh tầm mắt cho bên thương hiệu duyệt cảm giác; mặt bằng isometric và top-down cho "
             "bên thi công đo và chia việc."),
        ],
        "stats": [("5", "Bản dựng"), ("3", "Mặt bằng"), ("2025", "Năm")],
    },
    {
        "slug": "trien-lam-axe",
        "title": "AXEHIBITION: Hương trong “Ảnh”",
        "client": "AXE",
        "year": "2024",
        "role": "Ảnh ghi nhận triển lãm",
        "tools": "Nhiếp ảnh",
        "deliver": "Bộ ảnh ghi nhận toàn bộ tuyến tham quan",
        "back": "du-an-event.html",
        "back_label": "Khu Event",
        "desc": ("AXEHIBITION “Hương trong Ảnh” là triển lãm hương thơm đa giác quan của AXE, "
                 "khai mạc 5.10.2024. Bộ ảnh ghi nhận toàn bộ tuyến tham quan và từng khu mùi hương."),
        "hero": "assets/axehibition-toan-canh-khoi-dau-nguoi.webp",
        "hero_alt": "Toàn cảnh triển lãm AXEHIBITION với khối điêu khắc đầu người ở trung tâm",
        "intro": (
            "AXEHIBITION “Hương trong Ảnh” là triển lãm hương thơm đa giác quan của AXE, mở cửa từ "
            "5.10.2024. Ý tưởng: mỗi mùi hương được dựng thành một không gian có thể bước vào, thay vì "
            "một chai đặt trong tủ kính. Đây là bộ ảnh ghi nhận triển lãm sau khi đã thi công xong."
        ),
        "meta_rows": [
            ("Thương hiệu", "AXE"),
            ("Thời gian", "Từ 5.10.2024"),
            ("Địa điểm", "NEXT 600"),
            ("Ghi nhận trên bảng credit", "AXE · Square · Zee"),
            ("Nội dung", "Ảnh thực tế, không phải hình dựng 3D"),
        ],
        "challenge_h": "Ý tưởng",
        "chal_title": "Ba lớp của triển lãm",
        "challenge": [
            ("Mùi dịch sang hình",
             "Mỗi mùi được gán một màu, một chất liệu và một bối cảnh: Purple Patchouli tím, "
             "Golden Mango vàng truyện tranh, Fire Santal cỏ khô và xe mô tô. Khách nhớ mùi bằng hình "
             "trước khi ngửi."),
            ("Bảy khu, một tuyến",
             "Các khu không đặt rời mà nối thành một đường đi: dẫn nhập ở lối vào, các khu mùi hai bên, "
             "tường chiếu ở giữa, quầy bar khép lại ở cuối."),
            ("Một điểm neo ở giữa",
             "Khối điêu khắc đầu người đặt chính giữa sảnh, có khói và đèn quét. Đứng ở bất kỳ khu nào "
             "cũng thấy nó, nên không ai bị lạc hướng trong một không gian tối."),
        ],
        "shots_title": "Đi hết một vòng",
        "gallery": [
            ("assets/axehibition-loi-vao-trien-lam.webp",
             "Lối vào triển lãm AXEHIBITION với bảng tên Hương trong Ảnh",
             "Lối vào",
             "Hành lang trắng, thảm xám, một mảng tường đen duy nhất mang tên triển lãm. Cố tình sáng "
             "và trống, để bước qua cửa vào phòng tối là một cú chuyển hẳn."),
            ("assets/axehibition-bang-gioi-thieu.webp",
             "Bảng dẫn nhập AXEHIBITION Hương trong Ảnh",
             "Bảng dẫn nhập",
             "Đặt ngay sau cửa, giải thích “hương trong ảnh” nghĩa là gì trước khi khách đi tiếp. "
             "Một triển lãm khái niệm mà thiếu đoạn này thì nửa số khách sẽ chỉ chụp ảnh rồi về."),
            ("assets/axehibition-toan-canh-khoi-dau-nguoi.webp",
             "Toàn cảnh sảnh chính AXEHIBITION với khối đầu người và toa tàu điện",
             "Sảnh chính",
             "Nhìn từ đầu sảnh: khối đầu người ở giữa, toa tàu điện AXE bên trái, khu Fire Santal với "
             "xe mô tô bên phải. Đèn quét màu tím và xanh giữ cả phòng trong một tông."),
            ("assets/axehibition-khoi-dau-nguoi-khoi-suong.webp",
             "Khối điêu khắc đầu người phủ khói tại trung tâm triển lãm AXE",
             "Khối trung tâm",
             "Góc thấp hơn, thấy rõ lớp khói dưới chân khối. Khói làm luồng đèn hiện thành tia, "
             "thứ giữ cho một khối tĩnh không bị chìm trong phòng tối."),
            ("assets/axehibition-tuong-chieu-charming.webp",
             "Tường chiếu CHARMING với hiệu ứng hạt bay tại triển lãm AXE",
             "Tường chiếu “Charming”",
             "Hai mảng tường gập góc, chiếu cùng một nội dung nên hạt bay có vẻ xuyên qua góc phòng. "
             "Đây là khu khách đứng lâu nhất."),
            ("assets/axehibition-khu-purple-patchouli.webp",
             "Hộp đèn khu Purple Patchouli tại triển lãm AXE",
             "Purple Patchouli",
             "Hộp đèn tím với các bàn tay và chiếc cúp, dịch mùi hoắc hương thành một hình ảnh chiến "
             "thắng. Mỗi khu mùi đều có một hộp đèn như vậy làm mặt tiền."),
            ("assets/axehibition-khu-golden-mango.webp",
             "Khu Golden Mango với cuốn truyện tranh khổ lớn tại triển lãm AXE",
             "Golden Mango",
             "Một cuốn truyện tranh mở khổ lớn, các trang rời bay lên trần. Khu duy nhất dùng nét vẽ "
             "thay vì vật liệu thật, ở đây mùi ngọt được kể như một mẩu chuyện."),
            ("assets/axehibition-khu-spiced-latte.webp",
             "Khu Spiced Latte dạng cuốn sách mở tại triển lãm AXE",
             "Spiced Latte",
             "Cũng là hình cuốn sách mở nhưng tông gỗ và nâu, gáy sách xếp thành dãy. Cùng một ngôn ngữ "
             "hình với Golden Mango, khác chất liệu, nên đi liền nhau vẫn không lặp."),
            ("assets/axehibition-khu-fire-santal.webp",
             "Khu Fire Santal với xe mô tô và cỏ khô tại triển lãm AXE",
             "Fire Santal",
             "Xe mô tô đặt trong đám cỏ pampas khô, tủ gỗ và đèn vàng phía sau. Khu ấm nhất trong một "
             "triển lãm toàn tím và xanh, nên nó tự hút mắt từ xa."),
            ("assets/axehibition-tu-trung-bay-mui-huong.webp",
             "Tủ trưng bày các mùi hương AXE với hốc đèn thẳng đứng",
             "Tủ mùi hương",
             "Dãy hốc đèn thẳng đứng, mỗi hốc một tiểu cảnh nguyên liệu. Cách trưng bày này cho phép "
             "so sánh các mùi cạnh nhau, thứ mà đi từng khu riêng không làm được."),
            ("assets/axehibition-tuong-nha-che-huong.webp",
             "Tường giới thiệu các nhà chế hương của AXE",
             "Tường nhà chế hương",
             "Chân dung và tiểu sử những người pha ra các mùi này. Phần ít ai chụp nhưng là chỗ duy nhất "
             "nói rằng mùi hương có tác giả."),
            ("assets/axehibition-booth-dj.webp",
             "Booth DJ mang logo AXE tại triển lãm",
             "Booth DJ",
             "Đặt dựa vào tường hốc đèn, dùng luôn mảng sáng sẵn có làm phông. Triển lãm ban ngày, "
             "sự kiện ban đêm, vẫn cùng một không gian."),
            ("assets/axehibition-khu-bar-cuoi-trien-lam.webp",
             "Khu bar cuối triển lãm AXE với ghế trong suốt và quầy đèn hồng",
             "Quầy bar cuối tuyến",
             "Điểm kết: quầy đèn hồng, ghế nhựa trong suốt bắt đèn xanh. Sau khi đi hết các khu mùi, "
             "khách cần một chỗ ngồi xuống, chứ không phải thêm một thứ để xem."),
            ("assets/axehibition-khach-moi-khai-mac.webp",
             "Khách mời tại lễ khai mạc triển lãm AXEHIBITION",
             "Đêm khai mạc",
             "Bức ảnh duy nhất trong bộ có người làm chủ thể. Để ở cuối vì nó trả lời câu hỏi mà "
             "mọi ảnh không gian đều bỏ ngỏ: rồi có ai đến không."),
        ],
        "process_h": "Đường đi",
        "proc_title": "Tuyến tham quan",
        "process": [
            ("01", "Hành lang sáng",
             "Lối vào trắng, chỉ có tên triển lãm. Reset mắt trước khi vào phòng tối."),
            ("02", "Bảng dẫn nhập",
             "Giải thích khái niệm ngay đầu tuyến, khi khách còn chịu đọc."),
            ("03", "Các khu mùi",
             "Bảy không gian hai bên sảnh, mỗi khu một màu và một chất liệu, nối bằng các hộp đèn mặt tiền."),
            ("04", "Khối trung tâm và tường chiếu",
             "Điểm dừng giữa tuyến: chỗ để đứng lại, và cũng là mốc định hướng cho cả phòng."),
            ("05", "Quầy bar",
             "Kết bằng chỗ ngồi thay vì thêm một hạng mục trưng bày."),
        ],
        "stats": [("7", "Khu mùi hương"), ("14", "Ảnh ghi nhận"), ("2024", "Năm")],
    },
]

from duan_add import NEW_PROJECTS, CHIVAS18_EXTRA
PROJECTS += NEW_PROJECTS
for _p in PROJECTS:
    if _p["slug"] == "chivas-18":
        _have = {g[0] for g in _p["gallery"]}
        _p["gallery"] = [g for g in CHIVAS18_EXTRA if g[0] not in _have][:1] + _p["gallery"][:2] \
            + [g for g in CHIVAS18_EXTRA if g[0] not in _have][1:] + _p["gallery"][2:]
        _p["shots_title"] = "Mười ba bản dựng"
        _p["stats"] = [("13", "Bản dựng"), ("3", "Mặt bằng"), ("2025", "Năm")]


# ------------------------------------------------------------------ DỰNG HTML
def esc(t): return H.escape(t, quote=True)


QT_MARK = ('<svg class="qt-mark" viewBox="0 0 100 62" aria-hidden="true">'
           '<polygon points="20,0 46,0 32,62 0,62"/><polygon points="72,0 98,0 84,62 52,62"/></svg>')
QT_POOL = [
    "Chi tiết nhỏ là nơi người ta <em>tin</em> hay không tin.",
    "Thương hiệu không được nhớ vì nó xuất hiện. Nó được nhớ vì nó <em>khác đi</em>.",
    "Hình đẹp thì nhiều. Hình <em>được nhớ</em> thì hiếm.",
    "Đừng làm cho xong. Làm cho người ta phải <em>nhìn lại</em>.",
    "Tiêu chuẩn là thứ bạn giữ khi <em>không ai nhìn</em>.",
    "Khi ai đó bảo bạn không làm được, họ đang nói về <em>giới hạn</em> của họ, không phải của bạn.",
]


def quote_band(p):
    i = [x["slug"] for x in PROJECTS].index(p["slug"]) if p in PROJECTS else 0
    q = p.get("quote") or QT_POOL[i % len(QT_POOL)]
    return ('<section class="qt qt-band" style="min-height:min(78svh,720px);" aria-label="Quan điểm">'
            '<div class="qt-top"><span>Quan điểm</span><span>LXAM Studio</span></div>'
            '<div class="qt-in">%s<p class="qt-q">%s</p></div>'
            '<div class="qt-bot"><span>lxamstudio.com</span>'
            '<a href="index.html#portfolio" style="color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.4);padding-bottom:3px;">Xem dự án khác →</a></div>'
            '</section>' % (QT_MARK, q))


def build(p):
    slug = p["slug"]
    url = "du-an-%s.html" % slug
    title = p.get("title_seo") or ("%s | LXAM Studio" % p["title"])
    # vi tri cat anh bia, dung khi anh ngang bi cat lech o man hinh hep
    hero_pos = (' style="object-position:%s"' % p["hero_pos"]) if p.get("hero_pos") else ""

    ld = json.dumps({
        "@context": "https://schema.org", "@type": "CreativeWork",
        "name": p["title"], "description": p["desc"],
        "url": "https://lxamstudio.com/" + url,
        "image": "https://lxamstudio.com/" + p["hero"],
        "dateCreated": p["year"], "inLanguage": "vi-VN",
        "creator": {"@type": "Organization", "name": "LXAM Studio",
                    "url": "https://lxamstudio.com/"},
        "about": p["client"],
    }, ensure_ascii=False)
    crumbs = json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": "https://lxamstudio.com/"},
            {"@type": "ListItem", "position": 2, "name": "Portfolio", "item": "https://lxamstudio.com/index.html#portfolio"},
            {"@type": "ListItem", "position": 3, "name": p["title"], "item": "https://lxamstudio.com/" + url},
        ]}, ensure_ascii=False)

    meta = "".join(
        '<div class="meta-row"><dt>%s</dt><dd>%s</dd></div>' % (k, esc(v))
        for k, v in p.get("meta_rows") or [
            ("Khách hàng", p["client"]), ("Năm", p["year"]),
            ("Vai trò", p["role"]), ("Công cụ", p["tools"]),
            ("Bàn giao", p["deliver"])])

    stats = "".join(
        '<div class="ps"><span class="ps-n">%s</span><span class="ps-l">%s</span></div>' % (n, esc(l))
        for n, l in p["stats"])

    chal = "".join(
        '<div class="card"><h3>%s</h3><p style="margin:0;">%s</p></div>' % (esc(h), esc(t))
        for h, t in p["challenge"])

    steps = "".join(
        '<div class="step"><span class="step-n">%s</span>'
        '<div><h3>%s</h3><p style="margin:0;">%s</p></div></div>' % (n, esc(h), esc(t))
        for n, h, t in p["process"])

    shots = "".join(
        '<figure class="shot">'
        '<img src="%s" alt="%s"%s loading="lazy" decoding="async">'
        '<figcaption><strong>%s.</strong> %s</figcaption></figure>'
        % (src, esc(alt), imgdim(src), esc(cap), esc(note))
        for src, alt, cap, note in p["gallery"])
    if p.get("shot_cols"):
        shots = '<div class="shots-grid c%d">%s</div>' % (p["shot_cols"], shots)

    return url, f"""<!DOCTYPE html>
<html lang="vi"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(p['desc'])}">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="article">
<meta property="og:site_name" content="LXAM Studio">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:image" content="https://lxamstudio.com/{p['hero']}">
<meta property="og:url" content="https://lxamstudio.com/{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://lxamstudio.com/{url}">
<link rel="stylesheet" href="assets/lx.css?v=den2">
<script type="application/ld+json">{ld}</script>
<script type="application/ld+json">{crumbs}</script>
<style>
  .pj-hero{{position:relative;margin-top:-120px;padding-top:120px;}}
  .pj-hero-img{{position:relative;height:min(62vh,560px);overflow:hidden;border-radius:0 0 4px 4px;}}
  .pj-hero-img img{{width:100%;height:100%;object-fit:cover;display:block;}}
  .pj-hero-img::after{{content:"";position:absolute;inset:0;
    background:linear-gradient(180deg,rgba(0,0,0,.55),rgba(0,0,0,.1) 40%,rgba(0,0,0,.92));}}
  .pj-head{{max-width:var(--wrap);margin:-90px auto 0;padding:0 var(--pad);position:relative;z-index:2;}}
  .pj-back{{display:inline-block;font-size:13px;color:var(--muted);text-decoration:none;margin-bottom:18px;}}
  .pj-back:hover{{color:#fff;}}
  .pj-meta{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:0;
    border-top:1px solid var(--line);margin-top:34px;}}
  .meta-row{{padding:18px 0;border-bottom:1px solid var(--line-soft);padding-right:22px;}}
  .meta-row dt{{font-family:'Unbounded',sans-serif;font-size:10.5px;letter-spacing:2px;
    text-transform:uppercase;color:var(--ac);margin:0 0 7px;}}
  .meta-row dd{{margin:0;font-size:14.5px;line-height:1.6;color:#d8d0c8;}}
  .pj-stats{{display:flex;flex-wrap:wrap;gap:44px;margin-top:34px;}}
  .ps-n{{display:block;font-family:'Unbounded',sans-serif;font-size:clamp(26px,3.4vw,38px);
    font-weight:700;color:#fff;line-height:1.1;}}
  .ps-l{{display:block;font-size:12px;letter-spacing:1.6px;text-transform:uppercase;
    color:var(--dim);margin-top:6px;}}
  .shot{{margin:0 0 clamp(40px,6vw,72px);}}
  .shot img{{width:100%;display:block;border-radius:4px;border:1px solid var(--line);background:#050505;}}
  .shot figcaption{{margin:14px auto 0;max-width:720px;font-size:14.5px;line-height:1.75;color:#a79d93;}}
  .shot figcaption strong{{color:#fff;font-weight:600;}}
  .shots-grid{{display:grid;gap:clamp(18px,2.4vw,32px);align-items:start;}}
  .shots-grid.c2{{grid-template-columns:repeat(2,1fr);}}
  .shots-grid.c3{{grid-template-columns:repeat(3,1fr);}}
  .shots-grid .shot{{margin:0;}}
  .shots-grid .shot figcaption{{margin:12px 0 0;font-size:13.5px;}}
  @media (max-width:760px){{ .shots-grid.c2,.shots-grid.c3{{grid-template-columns:1fr;}} }}
  .step{{display:grid;grid-template-columns:64px 1fr;gap:22px;padding:24px 0;
    border-top:1px solid var(--line-soft);align-items:start;}}
  .step-n{{font-family:'Unbounded',sans-serif;font-size:13px;font-weight:600;
    letter-spacing:2px;color:var(--ac);padding-top:5px;}}
  .step h3{{margin:0 0 8px;font-size:clamp(16px,1.8vw,21px);}}
  @media (max-width:700px){{
    .pj-hero-img{{height:44vh;}}
    .pj-head{{margin-top:-60px;}}
    .pj-stats{{gap:28px;}}
    .step{{grid-template-columns:44px 1fr;gap:14px;}}
  }}
</style>
</head>
<body>
<nav class="lxnav">
  <a class="lxlogo" href="index.html" aria-label="LXAM Studio">
    <img src="assets/logo-lxam.png" alt="LXAM" class="lxlogo-icon" width="256" height="256">
    <div class="lxwordmark"><div class="wm">LXAM</div><div class="wm-sub">3D ART STUDIO</div></div>
  </a>
  <div class="lxnav-links">{NAV}</div>
  <div class="lxnav-actions">
    <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ</a>
    <button class="lxburger" id="lxburger" aria-label="Menu" aria-expanded="false">≡</button>
  </div>
</nav>
<div class="lxdrawer" id="lxdrawer">
  {DRAWER}
  <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ →</a>
</div>

<main>
  <div class="pj-hero">
    <div class="pj-hero-img">
      <img src="{p['hero']}" alt="{esc(p['hero_alt'])}" width="1600" height="900"{hero_pos}>
    </div>
    <div class="pj-head">
      <a class="pj-back" href="{p.get('back','index.html#portfolio')}">← {esc(p.get('back_label','Tất cả dự án'))}</a>
      <p class="eyebrow">Dự án · {esc(p['client'])} · {p['year']}</p>
      <h1 style="max-width:20ch;">{esc(p['title'])}</h1>
      <p class="lead" style="max-width:720px;">{esc(p['intro'])}</p>
      <div class="pj-stats">{stats}</div>
      <dl class="pj-meta">{meta}</dl>
    </div>
  </div>

  <section>
    <div class="wrap">
      <p class="eyebrow">{esc(p['challenge_h'])}</p>
      <h2>{esc(p.get('chal_title','Ba thứ khó nhất'))}</h2>
      <div class="grid3" style="margin-top:30px;">{chal}</div>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="wrap">
      <p class="eyebrow">Hình ảnh</p>
      <h2 style="margin-bottom:40px;">{esc(p.get("shots_title","Từng cảnh, và lý do"))}</h2>
      {shots}
    </div>
  </section>

  <section style="background:rgba(255,255,255,.014);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
    <div class="wrap">
      <p class="eyebrow">{esc(p['process_h'])}</p>
      <h2>{esc(p.get('proc_title','Năm bước'))}</h2>
      <div style="margin-top:30px;">{steps}</div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="card" style="text-align:center;padding:clamp(34px,5vw,62px);
           border-color:rgba(255,122,26,.28);background:rgba(255,122,26,.05);">
        <h2 style="margin-bottom:14px;">Muốn làm được shot như thế này?</h2>
        <p style="max-width:560px;margin:0 auto 28px;">Đây là đúng những kỹ năng trong lộ trình
        LXAM Academy, dựng hình, ánh sáng, render tách lớp, dựng phim. Học bằng dự án thật, có người sửa bài.</p>
        <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
          <a class="lxcta" href="lo-trinh.html" style="padding:15px 30px;font-size:15px;">Xem lộ trình học</a>
          <a class="lxcta-ghost" href="cam-nang.html?from=du-an-{slug}">Nhận cẩm nang miễn phí</a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="lxfooter">
  <div class="lxfoot">
    <div>
      <a class="lxlogo" href="index.html" style="margin-bottom:18px;">
        <img src="assets/logo-lxam.png" alt="LXAM" width="40" height="40" style="width:40px;height:40px;">
        <div class="lxwordmark">
          <div class="wm" style="font-size:26px;letter-spacing:9px;">LXAM</div>
          <div class="wm-sub" style="font-size:9px;letter-spacing:4.3px;">3D ART STUDIO</div>
        </div>
      </a>
      <p>Đào tạo 3D từ con số 0 đến TVC điện ảnh. Coaching 1:1 online, đồng hành trọn 1 năm cùng giảng viên 10 năm kinh nghiệm.</p>
    </div>
    <div>
      <div class="col-head">Điều hướng</div>
      <div class="links">
        <a href="ve-chung-toi.html">Về chúng tôi</a>
        <a href="index.html#portfolio">Portfolio</a>
        <a href="du-an-event.html">Dự án Event</a>
        <a href="du-an-automotive.html">Dự án Automotive</a>
        <a href="du-an-san-pham.html">Dự án sản phẩm</a>
        <a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>
        <a href="blog.html">Blog</a>
        <a href="lo-trinh.html">Lộ trình &amp; học phí</a>
      </div>
    </div>
    <div>
      <div class="col-head">Kết nối</div>
      <div class="links">
        <a href="https://www.facebook.com/lxamstudio/" target="_blank" rel="noopener">Fanpage Studio ↗</a>
        <a href="https://www.youtube.com/@LXAMStudios" target="_blank" rel="noopener">YouTube @LXAMStudios ↗</a>
        <a href="https://www.instagram.com/lxamstudio/" target="_blank" rel="noopener">Instagram ↗</a>
        <a href="tel:0942890363">Hotline 0942 890 363</a>
      </div>
    </div>
  </div>
  <div class="lxfoot-base">
    <span>© {YEAR} LXAM Studio. All rights reserved.</span>
    <span>3D · Modeling · Lighting · Rendering · Animation · TVC · AI</span>
  </div>
</footer>
<script>
(function(){{
  var b=document.getElementById('lxburger'), d=document.getElementById('lxdrawer');
  if(!b||!d) return;
  b.addEventListener('click', function(){{
    var open=d.classList.toggle('open');
    b.setAttribute('aria-expanded', open?'true':'false');
    b.textContent = open ? '✕' : '≡';
    document.body.style.overflow = open ? 'hidden' : '';
  }});
  d.addEventListener('click', function(e){{
    if(e.target.tagName==='A'){{ d.classList.remove('open'); b.textContent='≡'; document.body.style.overflow=''; }}
  }});
}})();
</script>
<script src="assets/lx-ui.js?v=den2" defer></script>
</body></html>
"""


if __name__ == "__main__":
    for p in PROJECTS:
        url, html_out = build(p)
        with open(os.path.join(SITE, url), "w", encoding="utf-8") as f:
            f.write(html_out)
        print("wrote", url, len(html_out), "bytes,", len(p["gallery"]), "ảnh")
