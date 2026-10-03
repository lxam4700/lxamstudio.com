#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh trang lo-trinh.html: 2 hệ lộ trình riêng biệt: 3D Automotive và 3D × A.I."""

import os, json, datetime

SITE = "/home/claude/site"
YEAR = datetime.date.today().year

NAV_LINKS = (
    '<a href="ve-chung-toi.html">Về chúng tôi</a>'
    '<a href="index.html#portfolio">Portfolio</a>'
    '<a href="blog.html">Blog</a>'
    '<a href="hoc-vien.html">Khu học viên</a>'
    '<a href="index.html#lienhe">Liên hệ</a>'
    '<a href="khoa-hoc.html">Khóa học</a>'
    '<a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>'
)
DRAWER_LINKS = (
    '<a href="ve-chung-toi.html">Về chúng tôi</a>'
    '<a href="index.html#portfolio">Portfolio</a>'
    '<a href="blog.html">Blog</a>'
    '<a href="hoc-vien.html">Khu học viên</a>'
    '<a href="index.html#lienhe">Liên hệ</a>'
    '<a href="khoa-hoc.html">Khóa học</a>'
    '<a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>'
    '<a href="cam-nang.html">Cẩm nang</a>'
    '<a href="lo-trinh.html">Lộ trình &amp; học phí</a>'
)

TITLE = "Lộ trình học Blender 3D và học phí | LXAM Studio"
DESC = ("Hai lộ trình riêng tại LXAM Academy: 3D Automotive (Blender từ Beginner đến Masterclass) "
        "và 3D × A.I dành cho người cần học AI vào quy trình hình ảnh.")

JSONLD = json.dumps({
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Lộ trình học LXAM Academy",
    "description": DESC,
    "itemListElement": [
        {"@type": "Course", "position": 1, "name": "The Blender Automotive Beginner",
         "description": "Modeling 2 tháng + Rendering 1 tháng. Dựng và render được sản phẩm, xe cơ bản trong Blender.",
         "provider": {"@type": "Organization", "name": "LXAM Academy", "url": "https://lxamstudio.com/"},
         "inLanguage": "vi-VN",
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                               "courseWorkload": "P3M"}},
        {"@type": "Course", "position": 2, "name": "The Blender Automotive Masterclass",
         "description": "Modeling nâng cao 2 tháng + TVC 1 tháng + Rendering 1 tháng. Hard-surface nâng cao, car modeling, rigging, animation, VFX, SFX.",
         "provider": {"@type": "Organization", "name": "LXAM Academy", "url": "https://lxamstudio.com/"},
         "inLanguage": "vi-VN",
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                               "courseWorkload": "P4M"}},
        {"@type": "Course", "position": 3, "name": "3D Basic: Blender Foundation",
         "description": "3 tháng nền tảng: modeling hard-surface, material & lighting, rendering, tư duy hình ảnh.",
         "provider": {"@type": "Organization", "name": "LXAM Academy", "url": "https://lxamstudio.com/"},
         "inLanguage": "vi-VN",
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                               "courseWorkload": "P3M"}},
        {"@type": "Course", "position": 4, "name": "A.I Advance: AI × Visual",
         "description": "1 tháng: tư duy prompt, góc máy và ánh sáng với AI, workflow 3D × AI, ứng dụng Nano Banana Pro, Seedance, Kling 3.0.",
         "provider": {"@type": "Organization", "name": "LXAM Academy", "url": "https://lxamstudio.com/"},
         "inLanguage": "vi-VN",
         "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                               "courseWorkload": "P1M"}},
    ],
}, ensure_ascii=False)


def module(tag, dur, items):
    lis = "".join('<li><strong>%s</strong> %s</li>' % (k, v) if k else '<li>%s</li>' % v
                  for k, v in items)
    return ('<div class="mod">'
            '<div class="mod-head"><span class="mod-tag">%s</span>'
            '<span class="mod-dur">%s</span></div>'
            '<ul class="mod-list">%s</ul></div>' % (tag, dur, lis))


def level(img, alt, badge, name, sub, modules, goal, note=""):
    return f"""
    <article class="lvl">
      <div class="lvl-art"><img src="{img}" alt="{alt}" loading="lazy" width="1200" height="1200"></div>
      <div class="lvl-body">
        <span class="badge">{badge}</span>
        <h3>{name}</h3>
        <p class="lvl-sub">{sub}</p>
        {modules}
        <div class="goal"><span class="goal-label">Mục tiêu</span><p>{goal}</p></div>
        {note}
      </div>
    </article>"""


# hai chặng bên trong gói kèm riêng, khác nhau theo từng hệ
TIERS = {
    "he01": {
        "label": "Hai chặng của hệ 3D Automotive",
        "rows": [
            ("Basic: Nền tảng", "15tr",
             "Modeling cơ bản · Materials &amp; Lighting · Rendering. Ba kỹ năng, khoảng 3 tháng."),
            ("Master: Chuyên sâu", "20tr",
             "Modeling nâng cao (hard-surface, car modeling) · Lighting điện ảnh · Animation và TVC. Bốn kỹ năng."),
        ],
        "sum": ("Học trọn cả hai", "30tr", "Basic + Master gộp lại, rẻ hơn 5tr so với mua rời từng chặng."),
        "line": "Trọn lộ trình 30tr, rẻ hơn 5tr so với mua lẻ từng chặng",
    },
    "he02": {
        "label": "Hai chặng của hệ 3D × A.I",
        "rows": [
            ("3D Basic: Nền tảng", "15tr",
             "Modeling hard-surface · Material &amp; Lighting · Rendering · tư duy hình ảnh. Ba kỹ năng, ba tháng."),
            ("A.I Advance: Chuyên sâu", "10tr",
             "AI × Visual (tư duy prompt, góc máy và ánh sáng với AI) · Workflow 3D × AI. Hai kỹ năng, một tháng."),
        ],
        "sum": ("Học trọn cả hai", "22tr",
                "3D Basic + A.I Advance gộp lại, rẻ hơn 3tr so với mua rời từng chặng."),
        "line": "Trọn hệ 22tr, rẻ hơn 3tr so với mua lẻ từng chặng",
    },
}

COACH_BENEFITS = [
    ("Mở khoá toàn bộ quyền lợi học viên",
     "Không phần nào bị khoá theo gói. Bài giảng, tài liệu, file dự án, nhóm học viên, có hết."),
    ("Hỏi bất kỳ lúc nào",
     "Vướng là nhắn, không phải để dành tới buổi học. Không giới hạn số câu hỏi."),
    ("Đặt lịch coach khi cần",
     "Kẹt ở đâu thì mở buổi ở đó. Lịch xếp theo bạn, không chờ tới khung giờ cố định."),
    ("Tư vấn sâu, không chỉ dạy phần mềm",
     "Chọn mảng nào, nhận job kiểu gì, báo giá ra sao, thị trường đang cần gì, nói thẳng."),
    ("Portfolio dựng theo thị trường lao động",
     "Làm đúng thứ nhà tuyển dụng và khách hàng đang tìm, không phải bài tập cho đẹp."),
    ("Cam kết đầu ra",
     "Đồng hành tới khi bạn làm được nghề. Hết nội dung mà chưa vững thì vẫn kèm tiếp."),
]


WAYS = [
    {
        "key": "tuhoc", "name": "Tự học có chữa bài", "price": "2,5tr",
        "unit": "học theo lịch của bạn", "hot": False, "badge": "",
        "lines": ["Trọn bộ bài giảng quay sẵn, xem lại không giới hạn",
                  "Mỗi tuần nộp bài, giảng viên chữa trực tiếp",
                  "Tài liệu và file dự án đi kèm"],
        "detail": [
            ("Bạn nhận gì", "Toàn bộ bài giảng quay sẵn của hệ này, tài liệu và file dự án. Xem lại bao nhiêu lần cũng được."),
            ("Chữa bài", "Mỗi tuần nộp một bài, giảng viên xem và chỉ thẳng chỗ sai. Nhận xét bằng văn bản và hình."),
            ("Thời gian", "Không có deadline. Bạn học nhanh hay chậm tuỳ lịch của bạn."),
            ("Hợp với", "Người đang đi làm, tự kỷ luật được, hoặc muốn thử trước khi đi sâu."),
            ("Không có", "Lịch cố định, lớp học cùng nhau, và chữa bài trực tiếp trên file của bạn."),
        ],
    },
    {
        "key": "lop8tuan", "name": "Lớp 8 tuần", "price": "12tr",
        "unit": "chia 2 mốc, mỗi mốc 6tr", "hot": True, "badge": "Nhiều người chọn",
        "lines": ["Tối đa 10 suất, có lịch và có deadline",
                  "Kết thúc lớp có 3 sản phẩm portfolio",
                  "Học cùng nhóm, chữa bài trước cả lớp"],
        "detail": [
            ("Bạn nhận gì", "Một lớp tối đa 10 người, lịch học và deadline rõ ràng trong 8 tuần."),
            ("Đầu ra", "Ba sản phẩm portfolio: hard-surface, scene lighting, và một sản phẩm thương mại."),
            ("Chữa bài", "Chữa trước cả lớp. Bạn học được cả từ lỗi của người khác, không chỉ lỗi của mình."),
            ("Đóng phí", "Hai mốc, mỗi mốc 6tr. Mốc hai đóng khi qua nửa lớp."),
            ("Hợp với", "Người cần áp lực và bạn đồng hành để không bỏ giữa chừng."),
            ("Không có", "Lịch linh hoạt riêng cho bạn, lớp chạy theo lịch chung."),
        ],
    },
    {
        "key": "kemrieng", "name": "Kèm riêng 1:1", "price": "từ 15tr",
        "unit": "lịch theo bạn", "hot": False, "badge": "Lựa chọn tiết kiệm nhất",
        "lines": ["Chữa bài trên chính file của bạn",
                  "Đồng hành trọn 1 năm",
                  "Trọn lộ trình 30tr, rẻ hơn 5tr so với mua lẻ từng kỹ năng"],
        "detail": [
            ("Chữa bài", "Giảng viên mở chính file của bạn, sửa tại chỗ và giải thích vì sao sửa như vậy."),
            ("Hợp với", "Người có mục tiêu nghề rõ ràng và muốn đi nhanh nhất có thể."),
        ],
    },
]


def tier_box(slug):
    t = TIERS[slug]
    rows = ""
    for name, price, desc in t["rows"]:
        pr = '<span class="tier-p">%s</span>' % price if price else ""
        rows += ('<div class="tier"><div class="tier-h"><strong>%s</strong>%s</div>'
                 '<p>%s</p></div>' % (name, pr, desc))
    sname, sprice, sdesc = t["sum"]
    rows += ('<div class="tier tier-sum"><div class="tier-h"><strong>%s</strong>'
             '<span class="tier-p">%s</span></div><p>%s</p></div>' % (sname, sprice, sdesc))
    return ('<div class="tierbox"><span class="tierbox-label">%s</span>%s</div>'
            % (t["label"], rows))


def benefit_box():
    lis = "".join('<li><strong>%s</strong><span>%s</span></li>' % (h, t)
                  for h, t in COACH_BENEFITS)
    return ('<div class="benbox"><span class="benbox-label">Kèm riêng mở khoá những gì</span>'
            '<ul class="benlist">%s</ul></div>' % lis)


def price_card(he, slug, w):
    lines = list(w["lines"])
    if w["key"] == "kemrieng":
        lines[-1] = TIERS[slug]["line"]
    lis = "".join("<li>%s</li>" % x for x in lines)
    rows = "".join(
        '<div class="prow"><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in w["detail"])
    extra = (tier_box(slug) + benefit_box()) if w["key"] == "kemrieng" else ""
    hot = w["hot"]
    badge = ('<span class="pbadge%s">%s</span>' % ("" if hot else " alt", w["badge"])) if w["badge"] else ""
    return (
        '<div class="pcard%s" data-card="%s">%s'
        '<button type="button" class="ptoggle" aria-expanded="false">'
        '<span class="pname">%s</span>'
        '<span class="pprice"><span class="pnum">%s</span><span class="punit">%s</span></span>'
        '<span class="pchev" aria-hidden="true"></span>'
        '</button>'
        '<ul class="plist">%s</ul>'
        '<div class="pdetail" hidden>'
        '%s<dl class="pdl">%s</dl>'
        '<a class="pbtn%s" href="#dangky" data-he="%s" data-goi="%s">Đăng ký gói này →</a>'
        '</div>'
        '<span class="phint">Bấm để xem chi tiết gói</span>'
        '</div>' % (" hot" if hot else "", w["key"], badge,
                    w["name"], w["price"], w["unit"], lis, extra, rows,
                    " hot" if hot else "", he, w["key"])
    )


def track_price(slug, he, label, line):
    cards = "".join(price_card(he, slug, w) for w in WAYS)
    return """
      <div class="price-wrap" id="hocphi-%s">
        <div class="price-head">
          <span class="price-eyebrow">Học phí %s</span>
          <p>%s</p>
        </div>
        <div class="price-grid">%s</div>
        <p class="price-note">Đóng trước <strong>50%% học phí</strong> thì được tặng thêm
        <strong>6 tháng coaching</strong>. Mọi học viên được đồng hành trọn 1 năm.</p>
        <details class="pmore">
          <summary>Chỉ cần học lẻ một kỹ năng?</summary>
          <p>Học riêng từng kỹ năng: <strong>5tr / kỹ năng</strong>. Hợp với người đã làm 3D và chỉ
          thiếu đúng một mảng. Để lại thông tin bên dưới, tôi xem rồi nói bạn cần học kỹ năng nào.</p>
        </details>
        <div class="track-cta">
          <div class="track-cta-txt">
            <strong>Chưa chắc chọn gói nào?</strong>
            <p>Để lại thông tin, tôi gọi tư vấn trước khi bạn đóng bất kỳ khoản nào.</p>
          </div>
          <div class="track-cta-btns">
            <a class="lxcta" href="#dangky" data-he="%s" data-goi="">Đăng ký tư vấn %s →</a>
            <a class="lxcta-ghost" href="cam-nang.html?from=%s">Nhận cẩm nang 112 trang miễn phí</a>
          </div>
        </div>
      </div>""" % (slug, label, line, cards, he, label, slug)


# ---------------------------------------------------------------- TRACK 1
RENDER_ITEMS = [
    ("Shading:", "Geometry Node, PBR materials"),
    ("Lighting:", "các loại đèn, hướng sáng"),
    ("Camera setting:", "layout frame, góc máy"),
    ("Render setting:", "resolution, denoise"),
    ("Compositing:", "grading, blur, glare"),
    ("Scene optimization:", "khai thác hết CPU và GPU"),
    ("Testing &amp; refinement:", "render thử, tinh chỉnh ánh sáng"),
]

T1_BEGINNER = level(
    "assets/lo-trinh-automotive-beginner.jpg",
    "The Blender Automotive Beginner: lộ trình 3D cơ bản của LXAM Academy",
    "Basic", "The Blender Automotive Beginner", "3 tháng · Blender từ con số 0",
    module("Modeling", "2 tháng", [
        ("Basic modeling:", "extrude, bevel, bridge, boolean…"),
        ("Product modeling:", "dựng sản phẩm đúng tỉ lệ, đúng form"),
    ]) + module("Rendering", "1 tháng", RENDER_ITEMS),
    "Tự dựng và render được một sản phẩm hoàn chỉnh, đủ đưa vào portfolio.")

T1_MASTER = level(
    "assets/lo-trinh-automotive-masterclass.jpg",
    "The Blender Automotive Masterclass: lộ trình 3D nâng cao của LXAM Academy",
    "Advance", "The Blender Automotive Masterclass", "4 tháng · đi tới TVC hoàn chỉnh",
    module("Modeling", "2 tháng", [
        ("", "Bao gồm toàn bộ nội dung bản Basic, cộng thêm:"),
        ("Hard-surface modeling:", "mức nâng cao"),
        ("Car modeling:", "dựng Lamborghini Veneno"),
    ]) + module("TVC", "1 tháng", [
        ("Concept:", "sketch, viết kịch bản, vẽ storyboard"),
        ("Rigging:", "rig xe bằng LC Addon"),
        ("Animation:", "keyframe, tư duy điện ảnh, công cụ"),
        ("VFX:", "khí động học, hiệu ứng ánh sáng"),
        ("SFX:", "sound effect, nhạc nền"),
    ]) + module("Rendering", "1 tháng", RENDER_ITEMS),
    "Hoàn thành một TVC ô tô từ concept đến bản dựng cuối.")

# ---------------------------------------------------------------- TRACK 2
T2_BASIC = level(
    "assets/lo-trinh-3d-basic-ai.jpg",
    "3D Basic: Blender Foundation, nền tảng 3D trước khi vào AI",
    "3D Basic", "Blender Foundation", "3 tháng · nền tảng bắt buộc",
    module("Nội dung", "3 tháng", [
        ("Modeling:", "hard surface, sản phẩm, form chuẩn"),
        ("Material &amp; Lighting:", "hiểu vật liệu và ánh sáng để render “ra tiền”"),
        ("Rendering:", "setup scene sạch, tối ưu workflow"),
        ("Tư duy hình ảnh:", "bố cục, góc máy, storytelling cơ bản"),
    ]),
    "Tự dựng và render được sản phẩm hoàn chỉnh.")

T2_AI = level(
    "assets/lo-trinh-ai-advance.jpg",
    "A.I Advance: AI × Visual, khoá AI cho người làm hình ảnh tại LXAM Academy",
    "A.I Advance", "AI × Visual", "1 tháng · AI từ cơ bản đến nâng cao",
    module("Nội dung", "1 tháng", [
        ("Tư duy Prompt:", "cách diễn đạt để AI hiểu đúng ý tưởng"),
        ("Góc máy &amp; ánh sáng với AI:", "kiểm soát mood, cinematic feel"),
        ("Workflow 3D × AI:", "kết hợp render và AI để tạo visual mạnh hơn"),
        ("Ứng dụng công cụ:", "Nano Banana Pro, Seedance, Kling 3.0"),
    ]),
    "Biến 1 sản phẩm thành 5 đến 10 biến thể chất lượng cao trong thời gian ngắn.",
    '<p class="lvl-note">Học phần này nối tiếp 3D Basic. AI thay bạn làm phần lặp lại, '
    'không thay phần bạn quyết định, nên nền 3D vẫn là điều kiện đi trước.</p>')


CTA_1 = track_price("he01", "Hệ 3D Automotive", "hệ 3D Automotive",
    "Ba cách học, cùng một nội dung ở trên. Khác nhau đúng một chỗ: ai ngồi cạnh bạn lúc sửa bài.")
CTA_2 = track_price("he02", "Hệ 3D × A.I", "hệ 3D × A.I",
    "Ba cách học, cùng một nội dung ở trên. Khác nhau đúng một chỗ: ai ngồi cạnh bạn lúc sửa bài.")

PAGE_CSS = """
<style>
  .track{margin-top:18px;}
  .track-head{
    display:flex;flex-wrap:wrap;align-items:baseline;gap:14px;
    padding-bottom:20px;margin-bottom:34px;border-bottom:1px solid var(--line);
  }
  .track-num{
    font-family:'Unbounded',sans-serif;font-size:12px;font-weight:600;
    letter-spacing:3px;color:var(--ac);text-transform:uppercase;
  }
  .track-dur{font-size:13px;color:var(--dim);letter-spacing:.4px;}
  .track-intro{max-width:640px;margin:0;}
  .lvl{
    display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:34px;
    align-items:start;padding:30px 0;border-top:1px solid var(--line-soft);
  }
  .lvl:first-of-type{border-top:0;padding-top:6px;}
  .lvl-art img{
    width:100%;height:auto;display:block;
    aspect-ratio:1/1;object-fit:contain;
    border-radius:4px;border:1px solid var(--line);background:#050505;
  }
  .badge{
    display:inline-block;font-family:'Unbounded',sans-serif;
    font-size:10.5px;letter-spacing:2.2px;text-transform:uppercase;font-weight:600;
    color:var(--ac);border:1px solid rgba(255,122,26,.38);
    border-radius:999px;padding:6px 13px;margin-bottom:16px;
  }
  .lvl h3{margin:0 0 8px;font-size:clamp(19px,2.3vw,27px);}
  .lvl-sub{font-size:13.5px;letter-spacing:1px;text-transform:uppercase;color:var(--dim);margin:0 0 24px;}
  .lvl-note{font-size:14px;line-height:1.7;color:#9a8f84;margin:18px 0 0;font-style:italic;}
  .mod{margin-bottom:22px;}
  .mod-head{display:flex;align-items:baseline;gap:12px;margin-bottom:12px;}
  .mod-tag{
    font-family:'Unbounded',sans-serif;font-size:14px;font-weight:600;
    text-transform:uppercase;letter-spacing:1.2px;color:#fff;
  }
  .mod-dur{
    font-size:11.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--ac);
    border:1px solid rgba(255,122,26,.3);border-radius:999px;padding:3px 10px;white-space:nowrap;
  }
  .mod-list{list-style:none;padding:0;margin:0;}
  .mod-list li{
    font-size:15px;line-height:1.7;color:#c9c0b7;margin:0 0 9px;
    padding-left:18px;position:relative;
  }
  .mod-list li::before{
    content:"";position:absolute;left:0;top:10px;
    width:6px;height:6px;border-radius:50%;background:rgba(255,122,26,.55);
  }
  .mod-list strong{color:#fff;font-weight:600;}
  .goal{
    margin-top:22px;padding:18px 22px;border-radius:4px;
    background:rgba(255,122,26,.06);border:1px solid rgba(255,122,26,.22);
  }
  .goal-label{
    display:block;font-family:'Unbounded',sans-serif;font-size:10.5px;
    letter-spacing:2.2px;text-transform:uppercase;color:var(--ac);margin-bottom:7px;
  }
  .goal p{margin:0;color:#e2dad2;font-size:15.5px;line-height:1.65;}
  .track-cta{
    display:flex;flex-wrap:wrap;align-items:center;gap:20px;
    margin-top:34px;padding:24px 28px;border-radius:4px;
    border:1px solid rgba(255,122,26,.26);background:rgba(255,122,26,.05);
  }
  .track-cta-txt{flex:1;min-width:260px;}
  .track-cta-txt strong{
    display:block;font-family:'Unbounded',sans-serif;font-size:15px;
    font-weight:600;color:#fff;margin-bottom:7px;line-height:1.45;
  }
  .track-cta-txt p{margin:0;font-size:14.5px;line-height:1.65;color:#b8afa6;}
  .track-cta-btns{display:flex;flex-wrap:wrap;gap:12px;align-items:center;}
  .track-cta .lxcta{padding:14px 28px;font-size:14.5px;}
  .lxcta-ghost{
    display:inline-flex;align-items:center;justify-content:center;
    padding:13px 24px;border-radius:999px;
    border:1px solid rgba(255,255,255,.22);background:transparent;
    color:#e6ded6;font-size:14px;font-weight:500;letter-spacing:.2px;
    text-decoration:none;white-space:nowrap;
    transition:border-color .2s ease,color .2s ease,background .2s ease;
  }
  .lxcta-ghost:hover{border-color:rgba(255,122,26,.55);color:#fff;background:rgba(255,122,26,.07);}
  @media (max-width:560px){
    .track-cta-btns{width:100%;}
    .track-cta-btns a{width:100%;}
  }
  /* ---- hoc phi trong tung he ---- */
  .price-wrap{margin-top:40px;padding-top:34px;border-top:1px solid var(--line);}
  .price-head{margin-bottom:24px;}
  .price-eyebrow{
    display:flex;align-items:center;gap:12px;
    font-family:'Unbounded',sans-serif;font-size:11px;letter-spacing:2.4px;
    text-transform:uppercase;color:var(--ac);font-weight:600;margin-bottom:12px;
  }
  .price-eyebrow::before{content:"";flex:0 0 auto;width:28px;height:1px;background:currentColor;opacity:.75;}
  .price-head p{margin:0;font-size:15.5px;line-height:1.7;color:#b8afa6;max-width:640px;}
  .price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:start;}
  .pcard{
    position:relative;display:flex;flex-direction:column;
    background:var(--card);border:1px solid var(--line);
    border-radius:4px;padding:26px 24px 20px;
    transition:border-color .22s ease,background .22s ease;
  }
  .pcard.hot{border-color:rgba(255,122,26,.42);background:rgba(255,122,26,.05);}
  .pcard.open{border-color:rgba(255,122,26,.62);background:rgba(255,122,26,.07);}
  .pbadge{
    position:absolute;top:-10px;left:24px;
    font-family:'Unbounded',sans-serif;font-size:9.5px;letter-spacing:1.8px;
    text-transform:uppercase;font-weight:600;color:#fff;
    background:var(--ac);
    border-radius:999px;padding:5px 12px;white-space:nowrap;
  }
  .pbadge.alt{
    background:rgba(0,0,0,.96);color:var(--ac);
    border:1px solid rgba(255,122,26,.55);
  }
  .ptoggle{
    display:block;width:100%;text-align:left;
    background:none;border:0;padding:0;margin:0 0 16px;
    font-family:inherit;color:inherit;cursor:pointer;position:relative;
  }
  .pname{
    display:block;font-family:'Unbounded',sans-serif;font-size:12.5px;font-weight:600;
    letter-spacing:2.2px;text-transform:uppercase;color:#cfc6bd;margin-bottom:14px;
    padding-right:34px;
  }
  .pcard.hot .pname{color:var(--ac);}
  .pprice{display:flex;align-items:baseline;flex-wrap:wrap;gap:8px;}
  .pnum{font-family:'Unbounded',sans-serif;font-size:clamp(30px,3.4vw,40px);font-weight:700;color:#fff;line-height:1;}
  .pcard.hot .pnum{color:var(--ac);}
  .punit{font-size:13px;color:var(--dim);}
  .pchev{
    position:absolute;right:0;top:-2px;width:26px;height:26px;border-radius:50%;
    border:1px solid rgba(255,255,255,.22);
    display:flex;align-items:center;justify-content:center;
    transition:transform .25s ease,border-color .2s ease;
  }
  .pchev::before{
    content:"";width:7px;height:7px;margin-top:-3px;
    border-right:1.6px solid #cfc6bd;border-bottom:1.6px solid #cfc6bd;
    transform:rotate(45deg);
  }
  .pcard.open .pchev{transform:rotate(180deg);border-color:rgba(255,122,26,.7);}
  .plist{list-style:none;padding:0;margin:0 0 18px;}
  .plist li{
    position:relative;padding-left:20px;margin:0 0 10px;
    font-size:14px;line-height:1.6;color:#d0c7be;
  }
  .plist li::before{
    content:"";position:absolute;left:0;top:8px;width:7px;height:7px;
    border-radius:50%;background:rgba(255,122,26,.6);
  }
  .phint{
    display:block;margin-top:auto;padding-top:4px;
    font-size:12.5px;color:var(--dim);letter-spacing:.2px;
  }
  .pcard.open .phint{display:none;}
  .pdetail{
    border-top:1px solid rgba(255,122,26,.25);margin-top:4px;padding-top:18px;
    animation:pgrow .28s ease;
  }
  @keyframes pgrow{from{opacity:0;transform:translateY(-6px);}to{opacity:1;transform:none;}}
  .pdl{margin:0 0 20px;}
  .prow{padding:0 0 13px;}
  .prow dt{
    font-family:'Unbounded',sans-serif;font-size:10.5px;font-weight:600;
    letter-spacing:1.8px;text-transform:uppercase;color:var(--ac);margin-bottom:5px;
  }
  .prow dd{margin:0;font-size:14px;line-height:1.68;color:#d0c7be;}
  .pbtn{
    display:block;text-align:center;
    padding:13px 18px;border-radius:999px;
    border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.05);
    color:#ece4db;font-family:'Unbounded',sans-serif;font-size:12.5px;font-weight:600;
    letter-spacing:1.6px;text-transform:uppercase;text-decoration:none;
    transition:border-color .2s ease,background .2s ease,color .2s ease;
  }
  .pbtn:hover{border-color:rgba(255,122,26,.6);color:#fff;background:rgba(255,122,26,.1);}
  .pbtn.hot{
    border:none;color:#fff;
    background:var(--ac);
    box-shadow:0 10px 26px rgba(226,45,15,.32);
  }
  /* ---- box 2 chang trong goi kem rieng ---- */
  .tierbox{
    border:1px solid rgba(255,122,26,.30);border-radius:4px;
    padding:18px 18px 6px;margin:0 0 20px;background:rgba(255,122,26,.045);
  }
  .tierbox-label{
    display:block;font-family:'Unbounded',sans-serif;font-size:10px;font-weight:600;
    letter-spacing:1.9px;text-transform:uppercase;color:var(--ac);margin-bottom:14px;
  }
  .tier{padding:0 0 14px;border-bottom:1px solid rgba(255,255,255,.07);margin-bottom:14px;}
  .tier:last-child{border-bottom:0;}
  .tier-h{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:6px;}
  .tier-h strong{
    font-family:'Unbounded',sans-serif;font-size:12.5px;font-weight:600;
    letter-spacing:.6px;color:#fff;line-height:1.35;
  }
  .tier-p{
    font-family:'Unbounded',sans-serif;font-size:17px;font-weight:700;
    color:#fff;white-space:nowrap;line-height:1;
  }
  .tier p{margin:0;font-size:13.5px;line-height:1.6;color:#b8afa6;}
  .tier-sum{
    background:rgba(255,122,26,.10);border:1px solid rgba(255,122,26,.34);
    border-radius:4px;padding:13px 14px;margin-bottom:12px;
  }
  .tier-sum .tier-h strong,.tier-sum .tier-p{color:var(--ac);}

  /* ---- quyen loi coaching ---- */
  .benbox{margin:0 0 20px;}
  .benbox-label{
    display:block;font-family:'Unbounded',sans-serif;font-size:10px;font-weight:600;
    letter-spacing:1.9px;text-transform:uppercase;color:var(--ac);margin-bottom:12px;
  }
  .benlist{list-style:none;padding:0;margin:0;}
  .benlist li{
    position:relative;padding:0 0 12px 24px;margin:0;
  }
  .benlist li::before{
    content:"";position:absolute;left:2px;top:6px;
    width:9px;height:5px;border-left:1.8px solid var(--ac);border-bottom:1.8px solid var(--ac);
    transform:rotate(-45deg);
  }
  .benlist strong{display:block;font-size:14px;font-weight:600;color:#fff;margin-bottom:3px;line-height:1.45;}
  .benlist span{display:block;font-size:13.5px;line-height:1.6;color:#b8afa6;}
  .price-note{margin:22px 0 0;font-size:14.5px;line-height:1.7;color:#b8afa6;}
  .price-note strong{color:#fff;}
  .pmore{margin-top:14px;border-top:1px solid var(--line-soft);padding-top:14px;}
  .pmore summary{
    cursor:pointer;font-size:14px;color:var(--dim);
    list-style:none;display:inline-flex;align-items:center;gap:8px;
  }
  .pmore summary::-webkit-details-marker{display:none;}
  .pmore summary::before{content:"+";color:var(--ac);font-size:15px;line-height:1;}
  .pmore[open] summary::before{content:"\2013";}
  .pmore summary:hover{color:#e6ded6;}
  .pmore p{margin:12px 0 0;font-size:14.5px;line-height:1.7;color:#b8afa6;}

  /* ---- form dang ky ---- */
  .reg{
    max-width:1180px;margin:0 auto;border:1px solid var(--line);
    border-radius:4px;overflow:hidden;
    background:linear-gradient(180deg,rgba(255,255,255,.02),rgba(255,255,255,0));
    display:grid;grid-template-columns:1.1fr .9fr;
  }
  .reg-form{padding:clamp(26px,4vw,52px);border-right:1px solid var(--line);}
  .reg-pay{
    padding:clamp(26px,4vw,52px);display:flex;flex-direction:column;
    align-items:center;text-align:center;
    background:radial-gradient(420px 320px at 70% 0%, rgba(255,122,26,.10), transparent 65%);
  }
  .reg-form label{
    display:block;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;
    color:var(--dim);margin-bottom:8px;
  }
  .reg-form input{
    width:100%;padding:14px 16px;background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.12);border-radius:4px;
    color:#fff;font-size:15px;font-family:inherit;outline:none;
  }
  .reg-form input:focus{border-color:rgba(255,122,26,.55);}
  .reg-row{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
  .reg-field{margin-bottom:16px;}
  .pills{display:flex;flex-wrap:wrap;gap:10px;}
  .pill{
    padding:11px 17px;border-radius:40px;background:rgba(255,255,255,.04);
    border:1px solid rgba(255,255,255,.14);color:#cfc6bd;
    font-size:13px;font-weight:500;cursor:pointer;font-family:inherit;
  }
  .pill[aria-pressed="true"]{
    border-color:var(--ac);background:rgba(255,122,26,.14);color:#fff;
  }
  .reg-submit{
    margin-top:8px;width:100%;padding:16px;border-radius:44px;
    background:var(--ac);border:none;color:#140c06;
    font-family:'Unbounded',sans-serif;font-size:15px;font-weight:600;
    letter-spacing:2px;text-transform:uppercase;cursor:pointer;
    box-shadow:0 12px 30px rgba(226,45,15,.34);
  }
  .reg-err{display:none;margin:12px 0 0;color:#ff9c6b;font-size:14px;}
  .reg-done{
    border:1px solid rgba(255,122,26,.4);border-radius:4px;padding:30px;
    background:rgba(255,122,26,.06);text-align:center;
  }
  @media (max-width:900px){
    .price-grid{grid-template-columns:1fr;}
    .reg{grid-template-columns:1fr;}
    .reg-form{border-right:0;border-bottom:1px solid var(--line);}
  }
  @media (max-width:560px){
    .reg-row{grid-template-columns:1fr;}
  }
  /* ---- trang hub: 2 the he ---- */
  .hubgrid{display:grid;grid-template-columns:1fr 1fr;gap:24px;}
  .hubcard{
    display:flex;flex-direction:column;text-decoration:none;color:inherit;
    border:1px solid var(--line);border-radius:4px;overflow:hidden;
    background:linear-gradient(180deg,rgba(255,255,255,.025),rgba(255,255,255,0));
    transition:transform .25s ease,border-color .25s ease;
  }
  .hubcard.hot{border-color:rgba(255,122,26,.34);background:linear-gradient(165deg,rgba(255,122,26,.10),rgba(226,45,15,.03) 55%,rgba(255,255,255,0));}
  .hubcard:hover{transform:translateY(-4px);border-color:rgba(255,122,26,.55);}
  .hubart{aspect-ratio:1/1;background:#050505;border-bottom:1px solid var(--line);}
  .hubart img{width:100%;height:100%;object-fit:contain;display:block;}
  .hubbody{padding:clamp(22px,3vw,32px);display:flex;flex-direction:column;flex:1;}
  .hubtop{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:18px;}
  .hubnum{
    font-family:'Unbounded',sans-serif;font-size:12.5px;font-weight:600;
    letter-spacing:2.4px;text-transform:uppercase;color:var(--dim);
  }
  .hubcard.hot .hubnum{color:var(--ac);}
  .hubdur{
    font-family:'Unbounded',sans-serif;font-size:13px;font-weight:600;
    color:var(--ac);white-space:nowrap;text-transform:uppercase;
  }
  .hubcard h3{margin:0 0 8px;font-size:clamp(20px,2.4vw,28px);}
  .hubsub{font-size:14.5px;line-height:1.65;color:#9a8f84;margin:0 0 20px;}
  .hubgo{
    margin-top:auto;padding-top:22px;
    font-family:'Unbounded',sans-serif;font-size:12.5px;font-weight:600;
    letter-spacing:1.6px;text-transform:uppercase;color:var(--ac);
  }

  /* ---- doi he ---- */
  .switch-box{
    display:flex;flex-wrap:wrap;align-items:center;gap:20px;
    padding:22px 26px;border-radius:4px;
    border:1px dashed rgba(255,255,255,.18);background:rgba(255,255,255,.02);
  }
  .switch-box>div{flex:1;min-width:260px;}
  .switch-label{
    display:block;font-family:'Unbounded',sans-serif;font-size:11px;
    letter-spacing:2.2px;text-transform:uppercase;color:var(--dim);margin-bottom:8px;
  }
  .switch-box p{margin:0;font-size:14.5px;line-height:1.7;color:#b8afa6;}
  .fit-list{max-width:720px;margin-top:6px;}
  .fit-list li{font-size:16px;}
  @media (max-width:820px){
    .hubgrid{grid-template-columns:1fr;}
    .switch-box .lxcta-ghost{width:100%;}
  }
  .pick{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:34px;}
  @media (max-width:900px){
    .lvl{grid-template-columns:1fr;gap:22px;}
    .lvl-art{max-width:420px;}
    .pick{grid-template-columns:1fr;}
  }
</style>
"""

# ==================================================================
#  3 trang: hub chọn hệ + 2 trang hệ riêng biệt
# ==================================================================

SITE_URL = "https://lxamstudio.com/"

PAGES = {
    "hub":  "lo-trinh.html",
    "auto": "lo-trinh-3d-automotive.html",
    "ai":   "lo-trinh-3d-ai.html",
}


def nav_links(active):
    items = [
        ("ve-chung-toi.html", "Về chúng tôi", None),
        ("index.html#portfolio", "Portfolio", None),
        ("blog.html", "Blog", None),
        ("hoc-vien.html", "Khu học viên", None),
        ("index.html#lienhe", "Liên hệ", None),
        ("khoa-hoc.html", "Khóa học", "hub"),
        ("nghe-nghiep.html", "Cơ hội nghề nghiệp", None),
    ]
    out = ""
    for href, label, key in items:
        cls = ' class="is-active"' if key == "hub" and active in ("hub", "auto", "ai") else ""
        out += '<a href="%s"%s>%s</a>' % (href, cls, label)
    return out


DRAWER = (
    '<a href="ve-chung-toi.html">Về chúng tôi</a>'
    '<a href="index.html#portfolio">Portfolio</a>'
    '<a href="blog.html">Blog</a>'
    '<a href="hoc-vien.html">Khu học viên</a>'
    '<a href="index.html#lienhe">Liên hệ</a>'
    '<a href="khoa-hoc.html">Khóa học</a>'
    '<a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>'
    '<a href="cam-nang.html">Cẩm nang</a>'
    '<a href="%s">Hệ 3D Automotive</a>'
    '<a href="%s">Hệ 3D × A.I</a>'
) % (PAGES["auto"], PAGES["ai"])


def head(title, desc, canonical, jsonld, og_image, active):
    return """<!DOCTYPE html>
<html lang="vi"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="LXAM Studio">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:image" content="%sassets/%s">
<meta property="og:url" content="%s%s">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="%s%s">
<link rel="stylesheet" href="assets/lx.css?v=den2">
<script type="application/ld+json">%s</script>
%s
</head>
<body>
<nav class="lxnav">
  <a class="lxlogo" href="index.html" aria-label="LXAM Studio">
    <img src="assets/logo-lxam.png" alt="LXAM" class="lxlogo-icon">
    <div class="lxwordmark">
      <div class="wm">LXAM</div>
      <div class="wm-sub">3D ART STUDIO</div>
    </div>
  </a>
  <div class="lxnav-links">%s</div>
  <div class="lxnav-actions">
    <a class="lxcta" href="#dangky">Giữ chỗ</a>
    <button class="lxburger" id="lxburger" aria-label="Menu" aria-expanded="false">≡</button>
  </div>
</nav>
<div class="lxdrawer" id="lxdrawer">
  %s
  <a class="lxcta" href="#dangky">Giữ chỗ →</a>
</div>
""" % (title, desc, title, desc, SITE_URL, og_image, SITE_URL, canonical,
       SITE_URL, canonical, jsonld, PAGE_CSS, nav_links(active), DRAWER)


# ---------------------------------------------------------------- FORM
HE_OPTS = [
    ("Hệ 3D Automotive", "Hệ 3D Automotive"),
    ("Hệ 3D × A.I", "Hệ 3D × A.I"),
    ("Chưa quyết", "Chưa quyết, cần tư vấn"),
]
GOI_OPTS = [
    ("tuhoc", "Tự học có chữa bài · 2,5tr", "Tự học · 2,5tr"),
    ("lop8tuan", "Lớp 8 tuần · 12tr", "Lớp 8 tuần · 12tr"),
    ("kemrieng", "Kèm riêng 1:1 · từ 15tr", "Kèm riêng 1:1 · từ 15tr"),
    ("tuvan", "Chưa chọn, cần tư vấn", "Cần tư vấn"),
]


def reg_form(title, line, he_default=""):
    he_pills = "".join(
        '<button type="button" class="pill" data-v="%s" aria-pressed="%s">%s</button>'
        % (v, "true" if v == he_default else "false", label)
        for v, label in HE_OPTS)
    goi_pills = "".join(
        '<button type="button" class="pill" data-k="%s" data-v="%s" aria-pressed="false">%s</button>'
        % (k, v, label) for k, v, label in GOI_OPTS)
    return """
  <section id="dangky" style="padding-top:0;">
    <div class="wrap">
      <div class="reg">
        <div class="reg-form">
          <p class="eyebrow">Đăng ký giữ chỗ</p>
          <h2 style="margin-bottom:12px;">%s</h2>
          <p style="font-size:14.5px;color:#9a8f84;margin:0 0 26px;">%s</p>

          <div id="lx-done" class="reg-done" hidden>
            <div style="font-family:'Unbounded',sans-serif;font-size:28px;font-weight:700;text-transform:uppercase;color:#fff;margin-bottom:8px;">Đã gửi ✓</div>
            <p style="font-size:14px;color:#bdb3a8;margin:0;line-height:1.55;">Cảm ơn bạn. LXAM Studio sẽ liên hệ sớm để xác nhận chỗ và hướng dẫn thanh toán.</p>
          </div>

          <form id="lx-form" novalidate>
            <div class="reg-field">
              <label>Bạn học hệ nào?</label>
              <div class="pills" id="lx-he" role="group">%s</div>
            </div>
            <div class="reg-field">
              <label>Cách học bạn muốn</label>
              <div class="pills" id="lx-goi" role="group">%s</div>
            </div>
            <div class="reg-field">
              <label for="lx-name">Họ và tên</label>
              <input id="lx-name" data-f="name" name="name" autocomplete="name" placeholder="Nguyễn Văn A">
            </div>
            <div class="reg-row reg-field">
              <div>
                <label for="lx-phone">Số điện thoại</label>
                <input id="lx-phone" data-f="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="09xx xxx xxx">
              </div>
              <div>
                <label for="lx-email">Email</label>
                <input id="lx-email" data-f="email" name="email" type="email" inputmode="email" autocomplete="email" placeholder="ban@email.com">
              </div>
            </div>
            <div class="reg-field">
              <label for="lx-fb">Facebook (không bắt buộc)</label>
              <input id="lx-fb" data-f="fb" name="fb" placeholder="fb.com/ban">
            </div>
            <button type="submit" id="lx-submit" class="reg-submit">Gửi đăng ký →</button>
            <p class="reg-err" id="lx-err"></p>
          </form>
        </div>

        <div class="reg-pay">
          <div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--dim);margin-bottom:6px;">Quét mã để chuyển khoản</div>
          <div style="font-family:'Unbounded',sans-serif;font-size:21px;font-weight:700;color:#fff;letter-spacing:1px;">LE XUAN ANH MINH</div>
          <div style="font-size:14px;color:var(--ac);letter-spacing:2px;font-weight:600;margin:4px 0 22px;">TECHCOMBANK · 7447 0088 8888</div>
          <div style="padding:10px;border-radius:4px;background:var(--ac);">
            <img src="assets/cef4dd06.webp" alt="Mã QR chuyển khoản Techcombank LXAM Studio" style="width:min(260px,62vw);height:auto;display:block;border-radius:4px;" width="700" height="788" loading="lazy" decoding="async">
          </div>
          <div style="margin-top:24px;display:flex;align-items:baseline;gap:8px;justify-content:center;">
            <span style="font-size:15px;color:var(--dim);">Phí giữ chỗ</span>
            <span style="font-family:'Unbounded',sans-serif;font-size:28px;font-weight:700;color:#fff;">5.000.000<span style="font-size:16px;color:var(--ac);">đ</span></span>
          </div>
          <div style="margin-top:6px;font-size:12px;color:var(--faint);">Nội dung CK: <span style="color:#cfc6bd;">[Họ tên] giu cho LXAMStudio</span></div>
        </div>
      </div>
    </div>
  </section>
""" % (title, line, he_pills, goi_pills)


# ---------------------------------------------------------------- SWITCH
def switch(href, name, line):
    return """
  <section style="padding-top:0;">
    <div class="wrap">
      <div class="switch-box">
        <div>
          <span class="switch-label">Hệ này chưa hợp?</span>
          <p>%s</p>
        </div>
        <a class="lxcta-ghost" href="%s">Xem %s →</a>
      </div>
    </div>
  </section>
""" % (line, href, name)


def fit_card(title, items):
    lis = "".join("<li>%s</li>" % x for x in items)
    return """
  <section>
    <div class="wrap">
      <p class="eyebrow">Hệ này hợp với ai</p>
      <h2>%s</h2>
      <ul class="mod-list fit-list">%s</ul>
    </div>
  </section>
""" % (title, lis)


# ---------------------------------------------------------------- PAGE BODIES
BODY_AUTO = """
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow"><a href="lo-trinh.html" style="color:inherit;text-decoration:none;">Lộ trình học</a> · Hệ 01</p>
      <h1>Hệ 3D Automotive</h1>
      <p class="lead" style="max-width:740px;">Lộ trình 3D truyền thống, đi từ thao tác đầu tiên trong Blender đến một
      TVC ô tô hoàn chỉnh. Dành cho người muốn làm nghề bằng chính tay mình: dựng, chiếu sáng, render, dựng phim.</p>
    </div>
  </section>

  <section id="automotive">
    <div class="wrap">
      <div class="track-head">
        <span class="track-num">Nội dung học</span>
        <span class="track-dur">Blender · 3 đến 4 tháng</span>
      </div>
      <div class="track">
        %s
        %s
      </div>
      %s
    </div>
  </section>
""" % (T1_BEGINNER, T1_MASTER, CTA_1) + fit_card(
    "Chọn hệ này nếu…",
    ["Bạn muốn <strong>làm nghề 3D</strong>, nhận job dựng và render.",
     "Bạn thích kiểm soát từng chi tiết trong khung hình.",
     "Bạn nhắm portfolio xin việc studio hoặc nhận khách trực tiếp.",
     "Bạn sẵn sàng bỏ 3 đến 4 tháng để có kỹ năng dùng được nhiều năm."]
) + switch(PAGES["ai"], "hệ 3D × A.I",
           "Nếu bạn cần hình nhanh cho marketing hoặc bán hàng hơn là làm nghề dựng, "
           "hệ 3D × A.I hợp với bạn hơn.") + reg_form(
    "Giữ chỗ hệ 3D Automotive",
    "Mỗi lớp giới hạn suất để còn sửa bài được cho từng người. Để lại thông tin, "
    "tôi liên hệ tư vấn trong 24h trước khi bạn quyết định.", "Hệ 3D Automotive") + "</main>\n"


BODY_AI = """
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow"><a href="lo-trinh.html" style="color:inherit;text-decoration:none;">Lộ trình học</a> · Hệ 02</p>
      <h1>Hệ 3D × A.I</h1>
      <p class="lead" style="max-width:740px;">Dành cho người cần AI trong công việc hình ảnh: marketing, thương mại
      điện tử, content sản phẩm. Vẫn học 3D trước, vì AI chỉ nghe lời người biết mình muốn gì, rồi mới ghép AI
      vào để nhân sản lượng lên.</p>
    </div>
  </section>

  <section id="ai">
    <div class="wrap">
      <div class="track-head">
        <span class="track-num">Nội dung học</span>
        <span class="track-dur">Blender + AI · 4 tháng</span>
      </div>
      <div class="track">
        %s
        %s
      </div>
      %s
    </div>
  </section>
""" % (T2_BASIC, T2_AI, CTA_2) + fit_card(
    "Chọn hệ này nếu…",
    ["Bạn đang làm <strong>marketing, bán hàng, content</strong> và cần hình nhanh.",
     "Bạn cần nhiều biến thể của cùng một sản phẩm, liên tục.",
     "Bạn muốn hiểu AI đủ sâu để nó ra đúng ý, không phải bấm may rủi.",
     "Bạn cần kết quả trong vài tháng, không phải vài năm."]
) + switch(PAGES["auto"], "hệ 3D Automotive",
           "Nếu bạn muốn làm nghề dựng và render bằng chính tay mình, "
           "hệ 3D Automotive mới là chỗ của bạn.") + reg_form(
    "Giữ chỗ hệ 3D × A.I",
    "Mỗi lớp giới hạn suất để còn sửa bài được cho từng người. Để lại thông tin, "
    "tôi liên hệ tư vấn trong 24h trước khi bạn quyết định.", "Hệ 3D × A.I") + "</main>\n"


def hub_card(href, num, name, dur, h3, sub, items, img, alt, hot):
    lis = "".join("<li>%s</li>" % x for x in items)
    return """
      <a class="hubcard%s" href="%s">
        <div class="hubart"><img src="%s" alt="%s" loading="lazy" width="1200" height="1200"></div>
        <div class="hubbody">
          <div class="hubtop">
            <span class="hubnum">%s</span>
            <span class="hubdur">%s</span>
          </div>
          <h3>%s</h3>
          <p class="hubsub">%s</p>
          <ul class="mod-list">%s</ul>
          <span class="hubgo">Xem nội dung &amp; học phí →</span>
        </div>
      </a>""" % (" hot" if hot else "", href, img, alt, name, dur, h3, sub, lis)


BODY_HUB = """
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow">Lộ trình học</p>
      <h1>Hai lộ trình,<br>hai đích đến khác nhau</h1>
      <p class="lead" style="max-width:740px;">LXAM Academy chia chương trình thành hai hệ đào tạo riêng biệt, mỗi hệ
      một trang riêng. Một hệ đi sâu vào 3D thương mại tới tận TVC ô tô. Một hệ dành cho người cần đưa AI vào quy
      trình hình ảnh của mình. Chọn theo việc bạn muốn làm được gì, không phải theo cái nào nghe mới hơn.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="hubgrid">
        %s
        %s
      </div>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="wrap">
      <p style="color:#9a8f84;font-size:15px;max-width:720px;">Chưa chắc mình hợp hệ nào? Đọc thêm bài
      <a href="blog-hoc-blender-3d-bao-lau.html" style="color:#ff7a1a;">học Blender bao lâu thì đi làm được</a>,
      hoặc để lại thông tin bên dưới, tôi xem qua rồi nói thẳng bạn nên vào hệ nào.</p>
    </div>
  </section>
""" % (
    hub_card(PAGES["auto"], "01", "Hệ 01 · 3D Automotive", "3 đến 4 tháng",
             "Làm nghề 3D bằng tay mình",
             "Từ thao tác đầu tiên trong Blender tới một TVC ô tô hoàn chỉnh.",
             ["Modeling · Lighting · Rendering · Animation",
              "Hard-surface nâng cao, car modeling Lamborghini Veneno",
              "Đầu ra là một TVC ô tô do bạn tự dựng",
              "Học phí từ 2,5tr tuỳ cách học"],
             "assets/lo-trinh-automotive-masterclass.jpg",
             "Hệ 3D Automotive: lộ trình Blender tới TVC ô tô tại LXAM Academy", False),
    hub_card(PAGES["ai"], "02", "Hệ 02 · 3D × A.I", "4 tháng",
             "Đưa AI vào quy trình hình ảnh",
             "Học 3D nền tảng trước, rồi ghép AI vào để nhân sản lượng lên.",
             ["3 tháng 3D Basic, 1 tháng A.I Advance",
              "Tư duy prompt, góc máy và ánh sáng với AI",
              "Nano Banana Pro · Seedance · Kling 3.0",
              "Học phí từ 2,5tr tuỳ cách học"],
             "assets/lo-trinh-ai-advance.jpg",
             "Hệ 3D × A.I: khoá AI cho người làm hình ảnh tại LXAM Academy", True),
) + reg_form(
    "Chưa biết chọn hệ nào?",
    "Để lại thông tin, tôi gọi tư vấn và nói thẳng bạn nên vào hệ nào, trước khi bạn đóng bất kỳ khoản nào."
) + "</main>\n"


FORM_JS = """
<script>
(function(){
  var ENDPOINT = 'https://script.google.com/macros/s/AKfycbyxhiWlUEYx4x-grFV-DImPZyea2Ca1iz2JFl3XjcpLXY4abll4eW1Ht0Bn9CstVL3Oww/exec';
  var form = document.getElementById('lx-form');
  if(!form) return;
  var errEl = document.getElementById('lx-err');
  var doneEl = document.getElementById('lx-done');

  function group(id){ return document.getElementById(id); }
  function pick(g, val, byKey){
    if(!g) return;
    var bs = g.querySelectorAll('.pill'), hit = null;
    for(var i=0;i<bs.length;i++){
      var m = byKey ? (bs[i].getAttribute('data-k') === val) : (bs[i].getAttribute('data-v') === val);
      if(m) hit = bs[i];
    }
    if(!hit) return;
    for(var j=0;j<bs.length;j++){ bs[j].setAttribute('aria-pressed','false'); }
    hit.setAttribute('aria-pressed','true');
  }
  function chosen(g){
    if(!g) return '';
    var b = g.querySelector('.pill[aria-pressed="true"]');
    return b ? (b.getAttribute('data-v') || '') : '';
  }

  // ---- bam the gia -> mo rong ra, dong cac the khac ----
  document.querySelectorAll('.price-grid').forEach(function(grid){
    grid.addEventListener('click', function(ev){
      if(ev.target.closest && ev.target.closest('a')) return;
      var card = ev.target.closest ? ev.target.closest('.pcard') : null;
      if(!card || !grid.contains(card)) return;
      var wasOpen = card.classList.contains('open');
      grid.querySelectorAll('.pcard').forEach(function(c){
        c.classList.remove('open');
        var d = c.querySelector('.pdetail'); if(d) d.hidden = true;
        var t = c.querySelector('.ptoggle'); if(t) t.setAttribute('aria-expanded','false');
      });
      if(!wasOpen){
        card.classList.add('open');
        var d2 = card.querySelector('.pdetail'); if(d2) d2.hidden = false;
        var t2 = card.querySelector('.ptoggle'); if(t2) t2.setAttribute('aria-expanded','true');
      }
    });
  });

  ['lx-he','lx-goi'].forEach(function(id){
    var g = group(id);
    if(!g) return;
    g.addEventListener('click', function(ev){
      var b = ev.target.closest ? ev.target.closest('.pill') : null;
      if(!b || !g.contains(b)) return;
      var bs = g.querySelectorAll('.pill');
      for(var i=0;i<bs.length;i++){ bs[i].setAttribute('aria-pressed','false'); }
      b.setAttribute('aria-pressed','true');
    });
  });

  document.addEventListener('click', function(ev){
    var a = ev.target.closest ? ev.target.closest('a[data-he]') : null;
    if(!a) return;
    pick(group('lx-he'), a.getAttribute('data-he'), false);
    var k = a.getAttribute('data-goi');
    if(k) pick(group('lx-goi'), k, true);
    else pick(group('lx-goi'), 'tuvan', true);
  }, true);

  function val(k){
    var el = form.querySelector('[data-f="'+k+'"]');
    return el ? String(el.value == null ? '' : el.value).trim() : '';
  }
  function fail(msg){ if(errEl){ errEl.textContent = msg; errEl.style.display='block'; } }

  form.addEventListener('submit', function(ev){
    ev.preventDefault();
    if(errEl) errEl.style.display = 'none';
    var name = val('name'), phone = val('phone'), email = val('email');
    if(!name) return fail('Bạn điền giúp tên nhé.');
    if(phone.replace(/[^0-9]/g,'').length < 9) return fail('Số điện thoại trông chưa đúng.');
    if(!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email)) return fail('Email trông chưa đúng, kiểm tra lại giúp mình.');

    var btn = document.getElementById('lx-submit');
    if(btn){ btn.disabled = true; btn.textContent = 'Đang gửi…'; }

    var he = chosen(group('lx-he')) || 'Chưa chọn hệ';
    var goi = chosen(group('lx-goi')) || 'Chưa chọn gói';

    var data = new URLSearchParams();
    data.append('name',  name);
    data.append('phone', phone);
    data.append('email', email);
    data.append('fb',    val('fb'));
    data.append('pkg',   he + ' · ' + goi);
    data.append('src',   location.href);

    var sent = false;
    try { if (navigator.sendBeacon) sent = navigator.sendBeacon(ENDPOINT, data); } catch(err){}
    if(!sent){
      try { fetch(ENDPOINT, { method:'POST', mode:'no-cors', body:data, keepalive:true }); } catch(err){}
    }
    form.hidden = true;
    if(doneEl) doneEl.hidden = false;
  }, false);
})();
</script>
"""

FOOTER = """<footer class="lxfooter">
  <div class="lxfoot">
    <div>
      <a class="lxlogo" href="index.html" style="margin-bottom:18px;">
        <img src="assets/logo-lxam.png" alt="LXAM" style="width:40px;height:40px;">
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
        <a href="lo-trinh-3d-automotive.html">Hệ 3D Automotive</a>
        <a href="lo-trinh-3d-ai.html">Hệ 3D × A.I</a>
        <a href="blog.html">Blog</a>
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
    <span>© %d LXAM Studio. All rights reserved.</span>
    <span>3D · Modeling · Lighting · Rendering · Animation · TVC · AI</span>
  </div>
</footer>
<script>
(function(){
  var b=document.getElementById('lxburger'), d=document.getElementById('lxdrawer');
  if(!b||!d) return;
  b.addEventListener('click', function(){
    var open=d.classList.toggle('open');
    b.setAttribute('aria-expanded', open?'true':'false');
    b.textContent = open ? '\\u2715' : '\\u2261';
    document.body.style.overflow = open ? 'hidden' : '';
  });
  d.addEventListener('click', function(e){
    if(e.target.tagName==='A'){ d.classList.remove('open'); b.textContent='\\u2261'; document.body.style.overflow=''; }
  });
})();
</script>
%s
<script src="assets/lx-ui.js?v=den2" defer></script>
</body></html>
""" % (YEAR, FORM_JS)


# ---------------------------------------------------------------- JSON-LD
PROV = {"@type": "Organization", "name": "LXAM Academy", "url": SITE_URL}


def crumbs(name, url):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": SITE_URL},
        {"@type": "ListItem", "position": 2, "name": "Lộ trình học", "item": SITE_URL + "lo-trinh.html"},
        {"@type": "ListItem", "position": 3, "name": name, "item": SITE_URL + url},
    ]}


def course(name, desc, url, months):
    return {"@type": "Course", "name": name, "description": desc, "url": SITE_URL + url,
            "provider": PROV, "inLanguage": "vi-VN",
            "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "online",
                                  "courseWorkload": "P%dM" % months}}


JSONLD_AUTO = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "ItemList", "name": "Hệ 3D Automotive tại LXAM Academy", "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": course(
            "The Blender Automotive Beginner",
            "Modeling 2 tháng + Rendering 1 tháng. Dựng và render được sản phẩm, xe cơ bản trong Blender.",
            PAGES["auto"], 3)},
        {"@type": "ListItem", "position": 2, "item": course(
            "The Blender Automotive Masterclass",
            "Modeling nâng cao 2 tháng + TVC 1 tháng + Rendering 1 tháng. Hard-surface nâng cao, car modeling, rigging, animation, VFX, SFX.",
            PAGES["auto"], 4)},
    ]},
    crumbs("Hệ 3D Automotive", PAGES["auto"]),
]}, ensure_ascii=False)

JSONLD_AI = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "ItemList", "name": "Hệ 3D × A.I tại LXAM Academy", "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": course(
            "3D Basic: Blender Foundation",
            "3 tháng nền tảng: modeling hard-surface, material & lighting, rendering, tư duy hình ảnh.",
            PAGES["ai"], 3)},
        {"@type": "ListItem", "position": 2, "item": course(
            "A.I Advance: AI × Visual",
            "1 tháng: tư duy prompt, góc máy và ánh sáng với AI, workflow 3D × AI, ứng dụng Nano Banana Pro, Seedance, Kling 3.0.",
            PAGES["ai"], 1)},
    ]},
    crumbs("Hệ 3D × A.I", PAGES["ai"]),
]}, ensure_ascii=False)

JSONLD_HUB = json.dumps({"@context": "https://schema.org", "@type": "ItemList",
    "name": "Hai hệ đào tạo tại LXAM Academy", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Hệ 3D Automotive",
         "url": SITE_URL + PAGES["auto"]},
        {"@type": "ListItem", "position": 2, "name": "Hệ 3D × A.I",
         "url": SITE_URL + PAGES["ai"]},
    ]}, ensure_ascii=False)


# ---------------------------------------------------------------- WRITE
OUT = [
    (PAGES["hub"],
     "Lộ trình học Blender 3D và học phí | LXAM Studio",
     "Hai hệ đào tạo riêng tại LXAM Academy: 3D Automotive đi từ Blender tới TVC ô tô, và 3D × A.I cho người cần AI trong công việc hình ảnh. Kèm học phí từng hệ.",
     JSONLD_HUB, "lo-trinh-automotive-masterclass.jpg", BODY_HUB, "hub"),
    (PAGES["auto"],
     "Hệ 3D Automotive: học phí & lộ trình | LXAM",
     "Lộ trình 3D Automotive đi từ Blender con số 0 tới một TVC ô tô hoàn chỉnh: nội dung từng tháng, ba cách học, số vòng sửa bài và học phí của từng hình thức.",
     JSONLD_AUTO, "lo-trinh-automotive-masterclass.jpg", BODY_AUTO, "auto"),
    (PAGES["ai"],
     "Hệ 3D × A.I: học phí & lộ trình | LXAM",
     "Lộ trình 3D × A.I: 3 tháng 3D nền tảng cộng 1 tháng A.I Advance với prompt, ánh sáng cùng AI và workflow kết hợp 3D với AI. Nội dung từng tháng và học phí.",
     JSONLD_AI, "lo-trinh-ai-advance.jpg", BODY_AI, "ai"),
]

for fname, title, desc, ld, og, body, active in OUT:
    html = head(title, desc, fname, ld, og, active) + body + FOOTER
    with open(os.path.join(SITE, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %-28s %6d B" % (fname, len(html.encode("utf-8"))))
