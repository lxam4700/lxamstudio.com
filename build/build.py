#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh các trang phụ của lxamstudio.com (Về chúng tôi, Blog, Khu học viên).
Chạy:  python3 /home/claude/build/build.py
Thêm bài blog mới: thêm 1 dict vào POSTS rồi chạy lại."""

import os, html, datetime, re, unicodedata

SITE = "/home/claude/site"
YEAR = datetime.date.today().year
ENDPOINT = "https://script.google.com/macros/s/AKfycbyxhiWlUEYx4x-grFV-DImPZyea2Ca1iz2JFl3XjcpLXY4abll4eW1Ht0Bn9CstVL3Oww/exec"

NAV_ITEMS = [
    ("ve-chung-toi.html", "Về chúng tôi", "about"),
    ("index.html#portfolio", "Portfolio", "portfolio"),
    ("blog.html", "Blog", "blog"),
    ("du-an-hoc-vien.html", "Bài học viên", "duanhocvien"),
    ("hoc-vien.html", "Khu học viên", "hocvien"),
    ("index.html#lienhe", "Liên hệ", "lienhe"),
    ("khoa-hoc.html", "Khóa học", "khoahoc"),
    ("nghe-nghiep.html", "Cơ hội nghề nghiệp", "nghenghiep"),
]


def head(title, desc, active, extra_css="", canonical="", og_image="", jsonld="", og_type="website", published=""):
    canonical_full = "https://lxamstudio.com/" + (canonical or "")
    og_image_full = "https://lxamstudio.com/" + (og_image or "assets/hero-p.jpg")
    pub_meta = ('\n<meta property="article:published_time" content="%s">' % published) if published else ""
    return f"""<!DOCTYPE html>
<html lang="vi"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{og_type}">{pub_meta}
<meta property="og:site_name" content="LXAM Studio">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{og_image_full}">
<meta property="og:url" content="{canonical_full}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{canonical_full}">
<link rel="stylesheet" href="assets/lx.css?v=den3">
{jsonld}
{extra_css}
</head>
<body>
{nav(active)}
"""


def nav(active):
    ACT = ' class="is-active"'
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ACT if k == active else "", html.escape(t))
        for h, t, k in NAV_ITEMS
    )
    drawer = "".join(
        f'<a href="{h}">{html.escape(t)}</a>' for h, t, k in NAV_ITEMS
    )
    return f"""<nav class="lxnav">
  <a class="lxlogo" href="index.html" aria-label="LXAM Studio">
    <img src="assets/logo-lxam.png" alt="LXAM" class="lxlogo-icon" width="256" height="256" decoding="async">
    <div class="lxwordmark">
      <div class="wm">LXAM</div>
      <div class="wm-sub">3D ART STUDIO</div>
    </div>
  </a>
  <div class="lxnav-links">{links}</div>
  <div class="lxnav-actions">
    <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ</a>
    <button class="lxburger" id="lxburger" aria-label="Menu" aria-expanded="false">≡</button>
  </div>
</nav>
<div class="lxdrawer" id="lxdrawer">
  {drawer}
  <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ →</a>
</div>
"""


FOOTER = f"""<footer class="lxfooter">
  <div class="lxfoot">
    <div>
      <a class="lxlogo" href="index.html" style="margin-bottom:18px;">
        <img src="assets/logo-lxam.png" alt="LXAM" width="40" height="40" loading="lazy" decoding="async" style="width:40px;height:40px;">
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
        <a href="du-an-hoc-vien.html">Bài học viên</a>
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
    <span>3D · Modeling · Lighting · Rendering · Animation · TVC</span>
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


def write(name, content):
    path = os.path.join(SITE, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name, len(content), "bytes")


# ---------------------------------------------------------------- ABOUT
ABOUT_BODY = """
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow">Về chúng tôi</p>
      <h1>Chúng tôi làm 3D<br>như làm nghệ thuật thị giác</h1>
      <p class="lead" style="max-width:780px;">LXAM Studio là một studio visual 3D ở Việt Nam. Chúng tôi làm TVC, render sản phẩm, phối cảnh sự kiện và animation kỹ thuật, rồi dạy lại đúng cái nghề đó. Mục tiêu dài hạn thì chỉ có một: đưa tên Việt Nam lên bản đồ 3D motion art thế giới.</p>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="grid4">
        <div class="card"><p class="stat grad">10</p><p class="stat-label">Năm làm 3D &amp; Multimedia</p></div>
        <div class="card"><p class="stat grad">7</p><p class="stat-label">Kỹ năng trong lộ trình</p></div>
        <div class="card"><p class="stat grad">1:1</p><p class="stat-label">Kèm trực tiếp, không lớp đông</p></div>
        <div class="card"><p class="stat grad">12</p><p class="stat-label">Tháng đồng hành sau khoá</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="grid2" style="gap:48px;align-items:start;">
        <div>
          <p class="eyebrow">Thứ chúng tôi đuổi theo</p>
          <h2>Việt Nam không thiếu người có mắt</h2>
        </div>
        <div>
          <p>Thiếu là một chỗ để luyện con mắt đó thành nghề. Và thiếu người đủ lì để không hạ chuẩn khi thị trường trả giá thấp, thứ làm hỏng nhiều người giỏi hơn cả sự thiếu tài năng.</p>
          <p>Trong ngành hình ảnh, cái tên Việt Nam thường xuất hiện ở ô “nhân sự gia công”, hiếm khi ở ô tác giả. Không phải vì tay nghề, mà vì hiếm ai ở lại đủ lâu với một tiêu chuẩn để tạo ra thứ người khác phải nhìn hai lần.</p>
          <p><strong style="color:#fff;">Chúng tôi muốn đổi cái ô đó.</strong> Không phải bằng khẩu hiệu, mà bằng cách làm từng shot đúng đến mức không cần hỏi nó được làm ở đâu, và bằng cách để lại cách làm đó cho lớp sau.</p>
        </div>
      </div>
    </div>
  </section>

  <section style="background:rgba(255,255,255,.014);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
    <div class="wrap">
      <p class="eyebrow">Quan điểm</p>
      <h2 style="max-width:900px;">Phần mềm chỉ là cái đục</h2>
      <div class="grid2" style="gap:48px;align-items:start;margin-top:22px;">
        <div>
          <p>Một người mới thường nghĩ nghề này là nghề học phần mềm. Học hết Blender là xong. Nhưng phần mềm chỉ làm được đúng một việc: biến ý định thành pixel. Nó không có ý kiến gì về việc ý định đó có đáng hay không.</p>
          <p>Thứ quyết định một khung hình đứng được là những thứ không có nút bấm: ánh sáng đặt ở đâu, để lại bao nhiêu bóng tối, chuyển động chậm lại ở nhịp nào, và biết dừng lại đúng lúc. Bớt đi thường mạnh hơn thêm vào, nhưng phải làm hỏng vài chục lần mới tin được điều đó.</p>
        </div>
        <div>
          <p>Vì vậy chúng tôi không tự gọi việc mình làm là “làm 3D”. Gọi đúng hơn là nghệ thuật thị giác: dùng hình để nói một điều gì đó, và dùng công cụ nào cũng được miễn nói được.</p>
          <p>Cái đó khó dạy hơn phím tắt rất nhiều, và cũng là lý do duy nhất khiến việc mở lớp đáng làm. Phím tắt thì YouTube có sẵn, miễn phí, và dạy tốt hơn chúng tôi.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="founder" style="background:linear-gradient(180deg,rgba(255,122,26,.045),transparent 34%),rgba(255,255,255,.022);border-top:1px solid rgba(255,122,26,.22);border-bottom:1px solid var(--line);">
    <div class="wrap">
      <p class="eyebrow">Founder</p>

      <div class="founder">
        <div class="founder-media">
          <img class="founder-portrait" src="assets/founder-le-xuan-anh-minh.webp" alt="Chân dung Lê Xuân Anh Minh, founder LXAM Studio, ảnh đen trắng chụp nghiêng, đeo kính râm, mặc áo varsity, nền tối có dải sáng" width="1200" height="1500" loading="lazy" decoding="async">
          <p class="founder-cap">Lê Xuân Anh Minh &middot; TP. Hồ Chí Minh</p>
        </div>

        <div>
          <h2 class="founder-name">Lê Xuân<br>Anh Minh</h2>
          <p class="founder-role">Founder &amp; Creative Director &middot; LXAM Studio</p>

          <p class="founder-say">Bạn đang không làm 3D, bạn đang là đấng tạo hoá toàn năng trong ngôi đền tâm trí của bạn.</p>

          <p style="margin-top:28px;">Năm lớp 11 tôi đứng bét lớp. Không phải gần cuối, là cuối. Ở một tỉnh nghèo miền Trung, kết quả đó gần như đồng nghĩa với việc chỗ ngồi của bạn trong đời đã được xếp sẵn: một nghề tay chân, một thị trấn, và hết.</p>

          <p>Vài năm sau tôi bưng cà phê, hai mươi nghìn một giờ. Ca đứng liên tục, hết ca thì chân gần như không còn cảm giác. Giãn tĩnh mạch đến sớm hơn tuổi. Có những tối về phòng, việc đầu tiên làm được không phải là mở máy, mà là nằm gác chân lên tường chờ máu chảy ngược lại.</p>

          <p>Thứ giữ tôi lại không phải quyết tâm gì to tát. Là một cái máy cũ và Blender, phần mềm miễn phí nên không phải xin phép ai. Tôi muốn dựng một chiếc xe. Chỉ vậy thôi. Dựng hỏng, dựng lại, trong đúng những giờ lẽ ra phải ngủ.</p>

          <p>Vào nghề sớm hơn dự định, năm ba đại học, công cụ trong tay vẫn chỉ có Blender và vài phần mềm Adobe. Không studio đứng sau, không ai cầm tay chỉ việc. Mọi thứ học được đều đến từ việc nhận job, làm hỏng, sửa, rồi làm lại cho tới khi khách gật đầu.</p>

          <p>Hiện tại tôi là <strong style="color:#fff;">Multimedia Director của KHP</strong>, tập đoàn trang sức phân phối trực tiếp cho PNJ và xuất khẩu ra thị trường quốc tế, song song với việc vận hành LXAM Studio nhận các dự án TVC và hình ảnh thương mại. Hai vai trò đó nuôi nhau: con mắt của người duyệt bài cho biết một portfolio còn thiếu gì, còn việc trực tiếp làm job giữ cho bài giảng không dạy những thứ đã lỗi thời.</p>

          <p>Điều dẫn tới việc mở lớp không phải vì thiếu khoá học Blender trên mạng, có quá nhiều là đằng khác. Mà vì gần như không khoá nào trả lời được câu hỏi thật sự khó: <strong style="color:#fff;">làm sao đi từ chỗ biết dùng phần mềm đến chỗ có người trả tiền cho sản phẩm của bạn.</strong></p>

          <p>Tôi kể chuyện này không phải để ai thấy nó hay. Kể vì nó là bằng chứng cho một điều rất khô khan: điểm xuất phát quyết định ít hơn nhiều so với việc bạn có chịu làm lại lần thứ mười hay không. Thằng bé đứng bét lớp vẫn học được cái nghề này. Tôi là ví dụ, và tôi không phải ví dụ đặc biệt.</p>

          <div class="founder-meta">
            <span>Multimedia Director &middot; tập đoàn trang sức KHP</span>
            <span>10 năm 3D &amp; Multimedia</span>
            <span>Blender-first pipeline</span>
            <span>TVC &middot; Sản phẩm &middot; Event</span>
            <span>Kèm 1 kèm 1</span>
          </div>

          <div class="founder-sign">
            <b>lxam</b>
            <em>Founder, LXAM Studio</em>
          </div>
        </div>
      </div>

      <div class="arc">
        <div class="arc-i"><p class="arc-k">Năm lớp 11</p><p class="arc-v">Đứng bét lớp</p></div>
        <div class="arc-i"><p class="arc-k">20.000đ một giờ</p><p class="arc-v">Ca bưng cà phê</p></div>
        <div class="arc-i"><p class="arc-k">Năm ba đại học</p><p class="arc-v">Job 3D đầu tiên</p></div>
        <div class="arc-i"><p class="arc-k">Hôm nay</p><p class="arc-v">Multimedia Director &amp; Founder</p></div>
      </div>

      <div style="margin-top:clamp(56px,7vw,96px);">
        <p class="eyebrow">Hệ triết lý</p>
        <h2 style="max-width:900px;">Bốn điều đặt nền cho mọi thứ chúng tôi làm</h2>

        <div class="tenets">
          <div class="tenet">
            <p class="tenet-n">01</p>
            <div>
              <h3>Phần mềm chỉ là cái đục</h3>
              <p>Công cụ làm được đúng một việc: biến ý định thành pixel. Nó không có ý kiến gì về việc ý định đó có đáng hay không. Thứ quyết định một khung hình đứng được là những thứ không có nút bấm.</p>
            </div>
          </div>
          <div class="tenet">
            <p class="tenet-n">02</p>
            <div>
              <h3>Bớt đi thường mạnh hơn thêm vào</h3>
              <p>Một nguồn sáng đặt đúng chỗ ăn đứt sáu nguồn đặt cho đủ. Nhưng phải làm hỏng vài chục lần mới thật sự tin được điều đó, nên nó là thứ phải luyện chứ không phải thứ để nghe.</p>
            </div>
          </div>
          <div class="tenet">
            <p class="tenet-n">03</p>
            <div>
              <h3>Không hạ chuẩn theo giá</h3>
              <p>Thứ làm hỏng người giỏi trong ngành này hiếm khi là thiếu tài năng. Thường là quen tay với mức vừa đủ để khách duyệt. Một tiêu chuẩn chỉ có giá trị khi nó không đổi vào ngày ngân sách thấp.</p>
            </div>
          </div>
          <div class="tenet">
            <p class="tenet-n">04</p>
            <div>
              <h3>Dạy lại đúng cái nghề đang làm</h3>
              <p>Bài giảng lấy chất liệu từ job đã lên sóng, kèm cả phương án bị khách gạt đi và lý do. Không dạy quy trình trong sách, vì quy trình trong sách không có đoạn khách đổi ý ở phút cuối.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Cách chúng tôi dạy</p>
      <h2>Bốn nguyên tắc, không thoả hiệp</h2>
      <div class="grid2" style="margin-top:36px;">
        <div class="card">
          <h3>Học bằng dự án, không học bằng nút bấm</h3>
          <p style="margin:0;">Mỗi kỹ năng gắn với một sản phẩm cụ thể bạn phải hoàn thành. Bạn không xem tôi làm rồi gật đầu. Bạn làm, tôi sửa, bạn làm lại. Kết thúc lộ trình bạn cầm về portfolio, không phải một xấp file bài tập.</p>
        </div>
        <div class="card">
          <h3>Sửa bài đến nơi đến chốn</h3>
          <p style="margin:0;">Feedback không dừng ở "đẹp rồi" hay "chưa ổn". Mỗi lần sửa là chỉ rõ sai ở đâu, vì sao sai, và sửa thế nào, kèm file so sánh trước/sau để bạn thấy được sự khác biệt bằng mắt chứ không phải bằng lời.</p>
        </div>
        <div class="card">
          <h3>Blender thuần: chi phí phần mềm bằng 0</h3>
          <p style="margin:0;">Toàn bộ lộ trình chạy trên Blender, phần mềm miễn phí và mã nguồn mở. Bạn không cần license vài chục triệu để bắt đầu. Khi cần, chúng tôi bổ sung công cụ hậu kỳ, nhưng lõi nghề nằm ở tư duy, không nằm ở giá phần mềm.</p>
        </div>
        <div class="card">
          <h3>Dạy cả phần không ai dạy</h3>
          <p style="margin:0;">Báo giá thế nào, nhận brief ra sao, xử lý khi khách đổi ý ở phút cuối, cách trình bày một shot để người duyệt hiểu ngay. Đây là phần quyết định bạn sống được với nghề hay không, và gần như không có trên YouTube.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="grid2" style="gap:48px;align-items:start;">
        <div>
          <p class="eyebrow">Studio làm gì</p>
          <h2>Job thật nuôi bài giảng</h2>
          <p>LXAM Studio nhận dự án hình ảnh và TVC thương mại: dựng sản phẩm hard-surface, lighting và rendering, animation, phối cảnh sự kiện, hậu kỳ. Những dự án này không nằm ngoài lớp học, chúng chính là chất liệu của bài giảng.</p>
          <p>Khi bạn học lighting, cái bạn mổ xẻ là file lighting của một shot đã lên sóng, kèm cả những phương án bị khách gạt đi và lý do. Đó là thứ một khoá học đóng gói sẵn không có.</p>
          <a class="lxcta" href="index.html#portfolio" style="margin-top:8px;">Xem portfolio studio</a>
        </div>
        <div class="grid2" style="gap:14px;">
          <img src="assets/a26a7e39.jpg" alt="Shot TVC ô tô dựng bằng Blender cho dự án thương mại của LXAM Studio" width="1920" height="1080" loading="lazy" style="border-radius:4px;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;">
          <img src="assets/card-chivas18.webp" alt="Phối cảnh 3D khu trung tâm triển lãm Chivas Regal 18 do LXAM Studio dựng" width="1600" height="1000" loading="lazy" style="border-radius:4px;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;">
          <img src="assets/b64a4cd7.jpg" alt="Shot hard-surface sản phẩm kỹ thuật dựng bằng Blender" width="1920" height="810" loading="lazy" style="border-radius:4px;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;">
          <img src="assets/4c9ff169.jpg" alt="Shot render thương mại trong portfolio LXAM Studio" width="1920" height="810" loading="lazy" style="border-radius:4px;width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;">
        </div>
      </div>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="wrap">
      <div style="border-top:1px solid var(--line);padding-top:clamp(34px,5vw,60px);">
        <h2 style="max-width:1000px;line-height:1.3;">Một ngày nào đó có người ở Paris, Tokyo hay New York mở một shot lên và hỏi <span class="grad">ai làm cái này</span>, câu trả lời là một cái tên Việt Nam.</h2>
        <p style="max-width:640px;margin-top:20px;">Chúng tôi làm việc cho ngày đó. Từng shot một, từng học viên một. Nếu bạn muốn đi cùng, cứ để lại thông tin, tôi sẽ xem qua và nói thẳng bạn nên bắt đầu từ đâu, kể cả khi câu trả lời là “chưa cần học vội”.</p>
        <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:30px;">
          <a class="lxcta" href="lo-trinh.html#dangky" style="padding:15px 30px;font-size:15px;">Đăng ký tư vấn</a>
          <a class="lxcta-ghost" href="nghe-nghiep.html">Học xong làm gì</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""


ABOUT_LD = """<script type="application/ld+json">{"@context": "https://schema.org", "@graph": [{"@type": "AboutPage", "name": "Về LXAM Studio", "description": "Studio visual 3D và đào tạo Blender tại Việt Nam", "url": "https://lxamstudio.com/ve-chung-toi.html", "inLanguage": "vi-VN", "mainEntity": {"@id": "https://lxamstudio.com/ve-chung-toi.html#founder"}}, {"@type": "Person", "@id": "https://lxamstudio.com/ve-chung-toi.html#founder", "name": "Lê Xuân Anh Minh", "alternateName": "LXAM", "jobTitle": ["Founder & Creative Director", "Multimedia Director"], "description": "Founder LXAM Studio, studio visual 3D tại Việt Nam. Làm TVC, render sản phẩm, phối cảnh sự kiện và đào tạo Blender 1 kèm 1.", "knowsAbout": ["Blender", "3D modeling", "Lighting", "Rendering", "TVC 3D", "Phối cảnh sự kiện 3D"], "url": "https://lxamstudio.com/ve-chung-toi.html#founder", "worksFor": {"@type": "Organization", "name": "LXAM Studio", "url": "https://lxamstudio.com/"}}, {"@type": "Organization", "name": "LXAM Studio", "url": "https://lxamstudio.com/", "founder": {"@id": "https://lxamstudio.com/ve-chung-toi.html#founder"}}]}</script>"""


# ---------------------------------------------------------------- BLOG POSTS
POSTS = [
    {
        "slug": "lo-trinh-tu-hoc-blender",
        "title": "Lộ trình tự học Blender: 7 kỹ năng, đúng thứ tự",
        "desc": "Lộ trình tự học Blender gồm bảy kỹ năng theo đúng thứ tự, kèm mốc thời gian ước lượng, dấu hiệu đã qua từng bước và chỗ phần lớn người mới bỏ cuộc.",
        "tag": "Lộ trình",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "updated": "2026-10-08",
        "updated_vn": "08/10/2026",
        "read": "12 phút đọc",
        "thumb": "assets/2cdbf5f9.jpg",
        "faq": [
            ("Lộ trình tự học Blender mất bao lâu nếu học một mình?",
             "Ước lượng từ người học quanh LXAM Studio: đi hết bảy bước thường mất một tới hai năm nếu tự học hoàn toàn và học ngắt quãng, khoảng tám tới mười hai tháng nếu học đều mười giờ mỗi tuần và có người sửa bài. Phần lâu nhất không phải học thao tác mà là tự phát hiện bài mình sai ở đâu."),
            ("Nên học modeling trước hay lighting trước?",
             "Modeling trước. Ánh sáng chỉ đánh giá được khi hình khối đã đúng tỉ lệ. Chỉnh đèn trên một model sai tỉ lệ là sửa triệu chứng, càng chỉnh càng rối."),
            ("Tự học Blender có cần máy mạnh ngay không?",
             "Không trong sáu tháng đầu. Ba bước đầu của lộ trình gần như không phụ thuộc cấu hình. Máy chỉ thành nút thắt từ bước render trở đi, nhất là khi cảnh có volumetric hoặc nhiều ánh sáng gián tiếp."),
            ("Học xong bảy bước là đi làm được chưa?",
             "Chưa chắc. Bảy bước cho bạn kỹ năng, nhà tuyển dụng xem portfolio. Thường cần thêm ba tới năm bài hoàn chỉnh làm theo brief thật, có giới hạn thời gian và có người nhận xét, trước khi hồ sơ đủ sức thuyết phục."),
            ("Có nên học Blender song song với 3ds Max không?",
             "Không nên trong năm đầu. Hai phần mềm chia nhỏ thời gian luyện tập mà kỹ năng cốt lõi thì giống nhau. Học chắc một cái rồi chuyển sang cái kia sẽ nhanh hơn nhiều."),
        ],
        "body": """
<p class="lead">Thứ tự đúng của một lộ trình tự học Blender là: modeling, vật liệu, ánh sáng, render, hard-surface, chuyển động, hậu kỳ. Học đảo thứ tự là lý do phổ biến nhất khiến người mới dừng lại ở tháng thứ ba, chứ không phải vì phần mềm khó. Dưới đây là đủ bảy bước, kèm mốc thời gian ước lượng và dấu hiệu để tự biết mình đã qua bước nào.</p>

<p>Blender là phần mềm hiếm hoi làm được gần như mọi khâu trong một pipeline 3D. Đó vừa là điểm mạnh vừa là cái bẫy: người mới mở lên, thấy hai chục tab, và bắt đầu học theo thứ tự ngẫu nhiên của video được đề xuất. Ba tháng sau họ biết dựng một cái ghế, biết bấm nút render, nhưng không giải thích được vì sao ảnh của mình trông rẻ tiền.</p>

<h2>Vì sao thứ tự quan trọng</h2>

<p>Mỗi kỹ năng trong 3D đều đứng trên vai kỹ năng trước nó. Bạn không thể đánh giá vật liệu của mình đúng hay sai nếu ánh sáng đang sai. Bạn không thể sửa ánh sáng nếu hình khối đã lệch. Học đảo thứ tự nghĩa là bạn liên tục sửa triệu chứng thay vì sửa nguyên nhân, và đó là lý do người ta bỏ cuộc, chứ không phải vì Blender khó.</p>

<p>Có một cách kiểm chứng rất nhanh. Mở lại bài render gần nhất của bạn và hỏi: nếu bây giờ tắt hết đèn rồi bật lại một đèn duy nhất, hình khối này còn đọc được không? Nếu câu trả lời là không, vấn đề nằm ở bước một chứ không nằm ở bước ba, và mọi giờ bạn đổ vào việc chỉnh đèn tuần này đều là giờ mất trắng.</p>

<blockquote><p>Một cái model sai tỉ lệ, lighting đẹp cỡ nào cũng không cứu được. Nhưng một cái model đúng, chỉ cần một nguồn sáng tử tế là đã dùng được.</p></blockquote>

<h2>Bảy kỹ năng, theo đúng thứ tự</h2>

<h3>1. Modeling: dựng hình</h3>
<p>Đây là nền. Không phải để bạn dựng được thứ phức tạp, mà để bạn đọc được hình khối: tỉ lệ, topology, đâu là bề mặt cong thật và đâu là cong giả. Người dựng hình tốt tiết kiệm được hàng giờ ở mọi khâu phía sau.</p>
<p>Nếu bạn đang phân vân nên bắt đầu dựng hình từ bài tập nào, phần đầu của bài <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> có liệt kê thứ tự bài tập mà người mới nên đi qua, dùng được cả khi bạn tự học.</p>
<p><strong style="color:#fff;">Dấu hiệu bạn đã qua bước này:</strong> nhìn một vật thể ngoài đời, bạn phác được trong đầu nó gồm mấy khối cơ bản và nối với nhau ra sao.</p>

<h3>2. Materials: vật liệu</h3>
<p>Vật liệu là nơi người mới hay đốt thời gian nhất mà thu về ít nhất, vì họ chỉnh nó dưới ánh sáng sai. Học đủ để hiểu ba thông số thật sự quan trọng là base color, roughness và metallic, rồi đi tiếp. Phần còn lại quay lại sau khi biết lighting.</p>
<p><strong style="color:#fff;">Dấu hiệu bạn đã qua bước này:</strong> bạn phân biệt được khi nào một bề mặt trông sai vì sai thông số vật liệu, và khi nào nó sai vì thiếu một nguồn sáng để phản chiếu.</p>

<h3>3. Lighting: ánh sáng</h3>
<p>Đây là bước tạo ra khác biệt lớn nhất giữa ảnh nghiệp dư và ảnh thương mại, và cũng là bước bị bỏ qua nhiều nhất. Ánh sáng quyết định người xem nhìn vào đâu, cảm thấy gì, và tin sản phẩm đó đắt hay rẻ.</p>
<p>Nếu bạn chỉ có thời gian để giỏi một kỹ năng duy nhất trong bảy cái này, chọn cái này. Trước khi học thêm kỹ thuật mới, nên đọc bài <a href="blog-5-loi-lighting.html">học lighting trong Blender và năm lỗi làm render rẻ tiền</a>, vì phần lớn bài của người tự học mắc ít nhất hai trong số đó.</p>

<figure>
  <img src="assets/chivas15-glorifier-logo-anh-sang.webp" alt="Mô hình glorifier trưng bày Chivas Regal XV dựng bằng Blender, chai vàng kim loại và viền chữ phát sáng trên nền đen" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Glorifier trưng bày trong dự án Chivas 15 của LXAM Studio.</strong> Gần như toàn bộ sức nặng của hình này đến từ ánh sáng và chất liệu phản chiếu, hình khối bên dưới thực ra rất đơn giản. Đó là lý do bước ba đáng đầu tư hơn bước một về lâu dài.</figcaption>
</figure>

<h3>4. Rendering: kết xuất</h3>
<p>Không phải học bấm nút render, mà học đọc kết quả: nhiễu đến từ đâu, vì sao cảnh này lâu bất thường, khi nào nên dùng Cycles và khi nào EEVEE là đủ. Hiểu render giúp bạn tiết kiệm hàng chục giờ chờ máy mỗi tháng.</p>
<p>Đây cũng là bước đầu tiên mà cấu hình máy thật sự thành nút thắt. Trước đó bạn học được trên gần như mọi máy, nên đừng vội nâng cấp sớm; bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> có bảng tham khảo theo giai đoạn để bạn không mua thừa.</p>

<h3>5. Hard-surface: bề mặt cứng</h3>
<p>Đến đây bạn mới nên đụng vào sản phẩm công nghiệp: máy móc, thiết bị, xe cộ. Hard-surface đòi hỏi kỷ luật về topology và bevel mà ba bước đầu đã rèn cho bạn. Vào sớm hơn, bạn sẽ chỉ tạo ra những khối méo mà không biết vì sao nó méo.</p>

<figure>
  <img src="assets/jhm-khoi-kinh-ky-thuat.webp" alt="Chi tiết giá treo kim loại JHM dựng hard-surface bằng Blender, đặt trong khối kính trong suốt trên nền lưới kỹ thuật tối màu" loading="lazy" width="1800" height="1012">
  <figcaption><strong>Chi tiết giá treo kim loại trong dự án JHM.</strong> Một chi tiết cơ khí nhỏ như thế này là bài kiểm tra thẳng thắn cho bước năm: bevel sai một chút là ánh sáng trượt trên cạnh và mắt người xem nhận ra ngay, dù họ không gọi được tên lỗi.</figcaption>
</figure>

<h3>6. Animation: chuyển động</h3>
<p>Chuyển động là ngôn ngữ riêng, không phải phần mở rộng của dựng hình. Timing, easing, và quan trọng nhất là biết khi nào <em>không</em> nên cho vật thể chuyển động. Một shot sản phẩm đứng yên với camera trôi chậm thường thuyết phục hơn một shot mọi thứ đều quay.</p>

<h3>7. VFX và hậu kỳ</h3>
<p>Bước cuối, và là bước dễ bị lạm dụng nhất. Hậu kỳ để nâng một shot đã tốt lên, không phải để cứu một shot hỏng. Nếu bạn thấy mình đang kéo curve rất nhiều để ảnh đỡ tệ, vấn đề nằm ở khâu ba hoặc khâu một.</p>

<h2>Bảng lộ trình: mốc thời gian và dấu hiệu đã qua</h2>

<p>Các con số dưới đây là ước lượng, dựa trên người học quanh studio và giả định bạn bỏ ra khoảng tám tới mười hai giờ mỗi tuần. Học ít hơn thì kéo dài ra theo tỉ lệ, học nhiều hơn không rút ngắn được tương ứng vì mắt nhìn cần thời gian chứ không chỉ cần số giờ.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Bước</th><th>Thời gian ước lượng</th><th>Dấu hiệu đã qua</th></tr></thead>
<tbody>
<tr><td>1. Modeling</td><td>6 đến 10 tuần</td><td>Phác được vật thể thành các khối cơ bản</td></tr>
<tr><td>2. Vật liệu</td><td>2 đến 3 tuần</td><td>Đọc được roughness và metallic qua mắt</td></tr>
<tr><td>3. Ánh sáng</td><td>8 đến 12 tuần</td><td>Nói được vì sao đặt đèn ở đúng chỗ đó</td></tr>
<tr><td>4. Render</td><td>2 đến 4 tuần</td><td>Chẩn đoán được nguồn gốc của nhiễu</td></tr>
<tr><td>5. Hard-surface</td><td>8 đến 14 tuần</td><td>Giữ được cạnh sạch khi lên subdivision</td></tr>
<tr><td>6. Chuyển động</td><td>6 đến 10 tuần</td><td>Nhận ra timing sai khi xem lại bản nháp</td></tr>
<tr><td>7. Hậu kỳ</td><td>3 đến 5 tuần</td><td>Dừng lại đúng lúc, không chỉnh quá tay</td></tr>
</tbody>
</table>
</div>

<p>Mỗi bước có một kiểu đi sai riêng. Đây là những cái hay gặp nhất:</p>

<ul>
<li><strong style="color:#fff;">Bước 1:</strong> nhảy ngay vào model phức tạp thay vì luyện đọc khối cơ bản.</li>
<li><strong style="color:#fff;">Bước 2:</strong> tải bừa thư viện material rồi dừng ở đó, không hiểu thông số.</li>
<li><strong style="color:#fff;">Bước 3:</strong> thêm đèn để cứu hình, trong khi cách đúng thường là bớt đèn đi.</li>
<li><strong style="color:#fff;">Bước 4:</strong> tăng sample cho hết nhiễu thay vì tìm nguồn gốc của nhiễu.</li>
<li><strong style="color:#fff;">Bước 5:</strong> vào hard-surface khi bước 1 chưa vững, rồi bế tắc với topology.</li>
<li><strong style="color:#fff;">Bước 6:</strong> cho mọi thứ trong khung hình cùng chuyển động một lúc.</li>
<li><strong style="color:#fff;">Bước 7:</strong> dùng hậu kỳ để cứu một shot vốn đã hỏng từ khâu ánh sáng.</li>
</ul>

<p>Cộng lại khoảng tám tới mười hai tháng nếu mọi thứ suôn sẻ. Thực tế thì ít ai suôn sẻ, nên con số một tới hai năm cho người tự học hoàn toàn là hợp lý. Bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a> tách riêng hai trường hợp này kỹ hơn.</p>

<h2>Ba chỗ người tự học hay kẹt lại</h2>

<p><strong style="color:#fff;">Kẹt ở bước ba.</strong> Đây là chỗ đông người dừng nhất. Lý do là ánh sáng không có đáp án đúng sai rõ ràng như modeling, nên không có người nhận xét thì bạn không biết mình tiến hay lùi. Cách tự cứu rẻ nhất: chọn một ảnh tham chiếu thật, dựng lại bằng một đèn duy nhất, so sánh, lặp lại trong bốn tuần.</p>

<p><strong style="color:#fff;">Kẹt vì học quá nhiều nguồn.</strong> Mỗi người dạy một quy trình khác nhau, và người mới chưa đủ nền để biết quy trình nào hợp với mình. Kết quả là bạn có mười cách làm nửa vời thay vì một cách làm được. Trong ba tháng đầu, chọn một nguồn và đi hết nó. Nếu bạn vẫn đang ở chặng đó, bài <a href="blog-hoc-do-hoa-3d-tu-con-so-0.html">học đồ hoạ 3D từ con số 0</a> chia đúng ba tháng ấy thành việc của từng tháng.</p>

<p><strong style="color:#fff;">Kẹt vì không bao giờ hoàn thành bài.</strong> Bỏ dở ở phút thứ tám mươi là thói quen tốn kém nhất, vì mọi kỹ năng khó đều nằm ở hai mươi phần trăm cuối. Thà làm ba bài nhỏ xong hẳn còn hơn mười bài dang dở.</p>

<h2>Tự học hết bảy bước, hay học có người sửa bài</h2>

<p>Cả hai đường đều tới đích. Khác nhau ở chi phí: tự học rẻ tiền nhưng đắt thời gian, học kèm ngược lại. Thứ bạn thật sự mua khi trả học phí không phải bài giảng, vì bài giảng miễn phí đầy trên mạng, mà là người ngồi nhìn file của bạn và nói đúng chỗ sai.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Tự học hoàn toàn</th><th>Có người sửa bài</th></tr></thead>
<tbody>
<tr><td>Chi phí tiền</td><td>Gần như bằng không</td><td>Đáng kể, cần tính kỹ</td></tr>
<tr><td>Thời gian tới portfolio</td><td>Thường gấp hai tới gấp ba</td><td>Ngắn hơn rõ rệt</td></tr>
<tr><td>Rủi ro đi sai đường</td><td>Cao, phát hiện muộn</td><td>Thấp, phát hiện trong tuần</td></tr>
<tr><td>Tính kỷ luật đòi hỏi</td><td>Rất cao</td><td>Vừa phải vì có lịch</td></tr>
<tr><td>Hợp với ai</td><td>Người có nhiều thời gian rảnh</td><td>Người đang đi làm, ít thời gian</td></tr>
</tbody>
</table>
</div>

<p>Nếu bạn đã đi được tới bước ba rồi đứng yên, đó đúng là lúc hình thức <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> phát huy, vì cái bạn thiếu không còn là bài giảng mà là người chẩn đoán đúng chỗ kẹt. Còn nếu bạn mới ở bước một và chưa chắc có theo nghề hay không, một <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> hoặc đơn giản là ba tháng tự học nữa đều hợp lý hơn.</p>

<p>Trước khi quyết định đóng tiền ở bất kỳ đâu, nên xem qua cách bóc tách <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a> theo số lần được chữa bài. Con số đó nói nhiều hơn tổng học phí.</p>

<h2>Danh sách kiểm tra mỗi tháng một lần</h2>

<p>Tự học thiếu nhất là cơ chế phản hồi. Dùng danh sách này mỗi tháng, đánh dấu từng dòng. Thiếu quá ba dòng nghĩa là tháng vừa rồi bạn bận rộn chứ không tiến bộ.</p>

<ul>
<li>Tháng này có ít nhất một bài hoàn thành tới khâu cuối, không bỏ dở.</li>
<li>Nói được bằng một câu mình đang ở bước nào trong bảy bước.</li>
<li>Có ít nhất một bài được người khác nhận xét, dù chỉ là bạn cùng học.</li>
<li>Xem lại bài của tháng trước và chỉ ra được ít nhất hai lỗi.</li>
<li>Không dành quá một phần tư thời gian cho việc xem video mà không mở Blender.</li>
<li>Không nâng cấp phần cứng hoặc mua add-on mới nào trong tháng trừ khi đã chạm trần thật sự.</li>
<li>Có một ảnh tham chiếu thật cho mỗi bài, không dựng theo trí nhớ.</li>
<li>File đặt tên và sắp xếp sao cho mở lại sau ba tháng vẫn hiểu.</li>
</ul>

<h2>Sau bảy bước thì rẽ đi đâu</h2>

<p>Hết bảy bước, bạn có nền chung. Việc tiếp theo là chọn một mảng để đào sâu, vì thị trường trả tiền cho người chuyên chứ không trả cho người biết đều. Ba hướng phổ biến ở Việt Nam là hình ảnh sản phẩm, phối cảnh sự kiện và triển lãm, và automotive hoặc TVC.</p>

<p>Cách chọn đơn giản nhất là nhìn vào loại công việc thật đang có trên thị trường. Phần <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> của studio liệt kê các dạng đầu việc thường gặp, đọc qua là hình dung được mảng nào hợp với mình. Nếu muốn đi theo đường có lộ trình sẵn thay vì tự ghép, hai hệ trong trang <a href="khoa-hoc.html">khoá học 3D Blender</a> được dựng đúng theo thứ tự bảy bước ở trên, chỉ khác là có người chữa bài ở mỗi mốc.</p>

<p>Dù chọn đường nào, nên tải <a href="cam-nang.html">cẩm nang Blender</a> để có sẵn checklist lighting và quy trình render dùng khi làm việc thật. Có bảng tra cứu bên cạnh thì bớt được kha khá thời gian mò mẫm ở bước ba và bước bốn.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Lộ trình tự học Blender mất bao lâu nếu học một mình?</p>
<p>Ước lượng từ người học quanh LXAM Studio: đi hết bảy bước thường mất một tới hai năm nếu tự học hoàn toàn và học ngắt quãng, khoảng tám tới mười hai tháng nếu học đều mười giờ mỗi tuần và có người sửa bài. Phần lâu nhất không phải học thao tác mà là tự phát hiện bài mình sai ở đâu.</p>

<p class="faq-q">Nên học modeling trước hay lighting trước?</p>
<p>Modeling trước. Ánh sáng chỉ đánh giá được khi hình khối đã đúng tỉ lệ. Chỉnh đèn trên một model sai tỉ lệ là sửa triệu chứng, càng chỉnh càng rối.</p>

<p class="faq-q">Tự học Blender có cần máy mạnh ngay không?</p>
<p>Không trong sáu tháng đầu. Ba bước đầu của lộ trình gần như không phụ thuộc cấu hình. Máy chỉ thành nút thắt từ bước render trở đi, nhất là khi cảnh có volumetric hoặc nhiều ánh sáng gián tiếp.</p>

<p class="faq-q">Học xong bảy bước là đi làm được chưa?</p>
<p>Chưa chắc. Bảy bước cho bạn kỹ năng, nhà tuyển dụng xem portfolio. Thường cần thêm ba tới năm bài hoàn chỉnh làm theo brief thật, có giới hạn thời gian và có người nhận xét, trước khi hồ sơ đủ sức thuyết phục.</p>

<p class="faq-q">Có nên học Blender song song với 3ds Max không?</p>
<p>Không nên trong năm đầu. Hai phần mềm chia nhỏ thời gian luyện tập mà kỹ năng cốt lõi thì giống nhau. Học chắc một cái rồi chuyển sang cái kia sẽ nhanh hơn nhiều.</p>

<hr class="hr">

<p>Tóm lại, một lộ trình tự học Blender hiệu quả không nằm ở việc biết thêm thủ thuật, mà ở việc đứng đúng bước và không nhảy cóc. Bảy bước ở trên có thể đi một mình, chỉ là chậm hơn và cần kỷ luật hơn.</p>

<p>Nếu bạn đang tự học và thấy mình mắc kẹt ở đâu đó trong bảy bước, cứ nhắn cho tôi mô tả chỗ kẹt. Tôi trả lời được thì trả lời, không thì chỉ bạn chỗ tìm. Không cần đăng ký gì cả. Muốn đi theo đường có người chữa bài ở từng mốc, xem lộ trình hai hệ ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>.</p>
""",
    },
    {
        "slug": "5-loi-lighting",
        "title": "Học lighting trong Blender: 5 lỗi làm render rẻ tiền",
        "desc": "Học lighting trong Blender hay mắc năm lỗi làm render trông rẻ tiền. Bài này chỉ rõ từng lỗi, cách sửa trong một buổi và bài kiểm tra ảnh xám ba mươi giây.",
        "tag": "Kỹ thuật",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "updated": "2026-10-13",
        "updated_vn": "13/10/2026",
        "read": "11 phút đọc",
        "thumb": "assets/2afcaceb.jpg",
        "faq": [
            ("Học lighting trong Blender mất bao lâu để dùng được?",
             "Ước lượng từ các nhóm chúng tôi đã chữa bài, cần khoảng tám tới mười hai tuần làm đều để đặt đèn có lý do thay vì mò. Riêng việc sửa năm lỗi trong bài này thì nhanh hơn nhiều, thường chỉ một tới hai buổi là thấy khác."),
            ("Nên học lighting trong Cycles hay Eevee?",
             "Học nguyên lý trong Cycles vì nó phản ứng gần với ánh sáng thật, sai là thấy ngay. Eevee dùng để xem nhanh và cho việc cần tốc độ. Nguyên lý đặt đèn giống nhau, chỉ khác cách xử lý phản chiếu và bóng đổ."),
            ("Có cần mua HDRI hoặc add-on lighting trả phí không?",
             "Không cần, nhất là trong giai đoạn học. Năm lỗi phổ biến nhất đều sửa bằng area light và vài mặt phẳng hắt sáng có sẵn trong Blender. Add-on tiết kiệm thời gian khi đã biết mình muốn gì, chứ không dạy bạn muốn gì."),
            ("Máy yếu có học lighting được không?",
             "Được. Lighting là khâu ít ngốn máy nhất nếu bạn làm việc với ảnh xám và render nháp ở độ phân giải thấp. Phần cần máy mạnh là bản render cuối, và đó là việc có thể để sau."),
            ("Render vẫn trông giả dù đã sửa hết năm lỗi, vấn đề ở đâu?",
             "Thường là vật liệu hoặc bố cục, không phải đèn nữa. Làm bài kiểm tra ảnh xám trong bài này: nếu ảnh xám đã có chiều sâu mà bản màu vẫn giả, lỗi nằm ở roughness và màu bề mặt."),
        ],
        "body": """
<p class="lead">Học lighting trong Blender không vướng ở plugin hay cấu hình máy. Khi có người gửi tôi một bài render và hỏi sao nhìn nó chưa đã, tám trên mười lần vấn đề nằm ở ánh sáng, không phải model, không phải vật liệu, và gần như không bao giờ do card đồ hoạ. Năm lỗi dưới đây gặp ở gần như mọi bài tự học, và cái nào cũng sửa được trong một buổi.</p>

<p>Bài này xếp theo đúng thứ tự tôi dùng khi chữa bài: xét nguồn sáng chính trước, rồi mới tới kích thước đèn, môi trường phản chiếu, vùng tối và cuối cùng là hậu kỳ. Sửa theo thứ tự đó thì mỗi lần sửa một thứ là hình khá lên thật, không phải vá chỗ nọ hỏng chỗ kia.</p>

<h2>Học lighting trong Blender nên bắt đầu từ đâu</h2>

<p>Phần lớn người mới học ánh sáng theo kiểu sưu tầm. Thấy một setup ba đèn trên YouTube thì dựng lại ba đèn, thấy một HDRI đẹp thì tải về dùng. Cách đó cho ra ảnh tạm được nhưng không tích luỹ, lần sau gặp vật thể khác là mò lại từ đầu.</p>

<p>Thứ tích luỹ được là ba câu hỏi, đặt theo đúng thứ tự này cho mọi cảnh:</p>

<ul>
<li>Nguồn chính đến từ hướng nào, và vì sao hướng đó hợp với hình khối của vật thể này?</li>
<li>Bề mặt đang phản chiếu cái gì? Nếu câu trả lời là không có gì, đó đã là một lỗi.</li>
<li>Vùng tối nằm ở đâu, và nó có đang giúp mắt người đọc được hình khối hay chỉ làm mất chi tiết?</li>
</ul>

<p>Ba câu đó là toàn bộ nội dung của năm phần tiếp theo. Nếu bạn muốn biết ánh sáng nằm ở chỗ nào trong cả chuỗi kỹ năng, <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> đặt nó ở bước ba, sau modeling và vật liệu, và đó cũng là bước chiếm nhiều thời gian nhất trong bảy bước.</p>

<h2>Lỗi 1: dùng đúng một HDRI rồi gọi đó là lighting</h2>

<p>HDRI cho bạn ánh sáng môi trường tử tế trong ba mươi giây, nên rất dễ dừng lại ở đó. Vấn đề là HDRI chiếu đều từ mọi phía. Nó xoá đi cái bạn cần nhất: hướng. Không có hướng thì không có khối, không có khối thì vật thể trông như dán lên nền.</p>

<p><strong style="color:#fff;">Sửa:</strong> giữ HDRI làm nền, hạ cường độ xuống còn khoảng một phần ba, rồi thêm một area light làm nguồn chính. Chỉ một đèn thôi. So sánh trước và sau, bạn sẽ thấy vật thể đột nhiên có trọng lượng.</p>

<p>Một cách kiểm tra nhanh: xoay HDRI đi chín mươi độ. Nếu ảnh gần như không đổi, nghĩa là bạn đang không có nguồn chính nào cả, chỉ có ánh sáng môi trường.</p>

<h2>Lỗi 2: đèn quá nhỏ so với vật thể</h2>

<p>Đây là lỗi âm thầm nhất. Nguồn sáng nhỏ tạo bóng đổ sắc cạnh và highlight nhỏ như đầu kim, thứ ngoài đời chỉ xuất hiện dưới nắng gắt hoặc đèn flash trần. Sản phẩm chụp studio luôn dùng nguồn lớn, vì nguồn lớn cho chuyển sáng mềm dọc theo bề mặt cong, và chính cái chuyển đó nói cho mắt người biết vật thể làm bằng gì.</p>

<p><strong style="color:#fff;">Sửa:</strong> phóng area light của bạn to lên. To hơn nữa. Quy tắc thô: nguồn chính nên lớn ít nhất bằng vật thể, thường là gấp hai đến ba lần.</p>

<blockquote><p>Nếu highlight trên bề mặt kim loại của bạn là một chấm nhỏ thay vì một vệt dài, đèn của bạn đang quá nhỏ.</p></blockquote>

<p>Đi kèm kích thước là khoảng cách. Đèn lớn đặt xa sẽ hành xử như đèn nhỏ. Khi muốn chuyển sáng mềm hơn mà không đổi cường độ cảm nhận, kéo đèn lại gần và hạ power, thay vì phóng to mãi.</p>

<h2>Lỗi 3: không có gì để phản chiếu</h2>

<p>Kim loại và nhựa bóng không tự đẹp, chúng đẹp nhờ những gì xung quanh phản chiếu vào. Render một chiếc đồng hồ trong không gian trống, bề mặt của nó sẽ chỉ có màu xám chết. Studio thật luôn đầy vật thể: hắt sáng, cờ đen, tường, trần.</p>

<p><strong style="color:#fff;">Sửa:</strong> đặt vài mặt phẳng lớn quanh vật thể, một trắng để hắt sáng, một đen để tạo mảng tối tương phản trên cạnh. Tắt bóng đổ của chúng nếu cần. Chi phí render gần như bằng không, khác biệt thì thấy ngay.</p>

<p>Trang sức là trường hợp cực đoan của lỗi này, vì gần như toàn bộ bề mặt đều là thứ phản chiếu lại môi trường. Có thể xem <a href="du-an-locphuc-bo-suu-tap.html">key visual bộ sưu tập trang sức Lộc Phúc</a> để thấy mảng sáng và mảng tối trên kim loại được dựng từ vật đặt quanh chứ không phải từ việc tăng số đèn.</p>

<figure>
  <img src="assets/mercedes-g63-cum-den-truoc-can-canh.webp" alt="Cận cảnh cụm đèn trước Mercedes G63 render bằng Blender, vệt sáng dài trên mặt kính và viền kim loại phản chiếu mảng tối" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Cụm đèn trước trong dự án Mercedes G63 của LXAM Studio.</strong> Toàn bộ cảm giác kim loại và kính ở đây đến từ cái mà bề mặt phản chiếu, chủ yếu là các mặt hắt sáng và cờ đen quanh xe, không phải từ số lượng đèn.</figcaption>
</figure>

<h2>Lỗi 4: sáng đều tuyệt đối, không có vùng tối</h2>

<p>Người mới sợ vùng tối, nên thêm fill light cho tới khi mọi ngóc ngách đều nhìn rõ. Kết quả là ảnh phẳng lì. Vùng tối không phải chỗ thiếu thông tin. Nó là chỗ mắt người nghỉ, và là thứ làm vùng sáng trở nên sáng.</p>

<p><strong style="color:#fff;">Sửa:</strong> tắt hết đèn phụ, chỉ để nguồn chính. Nhìn kỹ. Rồi thêm lại từng đèn một, mỗi lần tự hỏi đèn này đang giải quyết vấn đề gì. Đèn nào không trả lời được thì xoá.</p>

<p>Một ví dụ đi ngược cả bốn lỗi trên: <a href="du-an-volvo-s90.html">bộ hình Volvo S90 dựng và render bằng Blender</a>, đèn lớn, có vật để phản chiếu, và vùng tối được giữ nguyên thay vì kéo sáng cho đều.</p>

<h2>Lỗi 5: chỉnh màu ở hậu kỳ để cứu ánh sáng sai</h2>

<p>Kéo contrast và saturation trong Compositor cho tới khi ảnh đỡ tệ là dấu hiệu bạn đang vá triệu chứng. Hậu kỳ nên là bước tinh chỉnh cuối, không phải bước cứu hộ. Nếu bạn phải kéo mạnh tay, quay lại sửa đèn, nhanh hơn nhiều.</p>

<p>Có một ngoại lệ đáng nói: khi ánh sáng đã đúng, hậu kỳ nhẹ lại rất hiệu quả, và đó cũng là lúc nên nghĩ tới thời gian render. Các cách cắt thời gian mà không làm hình xấu đi nằm trong bài <a href="blog-render-nhanh-hon-blender-cycles.html">render nhanh hơn trong Blender Cycles</a>. Và nếu cảnh sẽ có khách duyệt, nên đọc thêm <a href="blog-quy-trinh-mot-shot-tvc.html">quy trình dựng TVC 3D một shot sản phẩm</a> để biết lúc nào chốt ánh sáng là an toàn, lúc nào còn phải chờ duyệt bố cục.</p>

<h2>Ba kiểu setup đèn thường gặp và lúc nào nên dùng</h2>

<p>Không có setup nào đúng cho mọi cảnh. Bảng dưới là ba kiểu tôi dùng nhiều nhất khi làm hình sản phẩm, kèm điểm bất lợi của từng kiểu, vì phần bất lợi mới là thứ quyết định nên chọn cái nào.</p>

<table>
<thead><tr><th>Kiểu setup</th><th>Hợp với</th><th>Điểm bất lợi</th></tr></thead>
<tbody>
<tr><td>Một đèn lớn, nhiều mặt hắt</td><td>Sản phẩm bóng, kim loại, kính</td><td>Cần kiên nhẫn dịch từng mặt hắt</td></tr>
<tr><td>Đèn chính và một đèn viền</td><td>Vật thể tối trên nền tối</td><td>Dễ thành viền giả nếu đèn viền quá mạnh</td></tr>
<tr><td>HDRI hạ cường độ và một area light</td><td>Cảnh ngoại cảnh, dựng nhanh</td><td>Khó kiểm soát phản chiếu chi tiết</td></tr>
</tbody>
</table>

<p>Khi chưa chắc, chọn dòng đầu. Một đèn lớn với ba bốn mặt hắt sạch sẽ hầu như luôn cho kết quả đọc được, và nó cũng là nền để hiểu hai kiểu còn lại. Đây cũng là cách chúng tôi dựng phần lớn shot trong <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a>.</p>

<h2>Cách tự kiểm tra trong ba mươi giây</h2>

<p>Đổi toàn bộ vật liệu trong cảnh sang một chất xám trung tính rồi render nháp. Nếu ảnh xám đó đã đọc được hình khối và có chiều sâu, ánh sáng của bạn ổn, phần còn lại là chuyện vật liệu. Nếu ảnh xám trông phẳng và nhạt, không vật liệu nào cứu được nó.</p>

<p>Bài kiểm tra này tôi dùng cho gần như mọi shot, và nó bắt lỗi sớm hơn bất kỳ thứ gì khác. Lý do nó hiệu quả: khi còn màu và texture, mắt bạn bị lừa bởi chi tiết đẹp và bỏ qua việc hình khối đang phẳng.</p>

<p>Làm thêm một bước nữa thì tốt: thu ảnh xám xuống bằng con tem rồi nhìn. Ở kích thước đó chỉ còn mảng sáng và mảng tối. Nếu không phân biệt được vật thể với nền, ánh sáng chưa xong, dù zoom vào vẫn thấy đẹp.</p>

<h2>Danh sách kiểm tra trước khi render bản cuối</h2>

<p>Chạy qua danh sách này trước mỗi bản render cuối. Thiếu quá hai dòng thì nên quay lại sửa đèn, đừng render, vì render một bản sai mất nhiều thời gian hơn sửa.</p>

<ul>
<li>Có một nguồn chính rõ ràng, nói được nó đến từ hướng nào.</li>
<li>Nguồn chính lớn ít nhất bằng vật thể, thường là gấp hai tới ba lần.</li>
<li>Mỗi đèn phụ trả lời được câu hỏi nó đang giải quyết vấn đề gì.</li>
<li>Có ít nhất một mặt hắt trắng và một cờ đen quanh vật thể bóng.</li>
<li>Highlight trên bề mặt kim loại là vệt có hình, không phải chấm.</li>
<li>Vùng tối còn nguyên, không bị fill light kéo sáng cho đều.</li>
<li>Ảnh xám đã đọc được hình khối trước khi gắn vật liệu thật.</li>
<li>Hậu kỳ chỉ còn là tinh chỉnh nhẹ, không phải cứu hộ.</li>
<li>Có một ảnh tham chiếu thật đặt cạnh để so, không dựng theo trí nhớ.</li>
</ul>

<h2>Lộ trình học lighting trong Blender trong tám tuần</h2>

<p>Nếu bạn muốn một cách làm có thứ tự thay vì sửa lỗi lẻ, đây là khung tám tuần đủ để đi từ mò mẫm sang đặt đèn có lý do. Mỗi tuần một bài, làm xong mới sang tuần sau.</p>

<p>Hai tuần đầu chỉ dùng một đèn duy nhất, không HDRI, dựng lại ba vật thể đơn giản cho tới khi nói được vì sao đặt đèn ở đúng chỗ đó. Hai tuần tiếp thêm mặt hắt và cờ đen, làm việc với một vật thể kim loại. Hai tuần sau đó tập vùng tối: dựng lại cùng một shot theo ba phương án sáng khác nhau. Hai tuần cuối ghép vào quy trình thật, gồm cả hậu kỳ nhẹ và kiểm tra bằng ảnh xám.</p>

<p>Khung này cố tình không có phần học thêm phần mềm hay add-on mới. Phần khó của ánh sáng là thói quen đọc ảnh, và thói quen đó chỉ hình thành khi làm lại cùng một việc với điều kiện khác nhau. Bộ bảng tra cứu đi kèm nằm trong <a href="cam-nang.html">cẩm nang Blender</a>, trong đó có checklist lighting và quy trình render dùng khi làm việc thật.</p>

<p>Năm lỗi trên đều sửa được một mình. Thứ khó tự sửa là thói quen đọc ảnh, và đó là phần một <a href="blog-khoa-hoc-render.html">khoá học render</a> có người nhận xét từng vòng làm tốt hơn hẳn video hướng dẫn. Nếu bạn muốn học cả khâu dựng hình trước đó, hai hệ trong trang <a href="khoa-hoc.html">khoá học 3D Blender</a> đi theo đúng thứ tự modeling, vật liệu, rồi ánh sáng.</p>

<h2>Hỏi đáp về học lighting trong Blender</h2>

<p class="faq-q">Học lighting trong Blender mất bao lâu để dùng được?</p>
<p>Ước lượng từ các nhóm chúng tôi đã chữa bài, cần khoảng tám tới mười hai tuần làm đều để đặt đèn có lý do thay vì mò. Riêng việc sửa năm lỗi trong bài này thì nhanh hơn nhiều, thường chỉ một tới hai buổi là thấy khác.</p>

<p class="faq-q">Nên học lighting trong Cycles hay Eevee?</p>
<p>Học nguyên lý trong Cycles vì nó phản ứng gần với ánh sáng thật, sai là thấy ngay. Eevee dùng để xem nhanh và cho việc cần tốc độ. Nguyên lý đặt đèn giống nhau, chỉ khác cách xử lý phản chiếu và bóng đổ.</p>

<p class="faq-q">Có cần mua HDRI hoặc add-on lighting trả phí không?</p>
<p>Không cần, nhất là trong giai đoạn học. Năm lỗi phổ biến nhất đều sửa bằng area light và vài mặt phẳng hắt sáng có sẵn trong Blender. Add-on tiết kiệm thời gian khi đã biết mình muốn gì, chứ không dạy bạn muốn gì.</p>

<p class="faq-q">Máy yếu có học lighting được không?</p>
<p>Được. Lighting là khâu ít ngốn máy nhất nếu bạn làm việc với ảnh xám và render nháp ở độ phân giải thấp. Phần cần máy mạnh là bản render cuối, và đó là việc có thể để sau. Mức cấu hình hợp lý cho từng giai đoạn nằm trong bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a>.</p>

<p class="faq-q">Render vẫn trông giả dù đã sửa hết năm lỗi, vấn đề ở đâu?</p>
<p>Thường là vật liệu hoặc bố cục, không phải đèn nữa. Làm bài kiểm tra ảnh xám ở trên: nếu ảnh xám đã có chiều sâu mà bản màu vẫn giả, lỗi nằm ở roughness và màu bề mặt.</p>

<hr class="hr">

<p>Nếu bạn đang mắc ở một shot cụ thể, cứ gửi ảnh render kèm ảnh chụp màn hình phần đặt đèn. Chúng tôi xem và nói thẳng lỗi nào đang ăn nhiều nhất, kể cả khi câu trả lời là bố cục chứ không phải ánh sáng. Không cần đăng ký gì.</p>
""",
    },
    {
        "slug": "quy-trinh-mot-shot-tvc",
        "title": "Dựng TVC 3D: quy trình một shot sản phẩm",
        "desc": "Dựng TVC 3D cho một shot sản phẩm đi qua chín bước, từ brief tới vòng sửa. Bài viết nói cả phần ít ai quay hướng dẫn: chốt góc máy sớm và tách lớp render.",
        "tag": "Nghề",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "updated": "2026-10-20",
        "updated_vn": "20/10/2026",
        "read": "11 phút đọc",
        "thumb": "assets/0954717e.jpg",
        "faq": [
            ("Dựng TVC 3D một shot sản phẩm mất bao lâu?",
             "Ước lượng cho một shot độ phức tạp trung bình là bốn tới bảy ngày làm việc nếu khách phản hồi trong ngày, và dài hơn đáng kể khi vòng duyệt chậm. Phần chiếm thời gian thật thường không phải render mà là chờ duyệt bố cục và vật liệu."),
            ("Vì sao phải chốt góc máy trước khi model chi tiết?",
             "Vì chi tiết ở mặt không lên hình là chi tiết bỏ đi. Chốt camera từ giai đoạn khối xám cho biết chính xác cần làm kỹ chỗ nào, và ngăn tình huống dựng xong mới nghe khách nói muốn nhìn từ hướng khác."),
            ("Có nhất thiết phải render theo lớp không?",
             "Với bài tập cá nhân thì không. Với dự án có khách duyệt thì gần như bắt buộc, vì phần lớn yêu cầu sửa chỉ liên quan tới một lớp. Tách lớp biến một vòng sửa từ việc render lại cả cảnh thành việc chỉnh trong vài phút."),
            ("Người mới nên bắt đầu học khâu nào trong chuỗi này?",
             "Khối thô và góc máy. Hai khâu đó quyết định phần lớn chất lượng cuối cùng, lại ít phụ thuộc cấu hình máy và ít phụ thuộc phần mềm nhất, nên học sớm là có lãi lâu nhất."),
            ("Studio tính báo giá dựng 3D sản phẩm theo shot hay theo ngày?",
             "Cách phổ biến ở Việt Nam là tính theo shot với số vòng sửa ghi rõ trong hợp đồng, vì khách dễ hình dung hơn. Dù tính kiểu nào, phần cần chốt bằng văn bản là số vòng sửa được bao gồm và mốc nào coi là đã duyệt."),
        ],
        "body": """
<p class="lead">Dựng TVC 3D cho một shot sản phẩm là chuỗi chín bước, và nút render nằm ở khoảng giữa chuỗi đó chứ không phải ở cuối. Thứ tự chạy được trong dự án thật là: đọc brief, dựng khối thô, chốt góc máy, lighting trên chất xám, vật liệu, render theo lớp, hậu kỳ, duyệt, vòng sửa. Bài này đi hết chín bước theo cách một studio 3D làm việc với khách, kèm thời gian ước lượng và những chỗ quy trình hay vỡ.</p>

<p>Phần lớn hướng dẫn trên mạng dừng lại ở lúc bấm render. Hệ quả là nhiều người dựng hình khá nhưng vỡ ở khâu phối hợp, vì chỗ một dự án thương mại chết thường không nằm trong phần mềm: brief thiếu thông tin, duyệt sai thời điểm, file gộp một cục nên mỗi lần khách đổi ý là render lại từ đầu.</p>

<h2>Quy trình dựng TVC 3D trong một bảng</h2>

<p>Đây là bản đồ trước khi vào chi tiết. Cột thời gian là ước lượng cho một shot sản phẩm độ phức tạp trung bình, tính theo ngày làm việc. Con số sẽ lệch tuỳ số chi tiết phải dựng, cấu hình máy render và nhất là tốc độ phản hồi của khách.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Bước</th><th>Kết quả giao ra</th><th>Ai duyệt</th><th>Ước lượng</th></tr></thead>
<tbody>
<tr><td>1. Đọc brief, hỏi lại</td><td>Danh sách thông số đã chốt</td><td>Khách</td><td>Nửa ngày</td></tr>
<tr><td>2. Khối thô</td><td>Ảnh xám khối, chưa chi tiết</td><td>Nội bộ</td><td>Nửa tới một ngày</td></tr>
<tr><td>3. Chốt góc máy</td><td>Ảnh xám đúng khung hình cuối</td><td>Khách</td><td>Nửa ngày cộng thời gian chờ</td></tr>
<tr><td>4. Lighting trên chất xám</td><td>Bản ánh sáng trung tính</td><td>Nội bộ</td><td>Một ngày</td></tr>
<tr><td>5. Vật liệu</td><td>Bản màu đầu tiên</td><td>Khách</td><td>Một tới hai ngày</td></tr>
<tr><td>6. Render theo lớp</td><td>Các pass rời</td><td>Nội bộ</td><td>Nửa tới hai ngày máy</td></tr>
<tr><td>7. Hậu kỳ</td><td>Bản ghép hoàn chỉnh</td><td>Nội bộ</td><td>Nửa ngày</td></tr>
<tr><td>8. Gửi duyệt</td><td>Bản có số phiên bản</td><td>Khách</td><td>Tuỳ khách</td></tr>
<tr><td>9. Vòng sửa</td><td>Bản cuối</td><td>Khách</td><td>Nửa ngày mỗi vòng</td></tr>
</tbody>
</table>
</div>

<p>Nhìn bảng này sẽ thấy ngay một điều: khách xuất hiện ở bốn trong chín bước. Quy trình dựng TVC 3D vì thế không chỉ là chuỗi việc kỹ thuật, nó là chuỗi điểm duyệt. Đặt điểm duyệt sai chỗ là nguyên nhân phổ biến nhất khiến dự án đội thời gian gấp đôi.</p>

<h2>Bước 1: Đọc brief, và hỏi lại</h2>

<p>Brief từ khách hầu như luôn thiếu thứ quan trọng nhất: shot này dùng ở đâu. Cùng một sản phẩm, dựng cho banner web khác hẳn dựng cho màn LED ngoài trời hay cho video dọc trên điện thoại. Tỉ lệ khung, khoảng cách người xem, thời lượng họ dừng lại, ba thứ đó quyết định gần như mọi lựa chọn phía sau.</p>

<h3>Ba câu phải hỏi trước khi mở Blender</h3>

<p>Đăng ở đâu. Khung hình gì. Có chữ đè lên không. Câu thứ ba cứu được rất nhiều thời gian, vì bố cục đẹp mà chừa sai chỗ cho chữ thì vẫn phải dựng lại từ bước hai.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Nơi đăng</th><th>Tỉ lệ thường gặp</th><th>Phải tính trước</th></tr></thead>
<tbody>
<tr><td>Banner web</td><td>16:9 hoặc rộng hơn</td><td>Chừa khoảng trống cho chữ một bên</td></tr>
<tr><td>Feed Facebook, Instagram</td><td>1:1 hoặc 4:5</td><td>Sản phẩm phải đọc được ở kích thước nhỏ</td></tr>
<tr><td>Reels, TikTok, YouTube Shorts</td><td>9:16</td><td>Chi tiết dồn vào giữa khung, tránh viền</td></tr>
<tr><td>Màn LED ngoài trời</td><td>Tuỳ thiết bị</td><td>Tương phản cao, bỏ chi tiết quá nhỏ</td></tr>
<tr><td>Catalogue, in ấn</td><td>Tuỳ khổ</td><td>Độ phân giải cao hơn, không gian màu khác</td></tr>
</tbody>
</table>
</div>

<p>Nếu khách chưa chốt được nơi đăng, cách an toàn là dựng cho khung rộng nhất rồi cắt, nhưng phải nói trước rằng bản cắt sẽ không tối ưu bằng bản dựng riêng. Các dạng đầu việc thường gặp và cách mô tả yêu cầu nằm ở trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a>, đọc qua là dễ hỏi đúng câu hơn.</p>

<h2>Bước 2 và 3: Khối thô trước, chốt góc máy trước khi làm chi tiết</h2>

<p>Trước khi model chi tiết, dựng khối thô rồi chốt camera. Lý do đơn giản: chi tiết ở mặt không lên hình là chi tiết vứt đi. Chốt góc máy sớm cho biết chính xác cần làm kỹ chỗ nào, và cũng cho biết chỗ nào có thể bỏ qua hoàn toàn mà không ai nhận ra.</p>

<p>Ở bước này nên gửi khách ảnh xám khối thô. Nghe thô sơ, nhưng nó ngăn được thảm hoạ lớn nhất: làm xong hết rồi khách mới nói muốn nhìn từ bên kia.</p>

<blockquote><p>Duyệt bố cục ở giai đoạn khối xám mất của bạn một ngày. Duyệt ở giai đoạn đã render mất của bạn một tuần.</p></blockquote>

<p>Khâu này cũng là chỗ đo được trình độ dựng hình nhanh nhất. Người dựng chắc tay thì khối thô đã đúng tỉ lệ và đã đọc được là sản phẩm gì. Nếu khối thô còn méo, phần sau càng làm càng phải quay lại. Đây là phần được luyện kỹ nhất trong <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a>, vì nó quyết định phần lớn chất lượng cuối cùng.</p>

<h2>Bước 4: Lighting trước, vật liệu sau</h2>

<p>Dựng ánh sáng khi mọi thứ còn là chất xám trung tính. Ánh sáng đúng ở trạng thái xám thì gần như chắc chắn đúng khi có vật liệu. Làm ngược lại, tức chỉnh vật liệu dưới ánh sáng tạm, là tự tạo việc cho mình hai lần: sửa vật liệu rồi lại sửa đèn, rồi lại sửa vật liệu.</p>

<figure>
  <img src="assets/mercedes-g63-canh-mo-trong-duong-ham.webp" alt="Mercedes-AMG G63 đứng trong đường hầm bê tông, ánh sáng dải dài hai bên thân xe, dựng bằng Blender cho TVC 3D" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Shot mở trong dự án TVC Mercedes G63 của LXAM Studio.</strong> Toàn bộ cảm giác khối của thân xe ở đây đến từ hai dải sáng dọc hành lang, không phải từ số lượng đèn. Đó là loại quyết định phải chốt ở bước bốn, lúc cảnh vẫn còn là chất xám.</figcaption>
</figure>

<p>Một cách kiểm tra nhanh: nhìn bản xám và tự hỏi có đọc được hình khối hay không. Nếu bản xám đã phẳng thì thêm vật liệu cũng không cứu được. Những lỗi hay gặp ở khâu này được mổ kỹ trong bài về <a href="blog-5-loi-lighting.html">lỗi lighting làm render rẻ tiền</a>, phần lớn đều xuất phát từ việc chỉnh đèn khi đã có màu.</p>

<h2>Bước 5: Vật liệu, và kiềm chế</h2>

<p>Sản phẩm thương mại thường đơn giản hơn người ta tưởng: vài chất liệu sạch, đúng độ nhám, đúng màu thương hiệu. Cám dỗ lớn nhất là thêm trầy xước, bụi, vân tay cho thật. Với hình bán hàng, những thứ đó thường làm hại, vì khách muốn hàng mới tinh.</p>

<p>Ngoại lệ là các shot kể chuyện, nơi vết dùng thật làm hình có đời sống hơn. Phân biệt hai trường hợp này dựa vào mục đích của shot, không dựa vào sở thích người dựng. Toàn bộ chuỗi chín bước chạy trọn một lần trong <a href="du-an-mercedes-g63-tvc.html">dự án dựng TVC 3D Mercedes G63</a>, xem bản hoàn chỉnh dễ hình dung hơn đọc mô tả quy trình.</p>

<h2>Bước 6: Render theo lớp, không render một cục</h2>

<p>Tách render thành các pass riêng: sản phẩm, nền, bóng đổ, phản chiếu, phần phát sáng. Lý do không phải kỹ thuật mà là thực tế: khi khách nói nền tối hơn chút, bạn chỉnh trong ba phút thay vì render lại bốn tiếng.</p>

<figure>
  <img src="assets/mercedes-g63-khung-gam-va-doi-ky-thuat.webp" alt="Khung gầm Mercedes G63 và đội kỹ thuật đang lắp ráp trong cảnh TVC 3D dựng bằng Blender" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Cảnh nhiều thành phần trong dự án Mercedes G63.</strong> Một cảnh có người, khung gầm, khói và sàn phản chiếu như thế này gần như không thể sửa được nếu render thành một file duy nhất. Tách lớp ở đây không phải để đẹp hơn mà để còn sửa được.</figcaption>
</figure>

<p>Đây là khâu tách người làm nghề với người làm bài tập rõ nhất. Người mới render ra một file duy nhất rồi cầu trời khách duyệt. Phần cài đặt render, kiểm soát nhiễu và chia pass là nội dung chính của <a href="blog-khoa-hoc-render.html">khoá học render</a>, và cũng là chỗ tiết kiệm được nhiều giờ máy nhất.</p>

<h3>Tách tới mức nào là đủ</h3>

<p>Nguyên tắc gọn: tách theo thứ khách hay yêu cầu sửa. Nền, bóng đổ, cường độ phát sáng và màu sản phẩm là bốn thứ bị sửa nhiều nhất, nên để riêng bốn thứ đó là đã đủ cho phần lớn shot. Tách quá vụn thì khâu ghép lại thành gánh nặng mới.</p>

<h2>Bước 7: Hậu kỳ nhẹ tay</h2>

<p>Ghép pass, cân bằng tổng thể, thêm chút bloom nếu cảnh cần, xuất đúng không gian màu nơi sẽ đăng. Nếu ở bước này phải kéo mạnh tay, nên quay lại bước bốn. Luôn nhanh hơn, vì sửa gốc một lần rẻ hơn che bằng hậu kỳ ở mọi bản sau.</p>

<h2>Bước 8 và 9: Gửi duyệt và sống sót qua vòng sửa</h2>

<p>Sẽ có sửa. Luôn luôn. Điều kiểm soát được là chi phí mỗi vòng sửa, và nó được quyết định từ bước sáu: file tách lớp gọn gàng thì một vòng sửa là buổi chiều, file gộp một cục thì là hai ngày.</p>

<p>Một thói quen nhỏ giúp rất nhiều: mỗi lần gửi duyệt, đánh số phiên bản và ghi lại đúng một dòng đã đổi những gì. Khi khách bảo quay lại bản hôm trước, bạn có bản hôm trước thật, không phải dựng lại từ ký ức.</p>

<h3>Danh sách kiểm tra trước khi gửi khách</h3>

<ul>
<li>Khung hình đúng tỉ lệ đã chốt ở bước một, kể cả bản cắt cho từng nền tảng.</li>
<li>Chỗ chừa cho chữ còn trống, không bị chi tiết sản phẩm lấn vào.</li>
<li>Màu thương hiệu kiểm tra lại trên ảnh cuối, không chỉ trong cửa sổ render.</li>
<li>Không còn vết nhiễu ở vùng tối và vùng phản chiếu.</li>
<li>Logo và chữ trên bao bì đọc được ở kích thước thật khi đăng.</li>
<li>File xuất đúng không gian màu và đúng định dạng khách yêu cầu.</li>
<li>Tên file có số phiên bản và ngày, kèm một dòng ghi đã đổi gì.</li>
</ul>

<h2>Những chỗ quy trình này hay vỡ</h2>

<p>Nói cho công bằng, chuỗi chín bước không miễn nhiễm rủi ro. Có ba chỗ hay vỡ.</p>

<p>Thứ nhất, khách không duyệt ở bước ba. Nhiều khách thấy ảnh xám thì chưa hình dung được nên bảo cứ làm tiếp. Cách giảm thiệt hại là ghi rõ trong email rằng bố cục coi như đã chốt, và mọi thay đổi góc máy sau bước năm sẽ tính thành vòng sửa.</p>

<p>Thứ hai, brief đổi giữa đường vì phía khách đổi người phụ trách. Không ai chống được việc này, chỉ có thể giảm đau bằng cách giữ file tách lớp và giữ khối thô đủ sạch để dựng lại nhanh.</p>

<p>Thứ ba, shot đơn giản tới mức quy trình thành nặng. Một ảnh sản phẩm nền trắng cho sàn thương mại điện tử không cần chín bước. Dùng đúng mức phức tạp của việc là một phần của tay nghề, và các dạng shot khác nhau có thể xem ở <a href="du-an-san-pham.html">các dự án render sản phẩm</a> để ước lượng mức đầu tư hợp lý.</p>

<h2>Dựng TVC 3D: bước đi tiếp cho người đang học</h2>

<p>Không bước nào ở trên đòi hỏi kỹ thuật cao siêu. Chúng đòi hỏi biết trước điều gì sắp xảy ra, thứ mà học một mình thì phải trả giá bằng vài dự án hỏng mới rút ra được. Nếu bạn đang tự học và muốn rút ngắn đoạn đó, hai hệ trong <a href="khoa-hoc.html">khoá học 3D Blender</a> được dựng theo đúng thứ tự chín bước này, chỉ khác là có người chữa bài ở mỗi mốc.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Dựng TVC 3D một shot sản phẩm mất bao lâu?</p>
<p>Ước lượng cho một shot độ phức tạp trung bình là bốn tới bảy ngày làm việc nếu khách phản hồi trong ngày, và dài hơn đáng kể khi vòng duyệt chậm. Phần chiếm thời gian thật thường không phải render mà là chờ duyệt bố cục và vật liệu.</p>

<p class="faq-q">Vì sao phải chốt góc máy trước khi model chi tiết?</p>
<p>Vì chi tiết ở mặt không lên hình là chi tiết bỏ đi. Chốt camera từ giai đoạn khối xám cho biết chính xác cần làm kỹ chỗ nào, và ngăn tình huống dựng xong mới nghe khách nói muốn nhìn từ hướng khác.</p>

<p class="faq-q">Có nhất thiết phải render theo lớp không?</p>
<p>Với bài tập cá nhân thì không. Với dự án có khách duyệt thì gần như bắt buộc, vì phần lớn yêu cầu sửa chỉ liên quan tới một lớp. Tách lớp biến một vòng sửa từ việc render lại cả cảnh thành việc chỉnh trong vài phút.</p>

<p class="faq-q">Người mới nên bắt đầu học khâu nào trong chuỗi này?</p>
<p>Khối thô và góc máy. Hai khâu đó quyết định phần lớn chất lượng cuối cùng, lại ít phụ thuộc cấu hình máy và ít phụ thuộc phần mềm nhất, nên học sớm là có lãi lâu nhất.</p>

<p class="faq-q">Studio tính báo giá dựng 3D sản phẩm theo shot hay theo ngày?</p>
<p>Cách phổ biến ở Việt Nam là tính theo shot với số vòng sửa ghi rõ trong hợp đồng, vì khách dễ hình dung hơn. Dù tính kiểu nào, phần cần chốt bằng văn bản là số vòng sửa được bao gồm và mốc nào coi là đã duyệt.</p>

<hr class="hr">

<p>Nếu bạn muốn tự chạy thử chuỗi này trên một shot của mình, tải <a href="cam-nang.html">cẩm nang Blender</a> để có sẵn checklist lighting và bảng cài đặt render, rồi làm lại đúng một sản phẩm theo chín bước trên. Gửi bản xám ở bước ba cho một người biết nghề xem trước khi đi tiếp, đó là một bước nhỏ nhưng tiết kiệm nhiều nhất.</p>
""",
    },
    {
        "slug": "kho-hau-truong-overgrown-blender-studio",
        "title": "Kho hậu trường OVERGROWN của Blender Studio",
        "desc": "Blender Studio mở miễn phí nhật ký sản xuất phim OVERGROWN: rigging, lông, shading, ánh sáng, nước, compositing. Đây là cách khai thác nó cho ra kỹ năng thật.",
        "tag": "Tài nguyên",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "7 phút đọc",
        "thumb": "assets/a77adfda.jpg",
        "sources": [
            ("Blender Studio Opens OVERGROWN's Free Behind-the-Scenes Archive (80 Level)",
             "https://80.lv/articles/blender-studio-opens-overgrown-s-free-behind-the-scenes-archive"),
            ("Blender Studio, trang dự án chính thức", "https://studio.blender.org/"),
        ],
        "body": """
<p class="lead">Blender Studio vừa mở miễn phí kho nhật ký sản xuất của phim hoạt hình OVERGROWN trong đợt Open Doors Week. Với người tự học, đây là thứ hiếm: không phải tutorial dựng cho người xem, mà là ghi chép của một ê-kíp làm phim thật.</p>

<h2>Trong kho có gì</h2>

<p>Theo 80 Level, bộ tài liệu gồm sáu nhật ký sản xuất trải khắp pipeline: rigging nhân vật và xử lý lông, casting lồng tiếng, dựng bối cảnh, shading, animation từng shot, phát triển hình ảnh, hiệu ứng nước và giọt nước, ánh sáng, nhạc và compositing cuối. Kèm theo là một masterclass của Simon Thommes về kỹ thuật đổ bóng theo hướng painterly.</p>

<p>Toàn bộ truy cập qua trang dự án trên studio.blender.org. Miễn phí có thời hạn, nên nếu định xem, đừng để dành.</p>

<h2>Vì sao thứ này khác tutorial thường</h2>

<p>Tutorial trên mạng được dựng ngược: người dạy đã biết kết quả cuối, rồi quay lại làm từng bước cho mượt. Bạn xem xong thấy mọi quyết định đều hiển nhiên, và tưởng nghề này là chuỗi bước đúng nối nhau.</p>

<p>Nhật ký sản xuất thì ngược lại. Nó ghi lại lúc ê-kíp chưa biết đáp án: phương án bị bỏ, chỗ phải làm lại, ràng buộc về thời gian buộc phải cắt gọt. Đó mới là hình dạng thật của công việc.</p>

<blockquote><p>Xem tutorial dạy bạn làm được một thứ. Đọc nhật ký sản xuất dạy bạn cách nghĩ khi chưa biết phải làm gì.</p></blockquote>

<h2>Cách khai thác cho ra kỹ năng, không chỉ để xem cho biết</h2>

<h3>Chọn một khâu, đừng xem hết</h3>
<p>Cám dỗ lớn nhất là mở tất cả rồi lướt. Sáu nhật ký cộng masterclass là khối lượng đủ để bạn xem hai ngày và không nhớ gì. Chọn đúng khâu bạn đang yếu, nếu đang mắc ở ánh sáng thì chỉ xem phần ánh sáng và compositing.</p>

<h3>Dừng lại ở mỗi quyết định, tự trả lời trước</h3>
<p>Khi họ nêu vấn đề, bấm dừng. Tự hỏi mình sẽ xử lý thế nào, viết ra một câu. Rồi mới xem tiếp. Chênh lệch giữa câu trả lời của bạn và của họ chính là bài học, phần bạn xem trôi tuột không phải.</p>

<h3>Chép lại một shot, không phải cả phim</h3>
<p>Lấy một shot bạn thích, dựng lại bằng tài sản của riêng bạn. Không cần giống, cần hiểu vì sao ánh sáng đặt ở đó và vì sao camera dừng lại chỗ đó.</p>

<h2>Một lưu ý về phong cách</h2>

<p>OVERGROWN đi theo hướng stylized, không phải render sản phẩm thương mại. Nếu bạn đang học để làm TVC hay hình ảnh sản phẩm, đừng bê nguyên bảng màu và cách đổ bóng của phim vào job thương mại, hai bài toán khác nhau.</p>

<p>Cái đáng lấy là <strong style="color:#fff;">cách tổ chức công việc</strong>: chia shot ra sao, quản lý phiên bản thế nào, ai quyết cái gì ở khâu nào. Phần đó dùng được cho mọi thể loại, và là phần khó tự nghĩ ra nhất khi làm một mình.</p>

<p>Nếu bạn chưa rõ mình đang yếu khâu nào để chọn nhật ký mà xem, bài <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình 7 kỹ năng</a> có thể giúp bạn định vị.</p>
""",
    },
    {
        "slug": "add-on-hard-surface-blender",
        "title": "Add-on hard-surface Blender: nên cài những gì",
        "desc": "Danh sách add-on hard-surface mà artist tại CD Projekt Red dùng, và đánh giá thẳng thắn cái nào thật sự cần khi bạn làm sản phẩm thương mại.",
        "tag": "Công cụ",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "9 phút đọc",
        "thumb": "assets/b64a4cd7.jpg",
        "sources": [
            ("Tools and Tips for Hard-Surface Modeling in Blender (80 Level, Michał Kalisz, CD Projekt Red)",
             "https://80.lv/articles/tools-and-tips-for-hard-surface-modeling-in-blender-2-8"),
            ("Ahmed Yahya Shared a Breakdown of Hard-Surface Modeling Process (80 Level)",
             "https://80.lv/articles/artist-shared-how-to-make-hard-surface-modeling-more-artistic-easy"),
        ],
        "body": """
<p class="lead">Michał Kalisz, Environment/Prop Artist tại CD Projekt Red, từng chia sẻ trên 80 Level danh sách add-on anh dùng cho hard-surface. Danh sách đó tốt, nhưng nếu bạn đang học để làm sản phẩm thương mại chứ không phải asset game, không phải cái nào cũng cần.</p>

<p>Dưới đây là danh sách của anh ấy, kèm đánh giá của tôi về mức độ cần thiết cho công việc dựng sản phẩm và TVC.</p>

<h2>Nhóm đáng cài sớm</h2>

<h3>Hard Ops + Boxcutter</h3>
<p>Hai cái này thường đi cùng nhau. Boxcutter lo phần cắt boolean nhanh, Hard Ops là bộ trợ lý gom các thao tác lặp lại. Với đồ công nghiệp như vỏ máy, thiết bị, chi tiết kim loại, cặp này rút ngắn thời gian rõ rệt.</p>
<p><strong style="color:#fff;">Nhưng:</strong> đừng cài khi chưa dựng được vỏ máy bằng tay. Boolean tạo ra topology xấu, và nếu bạn chưa biết topology tốt trông thế nào thì bạn sẽ không thấy nó xấu, cho tới lúc bevel vỡ và không hiểu vì sao.</p>

<h3>MESHMachine</h3>
<p>Chuyên xử lý phần khó nhất của hard-surface: chỗ giao nhau giữa các bề mặt sau khi boolean. Đây là add-on tôi cho là đáng tiền nhất trong danh sách, vì nó giải quyết đúng chỗ mà người mới hay bỏ cuộc.</p>

<h3>Modifier List</h3>
<p>Nhỏ nhưng dùng hàng ngày. Stack modifier mặc định của Blender khó đọc khi dài; cái này làm nó gọn lại. Rẻ, không rủi ro.</p>

<h2>Nhóm tuỳ việc</h2>

<h3>Texel Density Checker &amp; UVPackMaster</h3>
<p>Cả hai đều xoay quanh UV. Nếu bạn làm asset game hoặc cần texture bake, chúng cần thiết. Nếu bạn render sản phẩm tĩnh với vật liệu procedural, và phần lớn job TVC sản phẩm rơi vào đây, thì bạn hiếm khi động tới.</p>

<h3>GroupPro, Array Tools, QBlocker, Rebevel</h3>
<p>Đều là tiện ích tiết kiệm thao tác. Hữu ích khi bạn đã làm nhanh và muốn nhanh hơn. Không nên là thứ bạn cài trong sáu tháng đầu.</p>

<h2>Phần Kalisz nói mà tôi cho là quan trọng hơn cả danh sách add-on</h2>

<p>Anh ấy nhấn mạnh nghiên cứu tham chiếu kỹ trước khi dựng, và làm blockout trước khi vào chi tiết. Về topology: giữ số vòng loop ở mức vừa đủ để kiểm soát, ưu tiên quad nhưng chấp nhận ngon trên bề mặt phẳng, và bevel theo đúng chất liệu, vì kim loại gia công có cạnh khác với nhựa đúc khuôn.</p>

<p>Không add-on nào thay được mấy điều đó. Một người nắm chắc blockout và bevel, dùng Blender trần, vẫn ra sản phẩm tốt hơn người cài đủ mười add-on mà bỏ qua tham chiếu.</p>

<h2>Góc nhìn ngược: đừng để kỹ thuật lấn hết</h2>

<p>Ahmed Yahya, một 3D Environment &amp; Prop Artist khác, đưa ra lập luận đáng cân nhắc: tập trung quá mức vào kỹ thuật làm gián đoạn quá trình sáng tạo, và định hướng nghệ thuật nên dẫn dắt kỹ thuật chứ không phải ngược lại. Quy trình của anh đi qua Plasticity để dựng, Blender để dọn dẹp, ZBrush để lên high-poly.</p>

<p>Tôi đồng ý với nguyên tắc, nhưng có một điều kiện: nó chỉ đúng khi bạn đã đủ kỹ thuật để nó không cản đường. Người mới nghe câu "nghệ thuật quan trọng hơn kỹ thuật" rất dễ dùng nó làm cớ để không học topology, rồi mắc kẹt ở đúng chỗ topology.</p>

<blockquote><p>Kỹ thuật đủ tốt là kỹ thuật bạn không phải nghĩ tới. Trước khi tới được đó, bỏ qua kỹ thuật không phải là tự do, mà là trần thấp.</p></blockquote>

<h2>Nếu chỉ được cài ba thứ</h2>

<p>Với người học hard-surface để làm sản phẩm thương mại, tôi chọn: <strong style="color:#fff;">Hard Ops, Boxcutter, MESHMachine</strong>, và chỉ sau khi đã dựng tay được vài món tử tế. Số tiền còn lại để dành mua tham chiếu tốt hoặc một khoá học có người sửa bài, giá trị cao hơn.</p>

<p>Muốn biết hard-surface nằm ở đâu trong lộ trình học, xem <a href="blog-lo-trinh-tu-hoc-blender.html">bài về 7 kỹ năng</a>. Nó là bước thứ năm, và có lý do nó không đứng sớm hơn. Còn nếu bạn đang nhắm hẳn vào mảng hàng tiêu dùng và thiết bị, bài <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a> nói rõ bốn kỹ năng một lớp dạng này phải dạy và chỗ các lớp hay cắt bớt.</p>
""",
    },
    {
        "slug": "sau-node-va-mot-hanh-lang",
        "title": "Sáu node và một hành lang: dựng không khí",
        "desc": "Andrew Price dựng cảnh Backrooms gần như không model, không UV, chỉ sáu node. Phân tích vì sao cách làm này hiệu quả và khi nào nên áp dụng.",
        "tag": "Kỹ thuật",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "6 phút đọc",
        "thumb": "assets/2cdbf5f9.jpg",
        "sources": [
            ("Blender Guru Shares How to Create The Backrooms Using Blender (80 Level)",
             "https://80.lv/articles/blender-guru-shares-how-to-create-the-backrooms-using-blender"),
        ],
        "body": """
<p class="lead">Andrew Price, tức Blender Guru, dựng lại cảnh Backrooms và tuyên bố khoảng 90% hiệu ứng đến từ sáu node, không cần model, không cần UV unwrap. Nghe như mẹo vặt, nhưng bên dưới là một nguyên tắc đáng học.</p>

<h2>Anh ấy làm gì</h2>

<p>Theo mô tả trên 80 Level: tường dựng bằng cách tính toán thay vì model, đường đi tạo từ texture, các khoảng khoét bằng khối hộp, texture áp bằng projection thay vì UV. Nhóm node chính gồm Grid, Greater Than, Mesh to Curve, Quadrilateral và Curve to Mesh. Đường đi được điều khiển bằng cách chỉnh scale của Noise Texture; box projection dùng để áp vật liệu cho gọn.</p>

<p>Phần render đi qua Cycles, chỉnh màu bằng RGB curve, thêm film grain cho chất analog, và thêm glare khi compositing. Giá trị shader được nối vào Geometry Nodes để bật tắt đèn và tạo sự ngẫu nhiên cho các tấm đèn trần.</p>

<h2>Điểm đáng học không phải là sáu node</h2>

<p>Nếu bạn chỉ chép lại setup node, bạn có một cảnh Backrooms. Hết. Điều đáng lấy là câu hỏi Price đặt ra trước khi bắt đầu: <strong style="color:#fff;">cảnh này thật ra cần gì để thuyết phục?</strong></p>

<p>Backrooms thuyết phục nhờ ba thứ: sự lặp lại đến mức bất an, ánh sáng huỳnh quang bẹt, và cảm giác không gian kéo dài vô tận. Không thứ nào đòi hỏi model chi tiết. Nhận ra điều đó cho phép bỏ qua 90% khối lượng công việc mà không mất gì.</p>

<blockquote><p>Trước khi hỏi làm thế nào, hỏi cảnh này thật sự cần gì. Câu trả lời thường ngắn hơn bạn tưởng.</p></blockquote>

<h2>Khi nào cách này dùng được, khi nào không</h2>

<h3>Dùng được</h3>
<p>Không gian lặp lại và mang tính không khí: hành lang, kho, bãi đỗ xe, nội thất công nghiệp, background phía sau chủ thể chính. Những chỗ người xem cảm nhận tổng thể chứ không soi chi tiết.</p>

<h3>Không dùng được</h3>
<p>Sản phẩm nằm ở tiền cảnh. Nếu khách trả tiền để chai nước hay chiếc điện thoại của họ lên hình, mọi bevel đều bị soi. Không mẹo procedural nào thay được model đúng ở đó.</p>

<p>Nhưng ngay trong job sản phẩm, nguyên tắc vẫn dùng được cho phần nền. Dựng cả một studio chi tiết phía sau chai nước là lãng phí. Nền chỉ cần đúng ánh sáng và đúng vệt phản chiếu.</p>

<h2>Ba chi tiết nhỏ đáng chú ý</h2>

<h3>Box projection thay UV</h3>
<p>Với bề mặt phẳng và lặp lại, projection cho kết quả đủ tốt và tiết kiệm hoàn toàn khâu UV. Đây là thứ nhiều người học Blender không biết mình được phép bỏ qua.</p>

<h3>Ngẫu nhiên hoá đèn trần</h3>
<p>Một vài tấm đèn tắt, một vài tấm sáng yếu hơn. Chi tiết rất nhỏ nhưng là thứ tách cảnh CG khỏi cảnh trông như thật, vì sự đều tăm tắp là dấu hiệu của máy tính.</p>

<h3>Film grain và glare</h3>
<p>Hai thứ này thêm ở khâu compositing, nhưng chỉ hiệu quả khi ánh sáng bên dưới đã đúng. Nếu bạn thấy mình dựa vào grain để cảnh đỡ giả, vấn đề nằm ở đèn. Tôi có viết kỹ hơn trong bài <a href="blog-5-loi-lighting.html">học lighting trong Blender</a>.</p>

<h2>Bài tập</h2>

<p>Lấy một không gian bạn từng dựng thủ công và tự hỏi: nếu chỉ được dùng năm node, phần nào của cảnh này thật sự cần thiết? Trả lời được câu đó, bạn tiết kiệm được vài chục giờ cho mọi dự án sau.</p>
""",
    },
    {
        "slug": "hoc-blender-3d-bao-lau",
        "title": "Học Blender 3D bao lâu thì nhận được job đầu tiên?",
        "desc": "Học Blender 3D bao lâu mới nhận được job đầu tiên? Mốc thời gian theo số giờ học mỗi tuần, bốn giai đoạn kèm dấu hiệu đã qua và cách rút ngắn quãng đường.",
        "tag": "Định hướng",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "updated": "2026-10-22",
        "updated_vn": "22/10/2026",
        "read": "12 phút đọc",
        "thumb": "assets/vplas-render-san-pham-blender.jpg",
        "faq": [
            ("Học Blender 3D bao lâu thì đi làm được?",
             "Học đều 10-15 giờ mỗi tuần và có người sửa bài: khoảng 4-6 tháng để có portfolio nhận job nhỏ, 10-14 tháng để nhận job thương mại. Tự học hoàn toàn thường mất gấp hai tới gấp ba."),
            ("Không biết vẽ có học Blender được không?",
             "Được. Mảng 3D thương mại như sản phẩm, hard-surface hay kiến trúc không đòi hỏi kỹ năng vẽ tay. Chỉ mảng character và concept stylized mới cần."),
            ("Học Blender rồi có phải học thêm 3ds Max hay Maya không?",
             "Không, trừ khi bạn nhắm vào studio bắt buộc dùng phần mềm đó. Blender làm được trọn pipeline sản phẩm và TVC."),
            ("Trên 30 tuổi học Blender có muộn không?",
             "Không. Khách hàng nhìn portfolio chứ không nhìn tuổi. Người chuyển ngành còn có lợi thế vì đã quen deadline và làm việc với khách."),
            ("Học Blender bao lâu thì nên bỏ tiền đi học khoá?",
             "Thường là sau một tới hai tháng tự đi, khi bạn bắt đầu thấy mình lặp lại cùng một lỗi. Lúc đó bạn đã đủ nền để tận dụng buổi chữa bài, nên so các nơi bằng số lần được chữa bài thay vì tổng học phí."),
            ("Học 3D online có chậm hơn học trực tiếp không?",
             "Không chậm hơn đáng kể, miễn là bài của bạn vẫn được mở ra và sửa trực tiếp trên file. Cái quyết định là tần suất phản hồi chứ không phải việc ngồi cùng phòng."),
        ],
        "body": """
<p class="lead">Học Blender 3D bao lâu thì nhận được job đầu tiên? Với người học đều 10 tới 15 giờ mỗi tuần và có người sửa bài, mốc thường thấy là 4 tới 6 tháng để có portfolio nhận job nhỏ, 10 tới 14 tháng để nhận job thương mại. Tự học một mình thường cộng thêm gấp hai tới gấp ba. Đây là khoảng ước lượng rút ra từ việc kèm học viên, không phải cam kết.</p>

<h2>Câu trả lời ngắn</h2>

<p>Với người học đều <strong style="color:#fff;">10 đến 15 giờ mỗi tuần</strong> và có người sửa bài: khoảng <strong style="color:#fff;">4 đến 6 tháng</strong> để có portfolio đủ nhận job nhỏ, <strong style="color:#fff;">10 đến 14 tháng</strong> để nhận được job thương mại tử tế.</p>

<p>Tự học hoàn toàn, không ai sửa: cộng thêm gấp đôi tới gấp ba. Không phải vì bạn học chậm hơn, mà vì bạn mất nhiều tháng đi sai hướng rồi mới nhận ra.</p>

<p>Câu "ba tháng là làm được" nghe thì dễ chốt đơn, nhưng nó bỏ qua phần tốn thời gian nhất của nghề: không phải học nút bấm, mà học cách nhìn ra hình của mình sai ở đâu. Phần đó không rút ngắn được bằng cách xem thêm video.</p>

<h2>Học Blender 3D bao lâu nếu mỗi tuần chỉ rảnh vài giờ</h2>

<p>Số giờ mỗi tuần là biến dễ đo nhất, nên bắt đầu từ đó. Bảng dưới là ước lượng cho người có người chữa bài định kỳ. Nếu tự học hoàn toàn, nhân đôi mọi cột.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Số giờ mỗi tuần</th><th>Có bài tử tế đầu tiên</th><th>Nhận được job nhỏ</th><th>Nhận job thương mại</th></tr></thead>
<tbody>
<tr><td>4 tới 6 giờ</td><td>5 tới 8 tháng</td><td>12 tới 18 tháng</td><td>Khó nói trước</td></tr>
<tr><td>10 tới 15 giờ</td><td>3 tới 4 tháng</td><td>4 tới 6 tháng</td><td>10 tới 14 tháng</td></tr>
<tr><td>25 giờ trở lên</td><td>6 tới 10 tuần</td><td>3 tới 5 tháng</td><td>8 tới 11 tháng</td></tr>
</tbody>
</table>
</div>

<p>Dòng đầu tiên là dòng cần nói thẳng. Bốn tới sáu giờ mỗi tuần vẫn học được, nhưng quãng đường dài tới mức phần lớn người bỏ giữa chừng vì không thấy mình nhúc nhích. Nếu lịch của bạn chỉ cho phép tới đó, nên thu hẹp mục tiêu lại: chọn một mảng hẹp, ví dụ dựng hình sản phẩm, thay vì học dàn trải cả modeling, lighting, chuyển động và hậu kỳ cùng lúc.</p>

<h2>Bốn giai đoạn, và dấu hiệu bạn đã qua</h2>

<h3>Tháng 1 đến 2: làm quen công cụ</h3>
<p>Bạn dựng được vật thể đơn giản, biết di chuyển trong viewport không phải nghĩ, hiểu modifier cơ bản. Đây là giai đoạn dễ chịu nhất và cũng gây ảo tưởng nhất, vì nhiều người tưởng mình đã học được nghề.</p>
<p><strong style="color:#fff;">Dấu hiệu qua:</strong> bạn dựng được một vật ngoài đời mà không cần xem hướng dẫn từng bước.</p>

<h3>Tháng 3 đến 5: hình bắt đầu "trông được"</h3>
<p>Ánh sáng và vật liệu vào cuộc. Đây là chỗ khoảng cách giữa người có người kèm và người tự học mở ra lớn nhất, vì bạn không tự thấy được ánh sáng của mình sai ở đâu khi chưa có ai chỉ. Phần lớn lỗi ở giai đoạn này lặp lại y hệt nhau, tôi gom trong bài <a href="blog-5-loi-lighting.html">năm lỗi lighting thường gặp</a>.</p>
<p><strong style="color:#fff;">Dấu hiệu qua:</strong> bạn nhìn render của mình và nói được cụ thể chỗ nào chưa ổn, chứ không chỉ cảm giác "chưa đã".</p>

<figure>
  <img src="assets/vplas-render-san-pham-blender.jpg" alt="Render sản phẩm thiết bị y tế VPLAS dựng bằng Blender, bề mặt kim loại, ánh sáng studio nền tối" loading="lazy" width="1600" height="900">
  <figcaption><strong>Shot sản phẩm trong dự án VPLAS của LXAM Studio.</strong> Chỉ một nguồn sáng chính và vài mặt hắt, cái khó không nằm ở số lượng đèn mà ở việc đặt đúng chỗ để bề mặt kim loại có chuyển sáng.</figcaption>
</figure>

<h3>Tháng 6 đến 10: làm được sản phẩm hoàn chỉnh</h3>
<p>Bạn xử lý được hard-surface, biết tổ chức scene cho dự án nhiều shot, render ra file dùng được chứ không phải file phải sửa lại. Đây là lúc portfolio bắt đầu có sức nặng. Số món cần có và thứ tự làm chúng nằm ở bài <a href="blog-kem-1-1-lam-portfolio-3d.html">kèm 1 kèm 1 làm portfolio 3D</a>.</p>
<p><strong style="color:#fff;">Dấu hiệu qua:</strong> bạn hoàn thành một dự án từ đầu tới cuối mà không bỏ dở giữa chừng.</p>

<h3>Tháng 10 trở đi: làm được job thật</h3>
<p>Khác biệt ở giai đoạn này không còn là kỹ thuật. Là biết đọc brief, biết báo giá, biết xử lý khi khách đổi ý ở phút cuối, biết chia file để sửa nhanh. Tôi có viết riêng về <a href="blog-quy-trinh-mot-shot-tvc.html">quy trình một shot chạy thật</a>.</p>

<figure>
  <img src="assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp" alt="Key visual khoá cửa thông minh dựng bằng Blender, hai thân khoá màu đen lơ lửng trên nền xám sáng với dòng chữ DIGITAL LOCK phía sau" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một key visual sản phẩm trong dự án khoá cửa thông minh của LXAM Studio.</strong> Mức hoàn thiện mà khách trả tiền không nằm ở số chi tiết trên mẫu, mà ở chỗ bố cục, chữ và ánh sáng cùng phục vụ một thông điệp.</figcaption>
</figure>

<h2>Danh sách kiểm tra: bạn đang ở giai đoạn nào</h2>

<p>Đọc từ trên xuống, dừng ở dòng đầu tiên bạn chưa làm được. Đó là chỗ bạn đang đứng, và cũng là việc cần làm trong vài tuần tới. Phần lớn người tự học kẹt ở dòng thứ ba hoặc thứ tư mà tưởng mình đã ở dòng thứ sáu.</p>

<ul>
<li>Mở Blender và dựng được một vật đơn giản mà không bật video hướng dẫn.</li>
<li>Nói được vì sao đặt đèn chính ở đúng hướng đó, không phải thử tới khi thấy ổn.</li>
<li>Nhìn render của mình và chỉ ra được ít nhất hai chỗ sai cụ thể.</li>
<li>Hoàn thành một bài tới khâu cuối, kể cả phần hậu kỳ, không bỏ dở.</li>
<li>Dựng lại cùng một vật lần thứ hai và thấy rõ bản sau tốt hơn ở chỗ nào.</li>
<li>Giữ được cạnh sạch trên hard-surface khi lên subdivision.</li>
<li>Mở lại file của ba tháng trước và vẫn hiểu mình đặt tên, chia nhóm thế nào.</li>
<li>Có ít nhất ba bài đủ chất lượng đặt cạnh nhau mà không bài nào kéo hai bài kia xuống.</li>
<li>Đọc một brief và ước lượng được số buổi làm, không phải đoán bừa.</li>
</ul>

<p>Danh sách này dùng tốt nhất mỗi tháng một lần. Nếu sau ba tháng bạn vẫn dừng ở đúng một dòng, vấn đề không phải thời gian, mà là thiếu phản hồi. Bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm</a> so sánh thẳng hai con đường ở chính điểm này.</p>

<h2>Học bao lâu còn tuỳ hướng bạn chọn</h2>

<p>"Nghề 3D" không phải một nghề. Mỗi hướng có độ dốc khác nhau, và chọn sai hướng so với quỹ thời gian của mình là cách mất một năm êm ái nhất.</p>

<h3>Dựng hình sản phẩm: dốc thoải nhất</h3>
<p>Vật thể có ảnh tham chiếu rõ, yêu cầu của khách cụ thể, và bạn biết ngay mình đúng hay sai vì đặt cạnh ảnh thật là thấy. Đây là hướng cho kết quả sớm nhất, thường 6 tới 10 tháng là có bài dùng được. Nội dung của hướng này nằm ở <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a>.</p>

<h3>Hard-surface và automotive: lâu hơn, rõ ràng hơn</h3>
<p>Bề mặt phản chiếu không tha cho lỗi nào, nên yêu cầu về lưới và ánh sáng cao hơn hẳn. Cộng thêm 4 tới 8 tháng so với sản phẩm thường. Bù lại thị trường hẹp và người làm được không nhiều.</p>

<h3>Phối cảnh sự kiện và triển lãm: nhanh có việc</h3>
<p>Hướng này ở Việt Nam có nhu cầu đều, vì mỗi sự kiện đều cần phối cảnh để duyệt trước khi dựng thật. Yêu cầu về độ chính xác bề mặt thấp hơn automotive, nhưng đòi hỏi đọc được bản vẽ và làm việc theo deadline gấp. Xem các dạng việc thật ở trang <a href="dich-vu.html">dịch vụ render 3D và phối cảnh sự kiện</a>.</p>

<h3>TVC và chuyển động: dốc nhất</h3>
<p>Cộng thêm timing, camera, mô phỏng và hậu kỳ, nên thời gian gần như nhân đôi so với làm hình tĩnh. Đừng bắt đầu từ đây nếu bạn chưa làm chủ được một shot tĩnh.</p>

<h2>Bốn thứ quyết định bạn nhanh hay chậm</h2>

<h3>1. Có được sửa bài hay không</h3>
<p>Đây là biến số lớn nhất, hơn cả tài năng hay số giờ ngồi máy. Người tự học có thể ngồi sáu tháng với một thói quen sai mà không biết. Người được sửa bài mất một buổi để bỏ thói quen đó. Nếu chưa muốn đi học hẳn, thuê <a href="blog-gia-su-blender.html">gia sư Blender</a> theo buổi cũng đủ để cắt những vòng lặp sai dài nhất.</p>

<h3>2. Làm dự án hay làm bài tập</h3>
<p>Bài tập có đáp án sẵn, làm xong thấy vui rồi thôi. Dự án có ràng buộc thật: deadline, yêu cầu, người duyệt, và ép bạn giải quyết vấn đề chưa ai dạy. Một dự án hoàn chỉnh dạy nhiều hơn hai mươi bài tập.</p>

<h3>3. Đi đúng thứ tự kỹ năng</h3>
<p>Học đúng nội dung nhưng sai thứ tự vẫn chậm, vì mỗi bước cần bước trước làm nền. Bảng <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> chia bảy bước kèm mốc thời gian ước lượng, dùng để tự kiểm tra xem mình có đang nhảy cóc hay không.</p>

<h3>4. Đều đặn hơn là dồn dập</h3>
<p>10 giờ mỗi tuần trong sáu tháng ăn đứt 40 giờ một tuần rồi nghỉ hai tháng. Kỹ năng 3D là kỹ năng vận động, mắt và tay cần lặp lại thường xuyên mới giữ được.</p>

<blockquote><p>Thứ khiến người ta bỏ Blender hiếm khi là độ khó. Thường là sáu tháng không thấy mình tiến bộ, vì không ai nói cho họ biết họ đang sai ở đâu.</p></blockquote>

<h2>Rút ngắn thời gian mà không đốt cháy giai đoạn</h2>

<p>Có vài cách rút ngắn thật sự có tác dụng, và chúng đều nhàm chán hơn người ta mong đợi.</p>

<ul>
<li><strong style="color:#fff;">Dựng lại một vật ba lần, thay vì dựng ba vật một lần.</strong> Lần hai và lần ba là nơi kỹ năng thật sự hình thành, vì bạn đã biết chỗ khó nằm ở đâu.</li>
<li><strong style="color:#fff;">Nhờ nhận xét sớm, đừng đợi đến khi thấy mình đủ giỏi.</strong> Bài càng thô thì lỗi càng cơ bản, mà lỗi cơ bản sửa một lần là xong, để lâu thành thói quen.</li>
<li><strong style="color:#fff;">Luôn có ảnh tham chiếu thật đặt cạnh.</strong> Dựng theo trí nhớ là cách luyện sai nhanh nhất.</li>
<li><strong style="color:#fff;">Đừng đổi phần mềm giữa chừng.</strong> Nếu còn phân vân, đọc <a href="blog-blender-hay-3dsmax-c4d.html">so sánh Blender với 3ds Max và C4D</a> một lần rồi chốt, đừng để câu hỏi đó quay lại mỗi hai tháng.</li>
<li><strong style="color:#fff;">Giới hạn thời gian xem video.</strong> Quá một phần tư quỹ thời gian dành cho việc xem mà không mở Blender nghĩa là bạn đang tiêu thụ chứ không học.</li>
</ul>

<p>Thứ không rút ngắn được là số lần bạn làm hỏng rồi sửa. Khoá học, gia sư hay nhóm học chỉ làm một việc: rút ngắn quãng giữa lúc bạn làm hỏng và lúc bạn biết mình đã hỏng ở đâu. Toàn bộ chênh lệch thời gian trong bài này nằm ở đó.</p>

<h2>Vài câu hỏi hay gặp</h2>

<p class="faq-q">Không biết vẽ có học được không?</p>
<p>Được. 3D thương mại, từ sản phẩm, hard-surface tới kiến trúc, không đòi hỏi kỹ năng vẽ tay. Mảng cần vẽ là character và concept stylized, không phải hướng duy nhất của nghề.</p>

<p class="faq-q">Học Blender rồi có phải học thêm 3ds Max hay Maya?</p>
<p>Không, trừ khi bạn nhắm vào một studio bắt buộc dùng phần mềm đó. Blender làm được trọn pipeline sản phẩm và TVC. Nắm chắc một công cụ hơn là biết lõm bõm ba cái.</p>

<p class="faq-q">Trên 30 tuổi bắt đầu có muộn không?</p>
<p>Không. Khách hàng nhìn portfolio, không nhìn tuổi. Người đi làm chuyển ngành thường còn có lợi thế: đã quen deadline và làm việc với khách, hai thứ dân mới ra trường phải học lại từ đầu.</p>

<p class="faq-q">Học bao lâu thì nên bỏ tiền đi học khoá?</p>
<p>Thường là sau khi bạn đã tự đi được một tới hai tháng và bắt đầu thấy mình lặp lại cùng một lỗi. Lúc đó bạn đủ nền để tận dụng buổi chữa bài. Cách bóc tách <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a> theo số lần được chữa bài giúp bạn so các nơi bằng cùng một thước.</p>

<p class="faq-q">Học online có chậm hơn học trực tiếp không?</p>
<p>Không chậm hơn đáng kể, miễn là bài của bạn vẫn được mở ra và sửa trực tiếp trên file. Cái quyết định là tần suất phản hồi chứ không phải ngồi cùng phòng. Chi tiết nằm ở bài <a href="blog-khoa-hoc-3d-online.html">khoá học 3D online</a>.</p>

<p class="faq-q">Cần máy mạnh không?</p>
<p>Lúc bắt đầu thì không. Tôi có viết riêng một bài về <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> và khi nào thật sự cần nâng cấp.</p>

<hr class="hr">

<p>Tóm lại, học Blender 3D bao lâu phụ thuộc vào ba thứ theo đúng thứ tự: có ai sửa bài cho bạn không, bạn học đều hay học dồn, và bạn chọn hướng nào. Nếu muốn xem nội dung từng chặng được chia ra sao, hai hệ đào tạo nằm ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>, còn bản tóm tắt lộ trình để tự dò thì tải ở <a href="cam-nang.html">cẩm nang 3D</a>.</p>

<p>Nếu bạn đang tự học và không chắc mình đang ở giai đoạn nào, gửi tôi vài bài render, tôi xem qua và nói thẳng bạn đang mắc ở đâu, kể cả khi câu trả lời là bạn chưa cần học khoá nào cả.</p>
""",
    },
    {
        "slug": "cau-hinh-may-hoc-blender",
        "title": "Cấu hình máy học Blender 3D: máy yếu có học được?",
        "desc": "Cấu hình máy học Blender 3D cần tới đâu, máy yếu kẹt lại ở khâu nào trước, nên nâng GPU hay RAM trước, và mốc nào thì nâng cấp mới thật sự đáng tiền.",
        "tag": "Thiết bị",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "9 phút đọc",
        "thumb": "assets/vplas-hieu-ung-plasma-blender.jpg",
        "body": """
<p class="lead">Câu hỏi này thường đến kèm một mong đợi ngầm: rằng máy mạnh hơn sẽ làm hình đẹp hơn. Nói thẳng: không. Máy mạnh làm bạn chờ ít hơn. Đẹp hay không nằm ở chỗ khác.</p>

<p>Nhưng chờ ít hơn cũng đáng tiền, nên đây là hướng dẫn thật theo từng giai đoạn.</p>

<h2>Giai đoạn 1: Mới học: đừng mua gì cả</h2>

<p>Blender chạy được trên máy khá phổ thông. Nếu máy bạn có card rời bất kỳ, 16GB RAM và SSD, bạn đủ đi hết giai đoạn học modeling, vật liệu và ánh sáng cơ bản, tức là khoảng nửa năm đầu.</p>

<p>Ở giai đoạn này cảnh của bạn nhẹ, render nháp vài phút là xong. Nâng cấp máy lúc này giống mua giày chạy marathon khi mới tập đi bộ. Thứ nên đổ công vào thay vì phần cứng được liệt kê trong bài <a href="blog-hoc-do-hoa-3d-tu-con-so-0.html">học đồ hoạ 3D từ con số 0</a>.</p>

<blockquote><p>Người mới hay đổ cho máy khi hình chưa đẹp. Chín trên mười lần, đổi máy xong hình vẫn vậy, chỉ là ra kết quả nhanh hơn.</p></blockquote>

<h2>Giai đoạn 2: Bắt đầu render nặng: ưu tiên GPU và RAM</h2>

<p>Khi cảnh có nhiều vật thể, vật liệu phức tạp và bạn render Cycles, thứ tự ưu tiên rất rõ:</p>

<h3>GPU: quan trọng nhất</h3>
<p>Cycles render bằng GPU nhanh hơn CPU nhiều lần. Điều cần chú ý không chỉ là tốc độ mà là <strong style="color:#fff;">dung lượng VRAM</strong>: nếu cảnh không nhét vừa VRAM, render sẽ đổ ngược về RAM hệ thống và chậm đi thảm hại, hoặc lỗi hẳn. Với công việc sản phẩm, 12GB VRAM là mức dễ thở, 24GB thì thoải mái.</p>

<h3>RAM: thứ hai</h3>
<p>32GB là mức làm việc được. 64GB dành cho cảnh nặng, nhiều texture độ phân giải cao, hoặc khi bạn vừa mở Blender vừa mở phần mềm dựng phim. Thiếu RAM biểu hiện rất khó chịu: máy không báo lỗi, chỉ đơ dần.</p>

<h3>CPU: thứ ba</h3>
<p>Ảnh hưởng tới thao tác trong viewport, mô phỏng vật lý, và khâu dựng phim. Không cần đắt nhất; một CPU tầm trung đời mới là đủ.</p>

<h3>SSD: bắt buộc, nhưng rẻ</h3>
<p>File Blender dự án thương mại dễ vượt 200MB, có khi vài trăm. Mỗi lần lưu và mở trên ổ cứng cơ là một lần bạn mất kiên nhẫn. NVMe rẻ hơn nhiều so với thời gian nó tiết kiệm.</p>

<figure>
  <img src="assets/vplas-hieu-ung-plasma-blender.jpg" alt="Hiệu ứng tia plasma render bằng Blender Cycles trong dự án TVC VPLAS" loading="lazy" width="1600" height="900">
  <figcaption><strong>Shot hiệu ứng trong TVC VPLAS.</strong> Những cảnh có phát sáng và volumetric như thế này là chỗ VRAM và thời gian render bắt đầu thành vấn đề thật, không phải ở khâu dựng hình.</figcaption>
</figure>

<h2>Bảng tham khảo theo giai đoạn</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Thành phần</th><th>Mới học (0 đến 6 tháng)</th><th>Làm dự án thật</th></tr></thead>
<tbody>
<tr><td>GPU</td><td>Card rời bất kỳ, ≥6GB VRAM</td><td>≥12GB VRAM, lý tưởng 24GB</td></tr>
<tr><td>RAM</td><td>16GB</td><td>32 đến 64GB</td></tr>
<tr><td>CPU</td><td>Tầm trung đời gần</td><td>Nhiều nhân, đời mới</td></tr>
<tr><td>Ổ cứng</td><td>SSD 512GB</td><td>NVMe 1 đến 2TB</td></tr>
<tr><td>Màn hình</td><td>Cái đang có</td><td>Màu chuẩn, hiệu chuẩn được</td></tr>
</tbody>
</table>
</div>

<h2>Thứ ít người nhắc: màn hình</h2>

<p>Nếu bạn làm hình ảnh thương mại, màn hình sai màu là vấn đề nghiêm trọng hơn card yếu. Bạn chỉnh ánh sáng và màu theo cái mình thấy, nên màn ám xanh hoặc quá sáng nghĩa là mọi quyết định màu của bạn đều lệch, và khách sẽ thấy khác hẳn.</p>

<p>Không cần màn đắt tiền. Cần một màn có thể hiệu chuẩn và một lần hiệu chuẩn tử tế.</p>

<h2>Máy tính xách tay hay để bàn?</h2>

<p>Cùng tầm tiền, máy để bàn mạnh hơn đáng kể và tản nhiệt tốt hơn. Laptop render lâu sẽ giảm xung để hạ nhiệt, nghĩa là con số trên giấy không phải con số bạn nhận được. Chọn laptop khi bạn thật sự cần di chuyển, không phải vì "cho tiện".</p>

<h2>Ba cách tiết kiệm không cần mua gì</h2>

<ul>
<li><strong style="color:#fff;">Render nháp ở độ phân giải thấp.</strong> Kiểm tra ánh sáng và bố cục ở 50% là đủ; chỉ render đủ kích thước ở bản cuối.</li>
<li><strong style="color:#fff;">Dùng EEVEE để căn chỉnh.</strong> Dựng ánh sáng ở EEVEE cho nhanh, chuyển Cycles ở bước cuối.</li>
<li><strong style="color:#fff;">Giảm texture khi làm việc.</strong> Texture 4K trong lúc dựng là lãng phí VRAM; chỉ bật lên ở bản render cuối.</li>
</ul>

<hr class="hr">

<p>Tóm lại: bắt đầu bằng máy đang có. Khi nào bạn thấy mình <em>chờ</em> nhiều hơn <em>làm</em>, lúc đó nâng cấp, và nâng GPU trước. Còn nếu vấn đề là hình chưa đẹp thì máy mới không giải quyết được; cái cần xem lại là ánh sáng, xem bài <a href="blog-5-loi-lighting.html">học lighting trong Blender</a>.</p>
""",
    },
    {
        "slug": "tu-hoc-blender-hay-hoc-kem",
        "title": "Tự học Blender hay học kèm 3D? So sánh thẳng thắn",
        "desc": "Tự học Blender miễn phí và nhiều người thành công. Vậy học kèm 3D Blender đáng tiền khi nào, lãng phí khi nào? Phân tích thẳng từ người đang dạy.",
        "tag": "Định hướng",
        "date": "2026-10-06",
        "date_vn": "06/10/2026",
        "read": "11 phút đọc",
        "thumb": "assets/vplas-exploded-view-blender.jpg",
        "faq": [
            ('Tự học Blender có xin được việc không?',
             'Được. Không ai hỏi bằng, người ta xem portfolio. Nhưng tự học thường mất lâu hơn để đạt mức portfolio đủ thuyết phục, vì phần lâu nhất không phải học kỹ thuật mà là tự nhận ra bài mình còn thiếu gì.'),
            ('Học kèm 3D Blender online có kém hơn ngồi cạnh nhau không?',
             'Khác biệt nhỏ, vì bài nộp là file và ảnh, gửi đi rất nhanh. Phần quyết định là người kèm có mở được file của bạn và sửa trực tiếp trong đó không, và buổi học có được ghi hình để bạn xem lại không.'),
            ('Đã tự học một năm rồi, học kèm có bị trùng lặp không?',
             'Thường là không, nếu bạn nói rõ trình độ từ đầu và người kèm chịu bỏ qua phần nền. Đây cũng là lý do kèm riêng hoặc gia sư theo buổi hợp với người đã tự học hơn là lớp nhóm có giáo trình cố định.'),
            ('Cần bao nhiêu buổi thì thấy khác?',
             'Ước lượng bốn tới sáu buổi, với điều kiện giữa hai buổi bạn có làm bài mới. Nếu sau sáu buổi bạn vẫn không tự chẩn đoán được lỗi của chính mình, vấn đề nằm ở cách dạy hoặc ở lượng bài bạn làm, không nằm ở số buổi.'),
            ('Không có tiền học thì nên làm gì trước?',
             'Lấy một vật thể thật trên bàn, dựng lại ba lần trong ba tuần, mỗi lần tự so với ảnh gốc và ghi ra ba chỗ lệch. Cách này rèn đúng cái mà học kèm bán cho bạn, chỉ chậm hơn. Phần nền để làm việc đó có trong cẩm nang Blender 3D, tải miễn phí, không cần đăng ký khoá nào.'),
        ],
        "body": """
<p class="lead">Câu trả lời ngắn: tự học đủ để bạn đi hết phần nền, còn học kèm 3D Blender chỉ đáng tiền khi bạn đã có bài nộp và bắt đầu đứng yên. Nếu bạn chưa mở Blender bao giờ, chưa cần trả đồng nào. Nếu bạn đã học vài tháng mà chất lượng không nhích, phần dưới đây là chỗ để đọc.</p>

<p>Tôi đang bán khoá học, nên bạn có quyền nghi ngờ bài này. Vì vậy tôi bắt đầu bằng phần bất lợi cho mình: rất nhiều người tự học Blender thành công, hoàn toàn miễn phí, và bạn có thể là một trong số đó.</p>

<h2>Tự học được gì</h2>

<p>Blender là phần mềm miễn phí có cộng đồng dạy học tốt nhất trong ngành 3D. Tài nguyên chất lượng cao, miễn phí, nhiều tới mức không xem hết. Riêng khoản tài liệu, bạn không thiếu gì.</p>

<p>Người tự học tốt thường có ba đặc điểm: kỷ luật ngồi đều mà không cần ai nhắc, khả năng tự đánh giá bài mình khá chính xác, và kiên nhẫn với việc thử sai. Nếu bạn có đủ ba thứ đó, tự học là lựa chọn đúng, và tôi nói thật lòng.</p>

<h2>Tự học mắc ở đâu</h2>

<p>Vấn đề của tự học không nằm ở thiếu thông tin. Nằm ở ba chỗ khác:</p>

<h3>Không biết mình sai ở đâu</h3>
<p>Đây là cái kẹt lớn nhất. Bạn nhìn render của mình, thấy "chưa đã", nhưng không chỉ ra được vì sao. Không chỉ ra được thì không sửa được, và bạn lặp lại cùng một lỗi qua hàng chục bài.</p>

<h3>Không biết thứ tự học</h3>
<p>YouTube gợi ý theo lượt xem, không theo trình độ của bạn. Nhiều người học vật liệu nâng cao trước khi biết đặt đèn, rồi kết luận mình không có năng khiếu. Tôi có viết riêng về <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> và vì sao đảo thứ tự lại hại.</p>

<h3>Không ai dạy phần ngoài phần mềm</h3>
<p>Báo giá thế nào, nhận brief ra sao, file phải chia thế nào để sửa nhanh, trình bày một shot ra sao để người duyệt hiểu ngay. Không có video nào dạy mấy thứ này, vì chúng đến từ việc làm job thật và va vấp.</p>

<figure>
  <img src="assets/vplas-exploded-view-blender.jpg" alt="Ảnh render tách rời linh kiện thiết bị VPLAS dựng bằng Blender, hard-surface, bo mạch, vỏ kim loại" loading="lazy" width="1600" height="900">
  <figcaption><strong>Shot tách rời linh kiện, dự án VPLAS.</strong> Loại shot này không khó về kỹ thuật. Khó ở chỗ sắp xếp sao cho người xem đọc được thứ tự lắp ráp. Đây là quyết định thẩm mỹ, và là thứ khó tự học nhất.</figcaption>
</figure>

<h2>Học kèm 3D Blender gồm mấy hình thức</h2>

<p>Nói "học kèm" là nói gộp bốn thứ rất khác nhau về giá và về tác dụng. Biết mình đang cần cái nào thì đỡ trả tiền cho cái mình không dùng.</p>

<h3>Kèm 1 kèm 1</h3>
<p>Một người dạy, một người học, toàn bộ buổi dành cho bài của bạn. Đắt nhất trên mỗi giờ, nhưng hiệu quả nhất ở giai đoạn đã mắc kẹt, vì không có phút nào bị chia cho người khác. Phần chi tiết hơn về cách một buổi nên diễn ra nằm ở bài <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a>.</p>

<h3>Lớp nhóm nhỏ</h3>
<p>Khoảng năm tới mười người, có giáo trình, có bài nộp theo tuần. Rẻ hơn kèm riêng, và phần nghe người khác bị sửa bài thực sự có giá trị, vì bạn thấy được những lỗi mình chưa kịp mắc. Nhược điểm là nhịp lớp không chờ bạn.</p>

<h3>Gia sư Blender theo buổi</h3>
<p>Không giáo trình, bạn mang vấn đề tới, trả tiền theo giờ. Hợp với người đang tự học và chỉ cần gỡ đúng một chỗ, chẳng hạn topology một chi tiết khó hoặc một cảnh render chậm bất thường. Không hợp nếu bạn còn chưa biết mình thiếu gì, vì lúc đó tiền giờ sẽ trôi vào việc chẩn đoán. Ranh giới giữa hai trường hợp đó, cùng cách kiểm tra người dạy trước buổi đầu, được viết kỹ trong bài <a href="blog-gia-su-blender.html">gia sư Blender</a>.</p>

<h3>Kèm theo dự án</h3>
<p>Bạn làm một shot hoàn chỉnh, người kèm đi cùng từ brief tới file giao. Đây là hình thức giống việc thật nhất và cũng là cách nhanh nhất để có một bài portfolio dùng được. Cách gộp nhiều shot như vậy thành một bộ bốn tới sáu món nằm ở bài <a href="blog-kem-1-1-lam-portfolio-3d.html">kèm 1 kèm 1 làm portfolio 3D</a>. Hai hệ chuyên sâu theo hướng sản phẩm và hướng automotive đang mô tả ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>, xem để biết một lộ trình đầy đủ gồm những chặng nào.</p>

<h2>So sánh trực tiếp</h2>

<div class="table-wrap">
<table>
<thead><tr><th></th><th>Tự học</th><th>Có người kèm</th></tr></thead>
<tbody>
<tr><td>Chi phí</td><td>Gần như 0</td><td>Vài triệu đến vài chục triệu</td></tr>
<tr><td>Thời gian tới portfolio dùng được</td><td>Thường 1 đến 2 năm</td><td>Thường 6 đến 12 tháng</td></tr>
<tr><td>Rủi ro lớn nhất</td><td>Đi sai hướng nhiều tháng mà không biết</td><td>Chọn nhầm người dạy</td></tr>
<tr><td>Phần kỹ năng nghề</td><td>Phải tự va vấp mà học</td><td>Được truyền lại trực tiếp</td></tr>
<tr><td>Tốc độ phát hiện lỗi của mình</td><td>Tính bằng tuần hoặc tháng</td><td>Tính bằng buổi</td></tr>
<tr><td>Yêu cầu kỷ luật</td><td>Rất cao, không ai nhắc</td><td>Vừa, có nhịp bài nộp giữ chân</td></tr>
<tr><td>Phù hợp với</td><td>Người kỷ luật cao, không gấp</td><td>Người cần đi nhanh, hoặc đã mắc kẹt</td></tr>
</tbody>
</table>
</div>

<p>Hai dòng thời gian trong bảng là ước lượng từ những người tôi quan sát được, không phải số liệu khảo sát. Khoảng dao động thật rộng hơn nhiều, và nó phụ thuộc gần như hoàn toàn vào số giờ bạn ngồi mỗi tuần. Bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a> bóc kỹ hơn từng mốc.</p>

<h2>Học phí gồm những khoản nào</h2>

<p>Đừng so hai khoá bằng con số tổng. Một khoá mười triệu có hai mươi lần chữa bài rẻ hơn một khoá sáu triệu chỉ có bốn lần, dù nhìn vào giá thì ngược lại. Cách bóc hợp lý hơn là chia học phí cho số lần bài của bạn thật sự được một người có nghề ngồi xem và nói đúng chỗ sai.</p>

<p>Những khoản thường bị gộp vào mà bạn nên tách ra để hỏi riêng:</p>

<ul>
<li><strong style="color:#fff;">Số lần chữa bài,</strong> và ai chữa. Giảng viên chính hay trợ giảng là hai giá trị khác nhau.</li>
<li><strong style="color:#fff;">Bản ghi buổi học của chính bạn</strong> có được giữ không, giữ bao lâu.</li>
<li><strong style="color:#fff;">Phản hồi giữa hai buổi</strong> có hay không. Đây là khoản chênh lệch lớn mà ít nơi nói rõ.</li>
<li><strong style="color:#fff;">Tài nguyên kèm theo:</strong> model mẫu, HDRI, file dự án mở ra xem được.</li>
<li><strong style="color:#fff;">Thời gian truy cập</strong> sau khi khoá kết thúc.</li>
</ul>

<p>Bộ tiêu chí đầy đủ hơn, gồm cả những lời quảng cáo nên bỏ qua, nằm ở bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">khoá học Blender 3D ở Việt Nam</a>. Nếu phần bạn còn yếu là dựng hình chứ không phải ánh sáng, đọc <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> trước để biết mình nên trả tiền cho chặng nào.</p>

<h2>Khi nào bỏ tiền học là hợp lý</h2>

<ul>
<li>Bạn đã tự học vài tháng và <strong style="color:#fff;">cảm thấy đứng yên</strong>, làm được thêm thứ mới nhưng chất lượng không nhích.</li>
<li>Bạn cần <strong style="color:#fff;">đi nhanh vì lý do cụ thể</strong>: chuyển nghề, có deadline, đang cần portfolio để ứng tuyển.</li>
<li>Bạn biết mình <strong style="color:#fff;">không giữ được kỷ luật khi học một mình</strong>, điều này không có gì đáng xấu hổ, đa số là vậy.</li>
<li>Bạn <strong style="color:#fff;">đã có bài nộp</strong> nhưng không ai cho bạn một nhận xét nào ngoài "đẹp đó".</li>
</ul>

<h2>Khi nào chưa nên</h2>

<ul>
<li>Bạn <strong style="color:#fff;">chưa mở Blender bao giờ</strong>. Học miễn phí một tháng trước đã, để chắc mình thật sự thích công việc này.</li>
<li>Bạn kỳ vọng khoá học <strong style="color:#fff;">thay bạn luyện tập</strong>. Không có khoá nào làm được điều đó.</li>
<li>Học phí <strong style="color:#fff;">ảnh hưởng tới sinh hoạt của bạn</strong>. Nghề này không đi đâu mất; học sau vẫn kịp.</li>
<li>Bạn <strong style="color:#fff;">chưa biết mình muốn đi hướng nào</strong>. Chọn sai hướng chuyên sâu thì tiền học thành tiền thử.</li>
</ul>

<blockquote><p>Tiền học không mua kỹ năng. Nó mua thời gian, cụ thể là mấy tháng bạn sẽ mất để tự nhận ra điều một người có kinh nghiệm chỉ trong mười phút.</p></blockquote>

<figure>
  <img src="assets/insta360-gimbal-hoc-vien-loc.jpg" alt="Bài hard-surface của học viên Lộc, dựng gimbal Insta360 bằng Blender, thân máy đen và tay cầm trên nền sáng" loading="lazy" width="1600" height="900">
  <figcaption><strong>Bài hard-surface của học viên Lộc, gimbal Insta360.</strong> Mức hoàn thiện này không đến từ một buổi học nào cả. Nó đến từ việc cùng một vật thể được dựng lại ba lần, mỗi lần sau khi nghe đúng một câu về chỗ sai.</figcaption>
</figure>

<h2>Nếu chọn học, hỏi ba câu này trước</h2>

<ol>
<li><strong style="color:#fff;">Người dạy có đang làm job thật không?</strong> Người chỉ dạy mà không làm sẽ dạy những thứ đúng của năm năm trước. Xem tác phẩm gần đây của chính người đứng lớp, không phải brochure của trung tâm.</li>
<li><strong style="color:#fff;">Bài của tôi được sửa như thế nào?</strong> "Có hỗ trợ" là câu vô nghĩa. Hỏi cụ thể: sửa mấy lần, ai sửa, phản hồi dạng gì.</li>
<li><strong style="color:#fff;">Kết thúc khoá tôi cầm về cái gì?</strong> Câu trả lời tốt là một danh sách sản phẩm cụ thể, không phải một danh sách bài giảng.</li>
</ol>

<p>Ba câu này áp dụng cho mọi khoá học, kể cả của tôi. Nếu ai không trả lời được rõ ràng, đó là câu trả lời rồi. Muốn thấy mức hoàn thiện mà khách thật thường yêu cầu, xem vài shot ở trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a>, rồi so với bài gần nhất của bạn. Khoảng cách đó chính là thứ bạn đang cân nhắc trả tiền để rút ngắn.</p>

<h2>Danh sách kiểm tra trước khi quyết định</h2>

<p>Đánh dấu từng dòng. Thiếu quá hai dòng thì hoãn một tuần, không mất gì cả.</p>

<ul>
<li>Đã tự chạy Blender ít nhất bốn tuần và có ít nhất ba bài hoàn chỉnh.</li>
<li>Viết ra được bằng một câu mình đang kẹt ở đâu, không phải "muốn giỏi hơn".</li>
<li>Đã biết mình cần hình thức nào trong bốn hình thức ở trên.</li>
<li>Đã xem tác phẩm gần đây của chính người sẽ kèm mình.</li>
<li>Đã biết số buổi, số bài nộp và số lần được chữa bài.</li>
<li>Đã tính học phí chia cho số lần chữa bài, và thấy con số đó chấp nhận được.</li>
<li>Đã hỏi về bản ghi buổi học và phản hồi giữa hai buổi.</li>
<li>Không bị hối phải chốt trong hôm nay.</li>
</ul>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Tự học Blender có xin được việc không?</p>
<p>Được. Không ai hỏi bằng, người ta xem portfolio. Nhưng tự học thường mất lâu hơn để đạt mức portfolio đủ thuyết phục, vì phần lâu nhất không phải học kỹ thuật mà là tự nhận ra bài mình còn thiếu gì.</p>

<p class="faq-q">Học kèm 3D Blender online có kém hơn ngồi cạnh nhau không?</p>
<p>Khác biệt nhỏ, vì bài nộp là file và ảnh, gửi đi rất nhanh. Phần quyết định là người kèm có mở được file của bạn và sửa trực tiếp trong đó không, và buổi học có được ghi hình để bạn xem lại không.</p>

<p class="faq-q">Đã tự học một năm rồi, học kèm có bị trùng lặp không?</p>
<p>Thường là không, nếu bạn nói rõ trình độ từ đầu và người kèm chịu bỏ qua phần nền. Đây cũng là lý do kèm riêng hoặc gia sư theo buổi hợp với người đã tự học hơn là lớp nhóm có giáo trình cố định.</p>

<p class="faq-q">Cần bao nhiêu buổi thì thấy khác?</p>
<p>Ước lượng bốn tới sáu buổi, với điều kiện giữa hai buổi bạn có làm bài mới. Nếu sau sáu buổi bạn vẫn không tự chẩn đoán được lỗi của chính mình, vấn đề nằm ở cách dạy hoặc ở lượng bài bạn làm, không nằm ở số buổi.</p>

<p class="faq-q">Không có tiền học thì nên làm gì trước?</p>
<p>Lấy một vật thể thật trên bàn, dựng lại ba lần trong ba tuần, mỗi lần tự so với ảnh gốc và ghi ra ba chỗ lệch. Cách này rèn đúng cái mà học kèm bán cho bạn, chỉ chậm hơn. Phần nền để làm việc đó có trong <a href="cam-nang.html">cẩm nang Blender 3D</a>, tải miễn phí, không cần đăng ký khoá nào.</p>

<hr class="hr">

<p>Bước tiếp theo cụ thể: nếu bạn chưa biết mình đang ở chặng nào, mở <a href="khoa-hoc.html">lộ trình hai hệ ở trang khoá học</a> và đọc mô tả đầu vào của từng chặng, chỗ nào bạn thấy quen là chỗ bạn đang đứng. Nếu bạn vẫn muốn tự học thêm một thời gian, tải <a href="cam-nang.html">cẩm nang Blender 3D</a> và cứ nhắn cho tôi mô tả chỗ kẹt. Tôi trả lời được thì trả lời, không thì chỉ bạn chỗ tìm, không cần đăng ký gì cả.</p>
""",
    },
    {
        "slug": "khoa-hoc-blender-3d-o-viet-nam",
        "title": "Khoá học Blender 3D ở Việt Nam: chọn sao cho đúng",
        "desc": "Chọn khoá học Blender 3D ở Việt Nam: bốn loại khoá đang có, học phí gồm những khoản nào, bảy câu nên hỏi trước khi đóng tiền và quảng cáo nên bỏ qua.",
        "tag": "Định hướng",
        "date": "2026-09-26",
        "date_vn": "26/09/2026",
        "read": "12 phút đọc",
        "thumb": "assets/mercedes-g63-canh-chay-no-phia-sau.webp",
        "faq": [
            ("Học phí khoá học Blender ở Việt Nam khoảng bao nhiêu?",
             "Theo quan sát của chúng tôi, khoá quay sẵn thường ở mức vài triệu đồng, lớp nhóm có chữa bài hằng tuần ở mức vài chục triệu cho một chương trình dài, kèm riêng tính theo giờ và đắt nhất. Đây là ước lượng mặt bằng chung, mỗi nơi công bố một kiểu nên hãy hỏi số buổi và số lần chữa bài rồi chia ra để so sánh."),
            ("Khoá học 3D online có kém hơn học trực tiếp tại TPHCM không?",
             "Với 3D thì không, vì toàn bộ công việc diễn ra trên màn hình và buổi học online có thể ghi hình lại để xem lại đoạn giảng viên sửa file của bạn. Học trực tiếp chỉ hơn ở chỗ bạn khó bỏ buổi khi có người ngồi cạnh."),
            ("Nên học khoá tổng hợp hay khoá chuyên về render, modeling?",
             "Người mới nên học khoá tổng hợp đi hết một quy trình từ dựng hình tới render, vì chưa đủ dữ kiện để biết mình hợp mảng nào. Khoá chuyên sâu về render hay modeling chỉ đáng tiền khi bạn đã làm xong vài shot và biết rõ mình đang yếu ở đâu."),
            ("Chưa biết gì về 3D thì có nên đóng tiền học ngay không?",
             "Nên dành một tháng tự học bằng tài liệu miễn phí trước. Sau một tháng bạn biết mình có chịu được việc ngồi hàng giờ chỉnh một khung hình hay không, và biết mình đang mắc ở đâu, lúc đó học phí mới mua được thứ đáng mua."),
        ],
        "body": """
<p class="lead">Gõ "khoá học Blender 3D" bây giờ ra vài chục kết quả, cái nào cũng hứa đi làm được sau ba tháng. Câu trả lời ngắn: ở Việt Nam đang có bốn loại khoá, giá chênh nhau hàng chục lần, và thứ duy nhất đáng so sánh là số lần bài của bạn được người có nghề ngồi sửa. Bài này không kể tên ai. Nó đưa bạn bộ tiêu chí để tự chấm, và nói thẳng khi nào bạn chưa cần đóng tiền cho ai cả.</p>

<h2>Ở Việt Nam đang có mấy loại khoá</h2>

<p>Gom lại thì chỉ có bốn nhóm, và mỗi nhóm giải quyết một vấn đề khác nhau. Chọn sai nhóm là lý do phổ biến nhất khiến người học thấy tiền bỏ ra không đổi được gì. Bảng đối chiếu nhanh bốn nhóm này, kèm gợi ý nên đọc tiếp bài nào, nằm ở trang tổng hợp <a href="blog-khoa-hoc-3d-blender.html">khoá học 3D Blender</a>.</p>

<h3>Khoá quay sẵn, học theo video</h3>
<p>Rẻ nhất, học lúc nào cũng được. Điểm yếu nằm ở chỗ không ai nhìn bài của bạn. Bạn xem giảng viên làm một cảnh đẹp, làm theo ra cảnh gần giống, rồi tự mở một dự án của riêng mình và bế tắc, vì phần khó không nằm ở thao tác mà ở quyết định.</p>
<p>Nhóm này hợp với người đã biết tự đánh giá tác phẩm của mình, hoặc chỉ cần bổ một mảng cụ thể như khoá học render hay khoá học modeling 3D.</p>

<h3>Lớp theo nhóm, có buổi chữa bài</h3>
<p>Phổ biến nhất và cũng là lựa chọn hợp lý cho đa số người mới. Có lịch cố định nên bạn khó bỏ giữa chừng, có bạn học để so sánh tiến độ. Chất lượng phụ thuộc gần như hoàn toàn vào việc giảng viên dành bao nhiêu thời gian cho từng bài nộp. Nếu bạn xuất phát từ con số 0, xem thêm một <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> cần đạt tới đâu sau tám tuần.</p>

<h3>Kèm riêng một kèm một</h3>
<p>Đắt nhất trên mỗi giờ, nhưng đi nhanh nhất nếu bạn đã có nền và đang mắc ở một chỗ cụ thể. Người kèm nhìn thẳng vào file của bạn, thấy cái sai trong ba phút thay vì để bạn mò ba tuần. Chúng tôi viết riêng một bài về <a href="blog-hoc-blender-kem-1-1.html">học kèm một kèm một</a>, khi nào đáng tiền và khi nào phí.</p>

<h3>Trung tâm đa ngành</h3>
<p>Dạy đủ thứ từ photoshop tới dựng phim, 3D chỉ là một môn trong danh mục. Được cái có cơ sở vật chất và giấy chứng nhận, tiện cho người cần bằng cấp để nộp hồ sơ. Điểm cần hỏi kỹ là người đứng lớp có đang làm dự án thương mại hay không, vì giáo trình đa ngành thường cập nhật chậm hơn tốc độ đổi của phần mềm.</p>

<h2>Học phí khoá học Blender gồm những khoản nào</h2>

<p>Mặt bằng chung ở Việt Nam hiện nay trải từ vài triệu cho khoá quay sẵn, tới vài chục triệu cho chương trình dài kèm chữa bài hằng tuần. Đây là ước lượng theo quan sát, không phải bảng giá, vì mỗi nơi gói nội dung một kiểu.</p>

<p>Cách so sánh công bằng nhất là bỏ qua con số tổng và tách học phí thành bốn khoản: giờ giảng, số lần bài được chữa, tài nguyên đi kèm và hỗ trợ sau khoá. Hai nơi cùng báo một mức giá có thể chênh nhau nhiều lần ở khoản thứ hai. Phần tính chi tiết theo đơn giá mỗi lần được chữa bài nằm trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Cách họ nói về học phí</th><th>Nên hiểu là</th></tr></thead>
<tbody>
<tr><td>Nói rõ số buổi, số bài được chữa, ai chữa</td><td>Họ đã tính chi phí thật của việc dạy</td></tr>
<tr><td>Chỉ nhấn mạnh "ưu đãi hôm nay", giục chốt</td><td>Giá được đặt theo tâm lý, không theo nội dung</td></tr>
<tr><td>Không công bố giá, phải để lại số mới biết</td><td>Giá sẽ thay đổi theo mức độ bạn tỏ ra muốn mua</td></tr>
<tr><td>Cam kết việc làm kèm điều kiện mập mờ</td><td>Đọc kỹ phần điều kiện trước khi tin phần cam kết</td></tr>
<tr><td>Tính theo số giờ video, không nhắc tới bài nộp</td><td>Bạn đang mua một thư viện, không phải một lớp học</td></tr>
</tbody>
</table>
</div>

<figure>
  <img src="assets/mercedes-g63-canh-chay-no-phia-sau.webp" alt="Khung hình TVC 3D xe Mercedes AMG G63 dựng bằng Blender, có hiệu ứng cháy nổ và nhân vật" loading="lazy" width="1800" height="759">
  <figcaption><strong>Một khung trong TVC 3D dựng bằng Blender.</strong> Mức này không đến từ một khoá học nào cả. Nó đến từ vài trăm giờ làm lại cùng một cảnh cho tới khi ánh sáng, chuyển động và hậu kỳ khớp nhau.</figcaption>
</figure>

<h2>Bảy câu hỏi nên hỏi trước khi đóng tiền</h2>

<ol>
<li><strong style="color:#fff;">Ai đứng lớp và họ đang làm dự án gì?</strong> Xin xem sản phẩm gần nhất, có năm tháng cụ thể.</li>
<li><strong style="color:#fff;">Một bài của tôi được chữa bao nhiêu lần?</strong> Con số cụ thể, không phải chữ "hỗ trợ trọn đời".</li>
<li><strong style="color:#fff;">Chữa bài bằng hình thức nào?</strong> Nhận xét bằng chữ, vẽ đè lên hình, hay ngồi sửa trực tiếp trong file.</li>
<li><strong style="color:#fff;">Học xong tôi cầm về sản phẩm gì?</strong> Nên là danh sách shot cụ thể, đủ để dựng portfolio.</li>
<li><strong style="color:#fff;">Lớp bao nhiêu người?</strong> Trên hai mươi người mà một giảng viên thì phần chữa bài sẽ mỏng.</li>
<li><strong style="color:#fff;">Có được xem lại bài giảng không, trong bao lâu?</strong> Hỏi luôn là bản ghi buổi chữa bài của chính mình có được giữ không.</li>
<li><strong style="color:#fff;">Học viên cũ giờ đang làm gì?</strong> Xin liên hệ một hai người để hỏi trực tiếp, nơi tử tế sẽ không ngại.</li>
</ol>

<h2>Danh sách kiểm tra trước khi chuyển khoản</h2>

<p>In ra hoặc chép vào ghi chú, đánh dấu từng dòng. Thiếu quá hai dòng thì hoãn lại một tuần, không mất gì cả.</p>

<ul>
<li>Đã xem ít nhất ba tác phẩm gần đây của chính người sẽ đứng lớp, không phải của trung tâm.</li>
<li>Đã biết số buổi, thời lượng mỗi buổi và tổng số bài mình phải nộp.</li>
<li>Đã biết ai chữa bài và chữa bằng cách nào.</li>
<li>Đã xem thử một bản ghi buổi học hoặc một buổi học thử.</li>
<li>Đã đọc điều khoản hoàn tiền và điều kiện của mọi lời cam kết việc làm.</li>
<li>Đã tự chạy Blender ít nhất vài buổi và biết mình đang thiếu gì.</li>
<li>Đã tính được học phí chia cho số lần bài được chữa, và thấy con số đó chấp nhận được.</li>
<li>Không bị hối phải chốt trong hôm nay.</li>
</ul>

<blockquote><p>Một khoá học tốt không bán cho bạn kiến thức. Kiến thức nằm đầy trên mạng và miễn phí. Thứ bạn trả tiền là người chịu ngồi nhìn bài của bạn và nói đúng chỗ sai.</p></blockquote>

<h2>Những lời quảng cáo nên bỏ qua</h2>

<ul>
<li><strong style="color:#fff;">"Không cần năng khiếu, ai cũng học được."</strong> Đúng một nửa. Ai cũng học được phần thao tác, nhưng mắt nhìn thì phải luyện, và luyện thì mất thời gian.</li>
<li><strong style="color:#fff;">"Ra trường thu nhập trăm triệu."</strong> Có người đạt được, nhưng sau nhiều năm và thường nhờ nhận dự án trực tiếp chứ không phải nhờ khoá học.</li>
<li><strong style="color:#fff;">"Trọn bộ hai trăm giờ video."</strong> Số giờ video là thước đo tệ. Không ai xem hết, và xem hết cũng không đồng nghĩa làm được.</li>
<li><strong style="color:#fff;">"Cam kết đầu ra, không có việc hoàn tiền."</strong> Đọc phần điều kiện đi kèm. Thường có ràng buộc về số buổi vắng, điểm bài tập và thời hạn nộp hồ sơ, đủ để lời cam kết gần như không bao giờ phải thực hiện.</li>
</ul>

<h2>Khoá học 3D online hay khoá học 3D tại TPHCM</h2>

<p>Với 3D, online không thua trực tiếp, vì mọi thứ đều diễn ra trên màn hình. Chia sẻ màn hình cộng với ghi hình buổi học thậm chí tiện hơn: bạn xem lại được đoạn giảng viên sửa file của chính mình, đoạn đó mới là phần đắt nhất của buổi học.</p>

<p>Học trực tiếp hơn ở hai điểm: bạn khó lười khi có người ngồi cạnh, và ở TPHCM bạn gặp được người cùng nghề ngoài đời, nơi phần lớn job đầu tiên xuất hiện. Nếu nhà bạn cách lớp hơn một tiếng chạy xe, hãy trừ thẳng thời gian đó vào giờ luyện tập rồi mới quyết.</p>

<p>Phần khó nhất của hình thức từ xa không phải chất lượng bài giảng mà là giữ nhịp học hằng tuần. Bốn tiêu chí chọn lớp và cách dựng nhịp được viết riêng trong bài <a href="blog-khoa-hoc-3d-online.html">khoá học 3D online</a>.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Khoá học 3D online</th><th>Học trực tiếp tại TPHCM</th></tr></thead>
<tbody>
<tr><td>Xem lại buổi học</td><td>Gần như luôn có bản ghi</td><td>Tuỳ nơi, nhiều chỗ không ghi</td></tr>
<tr><td>Thời gian di chuyển</td><td>Không</td><td>Đáng kể nếu ở xa</td></tr>
<tr><td>Kỷ luật</td><td>Phải tự giữ</td><td>Dễ hơn vì có lịch và có người</td></tr>
<tr><td>Quan hệ nghề nghiệp</td><td>Chậm hơn, qua nhóm chat</td><td>Nhanh hơn, gặp mặt trực tiếp</td></tr>
<tr><td>Máy móc</td><td>Dùng máy của bạn</td><td>Có thể dùng máy phòng học</td></tr>
</tbody>
</table>
</div>

<p>Nếu bạn đang ở Sài Gòn và cần so sánh chi tiết hơn về học phí, thời gian đi lại và cách kiểm tra một lớp, bài <a href="blog-khoa-hoc-3d-tai-tphcm.html">khoá học 3D tại TPHCM</a> đi sâu vào riêng phần chọn giữa offline và online.</p>

<h2>Khoá tổng hợp, khoá render hay khoá modeling</h2>

<p>Người mới hay bị hút vào khoá chuyên sâu vì tên nghe chuyên nghiệp. Nhưng khi chưa đi hết một quy trình từ dựng hình, vật liệu, ánh sáng tới render và hậu kỳ, bạn không có dữ kiện để biết mình yếu ở đâu, nên tiền bỏ vào một <a href="blog-khoa-hoc-render.html">khoá học render</a> riêng thường bị phí ở giai đoạn này.</p>

<p>Thứ tự hợp lý là học một khoá tổng hợp đưa bạn qua trọn một shot, làm thêm hai ba shot của riêng mình, rồi mới chọn mảng để đào sâu. Bài <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> mô tả thứ tự bảy kỹ năng, và bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu thì nhận job đầu tiên</a> cho bạn mốc thời gian để đối chiếu xem mình đang nhanh hay chậm.</p>

<h2>Tự học một tháng trước khi đóng tiền</h2>

<p>Nếu bạn chưa mở Blender bao giờ, đừng đóng tiền vội. Dành một tháng làm theo tài liệu miễn phí, xem mình có thật sự thích ngồi hàng giờ chỉnh một khung hình hay không. Bên mình để sẵn <a href="cam-nang.html">cẩm nang Blender 3D miễn phí</a> và bài <a href="blog-hoc-do-hoa-3d-tu-con-so-0.html">học đồ hoạ 3D từ con số 0</a> để bạn thử trước.</p>

<p>Sau một tháng đó, nếu bạn vẫn muốn đi tiếp mà thấy mình đang loay hoay, lúc đó tiền học mới đáng, vì bạn đã biết mình cần gì. Nếu còn phân vân giữa hai hướng, bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học khoá có người kèm</a> phân tích kỹ hơn từng trường hợp.</p>

<h2>Sau khoá học, cái gì thật sự quyết định bạn có việc</h2>

<p>Không phải chứng chỉ. Người thuê nhìn ba thứ: portfolio có đủ shot hoàn chỉnh hay không, bạn có tự đi hết một dự án mà không cần cầm tay hay không, và bạn có giao đúng hạn hay không. Khoá học chỉ rút ngắn giai đoạn đầu.</p>

<p>Vì vậy, khi so hai khoá ngang giá, hãy chọn khoá buộc bạn nộp nhiều bài hơn, kể cả khi nghe có vẻ mệt hơn. Muốn biết mức hoàn thiện mà thị trường đang trả tiền, xem phần <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> rồi lấy các shot ở đó làm chuẩn tự chấm bài mình.</p>

<h2>Vài câu hỏi hay gặp</h2>

<p class="faq-q">Học phí khoá học Blender ở Việt Nam khoảng bao nhiêu?</p>
<p>Theo quan sát của chúng tôi: khoá quay sẵn vài triệu, lớp nhóm có chữa bài vài chục triệu cho chương trình dài, kèm riêng tính theo giờ và đắt nhất. Đây là ước lượng. Hãy hỏi số buổi và số lần chữa bài rồi chia ra, con số đó mới so sánh được.</p>

<p class="faq-q">Khoá học 3D online có kém hơn học trực tiếp không?</p>
<p>Với 3D thì không. Toàn bộ công việc diễn ra trên màn hình, và buổi học online ghi hình lại được. Học trực tiếp hơn ở kỷ luật và quan hệ nghề nghiệp, không hơn ở chất lượng dạy.</p>

<p class="faq-q">Máy yếu có nên đợi nâng cấp rồi mới học?</p>
<p>Không cần. Giai đoạn đầu bạn làm cảnh nhỏ, máy phổ thông chạy được. Chúng tôi có bài riêng về <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> và mốc nào thì nâng cấp mới đáng.</p>

<p class="faq-q">Học xong một khoá là đủ để nhận job chưa?</p>
<p>Thường là chưa. Khoá học đưa bạn tới chỗ làm xong một shot có hướng dẫn. Job đầu tiên thường tới sau vài shot bạn tự làm từ đầu tới cuối, và sau khi bạn đã sửa lại chúng vài lần theo góp ý.</p>

<hr class="hr">

<p>LXAM Academy có hai hệ đào tạo, nội dung và học phí công khai ở trang <a href="khoa-hoc.html">khoá học Blender 3D</a>. Bước tiếp theo gọn nhất: mở trang đó so hai hệ, rồi tải cẩm nang và làm hết bài tập trong ba tuần. Sau đó bạn sẽ tự biết mình cần khoá học hay chỉ cần thêm kỷ luật.</p>
""",
    },
    {
        "slug": "hoc-blender-kem-1-1",
        "title": "Học kèm 1 kèm 1 Blender: khi nào đáng tiền",
        "desc": "Học kèm 1 kèm 1 Blender đắt hơn lớp nhóm nhiều lần. Ai thật sự hợp, một buổi kèm tử tế diễn ra thế nào và cách thử người kèm trước khi trả tiền.",
        "tag": "Định hướng",
        "date": "2026-09-26",
        "date_vn": "26/09/2026",
        "read": "10 phút đọc",
        "thumb": "assets/porsche-911-pit-lane-toan-canh.webp",
        "faq": [
            ("Học kèm 1 kèm 1 Blender giá khoảng bao nhiêu?",
             "Chúng tôi không nêu một con số cố định vì nó phụ thuộc số buổi, thời lượng và mức người kèm. Cách đọc giá hợp lý hơn là hỏi mỗi buổi gồm bao nhiêu phút sửa bài trực tiếp, có ghi hình buổi học không và có được nhận xét giữa hai buổi không. Hai lớp cùng giá mà khác ba điểm đó thì giá trị thật khác nhau rất xa."),
            ("Người chưa từng mở Blender có nên học kèm 1 kèm 1 luôn không?",
             "Thường là không nên. Giai đoạn làm quen giao diện và phím tắt thì video miễn phí dạy tốt và rẻ hơn, kèm riêng sẽ trôi vào việc chỉ nút bấm. Hợp hơn là học nền bằng một khoá cho người mới hoặc lớp nhóm, rồi dùng kèm riêng khi đã có bài nộp và bắt đầu bị mắc kẹt."),
            ("Học kèm 1 kèm 1 online có kém hơn ngồi cạnh nhau không?",
             "Với đồ hoạ 3D thì khác biệt nhỏ, vì bài nộp là file và ảnh, gửi đi rất nhanh. Phần quan trọng là người kèm có mở được file của bạn và sửa trực tiếp trong đó hay không, cùng với việc buổi học có được ghi hình để bạn xem lại. Hình thức online còn tiện hơn ở chỗ bạn giữ lại được bản ghi."),
            ("Cần bao nhiêu buổi kèm riêng thì thấy tiến bộ?",
             "Ước lượng từ các nhóm học viên đã đi qua, khoảng bốn tới sáu buổi là đủ để thấy khác biệt, với điều kiện giữa hai buổi bạn có làm bài mới. Nếu sau sáu buổi mà bạn vẫn không tự chẩn đoán được lỗi của chính mình, vấn đề nằm ở cách dạy hoặc ở lượng bài bạn làm, không nằm ở số buổi."),
            ("Kèm riêng có giúp làm portfolio 3D nhanh hơn không?",
             "Có, và đây là chặng kèm riêng phát huy rõ nhất. Ở giai đoạn hoàn thiện portfolio, mỗi nhận xét đều đắt giá vì nó quyết định một shot được giữ hay bị bỏ. Nhưng người kèm chỉ nên chỉ ra vấn đề, không làm hộ, vì portfolio có bàn tay người khác trong đó sẽ lộ ngay ở buổi phỏng vấn."),
        ],
        "body": """
<p class="lead">Học kèm 1 kèm 1 là hình thức đắt nhất tính trên mỗi giờ học, và nó chỉ xứng đáng với một nhóm người khá hẹp: người đã có nền, có bài nộp đều và đang mắc kẹt ở một chỗ mà tự mò không ra. Nếu bạn chưa từng mở Blender, kèm riêng gần như chắc chắn là lãng phí. Phần khó là biết mình thuộc nhóm nào trước khi trả tiền.</p>

<p>Bài này đưa bộ tiêu chí để bạn tự soi: kèm riêng mua cái gì, so với lớp nhóm khác ở đâu, một buổi tử tế diễn ra thế nào và làm sao thử một gia sư Blender trước khi cam kết cả khoá.</p>

<h2>Học kèm 1 kèm 1 thật ra mua cái gì</h2>

<p>Bạn không mua thêm kiến thức. Kiến thức trong một buổi kèm không nhiều hơn một video hướng dẫn tốt. Cái bạn mua là ba thứ khó kiếm ở chỗ khác.</p>

<h3>Chẩn đoán đúng chỗ đang kẹt</h3>
<p>Người có nghề nhìn render của bạn vài giây là chỉ ra được vấn đề nằm ở ánh sáng, ở vật liệu hay ở bố cục. Bạn tự mò chỗ này có khi mất vài tháng, và cái mất lớn nhất không phải thời gian mà là việc bạn tập được một thói quen sai rồi khó sửa.</p>

<h3>Thứ tự ưu tiên</h3>
<p>Một bài có thể sai mười chỗ. Sửa chín chỗ nhỏ không làm hình khá hơn, sửa đúng một chỗ lớn thì khác hẳn. Người kèm giúp bạn biết sửa cái nào trước, và quan trọng hơn là giải thích vì sao chỗ đó lớn hơn, để lần sau bạn tự xếp được thứ tự.</p>

<h3>Phần nghề nằm ngoài phần mềm</h3>
<p>Báo giá ra sao, nhận brief thế nào, chia file để sửa nhanh, trình bày một shot cho người duyệt hiểu ngay. Mấy thứ này không có trong giáo trình vì chúng đến từ việc đi làm, và chúng thường là lý do thật khiến một người tự học mãi không chuyển được sang làm có tiền.</p>

<figure>
  <img src="assets/porsche-911-pit-lane-toan-canh.webp" alt="Cảnh xe Porsche 911 trong pit lane dựng 3D bằng Blender, ánh sáng chiều và mặt đường ướt" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một cảnh automotive dựng bằng Blender.</strong> Người mới thường nghĩ khó ở model xe. Thực tế phần quyết định là hướng đèn, phản chiếu trên thân và độ ướt của mặt đường, và đó là những thứ dễ chỉ nhất khi ngồi cạnh nhau.</figcaption>
</figure>

<h2>Học kèm 1 kèm 1 so với lớp nhóm và tự học</h2>

<p>Ba hình thức này không thay thế nhau, chúng giải quyết ba việc khác nhau. Bảng dưới đối chiếu theo những tiêu chí mà người học thường quên hỏi.</p>

<div class="table-wrap">
<table>
<thead><tr><th></th><th>Tự học</th><th>Lớp nhóm</th><th>Kèm 1 kèm 1</th></tr></thead>
<tbody>
<tr><td>Chi phí mỗi giờ</td><td>Gần như không</td><td>Thấp</td><td>Cao nhất</td></tr>
<tr><td>Nhịp sửa bài</td><td>Không có</td><td>Theo lịch lớp, chia cho nhiều người</td><td>Toàn bộ buổi dành cho bài của bạn</td></tr>
<tr><td>Linh hoạt giờ học</td><td>Hoàn toàn</td><td>Lịch cố định</td><td>Thoả thuận theo tuần</td></tr>
<tr><td>Nội dung</td><td>Bạn tự chọn, dễ chọn sai</td><td>Giáo trình chung</td><td>Cắt theo mục tiêu của bạn</td></tr>
<tr><td>Rủi ro lớn nhất</td><td>Đi sai hướng nhiều tháng mà không biết</td><td>Bị bỏ lại khi lớp đi nhanh hơn mình</td><td>Trả giá cao cho giai đoạn chưa cần</td></tr>
<tr><td>Hợp nhất với</td><td>Giai đoạn làm quen công cụ</td><td>Giai đoạn xây nền có hệ thống</td><td>Giai đoạn phá vỡ bế tắc và hoàn thiện portfolio</td></tr>
</tbody>
</table>
</div>

<p>Đọc bảng này theo chặng sẽ đúng hơn là theo giá. Nếu bạn đang ở chặng đầu, một <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> có lịch nộp bài sẽ cho bạn nhiều hơn với cùng số tiền. Nếu bạn muốn nhìn toàn bộ các loại khoá trước khi chọn, bài <a href="blog-khoa-hoc-3d-blender.html">khoá học 3D Blender</a> tập hợp đủ các hướng kèm tiêu chí so sánh.</p>

<h2>Ai hợp với học kèm 1 kèm 1</h2>

<ul>
<li><strong style="color:#fff;">Người đã tự học vài tháng và đang đứng yên.</strong> Có nền, có bài nộp, chỉ thiếu người soi.</li>
<li><strong style="color:#fff;">Người đi làm, giờ giấc thất thường.</strong> Lớp nhóm có lịch cố định thường bị bỏ giữa chừng vì công việc.</li>
<li><strong style="color:#fff;">Người có đích cụ thể.</strong> Cần portfolio automotive để ứng tuyển, cần làm được một dạng shot cho công ty đang làm.</li>
<li><strong style="color:#fff;">Người đã đi làm ngành khác muốn chuyển sang.</strong> Cần lộ trình rút gọn, bỏ hết phần không phục vụ mục tiêu.</li>
<li><strong style="color:#fff;">Người cần sửa một kỹ năng hẹp.</strong> Dựng hình thì ổn nhưng ánh sáng mãi không lên, hoặc ngược lại. Trường hợp này kèm riêng vài buổi rẻ hơn học lại cả khoá.</li>
</ul>

<h2>Ai chưa nên</h2>

<ul>
<li><strong style="color:#fff;">Người chưa từng mở Blender.</strong> Buổi kèm sẽ trôi vào việc chỉ nút bấm, phần đó video miễn phí làm tốt hơn và rẻ hơn.</li>
<li><strong style="color:#fff;">Người không có thời gian làm bài giữa các buổi.</strong> Kèm riêng chỉ có tác dụng khi bạn mang bài mới tới mỗi lần gặp.</li>
<li><strong style="color:#fff;">Người kỳ vọng người kèm làm hộ.</strong> Sửa hộ thì hình đẹp lên, còn bạn thì không.</li>
<li><strong style="color:#fff;">Người chưa biết mình muốn làm dòng hình nào.</strong> Kèm riêng là dao mổ, không phải bản đồ. Chưa có đích thì nên đi qua một lộ trình chung trước, xem <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> để chọn hướng.</li>
</ul>

<h2>Một buổi kèm tử tế diễn ra thế nào</h2>

<ol>
<li><strong style="color:#fff;">Xem bài bạn làm từ buổi trước</strong>, không phải bắt đầu bằng bài giảng.</li>
<li><strong style="color:#fff;">Chỉ ra một hoặc hai vấn đề lớn nhất</strong>, kèm lý do vì sao nó lớn hơn các lỗi khác.</li>
<li><strong style="color:#fff;">Sửa trực tiếp trong file của bạn</strong> để bạn thấy thao tác, không chỉ nghe mô tả.</li>
<li><strong style="color:#fff;">Giao bài tiếp theo</strong> có mục tiêu rõ, ví dụ dựng lại cùng cảnh đó với một nguồn sáng duy nhất.</li>
<li><strong style="color:#fff;">Ghi hình buổi học</strong> để bạn xem lại đoạn sửa.</li>
</ol>

<blockquote><p>Nếu buổi kèm nào cũng bắt đầu bằng việc thầy mở slide, bạn đang trả giá lớp riêng để nghe một bài giảng chung.</p></blockquote>

<h2>Kèm 1 kèm 1 làm portfolio 3D: dùng đúng chặng</h2>

<p>Đây là chặng kèm riêng đáng tiền nhất, vì mỗi nhận xét ở đây quyết định một shot được giữ hay bị bỏ. Một portfolio sáu shot đều tay thắng một portfolio mười hai shot lệch chất lượng, và người ngoài nhìn ra chỗ lệch nhanh hơn bạn rất nhiều.</p>

<p>Việc của người kèm ở chặng này gồm bốn phần: bỏ những shot kéo mặt bằng xuống, chỉ ra shot nào còn cứu được và cứu bằng cách nào, xếp thứ tự để shot mạnh nhất đứng đầu, và soát phần kỹ thuật như độ phân giải, tỷ lệ khung và cách xuất file cho từng kênh. Phần ánh sáng chiếm nhiều thời gian nhất, nên đọc trước <a href="blog-khoa-hoc-render.html">khoá học render</a> để biết những gì sẽ bị soi.</p>

<p>Một giới hạn cần nói thẳng: người kèm không được làm hộ. Portfolio có bàn tay người khác trong đó sẽ lộ ngay khi bạn phải mở file ra giải thích ở buổi phỏng vấn hoặc khi khách yêu cầu sửa.</p>

<p>Chặng này đủ dài để tách thành một bài riêng. Bộ hồ sơ cần mấy món, chia theo tuần thế nào và ba tình huống chưa nên trả tiền nằm ở bài <a href="blog-kem-1-1-lam-portfolio-3d.html">kèm 1 kèm 1 làm portfolio 3D</a>.</p>

<h2>Cách thử một gia sư Blender trước khi trả tiền</h2>

<p>Xin một buổi thử, mang theo một bài bạn làm và đang không ưng. Đừng hỏi họ dạy gì, hãy đưa bài và xem họ phản ứng thế nào. Danh sách dưới là những thứ cần kiểm trong đúng buổi đó, còn bộ câu hỏi đầy đủ để lọc người dạy thì nằm trong bài <a href="blog-gia-su-blender.html">gia sư Blender</a>.</p>

<ul>
<li><strong style="color:#fff;">Họ chỉ ra được vấn đề bạn chưa tự thấy.</strong> Nếu họ chỉ nhắc lại những lỗi bạn đã biết, buổi học sẽ không đưa bạn đi đâu.</li>
<li><strong style="color:#fff;">Giải thích dựa trên nguyên lý, không phải cảm tính.</strong> Nghe được câu vì sao, không chỉ câu hãy kéo thông số này lên.</li>
<li><strong style="color:#fff;">Dám nói bài bạn chưa được.</strong> Người chỉ khen là người dễ chịu, không phải người giúp bạn khá lên.</li>
<li><strong style="color:#fff;">Có mở file của bạn và sửa trực tiếp.</strong> Người chỉ nhìn ảnh rồi mô tả bằng lời thường không nắm được phần quy trình.</li>
<li><strong style="color:#fff;">Cho xem bài của học viên cũ, không chỉ bài của chính họ.</strong> Người làm giỏi và người dạy giỏi là hai việc khác nhau.</li>
<li><strong style="color:#fff;">Nói rõ số buổi, thời lượng, có ghi hình hay không, có nhận xét giữa hai buổi hay không.</strong> Bốn điểm này quyết định giá trị thật của cùng một mức học phí.</li>
</ul>

<h2>Chi phí và cách tính cho hợp lý</h2>

<p>Đừng so kèm riêng với lớp nhóm theo giá mỗi giờ, vì hai thứ giải quyết hai việc khác nhau. Cách tính đúng hơn là hỏi: nếu tự mò, bạn mất bao nhiêu tháng để nhận ra cùng một điều, và mấy tháng đó đáng bao nhiêu với bạn. Với người đang cần portfolio để đổi việc, vài tháng rút ngắn thường đáng hơn khoản học phí.</p>

<p>Một cách tiết kiệm mà vẫn hiệu quả là học nền bằng tài liệu miễn phí hoặc lớp nhóm, rồi dùng kèm riêng cho giai đoạn hoàn thiện portfolio, lúc mỗi nhận xét đều đắt giá. Nếu bạn đang so lớp nhóm với kèm riêng theo mức tiền, bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">khoá học Blender 3D ở Việt Nam</a> có bảng đối chiếu bốn loại khoá và các khoản học phí thường gặp.</p>

<h2>Mặt bất lợi của học kèm 1 kèm 1</h2>

<p>Phần này ít ai nói nên nói ở đây. Thứ nhất, kèm riêng không có bạn học, mà nhìn bài của người cùng trình độ là một kênh học rất mạnh, nhất là để biết mình đang ở đâu. Thứ hai, nó dễ tạo thói quen dựa dẫm: có người soi sẵn thì bạn bớt tập kỹ năng tự chẩn đoán, và kỹ năng đó mới là thứ theo bạn đi làm.</p>

<p>Thứ ba, chất lượng phụ thuộc gần như hoàn toàn vào một người: chọn nhầm thì mất cả tiền và cả hướng. Thứ tư, chi phí khiến phần lớn người học chỉ đi được vài chặng ngắn, và không có lộ trình rõ thì mấy chặng đó rời rạc.</p>

<p>Cách giảm bốn nhược điểm này khá đơn giản: dùng kèm riêng theo từng chặng có mục tiêu đóng, giữa các chặng tự làm bài một mình để tập chẩn đoán, và vẫn tham gia một nhóm nào đó để có người cùng trình độ mà đối chiếu. Nếu bạn còn phân vân ngay ở bước đầu, bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học hay học kèm</a> đi sâu hơn vào lựa chọn này.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Học kèm 1 kèm 1 Blender giá khoảng bao nhiêu?</p>
<p>Chúng tôi không nêu một con số cố định vì nó phụ thuộc số buổi, thời lượng và mức người kèm. Cách đọc giá hợp lý hơn là hỏi mỗi buổi gồm bao nhiêu phút sửa bài trực tiếp, có ghi hình buổi học không và có được nhận xét giữa hai buổi không. Hai lớp cùng giá mà khác ba điểm đó thì giá trị thật khác nhau rất xa.</p>

<p class="faq-q">Người chưa từng mở Blender có nên học kèm 1 kèm 1 luôn không?</p>
<p>Thường là không nên. Giai đoạn làm quen giao diện và phím tắt thì video miễn phí dạy tốt và rẻ hơn. Hợp hơn là học nền bằng một khoá cho người mới hoặc lớp nhóm, rồi dùng kèm riêng khi đã có bài nộp và bắt đầu bị mắc kẹt.</p>

<p class="faq-q">Học kèm 1 kèm 1 online có kém hơn ngồi cạnh nhau không?</p>
<p>Với đồ hoạ 3D thì khác biệt nhỏ, vì bài nộp là file và ảnh, gửi đi rất nhanh. Phần quan trọng là người kèm có mở được file của bạn và sửa trực tiếp trong đó hay không, cùng với việc buổi học có được ghi hình để bạn xem lại.</p>

<p class="faq-q">Cần bao nhiêu buổi kèm riêng thì thấy tiến bộ?</p>
<p>Ước lượng khoảng bốn tới sáu buổi là đủ để thấy khác biệt, với điều kiện giữa hai buổi bạn có làm bài mới. Nếu sau sáu buổi mà bạn vẫn không tự chẩn đoán được lỗi của chính mình, vấn đề nằm ở cách dạy hoặc ở lượng bài bạn làm, không nằm ở số buổi.</p>

<p class="faq-q">Kèm riêng có giúp làm portfolio 3D nhanh hơn không?</p>
<p>Có, và đây là chặng kèm riêng phát huy rõ nhất. Nhưng người kèm chỉ nên chỉ ra vấn đề, không làm hộ, vì portfolio có bàn tay người khác trong đó sẽ lộ ngay ở buổi phỏng vấn. Muốn thấy mức hoàn thiện mà khách thường yêu cầu, xem vài shot thật ở trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a>.</p>

<hr class="hr">

<p>Bên mình nhận kèm riêng theo từng chặng, nội dung tuỳ mục tiêu của bạn. Xem trước hai hệ đào tạo ở trang <a href="khoa-hoc.html">khoá học Blender 3D</a>. Còn nếu muốn tự thử trước khi quyết định, tải <a href="cam-nang.html">cẩm nang miễn phí</a>, chọn một bài cũ của bạn và tự soi nó theo danh sách sáu điểm phía trên, bạn sẽ biết mình cần người kèm ở chặng nào.</p>
""",
    },
    {
        "slug": "hoc-do-hoa-3d-tu-con-so-0",
        "title": "Học đồ hoạ 3D từ con số 0: ba tháng đầu nên làm gì",
        "desc": "Kế hoạch ba tháng đầu cho người học đồ hoạ 3D từ con số 0 bằng Blender: học gì trước, bỏ qua gì, luyện bao nhiêu mỗi tuần và danh sách kiểm tra cuối chặng.",
        "tag": "Bắt đầu",
        "date": "2026-09-26",
        "date_vn": "26/09/2026",
        "updated": "2026-10-15",
        "updated_vn": "15/10/2026",
        "read": "13 phút đọc",
        "thumb": "assets/jhm-khoi-kinh-ky-thuat.webp",
        "faq": [
            ("Học đồ hoạ 3D từ con số 0 mất bao lâu mới làm được hình xem được?",
             "Theo nhịp bốn tới năm buổi mỗi tuần, mỗi buổi khoảng một tiếng, phần lớn người mới có tấm hình đầu tiên dám đăng công khai trong tám tới mười hai tuần. Đây là khoảng ước lượng từ chỗ chúng tôi quan sát học viên, không phải cam kết. Người học dồn vào cuối tuần thường mất gấp đôi thời gian đó vì tuần nào cũng phải làm quen lại phần mềm."),
            ("Không biết vẽ thì học đồ hoạ 3D được không?",
             "Được, nếu bạn nhắm hướng sản phẩm, hard-surface, nội thất hoặc phối cảnh. Những hướng này làm việc với khối, tỉ lệ và ánh sáng chứ không cần kỹ năng vẽ tay. Hướng cần vẽ là nhân vật và concept stylized, và đó chỉ là một nhánh của nghề."),
            ("Ba tháng đầu có cần mua máy mới không?",
             "Phần lớn là không. Máy có 16GB RAM và một card rời tầm phổ thông đủ cho cả ba tháng đầu, vì bài tập còn nhỏ và render thử ở chất lượng thấp. Để tiền đó cho lúc render thật sự chặn đường bạn, thường là từ tháng thứ tư trở đi khi cảnh đã nhiều vật và nhiều đèn."),
            ("Nên tự học ba tháng đầu hay có người kèm ngay từ đầu?",
             "Nếu bạn chưa biết mình có thích nghề này hay không, tự học một tới hai tháng là cách thử rẻ nhất. Khi đã có vài bài mà không tự biết bài nào yếu ở đâu, lúc đó người kèm mới đáng tiền, vì cái bạn thiếu là người chẩn đoán chứ không phải thêm bài giảng."),
            ("Học đồ hoạ 3D bằng Blender rồi có phải học lại phần mềm khác không?",
             "Chỉ khi nơi bạn vào làm bắt buộc dùng phần mềm khác. Nguyên lý khối, UV, vật liệu, ánh sáng và render chuyển được gần hết giữa các phần mềm, phần phải học lại chủ yếu là phím tắt và cách tổ chức scene, thường mất vài tuần."),
        ],
        "body": """
<p class="lead">Học đồ hoạ 3D từ con số 0 nên bắt đầu bằng ba tháng có thứ tự rõ ràng: tháng đầu làm quen phần mềm và giữ nhịp luyện, tháng hai tập ánh sáng và vật liệu, tháng ba làm trọn vẹn một sản phẩm từ khối thô tới hình cuối. Người mới thường hỏi nên học phần mềm nào, nhưng câu hỏi đó ít quan trọng hơn thứ tự học. Ba tháng đầu quyết định bạn ở lại hay bỏ cuộc.</p>

<h2>Chọn phần mềm trong năm phút</h2>

<p>Nếu bạn bắt đầu từ con số 0 và tự trả tiền cho mọi thứ, chọn Blender. Miễn phí, chạy được trên máy phổ thông, làm được cả model, dựng cảnh, ánh sáng, hoạt hình và hậu kỳ trong một chỗ. Khi đi làm cần phần mềm khác, bạn học thêm trong vài tuần vì nguyên lý giống nhau.</p>

<p>Máy móc cũng vậy, đừng nâng cấp vội. Chúng tôi đã viết riêng về <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> và khi nào máy thật sự là thứ đang cản bạn. Nếu vẫn đang cân nhắc giữa các công cụ, bài <a href="blog-blender-hay-3dsmax-c4d.html">so sánh Blender với 3ds Max và C4D</a> nói rõ phần kỹ năng nào chuyển được giữa chúng.</p>

<h2>Ba tháng đầu nhìn trên một bảng</h2>

<p>Bảng dưới là khung chúng tôi dùng khi tư vấn người mới. Thời lượng là ước lượng theo nhịp bốn tới năm buổi mỗi tuần, mỗi buổi khoảng một tiếng.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Chặng</th><th>Việc chính</th><th>Thứ nên bỏ qua</th><th>Dấu hiệu đã qua chặng</th></tr></thead>
<tbody>
<tr><td>Tháng 1</td><td>Thao tác cơ bản, model khối đơn giản, một nguồn sáng</td><td>Add-on, vật liệu nhiều node, hoạt hình</td><td>Mở Blender không còn thấy sợ, dựng xong một vật trong một buổi</td></tr>
<tr><td>Tháng 2</td><td>Ánh sáng ba kiểu, vật liệu kim loại nhựa kính gỗ</td><td>Mô phỏng khói lửa vải, nhân vật</td><td>Nói được vì sao đặt đèn ở chỗ đó, không chỉ đặt theo mẫu</td></tr>
<tr><td>Tháng 3</td><td>Một sản phẩm trọn vẹn từ khối thô tới hình cuối</td><td>Làm thêm bài mới khi bài cũ chưa xong</td><td>Có một tấm hình dám đăng công khai và nhận nhận xét</td></tr>
</tbody>
</table>
</div>

<h2>Tháng đầu: làm quen và giữ nhịp</h2>

<p>Mục tiêu tháng này không phải làm ra hình đẹp. Là ngồi xuống đều đặn và không sợ phần mềm nữa.</p>

<ul>
<li><strong style="color:#fff;">Thao tác cơ bản:</strong> xoay cảnh, di chuyển, phóng to, chọn đối tượng, lưu file cho gọn.</li>
<li><strong style="color:#fff;">Model khối đơn giản:</strong> cái ly, cái loa, cái điều khiển. Vật gì trên bàn cũng được.</li>
<li><strong style="color:#fff;">Một nguồn sáng duy nhất:</strong> tập nhìn bóng đổ trước khi nghĩ tới ba đèn.</li>
<li><strong style="color:#fff;">Nhịp luyện:</strong> bốn tới năm buổi mỗi tuần, mỗi buổi một tiếng, hơn hẳn ngồi tám tiếng vào chủ nhật.</li>
</ul>

<p>Một mẹo nhỏ: chọn đúng một vật thật trong nhà và dựng lại nó mỗi hai tuần trong cả ba tháng. Cùng một đề thì không có chỗ để tự lừa mình.</p>

<h2>Tháng hai: ánh sáng và vật liệu</h2>

<p>Đây là chỗ hình của bạn bắt đầu khác người mới khác. Đa số người tự học nhảy vào vật liệu phức tạp quá sớm, trong khi thứ quyết định cảm giác của khung hình là ánh sáng.</p>

<ul>
<li>Dựng lại cùng một vật với ba kiểu sáng khác nhau, so sánh cảm giác từng bản.</li>
<li>Học đủ vật liệu cơ bản: kim loại, nhựa, kính, gỗ. Chưa cần node phức tạp.</li>
<li>Chụp ảnh tham khảo ngoài đời rồi bắt chước đúng kiểu sáng đó.</li>
</ul>

<figure>
  <img src="assets/jhm-khoi-kinh-ky-thuat.webp" alt="Khối kính kỹ thuật dựng bằng Blender, nền lưới, ánh sáng studio tối giản" loading="lazy" width="1800" height="1012">
  <figcaption><strong>Một shot kỹ thuật dựng tối giản.</strong> Cảnh này gần như không có vật liệu cầu kỳ. Toàn bộ cảm giác đến từ ánh sáng và bố cục, hai thứ người mới hay để sau cùng.</figcaption>
</figure>

<p>Nếu tháng này bạn thấy hình vẫn trông giả mà không biết sửa đâu, bài <a href="blog-5-loi-lighting.html">học lighting trong Blender</a> điểm ra năm lỗi làm render rẻ tiền, phần lớn người mới mắc ít nhất ba trong số đó.</p>

<h2>Tháng ba: làm cho xong một sản phẩm</h2>

<p>Tháng này bạn chọn một vật, làm trọn vẹn từ model tới hình cuối, và bắt mình kết thúc nó. Làm xong một thứ tử tế dạy bạn nhiều hơn mười thứ dở dang. Tới đây mà thấy cần người soi bài, bài <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> liệt kê những gì một khoá nền phải có.</p>

<ol>
<li>Chọn vật bạn có trong nhà, chụp ảnh tham khảo từ nhiều góc.</li>
<li>Dựng khối thô, chốt bố cục và góc máy trước khi làm chi tiết.</li>
<li>Làm vật liệu, đặt sáng, render thử ở chất lượng thấp cho nhanh.</li>
<li>Hậu kỳ nhẹ tay, xuất hai ba tỉ lệ khung.</li>
<li>Đăng công khai một chỗ nào đó và nhận nhận xét, kể cả nhận xét khó nghe.</li>
</ol>

<blockquote><p>Ba tháng đầu không phải để giỏi. Là để biết mình có chịu nổi việc ngồi sửa một khung hình tới lần thứ mười lăm hay không.</p></blockquote>

<figure>
  <img src="assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp" alt="Khoá cửa thông minh dựng 3D ở dạng tách rời linh kiện, nền tối, ánh sáng studio" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một vật trong nhà là đề bài đủ tốt.</strong> Khoá cửa, loa hay bình nước đều có đủ khối, vát cạnh và nhiều loại vật liệu để luyện cả ba tháng.</figcaption>
</figure>

<h2>Vì sao nhiều người mới dừng ở tuần thứ sáu</h2>

<p>Chúng tôi thấy bốn nguyên nhân lặp lại, và không nguyên nhân nào liên quan tới độ khó của phần mềm.</p>

<ul>
<li><strong style="color:#fff;">Học theo video dài, không có bài nộp.</strong> Xem ba tiếng rồi không mở Blender thì tay không nhớ gì.</li>
<li><strong style="color:#fff;">Đổi đề bài liên tục.</strong> Tuần nào cũng bắt đầu một vật mới nên không bao giờ đi tới phần khó, là hoàn thiện.</li>
<li><strong style="color:#fff;">Nhảy vào kỹ thuật vui trước.</strong> Khói lửa và vật lý cho cảm giác tiến bộ nhanh, nhưng không xây được nền nào.</li>
<li><strong style="color:#fff;">Không có ai nói mình sai ở đâu.</strong> Đây là nguyên nhân khó tự sửa nhất, vì bạn không thể thấy lỗi mà mắt mình chưa học cách thấy.</li>
</ul>

<p>Ba cái đầu bạn tự sửa được bằng kỷ luật. Cái thứ tư thì không.</p>

<h2>Học một mình, lớp nhóm hay có người kèm</h2>

<p>Không có lựa chọn nào đúng cho mọi người. Cách chọn hợp lý là nhìn vào thứ bạn đang thiếu nhất, tiền, thời gian hay người chẩn đoán.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Tự học hoàn toàn</th><th>Lớp nhóm</th><th>Kèm riêng</th></tr></thead>
<tbody>
<tr><td>Chi phí tiền</td><td>Gần như bằng không</td><td>Vừa phải</td><td>Cao nhất, cần tính kỹ</td></tr>
<tr><td>Thời gian tới bài đầu tiên</td><td>Dài nhất, dễ lạc hướng</td><td>Trung bình, theo lịch lớp</td><td>Ngắn nhất nếu đã có nền</td></tr>
<tr><td>Mức độ được sửa bài</td><td>Không có, trừ khi tự xin</td><td>Có nhưng chia cho cả lớp</td><td>Toàn bộ buổi là bài của bạn</td></tr>
<tr><td>Kỷ luật đòi hỏi ở bạn</td><td>Rất cao</td><td>Vừa phải</td><td>Vừa phải</td></tr>
<tr><td>Hợp với chặng nào</td><td>Tháng 1 và 2, lúc còn đang thử</td><td>Từ tháng 2 trở đi</td><td>Khi đã có bài mà không biết bài yếu ở đâu</td></tr>
</tbody>
</table>
</div>

<p>Nếu bạn muốn so sánh kỹ hơn hai hướng đầu, bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm 3D</a> đi sâu vào chi phí và rủi ro của từng hướng. Còn nếu đang nghĩ tới hướng thứ ba, bài <a href="blog-gia-su-blender.html">gia sư Blender</a> nói rõ khi nào thật sự cần một người kèm riêng và cách thử người đó trước khi trả tiền, còn <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> mô tả một buổi kèm tử tế diễn ra thế nào.</p>

<h2>Những thứ chưa cần trong ba tháng đầu</h2>

<ul>
<li><strong style="color:#fff;">Hoạt hình nhân vật.</strong> Một nhánh riêng, học sau khi vững cảnh tĩnh.</li>
<li><strong style="color:#fff;">Mô phỏng vật lý, khói lửa, vải.</strong> Vui nhưng không giúp bạn kiếm việc sớm.</li>
<li><strong style="color:#fff;">Sưu tầm add on.</strong> Cài mười add on không bằng hiểu một nguyên lý ánh sáng.</li>
<li><strong style="color:#fff;">Nâng cấp máy.</strong> Để tiền đó cho lúc thật sự bị render chặn đường.</li>
</ul>

<h2>Dấu hiệu bạn đang đi đúng</h2>

<p>Sau ba tháng, bạn nên nhìn lại bài tháng đầu và thấy nó xấu. Đó là dấu hiệu tốt nhất, vì mắt bạn đã đi trước tay. Ngược lại, nếu bài cũ vẫn thấy ổn, nhiều khả năng bạn đang xem nhiều mà làm ít.</p>

<p>Dấu hiệu tốt thứ hai là bạn bắt đầu nhìn ánh sáng ngoài đời theo kiểu khác: để ý nguồn sáng trong quán cà phê, bóng đổ trên vỉa hè. Nghề này bắt đầu từ chỗ đó.</p>

<p>Đến lúc có vài bài nộp mà vẫn không tự biết bài nào yếu ở đâu, học kèm là bước hợp lý tiếp theo.</p>

<h2>Danh sách kiểm tra cuối ba tháng</h2>

<p>Tự soát bằng bảy câu dưới. Trả lời được sáu câu là bạn đã qua chặng nền, dù hình chưa đẹp.</p>

<ul>
<li>Dựng xong một vật đơn giản trong một buổi, không cần xem lại hướng dẫn từng bước.</li>
<li>Giữ được nhịp ít nhất bốn buổi mỗi tuần trong tám tuần liên tiếp.</li>
<li>Giải thích được vì sao đặt đèn chính ở hướng đó, không chỉ sao chép theo mẫu.</li>
<li>Làm được bốn vật liệu cơ bản mà không cần tải sẵn từ thư viện.</li>
<li>Có đúng một sản phẩm hoàn thành từ khối thô tới hình xuất cuối.</li>
<li>Đã đăng công khai ít nhất một bài và đọc hết nhận xét, kể cả nhận xét khó nghe.</li>
<li>Nhìn lại bài tháng đầu và thấy rõ ba lỗi cụ thể của nó.</li>
</ul>

<h2>Sau ba tháng thì đi tiếp đường nào</h2>

<p>Hết chặng nền, bạn phải chọn hướng, vì học rộng tiếp sẽ loãng. Ba hướng dễ bắt đầu nhất ở Việt Nam:</p>

<ul>
<li><strong style="color:#fff;">Hình sản phẩm.</strong> Nhu cầu đều, đề bài rõ, dễ làm portfolio. Bài <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a> mô tả cần học gì để nhận việc.</li>
<li><strong style="color:#fff;">Modeling chuyên sâu.</strong> Nếu bạn thích phần khối và kỹ thuật hơn phần hình ảnh, xem <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> để biết thứ tự học.</li>
<li><strong style="color:#fff;">Ánh sáng và render.</strong> Hướng khó thấy tiến bộ nhưng được trả tiền tốt. Bài <a href="blog-khoa-hoc-render.html">khoá học render</a> nói rõ nên dạy gì và học bao lâu là đủ.</li>
</ul>

<p>Muốn nhìn toàn cảnh thứ tự bảy kỹ năng của nghề, đọc <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a>. Còn nếu bạn tò mò đầu ra của nghề trông thế nào trong thực tế, phần <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> của studio là các dạng đề bài khách hàng thật sự đặt hàng.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Học đồ hoạ 3D từ con số 0 mất bao lâu mới làm được hình xem được?</p>
<p>Theo nhịp bốn tới năm buổi mỗi tuần, mỗi buổi khoảng một tiếng, phần lớn người mới có tấm hình đầu tiên dám đăng công khai trong tám tới mười hai tuần. Đây là khoảng ước lượng từ chỗ chúng tôi quan sát học viên, không phải cam kết. Người học dồn vào cuối tuần thường mất gấp đôi thời gian đó vì tuần nào cũng phải làm quen lại phần mềm. Bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu thì nhận job đầu tiên</a> tính tiếp quãng đường sau mốc này.</p>

<p class="faq-q">Không biết vẽ thì học đồ hoạ 3D được không?</p>
<p>Được, nếu bạn nhắm hướng sản phẩm, hard-surface, nội thất hoặc phối cảnh. Những hướng này làm việc với khối, tỉ lệ và ánh sáng chứ không cần kỹ năng vẽ tay. Hướng cần vẽ là nhân vật và concept stylized, và đó chỉ là một nhánh của nghề.</p>

<p class="faq-q">Ba tháng đầu có cần mua máy mới không?</p>
<p>Phần lớn là không. Máy có 16GB RAM và một card rời tầm phổ thông đủ cho cả ba tháng đầu, vì bài tập còn nhỏ và render thử ở chất lượng thấp. Để tiền đó cho lúc render thật sự chặn đường bạn, thường là từ tháng thứ tư trở đi khi cảnh đã nhiều vật và nhiều đèn.</p>

<p class="faq-q">Nên tự học ba tháng đầu hay có người kèm ngay từ đầu?</p>
<p>Nếu bạn chưa biết mình có thích nghề này hay không, tự học một tới hai tháng là cách thử rẻ nhất. Khi đã có vài bài mà không tự biết bài nào yếu ở đâu, lúc đó người kèm mới đáng tiền, vì cái bạn thiếu là người chẩn đoán chứ không phải thêm bài giảng.</p>

<p class="faq-q">Học đồ hoạ 3D bằng Blender rồi có phải học lại phần mềm khác không?</p>
<p>Chỉ khi nơi bạn vào làm bắt buộc dùng phần mềm khác. Nguyên lý khối, UV, vật liệu, ánh sáng và render chuyển được gần hết giữa các phần mềm, phần phải học lại chủ yếu là phím tắt và cách tổ chức scene, thường mất vài tuần.</p>

<hr class="hr">

<p>Nếu muốn đi theo lộ trình có người chữa bài, xem <a href="khoa-hoc.html">khoá học Blender 3D</a> của LXAM Academy với hai hệ và mốc kiểm tra từng tuần. Muốn tự học trước thì tải <a href="cam-nang.html">cẩm nang miễn phí</a> rồi quay lại danh sách kiểm tra bảy câu sau tám tuần nữa.</p>
""",
    },
    {
        "slug": "khoa-hoc-blender-3d-cho-nguoi-moi",
        "title": "Khoá học Blender 3D cho người mới nên có những gì",
        "desc": "Khoá học Blender 3D cho người mới nên dạy gì trong tám tuần đầu, học online hay tại TPHCM, học phí gồm những khoản nào và sáu câu cần hỏi trước khi đóng tiền.",
        "tag": "Định hướng",
        "date": "2026-09-28",
        "date_vn": "28/09/2026",
        "read": "9 phút đọc",
        "thumb": "assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp",
        "faq": [
            ("Khoá học Blender 3D cho người mới nên kéo dài bao lâu?",
             "Tám tới mười hai tuần cho phần nền là đủ, với điều kiện tuần nào cũng có bài nộp và được sửa. Khoá ngắn hơn thường chỉ kịp dạy nút bấm, khoá dài hơn mà không có bài nộp thì độ dài không giúp được gì."),
            ("Chưa có máy mạnh thì học khoá Blender 3D cho người mới được không?",
             "Được. Phần nền gồm dựng khối, bố cục, ánh sáng và vật liệu cơ bản chạy tốt trên máy phổ thông. Máy chỉ trở thành vấn đề khi bạn bắt đầu render cảnh lớn hoặc làm hoạt hình."),
            ("Khoá học 3D online có kém lớp học trực tiếp tại TPHCM không?",
             "Không kém nếu khoá online có buổi sửa bài trực tiếp và ghi hình lại. Thứ quyết định kết quả là tần suất được nhận xét, không phải bạn ngồi ở phòng học hay ở nhà."),
            ("Học phí khoá học Blender thường gồm những gì?",
             "Thường gồm buổi học, tài liệu và số lần sửa bài. Nên hỏi rõ ba khoản hay bị bỏ ngoài báo giá: số lần sửa bài tối đa, thời hạn xem lại bài giảng, và có được hỗ trợ sau khi kết thúc khoá hay không."),
        ],
        "body": """
<p class="lead">Một khoá học Blender 3D cho người mới tử tế hay không, bạn biết được sau hai tuần. Nếu tới cuối tuần thứ hai bạn đã render xong một vật thật và nói được vì sao nó trông như vậy, khoá đó ổn. Còn nếu hai tuần đầu vẫn đang giới thiệu giao diện, bạn đang trả tiền cho phần YouTube cho không.</p>

<p>Bài này là bộ tiêu chí để soi một khoá học trước khi đóng tiền, viết từ chỗ đã ngồi sửa bài cho khá nhiều người bắt đầu từ con số 0. Nó không nói khoá nào tốt nhất, vì việc đó tuỳ mục tiêu của bạn. Nó chỉ giúp bạn hỏi đúng câu. Nếu bạn muốn xem bức tranh rộng hơn trước, bài tổng hợp <a href="blog-khoa-hoc-3d-blender.html">khoá học 3D Blender</a> đối chiếu cả bốn kiểu khoá và dẫn tới đúng bài hướng dẫn theo tình trạng của bạn.</p>

<h2>Khoá cho người mới khác khoá nâng cao ở chỗ nào</h2>

<p>Nhiều nơi gọi là lớp cơ bản nhưng thực chất chỉ là lớp nâng cao bị cắt ngắn. Ba khác biệt dưới đây mới là thứ phân định.</p>

<h3>Nó phải giảm số quyết định, không tăng</h3>
<p>Blender có hàng trăm cách làm một việc. Người mới không cần biết hết, họ cần một con đường duy nhất đi được tới đích. Khoá tốt dám nói thẳng rằng giai đoạn này bạn chỉ dùng ba modifier và một loại đèn, phần còn lại để sau.</p>

<h3>Nó phải có bài nộp mỗi tuần</h3>
<p>Không có bài nộp thì không có dữ liệu để biết bạn hiểu hay chỉ đang gật đầu. Bài nộp cũng là thứ duy nhất biến buổi học thành kỹ năng, vì tay bạn phải tự đi lại đoạn đường mà mắt vừa nhìn thấy.</p>

<h3>Nó phải chấp nhận máy yếu</h3>
<p>Người mới hay bị doạ nâng cấp máy ngay tuần đầu. Phần nền của nghề chạy được trên máy phổ thông, và bạn nên để tiền đó lại cho lúc thật sự bị render chặn đường. Tôi đã viết riêng về <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> và mốc nào thì nâng cấp mới có nghĩa.</p>

<figure>
  <img src="assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp" alt="Hai mặt khoá cửa thông minh màu đen dựng 3D bằng Blender, đặt lơ lửng trên nền xám sáng với dòng chữ Digital Lock phía sau" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một shot sản phẩm dạng tách lớp trong dự án khoá cửa thông minh.</strong> Nhìn thì tưởng phải giỏi model mới làm được. Thực tế phần quyết định là bố cục, nền và hướng sáng, đều là thứ nằm trong tám tuần đầu của một khoá nền tử tế.</figcaption>
</figure>

<h2>Tám tuần đầu của một khoá học Blender 3D tử tế</h2>

<p>Đây không phải giáo trình chuẩn, mỗi nơi sắp xếp một kiểu. Nhưng nếu một khoá học cho người mới thiếu hẳn một trong các mốc dưới đây, bạn nên hỏi lại lý do.</p>

<p>Thứ tự tám tuần này bám theo đúng <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> bảy bước: dựng hình trước, vật liệu và ánh sáng sau, render sau nữa. Khoá nào đảo thứ tự đó, hãy hỏi vì sao.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Giai đoạn</th><th>Học gì</th><th>Bài nộp nên có</th></tr></thead>
<tbody>
<tr><td>Tuần 1 đến 2</td><td>Di chuyển trong viewport, dựng khối cơ bản, giữ file gọn</td><td>Một vật đơn giản có trong nhà, render thô</td></tr>
<tr><td>Tuần 3 đến 4</td><td>Bố cục, góc máy, một nguồn sáng duy nhất</td><td>Cùng một vật, ba góc máy khác nhau</td></tr>
<tr><td>Tuần 5 đến 6</td><td>Vật liệu cơ bản: kim loại, nhựa, kính, gỗ</td><td>Một vật nhiều chất liệu, ví dụ tai nghe hoặc bình giữ nhiệt</td></tr>
<tr><td>Tuần 7 đến 8</td><td>Ánh sáng nhiều nguồn, hậu kỳ nhẹ, xuất file</td><td>Một shot sản phẩm hoàn chỉnh, xuất hai tỉ lệ khung</td></tr>
</tbody>
</table>
</div>

<p>Điểm chung của bốn mốc này là tuần nào cũng kết thúc bằng một tấm hình xem được. Người mới bỏ cuộc phần lớn không phải vì khó, mà vì học sáu tuần vẫn chưa có gì để khoe. Nếu bạn muốn đối chiếu với nhịp tự học, bài <a href="blog-hoc-do-hoa-3d-tu-con-so-0.html">học đồ hoạ 3D từ con số 0</a> mô tả cùng quãng đường nhưng không có người kèm.</p>

<blockquote><p>Một khoá cho người mới nên đo bằng số bài bạn làm xong, không phải số giờ bạn ngồi nghe.</p></blockquote>

<h2>Khoá học 3D online hay lớp trực tiếp tại TPHCM</h2>

<p>Câu hỏi này bị đặt sai từ đầu. Thứ quyết định kết quả không phải bạn ngồi ở đâu, mà là bạn được nhận xét bao nhiêu lần. Một lớp trực tiếp mà thầy chỉ giảng rồi về cũng vô ích như một khoá online chỉ có video.</p>

<div class="table-wrap">
<table>
<thead><tr><th></th><th>Khoá học 3D online</th><th>Lớp trực tiếp tại TPHCM</th></tr></thead>
<tbody>
<tr><td>Điểm mạnh</td><td>Xem lại được, linh hoạt giờ giấc, không mất thời gian di chuyển</td><td>Được nhìn thao tác tận mắt, dễ hỏi ngay khi bí</td></tr>
<tr><td>Điểm yếu</td><td>Dễ bỏ giữa chừng nếu không có lịch nộp bài</td><td>Lịch cố định, nghỉ một buổi là hụt, phụ thuộc chỗ ở</td></tr>
<tr><td>Hợp với ai</td><td>Người đi làm, ở tỉnh, giờ giấc thất thường</td><td>Người mới hoàn toàn, cần không khí lớp để giữ kỷ luật</td></tr>
<tr><td>Điều kiện để hiệu quả</td><td>Có buổi sửa bài trực tiếp, có ghi hình lại</td><td>Có thời gian thực hành riêng mỗi buổi, sĩ số nhỏ</td></tr>
</tbody>
</table>
</div>

<p>Sau tám tuần nền, phần lớn người học đi tiếp theo hướng làm ảnh, lúc đó tiêu chí chọn lớp đổi khác và bài <a href="blog-khoa-hoc-render.html">khoá học render nên dạy gì</a> mô tả rõ bốn phần bắt buộc phải có.</p>

<p>Nói thẳng mặt bất lợi của hình thức online: tỉ lệ bỏ giữa chừng cao hơn hẳn, và phần lớn rơi vào tuần thứ ba tới thứ năm, lúc hứng thú ban đầu hết mà kết quả chưa đủ đẹp để tự động viên. Nếu bạn biết mình khó giữ kỷ luật một mình, hãy chọn nơi có lịch nộp bài cứng, hoặc cân nhắc <a href="blog-hoc-blender-kem-1-1.html">học Blender kèm một kèm một</a> cho giai đoạn đầu.</p>

<h2>Học phí khoá học Blender gồm những gì</h2>

<p>Mình không nêu con số vì giá mỗi nơi mỗi khác và thay đổi theo thời gian. Thứ đáng quan tâm hơn là báo giá đó gồm những khoản nào. Ba khoản dưới đây hay bị để ngoài và chỉ lộ ra khi bạn đã đóng tiền.</p>

<ul>
<li><strong style="color:#fff;">Số lần sửa bài.</strong> Có nơi tính không giới hạn, có nơi giới hạn theo buổi. Đây là khoản có giá trị thật nhất trong học phí, nên hỏi trước.</li>
<li><strong style="color:#fff;">Thời hạn xem lại bài giảng.</strong> Ba tháng và trọn đời là hai sản phẩm khác nhau, dù giá niêm yết giống nhau.</li>
<li><strong style="color:#fff;">Hỗ trợ sau khoá.</strong> Lúc bạn nhận job đầu tiên mới là lúc câu hỏi khó nhất xuất hiện, thường là vài tháng sau khi lớp kết thúc.</li>
</ul>

<p>Một cách so sánh công bằng hơn giá mỗi buổi: lấy học phí chia cho số lần bài của bạn được người có nghề xem tận nơi. Con số đó mới phản ánh thứ bạn thật sự mua. Bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">chọn khoá học Blender 3D ở Việt Nam</a> có bảng dịch các kiểu nói về học phí sang nghĩa thật của chúng, và bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a> có đủ bốn khoản phát sinh nằm ngoài hoá đơn.</p>

<h2>Sáu câu nên hỏi trước khi đóng tiền</h2>

<ol>
<li><strong style="color:#fff;">Cho tôi xem bài của học viên mới, không phải bài của giảng viên.</strong> Bài học viên cho biết khoá dạy được gì, bài giảng viên chỉ cho biết họ giỏi.</li>
<li><strong style="color:#fff;">Tuần đầu tiên tôi nộp gì?</strong> Không trả lời được cụ thể nghĩa là chưa có lịch bài nộp.</li>
<li><strong style="color:#fff;">Ai là người sửa bài của tôi?</strong> Người dạy và người sửa nhiều khi không phải một.</li>
<li><strong style="color:#fff;">Mỗi bài được nhận xét mấy lần?</strong> Nhận xét một lần rồi thôi khác hẳn nhận xét rồi sửa rồi nhận xét lại.</li>
<li><strong style="color:#fff;">Máy của tôi cấu hình này có theo nổi không?</strong> Câu trả lời tử tế sẽ nói rõ phần nào chạy được, phần nào phải giảm chất lượng.</li>
<li><strong style="color:#fff;">Nếu tôi bỏ giữa chừng thì sao?</strong> Chính sách bảo lưu hoặc hoàn phí nói nhiều về mức tự tin của nơi đó.</li>
</ol>

<p>Nếu bạn vẫn đang phân vân giữa việc mua một khoá và tự mò thêm vài tháng, đọc <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học khoá có người kèm</a> trước khi quyết định. Có những trường hợp câu trả lời đúng là chưa nên học khoá nào cả.</p>

<h2>Dấu hiệu một khoá không dành cho người mới</h2>

<ul>
<li><strong style="color:#fff;">Buổi đầu đã nói về node phức tạp.</strong> Người mới cần thấy kết quả trước khi hiểu cơ chế.</li>
<li><strong style="color:#fff;">Không có bài nộp, chỉ có bài xem.</strong> Đây là khoá video trá hình.</li>
<li><strong style="color:#fff;">Hứa đi làm ngay sau khoá.</strong> Mốc thời gian thật dài hơn nhiều, bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender bao lâu thì nhận job đầu tiên</a> có con số theo từng giai đoạn.</li>
<li><strong style="color:#fff;">Học viên trong lớp chênh lệch trình độ quá xa.</strong> Người mới sẽ đuối, người khá sẽ chán.</li>
<li><strong style="color:#fff;">Chỉ dạy phần mềm, không dạy cách nhìn.</strong> Nút bấm tra được, mắt nhìn ánh sáng thì phải có người chỉ.</li>
</ul>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Khoá học Blender 3D cho người mới nên kéo dài bao lâu?</p>
<p>Tám tới mười hai tuần cho phần nền là hợp lý, với điều kiện tuần nào cũng có bài nộp và được sửa. Ngắn hơn thường chỉ kịp dạy nút bấm. Dài hơn mà không có bài nộp thì độ dài cũng không giúp được gì.</p>

<p class="faq-q">Chưa có máy mạnh có học được không?</p>
<p>Được. Dựng khối, bố cục, ánh sáng và vật liệu cơ bản chạy tốt trên máy phổ thông. Máy chỉ thành vấn đề khi bạn render cảnh lớn hoặc làm hoạt hình, và lúc đó bạn đã đủ hiểu để biết mình cần nâng cấp cái gì.</p>

<p class="faq-q">Không biết vẽ thì sao?</p>
<p>Không sao. Mảng 3D sản phẩm, hard-surface và kiến trúc không đòi hỏi vẽ tay. Nếu tò mò công việc thật trông thế nào, xem qua vài shot bên trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> để hình dung đích đến.</p>

<p class="faq-q">Học xong khoá cho người mới thì bước tiếp theo là gì?</p>
<p>Làm trọn một dự án cá nhân từ đầu tới cuối, rồi mới tính chuyện chuyên sâu theo hướng sản phẩm, automotive hay sự kiện. Chọn hướng quá sớm khi chưa hoàn thành cái gì trọn vẹn là lỗi phổ biến nhất ở giai đoạn này. Nếu phần bạn còn yếu là dựng hình chứ không phải ánh sáng, bài <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> mô tả ba giai đoạn nên đi qua theo đúng thứ tự.</p>

<hr class="hr">

<p>Nếu bạn đang tìm một khoá học Blender 3D cho người mới có lịch nộp bài rõ và người sửa bài thật, xem trước hai hệ đào tạo ở trang <a href="khoa-hoc.html">khoá học Blender 3D</a>. Còn nếu muốn thử sức trước khi quyết định, tải <a href="cam-nang.html">cẩm nang miễn phí</a> và làm hết phần bài tập trong đó, ba tuần sau bạn sẽ tự biết mình cần khoá hay chỉ cần thêm kỷ luật.</p>
""",
    },    {
        "slug": "khoa-hoc-render",
        "title": "Khoá học render: nên dạy gì và học bao lâu là đủ",
        "desc": "Khoá học render nên dạy gì ngoài nút bấm, nên học Cycles hay Eevee trước, học phí gồm khoản nào và năm dấu hiệu nhận ra một khoá chỉ dạy thao tác.",
        "tag": "Định hướng",
        "date": "2026-09-30",
        "date_vn": "30/09/2026",
        "read": "9 phút đọc",
        "thumb": "assets/aston-dbx-goc-ben-dai-sang.webp",
        "faq": [
            ("Khoá học render khác khoá modeling 3D ở chỗ nào?",
             "Khoá modeling dạy bạn tạo ra hình khối đúng. Khoá học render dạy bạn quyết định ánh sáng, vật liệu, góc máy và hậu kỳ để hình khối đó trông thật và bán được. Hai kỹ năng này rời nhau, giỏi cái này không tự động kéo theo cái kia."),
            ("Nên học Cycles hay Eevee trước?",
             "Học Cycles trước. Cycles mô phỏng ánh sáng gần vật lý nên bạn học được nguyên lý, và nguyên lý đó mang sang Eevee vẫn dùng được. Làm ngược lại thì bạn quen với mẹo vặt của Eevee và sẽ lúng túng khi phải giải thích vì sao ảnh sai."),
            ("Học phí khoá học Blender phần render thường gồm gì?",
             "Thường gồm buổi học, file cảnh mẫu và số lần sửa bài. Nên hỏi rõ số lần được nhận xét trên cùng một bài, vì render là kỹ năng phải sửa đi sửa lại mới lên, một lần nhận xét rồi thôi gần như không đổi được gì."),
            ("Máy yếu có học render được không?",
             "Được, nhưng bạn phải chấp nhận render thử ở độ phân giải thấp và ít mẫu. Phần khó của render nằm ở quyết định ánh sáng và vật liệu, không nằm ở tốc độ máy. Máy chỉ trở thành rào cản khi bạn nhận job có deadline."),
            ("Học render bao lâu thì ra ảnh xem được?",
             "Ước lượng từ các nhóm học viên đã đi qua, khoảng sáu tới mười tuần nếu mỗi tuần bạn hoàn thành và nộp một shot. Ra ảnh xem được và ra ảnh đủ chuẩn giao khách là hai mốc khác nhau, mốc sau thường cần thêm vài tháng làm dự án thật."),
        ],
        "body": """
<p class="lead">Một khoá học render tử tế không dạy bạn bấm nút nào để ảnh đẹp hơn, vì không có nút đó. Nó dạy bạn nhìn ra vì sao tấm hình hiện tại chưa ổn, rồi sửa đúng chỗ. Nếu sau khoá học bạn vẫn phải thử ngẫu nhiên từng thông số cho tới lúc trông tạm được, khoá đó chưa làm xong việc của nó.</p>

<p>Bài này mô tả nội dung một khoá học render nên có, viết từ chỗ ngồi sửa bài render cho người học và làm hình thương mại mỗi tuần. Nó không nói nơi nào tốt nhất, chỉ đưa bộ tiêu chí để bạn tự soi trước khi đóng tiền.</p>

<h2>Khoá học render dạy gì mà video miễn phí không dạy</h2>

<p>Video hướng dẫn trên mạng rất nhiều và phần lớn đều đúng. Vấn đề là chúng dạy một cảnh cụ thể, còn nghề thì luôn đưa bạn một cảnh khác. Ba thứ dưới đây là phần mà lớp có người sửa bài làm được còn video thì không.</p>

<h3>Chẩn đoán, không phải công thức</h3>
<p>Khi một tấm hình trông rẻ tiền, nguyên nhân có thể nằm ở độ tương phản, ở hướng sáng, ở vật liệu quá bóng, hoặc ở chỗ bạn đặt máy quá cao. Video sẽ đưa bạn một thiết lập đã chỉnh sẵn. Người kèm sẽ chỉ vào ảnh của bạn và nói đây là lỗi gì. Khác biệt này quyết định bạn có tự sửa được lần sau hay không.</p>

<h3>Tiêu chuẩn đủ tốt để giao</h3>
<p>Người tự học thường dừng quá sớm hoặc chỉnh mãi không dứt. Khoá học có người trong nghề sẽ cho bạn biết mức nào là đủ cho một shot thương mại, mức nào là đang phí thời gian. Đây là thứ hầu như không ai làm video, vì nó phụ thuộc bối cảnh dự án.</p>

<h3>Thứ tự sửa</h3>
<p>Render có một trình tự sửa khá cố định: bố cục trước, ánh sáng sau, vật liệu tiếp theo, hậu kỳ cuối cùng. Người mới hay làm ngược, kéo hậu kỳ để cứu ánh sáng hỏng. Năm lỗi hay gặp nhất trong nhóm này tôi đã viết riêng ở bài <a href="blog-5-loi-lighting.html">học lighting trong Blender</a>, kèm bảng ba kiểu setup đèn và danh sách kiểm tra trước khi render bản cuối. Thứ tự sửa này đặt trong một dự án thật thì thành chín bước, mô tả đầy đủ ở bài <a href="blog-quy-trinh-mot-shot-tvc.html">quy trình dựng TVC 3D</a>, kể cả cách tách pass để mỗi vòng sửa chỉ mất vài phút.</p>

<figure>
  <img src="assets/aston-dbx-goc-ben-dai-sang.webp" alt="Xe Aston Martin DBX màu xanh ngọc dựng và render 3D bằng Blender, chụp nghiêng trên nền vải xanh đậm với một dải sáng trắng chạy ngang sàn phía sau xe" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một key visual automotive dựng hoàn toàn bằng Blender.</strong> Thứ làm tấm này đứng được không phải model xe, mà là dải sáng chạy dọc thân và khoảng tối giữ cho nền không giành mất chú ý. Đó chính là phần một khoá học render phải dạy.</figcaption>
</figure>

<p>Nếu muốn xem tiêu chuẩn này trông thế nào trên bài thật, hai bộ hình xe dưới đây là ví dụ sát nhất: <a href="du-an-porsche-911.html">bộ hình Porsche 911 dựng bằng Blender</a> cho thấy cách xử lý sơn bóng và phản chiếu môi trường, còn <a href="du-an-volvo-s90.html">bộ hình Volvo S90 render trong Blender</a> cho thấy cách giữ chi tiết ở vùng tối mà không kéo sáng cả khung.</p>

<h2>Cycles hay Eevee: khoá học render nên bắt đầu từ đâu</h2>

<p>Câu hỏi này gần như luôn xuất hiện ở buổi đầu. Câu trả lời ngắn là học Cycles trước, nhưng lý do mới là phần đáng nhớ.</p>

<div class="table-wrap">
<table>
<thead><tr><th></th><th>Cycles</th><th>Eevee</th></tr></thead>
<tbody>
<tr><td>Cách tính sáng</td><td>Mô phỏng tia sáng, gần vật lý</td><td>Xấp xỉ theo thời gian thực</td></tr>
<tr><td>Điểm mạnh</td><td>Phản xạ, khúc xạ, đổ bóng đáng tin</td><td>Xem kết quả gần như tức thì, hợp làm nháp và hoạt hình dài</td></tr>
<tr><td>Điểm yếu</td><td>Chậm, cảnh nặng dễ nghẽn máy</td><td>Phải bù bằng thiết lập tay, dễ sai nếu không hiểu nguyên lý</td></tr>
<tr><td>Nên học khi nào</td><td>Ngay từ đầu, để hiểu ánh sáng thật hoạt động ra sao</td><td>Sau khi đã đọc được ảnh, dùng như công cụ tăng tốc</td></tr>
</tbody>
</table>
</div>

<p>Người học Eevee trước thường ra ảnh nhanh hơn trong tháng đầu, rồi chững lại vì không giải thích được vì sao ảnh sai. Người học Cycles trước chậm hơn lúc đầu nhưng sang tháng thứ ba thì tự sửa được. Nếu bạn đang thấy Cycles quá chậm để luyện tập, xem trước các cách <a href="blog-render-nhanh-hon-blender-cycles.html">render nhanh hơn trong Blender Cycles</a>, phần lớn không cần nâng cấp máy.</p>

<blockquote><p>Render không phải cuộc thi chỉnh thông số. Nó là việc quyết định người xem nên nhìn vào đâu trước, rồi dùng ánh sáng để ép mắt họ làm đúng như vậy.</p></blockquote>

<h2>Bốn phần một khoá học render phải có</h2>

<p>Nếu một khoá thiếu hẳn một trong bốn phần dưới, bạn nên hỏi lại lý do trước khi đóng tiền.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Phần</th><th>Học được gì</th><th>Bài nộp nên có</th></tr></thead>
<tbody>
<tr><td>Ánh sáng</td><td>Một nguồn chính, vai trò của đèn phụ, cách tạo khoảng tối có chủ đích</td><td>Cùng một vật, ba phương án sáng khác nhau</td></tr>
<tr><td>Vật liệu</td><td>Kim loại, nhựa, kính, gỗ, vải và cách chúng phản ứng với đèn</td><td>Một vật nhiều chất liệu, ví dụ chai rượu hoặc tai nghe</td></tr>
<tr><td>Máy ảnh và bố cục</td><td>Tiêu cự, độ sâu trường ảnh, tỉ lệ khung cho từng kênh đăng</td><td>Một shot xuất hai tỉ lệ khung, ngang và dọc</td></tr>
<tr><td>Hậu kỳ</td><td>Đọc biểu đồ sáng, chỉnh màu vừa đủ, xuất file đúng chuẩn</td><td>So sánh ảnh trước và sau hậu kỳ, nói được đã sửa gì</td></tr>
</tbody>
</table>
</div>

<p>Bốn phần này áp dụng cho cả khoá học dựng hình sản phẩm lẫn khoá kiến trúc hay automotive, chỉ khác ở loại cảnh đem ra luyện. Nếu bạn còn đang phân vân giữa các kiểu lớp, bài tổng hợp <a href="blog-khoa-hoc-3d-blender.html">khoá học 3D Blender</a> đối chiếu bốn kiểu khoá đang có và nói rõ kiểu nào hợp với ai. Nếu bạn còn đang ở giai đoạn trước đó, nghĩa là chưa dựng được vật để render, thì bắt đầu từ <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> hợp lý hơn là nhảy thẳng vào render.</p>

<h2>Học phí khoá học Blender phần render gồm những khoản nào</h2>

<p>Mình không nêu con số vì giá mỗi nơi mỗi khác và thay đổi theo thời gian. Thứ nên soi là báo giá đó gồm gì. Ba khoản dưới hay bị để ngoài.</p>

<ul>
<li><strong style="color:#fff;">Số lần sửa trên cùng một bài.</strong> Render là kỹ năng sửa nhiều vòng. Được nhận xét một lần rồi thôi khác hẳn nhận xét, sửa, rồi nhận xét lại. Đây là khoản có giá trị thật nhất.</li>
<li><strong style="color:#fff;">File cảnh mẫu.</strong> Có nơi giao file gốc để bạn mổ xẻ, có nơi chỉ cho xem. Mổ được file của người có nghề tiết kiệm cho bạn hàng tuần mò mẫm.</li>
<li><strong style="color:#fff;">Hỗ trợ khi máy không kham nổi.</strong> Lớp render dễ vướng giới hạn phần cứng hơn lớp modeling. Nên hỏi trước nơi đó xử lý ra sao với máy cấu hình thấp.</li>
</ul>

<p>Một cách so sánh công bằng hơn giá mỗi buổi: lấy học phí chia cho số lần bài của bạn được người trong nghề xem tận nơi. Bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">chọn khoá học Blender 3D ở Việt Nam</a> có bảng dịch các kiểu nói về học phí sang nghĩa thật của chúng, dùng lại được cho khoá render. Cách quy báo giá về đơn giá phản hồi nằm trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>.</p>

<h2>Danh sách kiểm tra trước khi đóng tiền</h2>

<ol>
<li><strong style="color:#fff;">Xem bài render của học viên, không phải bài của giảng viên.</strong> Bài học viên cho biết khoá dạy được gì.</li>
<li><strong style="color:#fff;">Hỏi tuần đầu tiên nộp gì.</strong> Không trả lời cụ thể được nghĩa là chưa có lịch bài nộp.</li>
<li><strong style="color:#fff;">Hỏi ai sửa bài.</strong> Người dạy và người sửa nhiều khi không phải một người.</li>
<li><strong style="color:#fff;">Hỏi một bài được nhận xét mấy vòng.</strong> Với render, dưới hai vòng là gần như không đủ.</li>
<li><strong style="color:#fff;">Đưa cấu hình máy của bạn và hỏi thẳng.</strong> Câu trả lời tử tế sẽ nói rõ phần nào chạy được, phần nào phải giảm chất lượng khi luyện.</li>
<li><strong style="color:#fff;">Hỏi khoá dạy theo mảng nào.</strong> Sản phẩm, kiến trúc và automotive đòi hỏi cách sáng khác nhau, khoá dạy chung chung thường không đi sâu được mảng nào.</li>
</ol>

<p>Nếu bạn lo máy mình không theo nổi phần luyện render, đọc <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> trước, trong đó có mốc cụ thể cho biết khi nào nâng cấp mới thật sự có nghĩa. Còn nếu cảnh của bạn trông sai ngay từ khối chứ không phải từ ánh sáng, nên quay lại phần dựng hình trước đã, bài <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> chỉ ra ba giai đoạn và chỗ người học hay kẹt lâu nhất.</p>

<h2>Năm dấu hiệu một khoá học render chỉ dạy nút bấm</h2>

<ul>
<li><strong style="color:#fff;">Buổi nào cũng đưa thiết lập sẵn để bạn chép lại.</strong> Chép xong bạn có một tấm ảnh, không có kỹ năng.</li>
<li><strong style="color:#fff;">Không ai nói vì sao phương án sáng này bị loại.</strong> Chỉ nghe phương án đúng thì bạn không học được cách loại trừ.</li>
<li><strong style="color:#fff;">Chỉ luyện trên cảnh đã dọn sẵn.</strong> Cảnh thật luôn lộn xộn, và phần lớn thời gian làm nghề là dọn dẹp.</li>
<li><strong style="color:#fff;">Không dạy xuất file và không nhắc tới kênh đăng.</strong> Ảnh cho web, cho in và cho màn LED có yêu cầu khác nhau.</li>
<li><strong style="color:#fff;">Hứa ảnh đẹp như quảng cáo sau vài buổi.</strong> Ước lượng thực tế là vài tháng làm bài đều đặn, và điều đó không có gì đáng xấu hổ.</li>
</ul>

<p>Nói thẳng mặt bất lợi của việc học render trong lớp: nó tốn thời gian chờ. Bạn render thử, đợi, nhận xét, sửa, lại đợi. Người thiếu kiên nhẫn thường bỏ ở tuần thứ ba. Nếu bạn biết mình cần người đẩy, cân nhắc <a href="blog-hoc-blender-kem-1-1.html">học Blender kèm một kèm một</a> cho giai đoạn này, nhịp sửa bài dày hơn sẽ bù lại phần thời gian chờ.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Khoá học render khác khoá học modeling 3D ở chỗ nào?</p>
<p>Modeling dạy bạn tạo ra hình khối đúng. Render dạy bạn quyết định ánh sáng, vật liệu, góc máy và hậu kỳ để hình khối đó trông thật. Hai kỹ năng rời nhau, và người giỏi dựng hình vẫn có thể ra ảnh nhìn rẻ tiền nếu chưa học phần này.</p>

<p class="faq-q">Học render bao lâu thì ra ảnh xem được?</p>
<p>Ước lượng khoảng sáu tới mười tuần nếu tuần nào bạn cũng hoàn thành và nộp một shot. Nhưng ra ảnh xem được và ra ảnh đủ chuẩn giao khách là hai mốc khác nhau, mốc sau thường cần thêm vài tháng làm dự án thật.</p>

<p class="faq-q">Khoá học 3D online có học render hiệu quả không?</p>
<p>Có, nếu khoá đó có buổi sửa bài trực tiếp. Render đặc biệt hợp với hình thức online vì bài nộp là ảnh, gửi đi rất nhanh và người sửa nhìn ảnh là biết ngay vấn đề nằm ở đâu.</p>

<p class="faq-q">Học render xong thì làm được việc gì?</p>
<p>Phổ biến nhất là ảnh sản phẩm, key visual cho chiến dịch, phối cảnh sự kiện và ảnh kiến trúc. Bạn có thể xem vài shot thật bên trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> để hình dung mức hoàn thiện mà khách thường yêu cầu.</p>

<hr class="hr">

<p>Nếu bạn đang tìm một khoá học render có lịch nộp bài rõ và người sửa bài thật, xem trước hai hệ đào tạo ở trang <a href="khoa-hoc.html">khoá học Blender 3D</a>. Còn nếu muốn tự thử trước khi quyết định, tải <a href="cam-nang.html">cẩm nang miễn phí</a>, chọn một vật trong nhà và làm đủ ba phương án ánh sáng cho nó, bạn sẽ tự biết mình đang thiếu phần nào.</p>
""",
    },

    {
        "slug": "khoa-hoc-3d-blender",
        "title": "Khoá học 3D Blender: chọn hệ nào, học ở đâu, tốn gì",
        "desc": "Khoá học 3D Blender có mấy loại, nên học online hay tại TPHCM, học phí gồm những khoản nào, và ba bài hướng dẫn chi tiết cho từng nhóm người học.",
        "tag": "Định hướng",
        "date": "2026-09-30",
        "date_vn": "30/09/2026",
        "read": "10 phút đọc",
        "thumb": "assets/vplas-render-san-pham-blender.jpg",
        "faq": [
            ("Khoá học 3D Blender phù hợp với ai?",
             "Phù hợp với người muốn làm hình sản phẩm, quảng cáo, kiến trúc hoặc sự kiện và cần một lịch học có người sửa bài. Người chỉ muốn nghịch cho vui thì tài liệu miễn phí đã đủ, không cần đóng tiền."),
            ("Nên chọn khoá học 3D online hay học trực tiếp tại TPHCM?",
             "Online hợp với người đã có máy và biết tự ngồi vào bàn, vì bài nộp là file và ảnh nên gửi đi rất nhanh. Học trực tiếp hợp với người dễ bỏ giữa chừng và cần bị nhìn thấy mỗi tuần. Yếu tố quyết định là số lần bài của bạn được sửa, không phải hình thức lớp."),
            ("Học phí khoá học Blender thường gồm những khoản gì?",
             "Thường gồm buổi học, tài liệu và file mẫu, số lần sửa bài, và thời gian được hỏi sau khoá. Khoản dễ bị bỏ ngoài báo giá nhất là số vòng sửa trên cùng một bài, trong khi đó mới là phần quyết định bạn tiến bộ hay không."),
            ("Chưa có máy mạnh thì có nên đăng ký khoá học 3D Blender không?",
             "Nên, nếu bạn bắt đầu từ dựng hình và bố cục. Hai phần đó chạy tốt trên máy phổ thông. Máy chỉ trở thành rào cản khi bạn render cảnh nặng hoặc làm hoạt hình, và lúc đó bạn đã đủ hiểu để biết cần nâng cấp cái gì."),
            ("Học khoá 3D Blender bao lâu thì làm được việc?",
             "Ước lượng từ các nhóm học viên đã đi qua, khoảng ba tới sáu tháng học đều để có bộ ảnh đủ đi xin việc hoặc nhận job nhỏ. Con số này phụ thuộc số giờ bạn thật sự ngồi làm mỗi tuần nhiều hơn là phụ thuộc khoá học."),
        ],
        "body": """
<p class="lead">Khoá học 3D Blender ở Việt Nam hiện chia làm bốn kiểu, và chúng khác nhau ở một điểm duy nhất đáng quan tâm: bài của bạn được người trong nghề xem bao nhiêu lần. Mọi thứ còn lại, từ số buổi tới tên gọi lộ trình, đều là chi tiết phụ. Bài này là trang tổng hợp, dẫn bạn tới đúng bài hướng dẫn chi tiết theo tình trạng hiện tại của bạn.</p>

<p>Viết từ chỗ ngồi sửa bài cho người học và làm hình thương mại mỗi tuần. Không có tên nơi nào tốt nhất trong bài, chỉ có bộ tiêu chí và ba bài đọc sâu để bạn tự quyết định.</p>

<h2>Khoá học 3D Blender đang có mấy loại</h2>

<p>Bốn kiểu dưới đây bao gần hết thị trường. Chúng không xếp theo tốt xấu, mà theo việc chúng hợp với ai.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Kiểu</th><th>Hợp với ai</th><th>Rủi ro lớn nhất</th></tr></thead>
<tbody>
<tr><td>Khoá quay sẵn, học theo video</td><td>Người kỷ luật, đã biết mình cần gì</td><td>Không ai nói bài bạn sai chỗ nào</td></tr>
<tr><td>Lớp nhóm theo lịch cố định</td><td>Người mới, cần nhịp và bạn học</td><td>Sĩ số đông thì mỗi bài chỉ được nhìn lướt</td></tr>
<tr><td>Kèm riêng một kèm một</td><td>Người đi làm, ít thời gian, có mục tiêu rõ</td><td>Đắt, và phụ thuộc hoàn toàn vào người kèm</td></tr>
<tr><td>Khoá chuyên mảng: sản phẩm, kiến trúc, automotive</td><td>Người đã dựng được hình, muốn đi sâu</td><td>Vào sớm quá thì không theo nổi</td></tr>
</tbody>
</table>
</div>

<p>Nếu bạn chưa mở Blender bao giờ, ba kiểu đầu đều dùng được, kiểu thứ tư thì chưa. Còn nếu bạn đã dựng được vài vật nhưng ảnh ra vẫn nhìn rẻ tiền, vấn đề của bạn nằm ở ánh sáng và vật liệu chứ không nằm ở dựng hình. Thử đối chiếu với bài <a href="blog-5-loi-lighting.html">học lighting trong Blender</a> trước, còn nếu muốn có người chữa bài thì một <a href="blog-khoa-hoc-render.html">khoá học render</a> đúng nghĩa sẽ hiệu quả hơn là học lại từ đầu.</p>

<h2>Khoá học 3D online hay khoá học 3D tại TPHCM</h2>

<p>Câu hỏi này bị hỏi nhiều hơn mức nó đáng. Hình thức lớp không quyết định bạn giỏi hay không. Thứ quyết định là số vòng bài của bạn được sửa và mức độ thẳng thắn của người sửa.</p>

<h3>Khi nào online là lựa chọn tốt hơn</h3>
<p>Bài nộp trong nghề này là file và ảnh, gửi đi trong vài giây. Người sửa mở file của bạn ra là thấy ngay bạn dựng sai ở đâu, không cần ngồi cạnh. Nếu bạn đã có máy chạy được và tự ngồi vào bàn được, khoá học 3D online tiết kiệm cho bạn hàng giờ đi lại mỗi tuần, và thời gian đó đổ vào luyện tập thì có lợi hơn nhiều.</p>

<h3>Khi nào nên chịu khó tới lớp</h3>
<p>Nếu bạn từng mua hai ba khoá online rồi bỏ dở, đừng mua khoá thứ tư. Vấn đề của bạn không phải nội dung mà là sự có mặt. Một lớp có địa điểm cụ thể ở TPHCM, có giờ cố định và có người nhìn thấy bạn vắng, giải quyết đúng chỗ đó. Đây là lý do duy nhất đáng để chọn học trực tiếp, và nó là lý do chính đáng.</p>

<p>Phần so sánh đầy đủ giữa hai hình thức, gồm cả chi phí đi lại và bảy câu nên hỏi, nằm trong bài <a href="blog-khoa-hoc-3d-tai-tphcm.html">khoá học 3D tại TPHCM</a>.</p>

<figure>
  <img src="assets/mercedes-g63-khung-gam-va-doi-ky-thuat.webp" alt="Khung gầm xe Mercedes G63 dựng 3D bằng Blender với nhóm kỹ thuật viên đứng quanh trong xưởng, một cảnh trích từ dự án TVC" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một cảnh trong dự án TVC dựng bằng Blender.</strong> Phần khó của cảnh này không nằm ở nút bấm mà ở việc sắp xếp thứ tự công việc: dựng khối, chia vật liệu, đặt sáng, rồi mới tới render. Một khoá học 3D Blender tử tế dạy đúng cái thứ tự đó.</figcaption>
</figure>

<h2>Học phí khoá học Blender gồm những khoản nào</h2>

<p>Mình không nêu con số vì giá mỗi nơi mỗi khác và thay đổi theo thời gian. Thứ nên soi là báo giá đó gồm gì. Bốn khoản dưới hay bị nói lướt qua.</p>

<ul>
<li><strong style="color:#fff;">Số vòng sửa trên cùng một bài.</strong> Được nhận xét một lần rồi thôi khác hẳn nhận xét, sửa, rồi nhận xét lại. Đây là khoản có giá trị thật nhất và cũng hay bị để mờ nhất.</li>
<li><strong style="color:#fff;">Ai là người sửa bài.</strong> Người đứng lớp và người chấm bài nhiều khi không phải một người. Nên hỏi thẳng.</li>
<li><strong style="color:#fff;">File gốc và tài liệu.</strong> Có nơi giao file cảnh để bạn mổ xẻ, có nơi chỉ cho xem. Mổ được file của người có nghề tiết kiệm cho bạn hàng tuần mò mẫm.</li>
<li><strong style="color:#fff;">Thời gian được hỏi sau khoá.</strong> Phần lớn vướng mắc thật xuất hiện sau khi khoá kết thúc, lúc bạn làm dự án của riêng mình.</li>
</ul>

<p>Một cách so sánh công bằng hơn giá mỗi buổi: lấy học phí chia cho số lần bài của bạn được người trong nghề xem tận nơi. Cách đọc các kiểu nói về học phí, kể cả những lời hứa nên bỏ qua, mình viết kỹ trong bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">khoá học Blender 3D ở Việt Nam</a>, còn cách quy mọi báo giá về một con số so được thì nằm trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>.</p>

<blockquote><p>Bạn không mua số buổi học. Bạn mua số lần có người nhìn vào bài của bạn và nói thẳng nó sai ở đâu. Mọi con số khác trên tờ báo giá đều là phụ.</p></blockquote>

<h2>Bốn bài nên đọc trước khi chọn khoá học 3D Blender</h2>

<p>Tuỳ bạn đang đứng ở đâu, một trong bốn bài dưới sẽ hợp hơn ba bài còn lại. Đọc đúng bài rồi hãy quyết định.</p>

<h3>Nếu bạn chưa từng mở Blender</h3>
<p>Đọc <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a>. Bài đó mô tả tám tuần đầu nên dạy gì, tuần nào nộp bài gì, và sáu câu nên hỏi trước khi đóng tiền. Nó cũng nói rõ những thứ một khoá cho người mới không nên nhồi vào, ví dụ hoạt hình nhân vật hay mô phỏng vải, vì đưa vào sớm chỉ làm bạn rối.</p>

<h3>Nếu bạn dựng được hình nhưng ảnh chưa đẹp</h3>
<p>Đọc <a href="blog-khoa-hoc-render.html">khoá học render</a>. Bài đó phân tích một khoá render phải có bốn phần nào, nên học Cycles hay Eevee trước, và năm dấu hiệu nhận ra một khoá chỉ dạy thao tác chứ không dạy cách chẩn đoán. Đây là giai đoạn nhiều người kẹt lâu nhất mà lại hay chọn sai khoá nhất.</p>

<h3>Nếu bạn muốn chắc phần dựng hình trước đã</h3>
<p>Đọc <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a>. Bài đó nêu bốn phần một khoá dựng hình phải có, thứ tự ba giai đoạn nên đi qua, và sáu dấu hiệu nhận ra một khoá dựng hình sản phẩm làm được việc. Phù hợp với người thấy mình bấm được nút nhưng gặp món đồ mới là tắc.</p>

<h3>Nếu bạn đã chắc muốn làm mảng hàng hoá và thiết bị</h3>
<p>Đọc <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a>. Bài đó nói rõ mảng này khác lớp modeling chung ở chỗ nào, bốn kỹ năng bắt buộc, lộ trình tám tuần và bảy câu hỏi lọc lớp. Hợp với người muốn đi thẳng vào nhánh dễ nhận việc nhất của 3D tại Việt Nam.</p>

<h3>Nếu bạn ở TPHCM và chưa chốt được hình thức học</h3>
<p>Đọc <a href="blog-khoa-hoc-3d-tai-tphcm.html">khoá học 3D tại TPHCM</a>. Bài đó so sánh học trực tiếp và học online theo độ trễ khi gặp lỗi, thời gian di chuyển và các khoản nằm ngoài học phí, kèm bảy câu nên hỏi trước khi chuyển khoản. Phù hợp với người đã biết mình muốn học gì nhưng còn do dự giữa hai hình thức.</p>

<h3>Nếu bạn học từ xa</h3>
<p>Đọc <a href="blog-khoa-hoc-3d-online.html">khoá học 3D online</a>. Bài đó phân biệt ba kiểu lớp từ xa, nêu bốn tiêu chí chọn lớp và cách dựng nhịp học hằng tuần, phần làm hỏng nhiều khoá online hơn cả chất lượng bài giảng.</p>

<h3>Nếu bạn đang so nhiều nơi và sợ mất tiền oan</h3>
<p>Đọc <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">khoá học Blender 3D ở Việt Nam</a>. Bài đó chia thị trường thành bốn loại, dịch các cách nói về học phí sang nghĩa thật, và đưa bảy câu hỏi mà một nơi làm ăn tử tế sẽ trả lời được ngay.</p>

<p>Ngoài ba bài trên, nếu bạn còn phân vân giữa việc bỏ tiền và tự mò, bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm</a> so sánh thẳng hai con đường, kể cả trường hợp tự học là lựa chọn đúng.</p>

<h2>Danh sách kiểm tra trước khi đóng tiền</h2>

<ol>
<li><strong style="color:#fff;">Xem bài của học viên, không xem bài của giảng viên.</strong> Bài học viên cho biết khoá dạy được gì, bài giảng viên chỉ cho biết người đó giỏi gì.</li>
<li><strong style="color:#fff;">Hỏi tuần đầu tiên nộp gì.</strong> Không trả lời cụ thể được nghĩa là chưa có lịch bài nộp.</li>
<li><strong style="color:#fff;">Hỏi một bài được nhận xét mấy vòng.</strong> Dưới hai vòng thì bạn gần như chỉ nghe giảng.</li>
<li><strong style="color:#fff;">Hỏi ai chấm bài và người đó đang làm nghề gì.</strong> Người còn làm job thật sẽ sửa khác người chỉ đi dạy.</li>
<li><strong style="color:#fff;">Đưa cấu hình máy của bạn và hỏi thẳng.</strong> Câu trả lời tử tế sẽ nói rõ phần nào chạy được, phần nào phải giảm chất lượng khi luyện.</li>
<li><strong style="color:#fff;">Hỏi khoá đi theo mảng nào.</strong> Sản phẩm, kiến trúc và automotive đòi hỏi cách làm khác nhau, khoá dạy chung chung thường không đi sâu được mảng nào.</li>
<li><strong style="color:#fff;">Hỏi sau khoá còn được hỏi bài không, trong bao lâu.</strong> Đây là khoản chênh lệch lớn giữa các nơi mà ít ai để ý.</li>
</ol>

<p>Nếu câu hỏi số năm làm bạn lo, đọc <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> trước. Trong đó có mốc cụ thể cho biết khi nào nâng cấp máy mới thật sự có nghĩa, và vì sao máy yếu hiếm khi là thứ đang cản bạn ở giai đoạn đầu.</p>

<h2>Khoá học không làm thay bạn những gì</h2>

<p>Phần này nói mặt bất lợi, vì gần như không nơi nào tự nói ra.</p>

<p>Khoá học rút ngắn thời gian mò mẫm, nó không rút ngắn thời gian luyện tay. Số giờ bạn ngồi làm vẫn phải đủ, và không ai làm hộ được. Một người học khoá tốt nhưng mỗi tuần chỉ động vào Blender một buổi sẽ đi chậm hơn người tự học mà làm đều bốn buổi.</p>

<p>Khoá học cũng không tạo ra portfolio cho bạn. Bài tập trong khoá là bài tập, người tuyển dụng nhìn ra ngay. Bộ hình đi xin việc phải có ít nhất vài dự án bạn tự đặt đề bài và tự làm trọn, kể cả phần chán như dọn file và xuất nhiều tỉ lệ khung.</p>

<p>Và khoá học không thay được việc chọn hướng. Sớm hay muộn bạn phải quyết định mình đi theo sản phẩm, kiến trúc, automotive hay sự kiện. Muốn biết mỗi hướng dẫn tới công việc gì, xem qua vài shot bên trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a>, đó là mức hoàn thiện khách thường yêu cầu.</p>

<p>Còn nếu bạn chưa chắc nên gắn với Blender hay một phần mềm khác, đọc phần <a href="blog-blender-hay-3dsmax-c4d.html">so sánh Blender, 3ds Max và Cinema 4D</a> trước khi đóng tiền bất cứ khoá nào, vì chọn sai công cụ tốn nhiều thời gian hơn chọn sai khoá.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Khoá học 3D Blender có cần biết vẽ không?</p>
<p>Không, với mảng sản phẩm, hard-surface và kiến trúc. Vẽ tay chỉ thành lợi thế rõ rệt khi bạn làm nhân vật hoặc tạo hình sáng tạo. Phần lớn công việc thương mại ở Việt Nam hiện nay không đòi hỏi kỹ năng đó.</p>

<p class="faq-q">Đang đi làm trái ngành, mỗi tuần được khoảng sáu tiếng, có theo nổi không?</p>
<p>Theo nổi, nhưng phải chấp nhận tiến độ chậm hơn lịch chuẩn. Sáu tiếng một tuần đủ để hoàn thành một bài nhỏ, không đủ để vừa học vừa làm dự án lớn. Nhóm này thường hợp với hình thức kèm riêng hơn, vì lịch linh hoạt và mỗi buổi đi thẳng vào bài của bạn, chi tiết trong bài <a href="blog-hoc-blender-kem-1-1.html">học Blender kèm một kèm một</a>.</p>

<p class="faq-q">Học xong khoá là nhận được job luôn chứ?</p>
<p>Không nên kỳ vọng như vậy. Mốc thực tế là sau khoá bạn có quy trình làm việc và vài bài đủ tốt, rồi cần thêm một giai đoạn làm dự án tự đặt đề bài trước khi có khách trả tiền. Các mốc thời gian cụ thể mình viết trong bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu thì nhận được job đầu tiên</a>.</p>

<p class="faq-q">Có nên học nhiều phần mềm cùng lúc cho chắc không?</p>
<p>Không. Học một phần mềm tới mức làm được việc rồi mới tính chuyện thứ hai. Người rải đều ba phần mềm trong năm đầu thường không dùng tốt cái nào, và thị trường tuyển người làm được việc chứ không tuyển người biết nhiều tên phần mềm.</p>

<hr class="hr">

<p>Nếu sau khi đọc bạn đã biết mình thuộc nhóm nào, xem trước hai hệ đào tạo ở trang <a href="khoa-hoc.html">khoá học Blender 3D</a>, trong đó ghi rõ lịch nộp bài và cách sửa bài. Còn nếu muốn tự thử trước khi quyết định, tải <a href="cam-nang.html">cẩm nang miễn phí</a> và làm hết phần bài tập trong đó. Ba tuần sau bạn sẽ tự biết mình cần một khoá học 3D Blender, hay chỉ cần thêm kỷ luật.</p>
""",
    },
    {
        "slug": "khoa-hoc-modeling-3d",
        "title": "Khoá học modeling 3D: học gì, theo thứ tự nào",
        "desc": "Khoá học modeling 3D nên dạy gì, học theo thứ tự nào, và sáu dấu hiệu nhận ra một khoá dựng hình sản phẩm làm được việc thay vì chỉ dạy nút bấm.",
        "tag": "Định hướng",
        "date": "2026-10-02",
        "date_vn": "02/10/2026",
        "read": "9 phút đọc",
        "thumb": "assets/vplas-ban-ve-kich-thuoc-3d.jpg",
        "faq": [
            ("Khoá học modeling 3D có cần biết vẽ tay không?",
             "Không, với mảng sản phẩm và hard surface. Thứ cần là khả năng nhìn ra khối và đọc tỉ lệ, hai thứ này luyện bằng cách đo và dựng chứ không phải bằng bút chì. Vẽ tay chỉ thành lợi thế rõ khi bạn làm nhân vật hoặc tạo hình sáng tạo."),
            ("Máy cấu hình phổ thông có học modeling được không?",
             "Được, và đây là giai đoạn dễ chịu nhất với máy yếu. Dựng khối và chỉnh lưới gần như không dùng tới card đồ hoạ mạnh. Máy chỉ thành rào cản ở bước render cảnh nặng, lúc đó bạn đã đủ hiểu để biết nên nâng cấp cái gì."),
            ("Học modeling bao lâu thì dựng được món đồ phức tạp?",
             "Ước lượng từ các nhóm học viên đã đi qua, khoảng hai tới bốn tháng làm đều để dựng gọn một món đồ gia dụng nhiều chi tiết. Con số này phụ thuộc số giờ thật sự ngồi dựng mỗi tuần nhiều hơn phụ thuộc khoá học."),
            ("Nên học modeling trước hay học render trước?",
             "Modeling trước, vì không có hình thì không có gì để chiếu sáng. Nhưng đừng đợi dựng thật giỏi mới học render. Khi bạn dựng xong được ba bốn món đồ đơn giản mà tỉ lệ đúng, đó là lúc hợp lý để bắt đầu học ánh sáng song song."),
        ],
        "body": """
<p class="lead">Một khoá học modeling 3D làm được việc dạy bạn thứ tự dựng hình trước khi dạy nút bấm: đọc khối lớn của vật thật, dựng khối đó cho đúng tỉ lệ, rồi mới cắt chi tiết và chỉ chia nhỏ lưới ở chỗ bắt buộc. Khoá nào mở đầu bằng danh sách công cụ, bạn sẽ thuộc thao tác mà vẫn đứng hình khi gặp một món đồ chưa ai dựng mẫu sẵn.</p>

<p>Bài này viết từ chỗ ngồi dựng hình sản phẩm cho khách và sửa bài cho người học mỗi tuần. Không có tên nơi nào tốt nhất, chỉ có nội dung một khoá dựng hình nên có, thứ tự học hợp lý, và những chỗ các khoá hay cắt bớt vì khó quay thành video đẹp.</p>

<h2>Khoá học modeling 3D thật ra dạy cái gì</h2>

<p>Modeling là việc biến một vật có thật, hoặc một bản vẽ, thành khối ba chiều có tỉ lệ đúng và bề mặt sạch. Nghe đơn giản nhưng phần lớn người mới hiểu sai trọng tâm: họ nghĩ mình đang học phần mềm, trong khi thứ phải học là cách nhìn.</p>

<p>Trước khi chạm chuột, người dựng hình giỏi đã tách được món đồ trước mặt thành bốn tới bảy khối cơ bản, biết khối nào là gốc và khối nào chỉ là chi tiết gắn thêm. Kỹ năng đó không nằm trong bất kỳ phím tắt nào, và nó là thứ phân biệt người dựng được mọi món đồ với người chỉ làm lại được bài giảng.</p>

<p>Nội dung tối thiểu của một khoá dựng hình nghiêm túc gồm bốn phần: đọc hình và chia khối, dựng khối chuẩn tỉ lệ, kiểm soát lưới và dòng cạnh, và dọn file để giao cho người khác dùng tiếp. Phần thứ tư hay bị bỏ, và nó là phần khiến bài của bạn bị trả lại khi đi làm thật.</p>

<p>Hai dự án sau cho thấy mức độ sạch của lưới mà một bài giao khách cần: <a href="du-an-vplas.html">dựng hình sản phẩm VPlas bằng Blender</a> với bản vẽ kỹ thuật làm gốc, và <a href="du-an-khoa-cua-thong-minh.html">bộ hình khoá cửa thông minh tách rời linh kiện</a>, nơi mỗi chi tiết bên trong đều phải dựng đủ vì ảnh tách rời không giấu được gì.</p>

<h2>Học modeling từ đâu cho đỡ mất thời gian</h2>

<p>Thứ tự dưới đây là thứ tự mình thấy ít gây tắc nhất. Nó không phải thứ tự duy nhất đúng, nhưng nó tránh được cái bẫy phổ biến nhất là nhảy vào chi tiết khi khối còn sai.</p>

<h3>Giai đoạn một, dựng khối và tỉ lệ</h3>
<p>Hai tới ba tuần đầu nên chỉ làm việc với khối hộp, khối trụ và vài phép cắt cơ bản. Đề bài tốt ở giai đoạn này là những món đồ bạn cầm được trong tay: hộp đựng, cái cốc, remote điều hoà, ổ cắm. Mục tiêu không phải đẹp, mà là tỉ lệ đo được và đúng.</p>

<p>Nếu bạn đang bắt đầu từ con số không và chưa chắc nên học gì trước, bài <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> mô tả tám tuần đầu tiên nên dạy gì và tuần nào nộp bài gì, đọc trước sẽ đỡ chọn nhầm lớp.</p>

<h3>Giai đoạn hai, dòng cạnh và bề mặt sạch</h3>
<p>Đây là chỗ nhiều người kẹt lâu nhất. Một khối trông ổn trong chế độ xem nhanh có thể vỡ hoàn toàn khi bật làm mịn, vì các cạnh chạy sai hướng. Giai đoạn này phải học cách đặt cạnh đỡ, xử lý giao tuyến giữa hai khối, và chấp nhận dựng lại từ đầu khi lưới đã rối quá mức cứu chữa.</p>

<h3>Giai đoạn ba, chi tiết và quy trình nhanh</h3>
<p>Khi khối và lưới đã chắc, lúc đó mới nói chuyện công cụ hỗ trợ. Các bộ add-on cho hard surface tiết kiệm được nhiều giờ, nhưng chúng khuếch đại cả cái đúng lẫn cái sai. Mình viết riêng về chuyện chọn và dùng chúng trong bài <a href="blog-add-on-hard-surface-blender.html">add-on hard surface cho Blender</a>, kèm cả mặt trái của việc lệ thuộc quá sớm.</p>

<figure>
  <img src="assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp" alt="Hình tách rời các linh kiện của ổ khoá cửa thông minh dựng bằng Blender, từng chi tiết bung ra theo trục thẳng đứng trên nền tối" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một hình tách rời linh kiện từ dự án khoá cửa thông minh.</strong> Kiểu hình này chỉ làm được khi từng bộ phận được dựng rời và đặt gốc toạ độ đúng ngay từ đầu. Dựng dính liền một khối thì tới bước này phải làm lại toàn bộ, và đó là lý do phần dọn file nên được dạy từ sớm chứ không để cuối khoá.</figcaption>
</figure>

<h2>Bốn kiểu khoá học modeling 3D trên thị trường</h2>

<p>Chúng khác nhau chủ yếu ở chỗ bài của bạn được nhìn kỹ bao nhiêu lần, không phải ở số buổi.</p>

<div class="table-wrap">
<table>
<thead><tr><th>Kiểu</th><th>Mạnh ở</th><th>Yếu ở</th></tr></thead>
<tbody>
<tr><td>Video quay sẵn theo bài mẫu</td><td>Rẻ, học lại được nhiều lần</td><td>Làm theo thì ra, đổi đề bài là tắc</td></tr>
<tr><td>Lớp nhóm có bài nộp hàng tuần</td><td>Có nhịp, thấy bài người khác để so</td><td>Lớp đông thì lưới của bạn không ai soi kỹ</td></tr>
<tr><td>Kèm riêng theo dự án của bạn</td><td>Sửa đúng lỗi của bạn, đi rất nhanh</td><td>Chi phí cao, phụ thuộc người kèm</td></tr>
<tr><td>Khoá chuyên dựng hình sản phẩm</td><td>Sát việc thật, có chuẩn giao file</td><td>Vào khi chưa vững khối thì đuối</td></tr>
</tbody>
</table>
</div>

<p>Người đi làm trái ngành, mỗi tuần được vài tiếng, thường hợp kiểu thứ ba hơn cả, vì mỗi buổi đi thẳng vào bài đang làm dở. Cách thức và những trường hợp không nên chọn hình thức này, mình nói kỹ trong bài <a href="blog-hoc-blender-kem-1-1.html">học Blender kèm một kèm một</a>.</p>

<blockquote><p>Dựng hình không khó vì phần mềm phức tạp. Nó khó vì bạn phải quyết định bỏ bớt cái gì. Một khoá học modeling 3D tốt dạy bạn cách quyết định đó, chứ không dạy bạn làm cho đủ mọi chi tiết.</p></blockquote>

<h2>Dấu hiệu một khoá học dựng hình sản phẩm làm được việc</h2>

<p>Danh sách này dùng để soi trước khi đóng tiền. Không cần đủ hết, nhưng thiếu quá ba mục thì nên cân nhắc lại. Phần lộ trình tám tuần và bảy câu hỏi lọc lớp nằm riêng trong bài <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a>.</p>

<ul>
<li><strong style="color:#fff;">Có bài dựng từ ảnh tham chiếu thật, không chỉ từ bản vẽ sạch.</strong> Việc thật hiếm khi có bản vẽ kỹ thuật, phần lớn chỉ có vài tấm ảnh chụp lệch góc.</li>
<li><strong style="color:#fff;">Có dạy đo và khớp tỉ lệ theo đơn vị thật.</strong> Hình sai kích thước thì mọi thứ phía sau đều sai, kể cả ánh sáng.</li>
<li><strong style="color:#fff;">Có buổi riêng về dòng cạnh và làm mịn.</strong> Nếu không có, khoá đó chỉ dạy tới mức nhìn xa thì ổn.</li>
<li><strong style="color:#fff;">Có chuẩn đặt tên, gom nhóm và đặt gốc toạ độ.</strong> Đây là phần khiến file của bạn dùng được cho người khác.</li>
<li><strong style="color:#fff;">Bài được sửa nhiều vòng trên cùng một file.</strong> Nhận xét một lần rồi chuyển bài mới là cách học chậm nhất.</li>
<li><strong style="color:#fff;">Người sửa bài có hình thương mại để bạn xem.</strong> Không phải để khoe, mà để bạn biết chuẩn họ đang nhắm tới là gì.</li>
</ul>

<p>Mục cuối đáng được nhấn thêm. Bạn có quyền xem sản phẩm của nơi dạy trước khi học, giống như xem vài shot bên trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> để biết mức hoàn thiện mà khách hàng thường yêu cầu, rồi tự đối chiếu với bài mẫu trong khoá.</p>

<h2>Modeling xong rồi thì sao</h2>

<p>Dựng hình chỉ là chặng đầu. Rất nhiều người dựng khá nhưng ảnh xuất ra vẫn nhìn rẻ, và họ tưởng mình cần học dựng thêm. Thực ra vấn đề đã chuyển sang ánh sáng, vật liệu và cách xử lý ảnh cuối.</p>

<p>Nếu bạn đang ở đúng chỗ đó, học thêm modeling là phí thời gian. Bài <a href="blog-khoa-hoc-render.html">khoá học render</a> phân tích bốn phần một khoá render phải có và năm dấu hiệu nhận ra khoá chỉ dạy thao tác. Còn nếu bạn muốn nhìn toàn cảnh các loại khoá trước khi chọn, bài tổng hợp <a href="blog-khoa-hoc-3d-blender.html">khoá học 3D Blender</a> chia thị trường thành bốn nhóm và chỉ ra nhóm nào hợp với tình trạng nào.</p>

<h2>Những thứ khoá học modeling 3D không làm thay bạn</h2>

<p>Khoá học rút ngắn thời gian mò mẫm, không rút ngắn thời gian luyện tay. Số giờ ngồi dựng vẫn phải đủ. Một người học khoá tốt mà mỗi tuần chỉ mở máy một buổi sẽ đi chậm hơn người tự học nhưng làm đều.</p>

<p>Khoá học cũng không tạo portfolio cho bạn. Bài trong khoá là bài tập, người tuyển dụng nhận ra ngay vì ai học cùng khoá cũng nộp món đồ đó. Bộ hình đi xin việc cần vài món bạn tự chọn, tự đo, tự dựng trọn, kể cả phần chán như dọn lưới và xuất nhiều tỉ lệ khung.</p>

<p>Và khoá học không chọn hướng hộ bạn. Dựng hình sản phẩm, kiến trúc, automotive hay sự kiện đòi hỏi những thói quen khác nhau. Nếu chưa rõ mình hợp hướng nào, <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> mô tả từng nhánh và các mốc kiểm tra để bạn tự đo tiến độ.</p>

<h2>Hỏi đáp nhanh</h2>

<p class="faq-q">Khoá học modeling 3D có cần biết vẽ tay không?</p>
<p>Không, với mảng sản phẩm và hard surface. Thứ cần là khả năng nhìn ra khối và đọc tỉ lệ, hai thứ này luyện bằng cách đo và dựng chứ không phải bằng bút chì. Vẽ tay chỉ thành lợi thế rõ khi bạn làm nhân vật hoặc tạo hình sáng tạo.</p>

<p class="faq-q">Máy cấu hình phổ thông có học modeling được không?</p>
<p>Được, và đây là giai đoạn dễ chịu nhất với máy yếu. Dựng khối và chỉnh lưới gần như không dùng tới card đồ hoạ mạnh. Máy chỉ thành rào cản ở bước render cảnh nặng, lúc đó bạn đã đủ hiểu để biết nên nâng cấp cái gì, chi tiết trong bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a>.</p>

<p class="faq-q">Học modeling bao lâu thì dựng được món đồ phức tạp?</p>
<p>Ước lượng từ các nhóm học viên đã đi qua, khoảng hai tới bốn tháng làm đều để dựng gọn một món đồ gia dụng nhiều chi tiết. Con số này phụ thuộc số giờ thật sự ngồi dựng mỗi tuần nhiều hơn phụ thuộc khoá học.</p>

<p class="faq-q">Nên học modeling trước hay học render trước?</p>
<p>Modeling trước, vì không có hình thì không có gì để chiếu sáng. Nhưng đừng đợi dựng thật giỏi mới học render. Khi bạn dựng xong được ba bốn món đồ đơn giản mà tỉ lệ đúng, đó là lúc hợp lý để bắt đầu học ánh sáng song song.</p>

<hr class="hr">

<p>Nếu bạn đã xác định được mình đang ở giai đoạn nào trong ba giai đoạn phía trên, xem trước hai hệ đào tạo ở trang <a href="khoa-hoc.html">khoá học Blender 3D</a>, trong đó ghi rõ bài nộp từng tuần và cách sửa bài. Còn nếu muốn tự kiểm tra trước khi quyết định, tải <a href="cam-nang.html">cẩm nang miễn phí</a> và dựng hết phần bài tập trong đó. Làm xong bạn sẽ tự biết mình cần một khoá học modeling 3D, hay chỉ cần ngồi vào bàn đều hơn.</p>
""",
    },
    {
        "slug": "khoa-hoc-3d-tai-tphcm",
        "title": "Khoá học 3D tại TPHCM: chọn offline hay online",
        "desc": "Khoá học 3D tại TPHCM học trực tiếp có thật sự hơn học online? So sánh thời gian đi lại, tốc độ sửa bài, học phí và cách kiểm tra một lớp trước khi đóng tiền.",
        "tag": "Định hướng",
        "date": "2026-10-05",
        "date_vn": "05/10/2026",
        "read": "9 phút đọc",
        "thumb": "assets/volvo-s90-goc-ben-hoang-hon.webp",
        "faq": [
            ('Khoá học 3D tại TPHCM có bắt buộc phải học trực tiếp không?',
             'Không. Nhiều nơi, gồm cả LXAM Academy, dạy cả online và trực tiếp tại TPHCM với cùng nội dung. Điều cần hỏi là lớp online có chữa bài riêng hay chỉ phát video, vì đó mới là phần tạo ra khác biệt.'),
            ('Người đi làm toàn thời gian học được không?',
             'Được, nhưng phải tính thật số giờ rảnh mỗi tuần. Ước lượng từ các nhóm đã đi qua, cần khoảng sáu tới mười giờ mỗi tuần để theo kịp một chương trình có nộp bài. Dưới mức đó, nên chọn lớp cho phép giãn tiến độ thay vì lớp có lịch cứng.'),
            ('Chưa biết vẽ thì học khoá 3D được không?',
             'Được. Dựng hình sản phẩm và phối cảnh dựa vào quan sát tỉ lệ và hình khối, không dựa vào kỹ năng vẽ tay. Bài khoá học Blender 3D cho người mới nói rõ phần nền tối thiểu thật sự cần.'),
            ('Học bao lâu thì nhận được việc?',
             'Tuỳ vào việc bạn có được sửa bài đều hay không, và tuỳ mảng bạn nhắm. Khoảng ước lượng cùng các mốc cụ thể nằm trong bài học Blender 3D bao lâu, kèm phần nói thẳng về những trường hợp lâu hơn trung bình.'),
            ('Học phí chênh nhau nhiều thì nên chọn rẻ hay đắt?',
             'Chọn theo đơn giá mỗi lần bài của bạn được chữa, không theo tổng học phí. Một khoá đắt gấp đôi nhưng chữa bài hằng tuần thường rẻ hơn tính theo giá trị thật so với một khoá rẻ chỉ phát video.'),
        ],
        "body": """
<p class="lead">Nếu bạn đang tìm khoá học 3D tại TPHCM, câu hỏi thật sự không phải trung tâm nào nổi tiếng hơn, mà là bạn có cần ngồi cùng phòng với người sửa bài hay không. Với phần lớn người mới, học trực tiếp giúp ba tháng đầu đỡ hoang mang. Từ tháng thứ tư trở đi, cái quyết định tiến độ là tần suất bài được chữa, không phải chỗ ngồi.</p>

<p>Bài này không xếp hạng trung tâm. Nó mô tả những khác biệt thật giữa hai hình thức, các khoản tiền và thời gian ít ai tính trước, và một danh sách câu hỏi bạn nên hỏi trước khi chuyển khoản. Ở LXAM Studio, chúng tôi dạy cả hai hình thức, nên bài viết cố gắng nói cả mặt bất lợi của từng bên.</p>

<h2>Khoá học 3D tại TPHCM: học trực tiếp được gì</h2>

<p>Lợi thế lớn nhất của một lớp 3D offline ở Sài Gòn không phải máy phòng lab, mà là độ trễ khi bạn gặp lỗi. Người mới thường kẹt ở những chỗ rất nhỏ: một modifier bật sai thứ tự, một scale chưa apply, một đèn đặt ngoài vùng ảnh hưởng. Tự tìm có thể mất một buổi. Người ngồi cạnh nhìn màn hình thì mất ba mươi giây.</p>

<h3>Thứ hai: nhịp học bị ép</h3>
<p>Có lịch tới lớp nghĩa là mỗi tuần bạn buộc phải mở Blender ít nhất một lần, dù tuần đó công việc có bận. Nghe đơn giản nhưng đây mới là lý do nhiều người học offline đi xa hơn người học online, chứ không phải vì bài giảng hay hơn.</p>

<h3>Thứ ba: thấy người khác làm</h3>
<p>Ngồi trong lớp, bạn thấy cách bạn bên cạnh xoay viewport, gán vật liệu, sửa topology. Những thao tác đó không ai dạy thành bài, nhưng chúng là phần lớn tốc độ làm việc về sau.</p>

<p>Phần lớn job 3D ở TPHCM đi theo mùa sự kiện và mùa ra mắt sản phẩm. <a href="du-an-chivas-15-trung-bay.html">Bộ phối cảnh kệ trưng bày Chivas 15</a> là dạng việc hay gặp nhất: dựng nhiều phương án cho cùng một hạng mục để bên thi công chọn, chứ không phải một tấm hình đẹp duy nhất.</p>

<h2>Học online được gì mà offline không có</h2>

<p>Mặt ngược lại cũng thật. Một khoá học 3D online chấm bài đều đặn có ba thứ mà lớp trực tiếp khó bù.</p>

<p><strong style="color:#fff;">Bạn học trên máy của mình.</strong> Đây là điểm bị coi nhẹ nhất. Học trên máy phòng lab rồi về nhà mở máy yếu hơn là lúc nhiều người bỏ cuộc, vì cảnh render ở lớp mượt mà ở nhà thì treo. Nếu chưa rõ máy mình đủ hay không, xem trước phần <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> rồi hãy tính chuyện đăng ký.</p>

<p><strong style="color:#fff;">Bạn xem lại được.</strong> Lighting và render là hai khâu phải nghe lại nhiều lần mới ngấm. Lớp trực tiếp giảng một lần, bạn ghi được bao nhiêu thì còn bấy nhiêu.</p>

<p>Ba lợi thế trên chỉ thành hiện thực khi khoá từ xa có chữa bài và có hạn nộp. Cách phân biệt ba kiểu lớp và danh sách câu hỏi trước khi đăng ký nằm trong bài <a href="blog-khoa-hoc-3d-online.html">khoá học 3D online</a>.</p>

<p><strong style="color:#fff;">Bạn không mất thời gian đi lại.</strong> Ở TPHCM, hai buổi mỗi tuần vào giờ tan tầm thường tốn một tiếng rưỡi tới hai tiếng di chuyển cho mỗi buổi. Một khoá bốn tháng là khoảng năm mươi tới sáu mươi giờ ngồi xe. Số giờ đó, nếu đổ vào dựng hình, đủ để làm xong hai ba món trong portfolio.</p>

<blockquote><p>Lớp trực tiếp bán cho bạn sự tập trung. Lớp online bán cho bạn thời gian. Cái nào đáng hơn phụ thuộc vào thứ bạn đang thiếu.</p></blockquote>

<h2>Bảng so sánh hai hình thức</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Học trực tiếp tại TPHCM</th><th>Học online có chữa bài</th></tr></thead>
<tbody>
<tr><td>Độ trễ khi gặp lỗi</td><td>Gần như tức thì trong buổi học</td><td>Vài giờ tới một ngày, tuỳ cam kết của lớp</td></tr>
<tr><td>Thời gian di chuyển</td><td>Ước lượng 50 đến 60 giờ cho khoá 4 tháng</td><td>Không</td></tr>
<tr><td>Máy thực hành</td><td>Máy lớp, có thể khác máy ở nhà</td><td>Máy của bạn, đúng điều kiện thật</td></tr>
<tr><td>Xem lại bài</td><td>Phụ thuộc ghi chú của bạn</td><td>Xem lại không giới hạn nếu có bản ghi</td></tr>
<tr><td>Nhịp học</td><td>Bị ép theo lịch, dễ giữ đều</td><td>Tự giữ, dễ trôi nếu không có deadline nộp bài</td></tr>
<tr><td>Chi phí ngoài học phí</td><td>Đi lại, ăn uống, đôi khi gửi xe</td><td>Internet, có thể phải nâng cấp máy</td></tr>
<tr><td>Phù hợp nhất với</td><td>Người mới hoàn toàn, người khó tự kỷ luật</td><td>Người đi làm, người ở xa, người đã biết cơ bản</td></tr>
</tbody>
</table>
</div>

<p>Nhìn bảng này sẽ thấy hai hình thức không hơn kém nhau tuyệt đối. Chúng phục vụ hai loại vấn đề khác nhau. Nếu bạn còn chưa chắc mình thuộc loại nào, bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm</a> mô tả dấu hiệu nhận biết cụ thể hơn.</p>

<figure>
  <img src="assets/mercedes-g63-khung-gam-va-doi-ky-thuat.webp" alt="Khung gầm và cụm chi tiết kỹ thuật xe Mercedes G63 dựng bằng Blender, hiển thị dạng wireframe trên nền tối" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một cụm kỹ thuật trong dự án Mercedes G63 của LXAM Studio.</strong> Những bài như thế này là lúc khác biệt giữa có người chữa bài và không có hiện rõ nhất, vì lỗi nằm ở cách tổ chức khối chứ không ở thao tác.</figcaption>
</figure>

<h2>Học phí và những khoản ít ai tính trước</h2>

<p>Chúng tôi không nêu con số cụ thể của các đơn vị khác, vì học phí thay đổi theo thời điểm và theo việc lớp có chữa bài hay không. Thay vào đây là cách tính cho đủ, để bạn so sánh táo với táo.</p>

<p>Cách tính đầy đủ, kèm bốn khoản nằm ngoài hoá đơn, mình viết riêng trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>. Rút gọn lại: khi hỏi học phí, hãy quy về ba con số: tổng tiền, số buổi có người sửa bài trực tiếp cho bài của bạn, và số bài bạn phải nộp. Một khoá rẻ mà chỉ chiếu video rồi hỏi đáp chung thì đơn giá mỗi lần được chữa bài cao hơn nhiều so với một khoá đắt hơn nhưng sửa bài hằng tuần.</p>

<h3>Các khoản nằm ngoài hoá đơn</h3>
<ul>
<li>Thời gian đi lại, nếu học offline. Quy ra giờ rồi tự định giá giờ của bạn.</li>
<li>Nâng cấp máy, nếu cấu hình hiện tại không kham được khâu render.</li>
<li>Ổ cứng và sao lưu. File 3D phình nhanh hơn người mới tưởng.</li>
<li>Thời gian làm bài ở nhà. Phần này luôn lớn hơn số giờ trên lớp, bất kể hình thức nào.</li>
</ul>

<p>Nếu bạn muốn tự ước lượng trước khi tốn tiền, tải <a href="cam-nang.html">cẩm nang Blender miễn phí</a> và làm hết phần bài tập trong đó. Làm xong, bạn sẽ biết mình thiếu bài giảng hay chỉ thiếu thời gian ngồi vào bàn. Hai thứ đó cần hai giải pháp khác nhau.</p>

<h2>Danh sách kiểm tra trước khi đóng tiền</h2>

<p>Dùng được cho cả lớp offline ở TPHCM và lớp online. Hỏi thẳng, nơi dạy tử tế sẽ trả lời thẳng.</p>

<ul>
<li>Mỗi tuần tôi nộp mấy bài, và bài của tôi được chữa riêng hay nhận xét chung cho cả lớp?</li>
<li>Người chữa bài có đang làm dự án thật không, và tôi xem được dự án đó ở đâu?</li>
<li>Kết thúc khoá, tôi có bao nhiêu món hoàn chỉnh đủ đưa vào portfolio?</li>
<li>Nếu nghỉ một buổi thì học bù thế nào, có bản ghi hay không?</li>
<li>Lớp dạy cả khâu render và hậu kỳ, hay dừng ở dựng hình?</li>
<li>Có yêu cầu cấu hình máy tối thiểu nào không?</li>
<li>Xem được một bài đã chữa của học viên cũ không, kèm phần nhận xét?</li>
</ul>

<p>Câu cuối là câu lọc mạnh nhất. Một nơi có chữa bài thật thì luôn có sẵn ví dụ để đưa bạn xem. Trang <a href="hoc-vien.html">bài tập học viên</a> của chúng tôi là ví dụ về dạng bằng chứng bạn nên đòi ở bất cứ đâu bạn định học.</p>

<h2>Ai nên học offline, ai nên học online</h2>

<p>Chọn lớp trực tiếp nếu bạn chưa từng mở Blender, nếu bạn biết rõ mình hay bỏ giữa đường khi không có lịch, hoặc nếu bạn ở trong bán kính di chuyển dưới bốn mươi phút. Ba tháng đầu, việc có người ngồi cạnh tiết kiệm rất nhiều buổi loay hoay vô ích.</p>

<p>Chọn lớp online nếu bạn đang đi làm với giờ không cố định, nếu bạn ở xa trung tâm, hoặc nếu bạn đã dựng được vài món và cái đang thiếu là người chẩn đoán chỗ kẹt. Giai đoạn này, hình thức <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> thường hiệu quả hơn cả lớp đông, dù online hay offline.</p>

<p>Và một lựa chọn ít người nghĩ tới: học trực tiếp giai đoạn đầu để lấy nền và nhịp, rồi chuyển sang online khi đã tự đi được. Cách này giữ được ưu điểm của cả hai mà không phải trả giá cho nhược điểm của bên nào quá lâu.</p>

<h2>Lộ trình gợi ý nếu bạn đang ở TPHCM</h2>

<p>Bốn bước, theo đúng thứ tự này.</p>

<p><strong style="color:#fff;">Một.</strong> Xác định mục tiêu nghề trước khi chọn lớp. Dựng hình sản phẩm, phối cảnh sự kiện và TVC ô tô đòi ba bộ kỹ năng khác nhau. Chọn lớp trước khi chọn mục tiêu là cách chắc chắn nhất để học xong vẫn không biết nộp portfolio đi đâu.</p>

<p><strong style="color:#fff;">Hai.</strong> Làm hết phần bài tập trong cẩm nang. Mất một đến hai tuần, và nó loại bỏ phần lớn rủi ro chọn sai.</p>

<p><strong style="color:#fff;">Ba.</strong> Đi qua danh sách bảy câu hỏi ở trên với hai hoặc ba nơi bạn đang nhắm. So tổng tiền chia cho số lần được chữa bài, không so học phí thuần.</p>

<p><strong style="color:#fff;">Bốn.</strong> Chốt hình thức theo hoàn cảnh thật của bạn, không theo lời khuyên chung. Người ở Thủ Đức đi học ở quận 1 vào giờ cao điểm sẽ bỏ lớp sau tháng thứ hai, bất kể lớp đó tốt cỡ nào.</p>

<p>Nếu bạn muốn xem một ví dụ cụ thể về cách một chương trình được chia theo tuần, xem hai hệ ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>, trong đó ghi rõ bài nộp từng tuần và cách chữa bài. Còn nếu bạn đang nhắm khâu kết xuất là điểm yếu lớn nhất, đọc thêm bài <a href="blog-khoa-hoc-render.html">khoá học render</a> trước khi quyết định.</p>

<h2>Hỏi đáp</h2>

<p class="faq-q">Khoá học 3D tại TPHCM có bắt buộc phải học trực tiếp không?</p>
<p>Không. Nhiều nơi, gồm cả LXAM Academy, dạy cả online và trực tiếp tại TPHCM với cùng nội dung. Điều cần hỏi là lớp online có chữa bài riêng hay chỉ phát video, vì đó mới là phần tạo ra khác biệt.</p>

<p class="faq-q">Người đi làm toàn thời gian học được không?</p>
<p>Được, nhưng phải tính thật số giờ rảnh mỗi tuần. Ước lượng từ các nhóm đã đi qua, cần khoảng sáu tới mười giờ mỗi tuần để theo kịp một chương trình có nộp bài. Dưới mức đó, nên chọn lớp cho phép giãn tiến độ thay vì lớp có lịch cứng.</p>

<p class="faq-q">Chưa biết vẽ thì học khoá 3D được không?</p>
<p>Được. Dựng hình sản phẩm và phối cảnh dựa vào quan sát tỉ lệ và hình khối, không dựa vào kỹ năng vẽ tay. Bài <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> nói rõ phần nền tối thiểu thật sự cần.</p>

<p class="faq-q">Học bao lâu thì nhận được việc?</p>
<p>Tuỳ vào việc bạn có được sửa bài đều hay không, và tuỳ mảng bạn nhắm. Khoảng ước lượng cùng các mốc cụ thể nằm trong bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a>, kèm phần nói thẳng về những trường hợp lâu hơn trung bình.</p>

<p class="faq-q">Học phí chênh nhau nhiều thì nên chọn rẻ hay đắt?</p>
<p>Chọn theo đơn giá mỗi lần bài của bạn được chữa, không theo tổng học phí. Một khoá đắt gấp đôi nhưng chữa bài hằng tuần thường rẻ hơn tính theo giá trị thật so với một khoá rẻ chỉ phát video.</p>

<hr class="hr">

<p>Nếu bạn đang ở TPHCM và chưa chốt được hình thức, cứ nhắn mô tả hoàn cảnh của bạn: giờ rảnh mỗi tuần, khoảng cách di chuyển, máy đang dùng và mảng bạn nhắm. Chúng tôi nói thẳng là nên học trực tiếp, học online, hay chưa nên đóng tiền cho khoá nào cả mà cứ tải <a href="cam-nang.html">cẩm nang</a> làm trước một tháng. Không cần đăng ký gì.</p>
""",
    },
    {
        "slug": "hoc-phi-khoa-hoc-blender",
        "title": "Học phí khoá học Blender: tính sao cho đúng",
        "desc": "Học phí khoá học Blender chênh nhau rất xa. Cách quy mọi báo giá về đơn giá mỗi lần được chữa bài, bốn khoản nằm ngoài hoá đơn và câu hỏi lọc lớp kém.",
        "tag": "Định hướng",
        "date": "2026-10-07",
        "date_vn": "07/10/2026",
        "read": "9 phút đọc",
        "thumb": "assets/jhm-chu-thich-lo-vua.webp",
        "faq": [
            ('Học phí khoá học Blender khoảng bao nhiêu là hợp lý?',
             'Không có mức chung, vì một khoá phát video và một khoá chữa bài hằng tuần là hai sản phẩm khác nhau. Thay vì tìm mức hợp lý, hãy lấy tổng học phí chia cho số lần bài của bạn được chữa riêng, rồi so các báo giá bằng con số đó.'),
            ('Blender miễn phí thì sao vẫn phải trả học phí?',
             'Vì bạn trả cho thời gian của người chữa bài và cho cơ chế buộc bạn nộp bài đều, không trả cho phần mềm. Nếu bạn đã có khả năng tự kỷ luật và tự chẩn đoán lỗi, tài liệu miễn phí hoàn toàn đủ.'),
            ('Khoá đắt có chắc tốt hơn khoá rẻ không?',
             'Không chắc. Giá cao chỉ hợp lý khi nó mua được thời lượng dành riêng cho bạn. Một khoá đắt mà vẫn bốn mươi người một lớp và nhận xét chung thì chỉ là khoá rẻ bán giá cao.'),
            ('Có nên trả góp hoặc đóng theo từng phần?',
             'Nếu nơi dạy cho đóng theo chặng, đó thường là dấu hiệu tốt vì họ chịu rủi ro cùng bạn. Hỏi rõ điều kiện dừng giữa khoá trước khi ký, và đọc kỹ phần hoàn tiền.'),
            ('Học xong khoá là làm được việc ngay chứ?',
             'Thường là không ngay. Khoảng thời gian thực tế tới mức nhận được việc, cùng các mốc cụ thể, nằm trong bài học Blender 3D bao lâu. Bất cứ nơi nào cam kết có việc ngay sau khoá đều nên bị hỏi lại rất kỹ.'),
        ],
        "body": """
<p class="lead">Học phí khoá học Blender ở Việt Nam chênh nhau tới vài lần cho những lớp nghe mô tả gần giống nhau, nên so tổng tiền là cách so sai. Con số đáng nhìn là đơn giá mỗi lần bài của bạn được chữa riêng, cộng với số món hoàn chỉnh bạn mang ra khỏi khoá. Tính theo hai chỉ số đó, một lớp đắt gấp đôi thường lại rẻ hơn.</p>

<p>Bài này không nêu học phí của bất kỳ đơn vị nào, kể cả của chúng tôi, vì giá thay đổi theo thời điểm và theo việc lớp có chữa bài hay không. Thứ bài viết cung cấp là một cách tính bạn có thể áp lên mọi báo giá bạn nhận được, kèm bốn khoản chi phí hầu như không ai nhắc trước khi bạn chuyển khoản.</p>

<h2>Vì sao học phí khoá học Blender chênh nhau quá xa</h2>

<p>Blender miễn phí, nên toàn bộ tiền bạn trả là tiền mua thời gian của người dạy và cơ chế phản hồi. Ba mô hình dưới đây có cấu trúc chi phí hoàn toàn khác nhau, và đó là nguồn gốc của mọi khoảng cách giá.</p>

<h3>Lớp phát video, hỏi đáp chung</h3>
<p>Chi phí biên gần như bằng không, thêm một học viên không làm người dạy mất thêm giờ nào. Giá rẻ là hợp lý. Đổi lại, không ai xem cụ thể file của bạn.</p>

<h3>Lớp đông có chữa bài theo nhóm</h3>
<p>Người dạy phải mở bài thật, nhưng nhận xét được phát cho cả lớp. Giá trung bình. Phần bạn nhận được phụ thuộc vào việc bài của bạn có được chọn làm ví dụ hay không.</p>

<h3>Kèm riêng hoặc lớp rất nhỏ</h3>
<p>Mỗi giờ của người dạy chỉ phục vụ một hoặc vài người, nên giá cao nhất và đó là mức giá đúng. Mô hình này giải quyết được chỗ kẹt riêng của bạn, thứ mà video không bao giờ chạm tới. Phần so sánh chi tiết nằm trong bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm</a>.</p>

<blockquote><p>Bạn không mua bài giảng. Bài giảng về Blender trên mạng đã đủ nhiều và phần lớn là miễn phí. Bạn mua việc có người nhìn vào file của bạn và nói đúng chỗ sai.</p></blockquote>

<h2>Cách quy mọi báo giá về một con số so được</h2>

<p>Khi nhận báo giá, đừng ghi lại tổng tiền. Ghi lại bốn thứ: tổng học phí, số lần bài của chính bạn được chữa riêng trong cả khoá, số bài bắt buộc phải nộp, và số món hoàn chỉnh dự kiến có sau khoá. Rồi lấy tổng học phí chia cho số lần được chữa bài.</p>

<p>Con số đó là đơn giá phản hồi. Nó cho thấy vì sao hai lớp cùng giá có thể khác nhau hoàn toàn: một lớp mười hai tuần chữa bài hằng tuần cho đơn giá bằng một phần sáu so với một lớp cùng giá chỉ chữa bài hai lần ở giữa và cuối khoá.</p>

<h3>Chỉ số thứ hai: số món hoàn chỉnh</h3>
<p>Thứ xin việc được là portfolio, không phải chứng chỉ. Một khoá cho ra ba món hoàn chỉnh đủ đăng, kể cả khi đắt hơn, vẫn đáng hơn một khoá cho ra mười hai bài tập dở dang. Hỏi thẳng câu này trước khi đóng tiền, và đòi xem ví dụ thật. Trang <a href="hoc-vien.html">bài tập học viên</a> của chúng tôi là dạng bằng chứng bạn nên yêu cầu ở bất cứ nơi nào bạn định học.</p>

<h2>Bảng so sánh ba mô hình theo chi phí thật</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Khoá video, hỏi đáp chung</th><th>Lớp đông có chữa bài nhóm</th><th>Kèm riêng hoặc lớp rất nhỏ</th></tr></thead>
<tbody>
<tr><td>Mức học phí tương đối</td><td>Thấp nhất</td><td>Trung bình</td><td>Cao nhất</td></tr>
<tr><td>Bài của bạn được xem riêng</td><td>Không, hoặc rất hạn chế</td><td>Có, nhưng nhận xét chung cho lớp</td><td>Có, từng bài</td></tr>
<tr><td>Đơn giá mỗi lần được chữa bài</td><td>Rất cao vì số lần gần bằng không</td><td>Trung bình</td><td>Thường thấp nhất tính theo giá trị</td></tr>
<tr><td>Rủi ro bỏ giữa đường</td><td>Cao nhất, không ai nhắc bạn nộp bài</td><td>Trung bình</td><td>Thấp nhất</td></tr>
<tr><td>Phù hợp khi</td><td>Bạn đã có nền và chỉ cần tài liệu</td><td>Bạn mới bắt đầu, cần nhịp và bạn học</td><td>Bạn đang kẹt ở một khâu cụ thể</td></tr>
<tr><td>Thứ thường thiếu</td><td>Chẩn đoán chỗ sai của riêng bạn</td><td>Thời lượng dành riêng cho bạn</td><td>Môi trường có người cùng học</td></tr>
</tbody>
</table>
</div>

<p>Bảng này không nói mô hình nào tốt nhất. Nó nói rằng mức giá phản ánh thứ bạn nhận được, và sai lầm phổ biến nhất là trả tiền cho mô hình rẻ khi vấn đề của bạn chỉ mô hình đắt mới giải được. Nếu bạn còn chưa rõ mình đang thiếu gì, hai bài <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a> và <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> mô tả cụ thể phần nền và thứ tự học tối thiểu.</p>

<figure>
  <img src="assets/jhm-chu-thich-thep-ma-kem.webp" alt="Render kỹ thuật chi tiết giá treo xây dựng JHM với các đường chú thích mô tả lớp thép mạ kẽm" loading="lazy" width="1800" height="1012">
  <figcaption><strong>Một bản chú thích kỹ thuật trong dự án JHM của LXAM Studio.</strong> Dạng bài này là lý do học phí có người chữa bài khác học phí xem video: lỗi nằm ở cách đọc bản vẽ và tổ chức khối, không ở thao tác nào có thể chiếu lên màn hình.</figcaption>
</figure>

<h2>Bốn khoản nằm ngoài hoá đơn</h2>

<p>Đây là phần làm vỡ ngân sách của nhiều người, vì không nơi nào ghi vào báo giá.</p>

<p><strong style="color:#fff;">Máy tính.</strong> Khoản lớn nhất và dễ bị bỏ sót nhất. Nếu máy hiện tại không kham được khâu kết xuất, bạn sẽ phải nâng cấp giữa khoá, đúng lúc đang tốn học phí. Kiểm tra trước bằng bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a>, trong đó có phần nói rõ mức nào đủ và mức nào chỉ là mong muốn.</p>

<p><strong style="color:#fff;">Thời gian của bạn.</strong> Số giờ làm bài ở nhà luôn lớn hơn số giờ trên lớp. Ước lượng từ các nhóm đã đi qua là khoảng sáu tới mười giờ mỗi tuần để theo kịp một chương trình có nộp bài. Quy số giờ đó ra giá trị giờ của bạn rồi cộng vào, bạn sẽ thấy học phí thường là phần nhỏ trong tổng đầu tư.</p>

<p><strong style="color:#fff;">Lưu trữ và sao lưu.</strong> File 3D phình nhanh. Một dự án sản phẩm có texture độ phân giải cao dễ chiếm vài chục gigabyte. Mất file giữa khoá là mất cả tiền và tinh thần.</p>

<p>Nếu bạn định học từ xa để cắt khoản đi lại, lưu ý rằng khoản tiết kiệm đó chỉ có giá trị khi bạn đi hết khoá. Phần rủi ro bỏ giữa chừng và cách phòng được viết trong bài <a href="blog-khoa-hoc-3d-online.html">khoá học 3D online</a>.</p>

<p><strong style="color:#fff;">Chi phí đi lại, nếu học trực tiếp.</strong> Ở TPHCM, hai buổi mỗi tuần vào giờ tan tầm là khoảng năm mươi tới sáu mươi giờ ngồi xe cho một khoá bốn tháng. Phần tính chi tiết nằm trong bài <a href="blog-khoa-hoc-3d-tai-tphcm.html">khoá học 3D tại TPHCM</a>.</p>

<h2>Danh sách kiểm tra trước khi chuyển khoản</h2>

<p>Mười câu, dùng được cho mọi mức giá. Nơi dạy tử tế trả lời thẳng cả những câu bất lợi cho họ.</p>

<ul>
<li>Tổng học phí gồm những gì, có khoản nào phát sinh sau không?</li>
<li>Trong cả khoá, bài của riêng tôi được chữa bao nhiêu lần?</li>
<li>Chữa bài là nhận xét riêng cho file của tôi, hay nhận xét chung trước lớp?</li>
<li>Kết thúc khoá tôi có bao nhiêu món hoàn chỉnh đủ đưa vào portfolio?</li>
<li>Người chữa bài có đang làm dự án thật không, xem dự án đó ở đâu?</li>
<li>Lớp có bao nhiêu người, và tỉ lệ một người dạy trên bao nhiêu học viên?</li>
<li>Nghỉ một buổi thì học bù thế nào, có bản ghi hay không?</li>
<li>Khoá dạy tới đâu: dừng ở dựng hình, hay có cả vật liệu, ánh sáng và kết xuất?</li>
<li>Yêu cầu cấu hình máy tối thiểu là gì?</li>
<li>Có chính sách hoàn tiền hoặc đổi lớp nếu tôi thấy không phù hợp sau vài buổi đầu không?</li>
</ul>

<p>Câu thứ tư và câu thứ năm là hai câu lọc mạnh nhất. Một nơi dạy có kết quả thật thì luôn sẵn ví dụ để đưa bạn xem, cả bài tốt lẫn bài còn yếu kèm phần nhận xét.</p>

<h2>Khi nào chưa nên đóng học phí cho bất kỳ khoá nào</h2>

<p>Nói thẳng, có những trường hợp đóng tiền lúc này là lãng phí.</p>

<p>Nếu bạn chưa mở Blender lần nào và chưa chắc mình thật sự thích công việc này, hãy tải <a href="cam-nang.html">cẩm nang Blender miễn phí</a> và làm hết phần bài tập trong đó trước. Mất một đến hai tuần, không tốn đồng nào, và nó loại bỏ phần lớn rủi ro chọn sai khoá.</p>

<p>Nếu bạn đã dựng được vài món nhưng không biết chúng yếu ở đâu, vấn đề của bạn là chẩn đoán, không phải bài giảng. Một khoá đại trà sẽ dạy lại thứ bạn đã biết. Hình thức <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> hợp hơn, và tính theo đơn giá phản hồi thì thường còn rẻ hơn.</p>

<p>Nếu bạn chưa biết mình đang đứng ở đâu trong chuỗi kỹ năng, soi lại <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> bảy bước trước đã. Biết mình kẹt ở bước nào thì mới chọn đúng loại khoá, và đôi khi hoá ra bạn chỉ cần thêm một tháng tự luyện chứ chưa cần đóng tiền.</p>

<p>Nếu tuần nào bạn cũng chỉ còn dưới ba giờ rảnh, hãy để dành tiền. Không có mức học phí nào bù được việc không ngồi vào bàn. Đợi tới giai đoạn đời sống cho phép sáu tới mười giờ mỗi tuần rồi hãy đăng ký.</p>

<h2>Học phí khoá học Blender nên được nhìn như một khoản đầu tư có kỳ hạn</h2>

<p>Cách lành mạnh nhất để quyết định là đặt câu hỏi ngược: sau sáu tháng, thứ gì chứng minh khoản tiền này đáng. Nếu câu trả lời là một tấm chứng chỉ, bạn đang trả tiền cho thứ thị trường không chấm. Nếu câu trả lời là ba món trong portfolio, một quy trình làm việc lặp lại được và khả năng tự chẩn đoán lỗi, thì mức học phí cao hơn hoàn toàn chính đáng.</p>

<p>Mức lương và nhu cầu tuyển của mảng này ở Việt Nam được mô tả theo khoảng trong trang <a href="nghe-nghiep.html">nghề 3D artist</a>, kèm phần nói rõ đó là ước lượng chứ không phải số liệu chính thức. Đọc trang đó cùng với bài này sẽ cho bạn một bài toán hoàn chỉnh hơn, thay vì chỉ nhìn con số học phí trần trụi.</p>

<h2>Hỏi đáp</h2>

<p class="faq-q">Học phí khoá học Blender khoảng bao nhiêu là hợp lý?</p>
<p>Không có mức chung, vì một khoá phát video và một khoá chữa bài hằng tuần là hai sản phẩm khác nhau. Thay vì tìm mức hợp lý, hãy lấy tổng học phí chia cho số lần bài của bạn được chữa riêng, rồi so các báo giá bằng con số đó.</p>

<p class="faq-q">Blender miễn phí thì sao vẫn phải trả học phí?</p>
<p>Vì bạn trả cho thời gian của người chữa bài và cho cơ chế buộc bạn nộp bài đều, không trả cho phần mềm. Nếu bạn đã có khả năng tự kỷ luật và tự chẩn đoán lỗi, tài liệu miễn phí hoàn toàn đủ.</p>

<p class="faq-q">Khoá đắt có chắc tốt hơn khoá rẻ không?</p>
<p>Không chắc. Giá cao chỉ hợp lý khi nó mua được thời lượng dành riêng cho bạn. Một khoá đắt mà vẫn bốn mươi người một lớp và nhận xét chung thì chỉ là khoá rẻ bán giá cao.</p>

<p class="faq-q">Có nên trả góp hoặc đóng theo từng phần?</p>
<p>Nếu nơi dạy cho đóng theo chặng, đó thường là dấu hiệu tốt vì họ chịu rủi ro cùng bạn. Hỏi rõ điều kiện dừng giữa khoá trước khi ký, và đọc kỹ phần hoàn tiền.</p>

<p class="faq-q">Học xong khoá là làm được việc ngay chứ?</p>
<p>Thường là không ngay. Khoảng thời gian thực tế tới mức nhận được việc, cùng các mốc cụ thể, nằm trong bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a>. Bất cứ nơi nào cam kết có việc ngay sau khoá đều nên bị hỏi lại rất kỹ.</p>

<hr class="hr">

<p>Nếu bạn đang cầm hai ba báo giá và không biết chọn cái nào, cứ gửi cho chúng tôi mô tả từng lớp: số buổi, số người, số lần chữa bài và số bài nộp. Chúng tôi sẽ nói thẳng cái nào có đơn giá phản hồi tốt hơn, kể cả khi câu trả lời là không nên học ở đâu cả mà cứ tải <a href="cam-nang.html">cẩm nang</a> làm trước một tháng. Muốn xem cách một chương trình chia bài theo tuần trông thế nào, hai hệ ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a> ghi rõ bài nộp và cách chữa bài từng tuần.</p>
""",
    },
    {
        "slug": "khoa-hoc-3d-online",
        "title": "Khoá học 3D online: chọn và theo tới cùng",
        "desc": "Khoá học 3D online tiện nhưng tỉ lệ bỏ giữa chừng rất cao. Bốn tiêu chí chọn lớp từ xa, cách dựng nhịp học mỗi tuần và danh sách kiểm tra trước khi đóng tiền.",
        "tag": "Định hướng",
        "date": "2026-10-09",
        "date_vn": "09/10/2026",
        "read": "9 phút đọc",
        "thumb": "assets/vplas-lot-xac.webp",
        "faq": [
            ('Khoá học 3D online có hiệu quả bằng học trực tiếp không?',
             'Hiệu quả tương đương nếu khoá đó có người chữa bài riêng và có hạn nộp. Nếu chỉ là thư viện video, hiệu quả thấp hơn rõ rệt, không phải vì nội dung kém mà vì phần lớn người học dừng lại trước khi hết khoá.'),
            ('Tôi ở tỉnh, đường truyền không mạnh thì học được không?',
             'Được. Phần nặng là kết xuất chạy trên máy bạn chứ không qua mạng. Thứ cần đủ chỉ là gọi video và chia sẻ màn hình. Hỏi trước xem lớp có bản ghi lại để xem lại khi mạng chập chờn không.'),
            ('Máy yếu có nên đăng ký khoá online trước rồi nâng cấp sau?',
             'Không nên. Nâng cấp giữa khoá là lúc tốn kém và mất mạch nhất. Kiểm tra cấu hình trước, và nếu chưa đủ thì lùi lịch học lại một tháng thay vì vừa học vừa chờ máy.'),
            ('Học online bao lâu thì nhận được việc?',
             'Không khác học trực tiếp, vì thị trường chấm portfolio chứ không chấm hình thức học. Các mốc thời gian thực tế nằm trong bài học Blender 3D bao lâu. Nơi nào cam kết có việc ngay sau khoá đều nên bị hỏi lại rất kỹ.'),
            ('Nên chọn lớp trực tuyến hay kèm riêng qua màn hình?',
             'Nếu bạn mới bắt đầu và cần nhịp, chọn lớp trực tuyến theo lịch. Nếu bạn đã làm được vài món và đang kẹt ở một khâu, kèm riêng kết thúc nhanh hơn và tính theo số lần được chữa bài thì thường rẻ hơn.'),
        ],
        "body": """
<p class="lead">Một khoá học 3D online tốt hay dở không nằm ở chất lượng video, mà nằm ở việc có người mở file của bạn ra xem hay không. Học từ xa làm mất hai thứ mà lớp trực tiếp cho sẵn: nhịp đi học cố định và ánh mắt người ngồi cạnh. Chọn đúng khoá online nghĩa là chọn khoá có cơ chế bù lại đúng hai thứ đó, chứ không phải khoá nhiều bài giảng nhất.</p>

<p>Bài này viết cho người ở xa TPHCM, người đi làm giờ giấc thất thường, hoặc người đã thử một khoá online rồi bỏ dở và không hiểu vì sao. Chúng tôi nói cả phần bất lợi, kể cả khi phần bất lợi đó nằm ở hình thức mà chúng tôi cũng đang dạy.</p>

<h2>Khoá học 3D online khác khoá trực tiếp ở chỗ nào</h2>

<p>Khác biệt thật không nằm ở màn hình. Nội dung Blender dạy qua webcam hay dạy trong phòng đều giống nhau. Ba thứ dưới đây mới là chỗ hai hình thức tách khỏi nhau.</p>

<h3>Nhịp học biến mất</h3>
<p>Lớp trực tiếp có giờ cố định và quãng đường đi lại, hai thứ đó tạo ra cam kết. Khoá online bỏ cả hai, nên buổi học trở thành thứ dễ dời nhất trong tuần. Dời ba lần là mất mạch, mất mạch thường là bỏ hẳn.</p>

<h3>Phản hồi bị chậm một nhịp</h3>
<p>Trong phòng, người dạy liếc qua màn hình của bạn là thấy ngay topology đang hỏng. Học từ xa, bạn phải tự nhận ra có gì đó sai, chụp lại, mô tả, gửi đi, rồi chờ. Khoảng chờ đó là nơi người mới nản nhất.</p>

<h3>Đổi lại, bạn được ba thứ thật</h3>
<p>Không mất giờ đi lại, chọn được người dạy ngoài thành phố mình sống, và xem lại được bản ghi lúc làm bài lúc nửa đêm. Với người đi làm, ba thứ này thường đủ nặng để bù phần thiệt ở trên, miễn là khoá có cơ chế chữa bài.</p>

<blockquote><p>Học online không khó hơn học trực tiếp. Nó chỉ chuyển phần kỷ luật từ nhà trường sang bạn, và phần lớn người bỏ giữa chừng là vì không ai nói trước điều đó.</p></blockquote>

<h2>Bốn tiêu chí chọn một khoá học 3D online</h2>

<p>Bỏ qua số giờ video và số bài giảng. Bốn thứ sau quyết định bạn có đi hết khoá hay không.</p>

<p><strong style="color:#fff;">Một, bài của bạn được mở ra xem bao nhiêu lần.</strong> Đây là tiêu chí số một và nó lọc được hơn nửa thị trường. Hỏi thẳng: trong cả khoá, file của riêng tôi được người dạy mở ra và nhận xét bao nhiêu lần? Nếu câu trả lời là hỏi đáp trong nhóm chat, đó là thư viện video có kèm diễn đàn, không phải lớp học. Cách quy đổi học phí theo số lần chữa bài nằm trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>.</p>

<p><strong style="color:#fff;">Hai, buổi học có người thật ở đầu bên kia không.</strong> Lớp trực tuyến có mặt người dạy theo lịch cố định giữ được phần nhịp. Khoá chỉ gồm video dựng sẵn thì không. Cả hai đều gọi là khoá học 3D online, nhưng tỉ lệ đi hết khoá chênh nhau rất xa.</p>

<p><strong style="color:#fff;">Ba, có bài nộp bắt buộc và có hạn không.</strong> Khoá nào cũng nói học viên tự giác là được. Thực tế thì hạn nộp mới là thứ kéo người ta ngồi vào bàn. Hỏi xem nộp trễ thì sao, có ai nhắc không, và lớp có loại người không nộp bài ra khỏi phần chữa bài không.</p>

<p><strong style="color:#fff;">Bốn, kết thúc khoá bạn cầm được gì.</strong> Không phải chứng chỉ. Là số món hoàn chỉnh đủ đăng lên portfolio. Hỏi con số đó và đòi xem ví dụ thật, cả bài tốt lẫn bài còn yếu. Trang <a href="hoc-vien.html">bài tập học viên</a> là dạng bằng chứng bạn nên yêu cầu ở bất cứ nơi nào.</p>

<h2>Bảng so sánh ba kiểu khoá học 3D online</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Thư viện video tự học</th><th>Lớp trực tuyến theo lịch</th><th>Kèm riêng qua màn hình</th></tr></thead>
<tbody>
<tr><td>Nhịp học</td><td>Bạn tự tạo hoàn toàn</td><td>Có lịch cố định hằng tuần</td><td>Hẹn theo lịch của bạn</td></tr>
<tr><td>Bài của bạn được xem riêng</td><td>Hầu như không</td><td>Có, thường theo lượt</td><td>Có, mỗi buổi</td></tr>
<tr><td>Tốc độ nhận phản hồi</td><td>Chậm hoặc không có</td><td>Theo tuần</td><td>Ngay trong buổi</td></tr>
<tr><td>Rủi ro bỏ giữa chừng</td><td>Cao nhất</td><td>Trung bình</td><td>Thấp nhất</td></tr>
<tr><td>Chi phí tương đối</td><td>Thấp nhất</td><td>Trung bình</td><td>Cao nhất</td></tr>
<tr><td>Hợp với ai</td><td>Người đã có nền, cần tra cứu</td><td>Người mới, cần nhịp và bạn học</td><td>Người đang kẹt ở một khâu cụ thể</td></tr>
<tr><td>Thứ thường thiếu</td><td>Chẩn đoán lỗi của riêng bạn</td><td>Thời lượng dành riêng cho bạn</td><td>Môi trường có người cùng học</td></tr>
</tbody>
</table>
</div>

<p>Bảng này không chỉ ra kiểu nào tốt nhất. Nó chỉ ra rằng chọn sai kiểu là lý do phổ biến nhất khiến tiền học bay đi: mua thư viện video trong khi vấn đề thật là không biết mình sai ở đâu. Phần so sánh sâu hơn giữa tự học và có người kèm nằm trong bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm</a>.</p>

<figure>
  <img src="assets/vplas-che-do-auto.webp" alt="Render bút plasma VPLAS trên nền đen, màn hình hiển thị phát sáng xanh ở chế độ auto" loading="lazy" width="1800" height="1012">
  <figcaption><strong>Một shot sản phẩm trong dự án VPLAS của LXAM Studio.</strong> Dạng hình này là lý do khoá online cần chữa bài: lỗi nằm ở cách đọc phản xạ trên kim loại và cách đặt đèn viền, hai thứ không thể sửa bằng cách xem lại video lần thứ ba.</figcaption>
</figure>

<h2>Dựng nhịp học khi không ai ngồi cạnh</h2>

<p>Đây là phần hầu như không khoá nào dạy, nhưng nó quyết định bạn thuộc nhóm đi hết khoá hay nhóm dừng ở tuần thứ tư.</p>

<h3>Đặt hai khung giờ cố định, đừng đặt mục tiêu theo số giờ</h3>
<p>Thứ hoạt động là hai khung giờ có tên trong lịch, ví dụ tối thứ ba và sáng chủ nhật. Thứ không hoạt động là lời hứa học sáu giờ mỗi tuần vào lúc nào rảnh. Ước lượng từ các nhóm chúng tôi đã theo là khoảng sáu tới mười giờ mỗi tuần để theo kịp một chương trình có nộp bài, nhưng con số đó chỉ có ý nghĩa khi nó nằm trong khung giờ cụ thể.</p>

<h3>Mỗi buổi kết thúc bằng một file lưu lại, không phải một đoạn video đã xem</h3>
<p>Xem hết bài giảng cho cảm giác tiến bộ mà không tạo ra tiến bộ. Quy ước đơn giản: buổi nào cũng phải có một file blend mới hoặc một bản render mới, dù xấu. Tiến độ đo bằng file, không đo bằng phút xem.</p>

<h3>Chuẩn bị máy trước khi bắt đầu, không phải giữa khoá</h3>
<p>Lỗi thường gặp của người học từ xa là phát hiện máy không kham nổi khâu kết xuất vào đúng tuần đang bận nhất. Kiểm tra trước bằng bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a>, trong đó có phần nói rõ mức nào là đủ và mức nào chỉ là mong muốn.</p>

<h3>Gửi bài kể cả khi bài chưa xong</h3>
<p>Người học online hay giấu bài vì thấy chưa đẹp. Đó là cách nhanh nhất để lãng phí học phí. Bài dở gửi đúng hạn nhận được nhiều chỉnh sửa hơn bài đẹp gửi muộn hai tuần.</p>

<h2>Danh sách kiểm tra trước khi đăng ký</h2>

<p>Mười câu, dùng được cho mọi khoá từ xa. Nơi dạy tử tế trả lời thẳng cả những câu bất lợi cho họ.</p>

<ul>
<li>Trong cả khoá, file của riêng tôi được mở ra chữa bao nhiêu lần?</li>
<li>Chữa bài là nhận xét riêng cho file của tôi hay nhận xét chung trước lớp?</li>
<li>Buổi học có người dạy trực tiếp theo lịch, hay chỉ là video dựng sẵn?</li>
<li>Có bản ghi lại buổi học không, và lưu trong bao lâu?</li>
<li>Nghỉ một buổi thì học bù thế nào?</li>
<li>Có bài nộp bắt buộc kèm hạn không, nộp trễ thì xử lý ra sao?</li>
<li>Kết thúc khoá tôi có bao nhiêu món hoàn chỉnh đủ đưa vào portfolio?</li>
<li>Người chữa bài có đang làm dự án thật không, xem dự án đó ở đâu?</li>
<li>Khoá dạy tới đâu: dừng ở dựng hình, hay có cả vật liệu, ánh sáng và kết xuất?</li>
<li>Yêu cầu cấu hình máy tối thiểu là gì, và đường truyền cần bao nhiêu?</li>
</ul>

<p>Câu đầu tiên và câu thứ bảy lọc mạnh nhất. Một nơi dạy có kết quả thật luôn sẵn ví dụ để đưa bạn xem ngay trong buổi tư vấn. Nếu bạn chưa rõ mình cần học tới đâu, thứ tự kỹ năng tối thiểu nằm trong bài <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a>.</p>

<h2>Khi nào khoá học 3D online là lựa chọn sai</h2>

<p>Nói thẳng, có ba trường hợp nên chọn hình thức khác.</p>

<p>Nếu bạn ở TPHCM và lịch làm việc đều đặn, lớp trực tiếp vẫn hơn ở phần nhịp học và phần nhìn bài trực tiếp. Phần tính toán thời gian đi lại và các lựa chọn trong thành phố nằm trong bài <a href="blog-khoa-hoc-3d-tai-tphcm.html">khoá học 3D tại TPHCM</a>.</p>

<p>Nếu bạn đã dựng được vài món nhưng không biết chúng yếu ở đâu, vấn đề là chẩn đoán chứ không phải bài giảng. Một lớp đại trà, dù online hay offline, sẽ dạy lại thứ bạn đã biết. Hình thức <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> hợp hơn và thường kết thúc nhanh hơn.</p>

<p>Nếu tuần nào bạn cũng chỉ còn dưới ba giờ rảnh, hãy để dành tiền. Không có định dạng nào bù được việc không ngồi vào bàn. Trong lúc chờ giai đoạn đời sống dễ thở hơn, tải <a href="cam-nang.html">cẩm nang Blender miễn phí</a> và làm phần bài tập trong đó là đủ để giữ tay.</p>

<h2>Khoá học 3D online hợp lý khi bạn biết mình đang mua gì</h2>

<p>Thứ đáng trả tiền trong một khoá học 3D online không phải là quyền xem video, mà là thời gian của người chữa bài cộng với cơ chế buộc bạn nộp bài đều. Nhìn theo đó thì câu hỏi chọn lớp trở nên đơn giản: khoá này cho tôi bao nhiêu lần được chữa bài, và có gì giữ tôi lại khi tuần nào cũng có lý do để hoãn.</p>

<p>Nếu bạn muốn đối chiếu với một chương trình cụ thể, hai hệ ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a> ghi rõ bài nộp từng tuần và cách chữa bài, còn <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> bảy bước giúp bạn xác định mình đang đứng ở đâu trước khi đóng tiền. Mức lương và nhu cầu tuyển của mảng này được mô tả theo khoảng trong trang <a href="nghe-nghiep.html">nghề 3D artist</a>, kèm ghi chú rõ đó là ước lượng.</p>

<h2>Hỏi đáp</h2>

<p class="faq-q">Khoá học 3D online có hiệu quả bằng học trực tiếp không?</p>
<p>Hiệu quả tương đương nếu khoá đó có người chữa bài riêng và có hạn nộp. Nếu chỉ là thư viện video, hiệu quả thấp hơn rõ rệt, không phải vì nội dung kém mà vì phần lớn người học dừng lại trước khi hết khoá.</p>

<p class="faq-q">Tôi ở tỉnh, đường truyền không mạnh thì học được không?</p>
<p>Được. Phần nặng là kết xuất chạy trên máy bạn chứ không qua mạng. Thứ cần đủ chỉ là gọi video và chia sẻ màn hình. Hỏi trước xem lớp có bản ghi lại để xem lại khi mạng chập chờn không.</p>

<p class="faq-q">Máy yếu có nên đăng ký khoá online trước rồi nâng cấp sau?</p>
<p>Không nên. Nâng cấp giữa khoá là lúc tốn kém và mất mạch nhất. Kiểm tra cấu hình trước, và nếu chưa đủ thì lùi lịch học lại một tháng thay vì vừa học vừa chờ máy.</p>

<p class="faq-q">Học online bao lâu thì nhận được việc?</p>
<p>Không khác học trực tiếp, vì thị trường chấm portfolio chứ không chấm hình thức học. Các mốc thời gian thực tế nằm trong bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a>. Nơi nào cam kết có việc ngay sau khoá đều nên bị hỏi lại rất kỹ.</p>

<p class="faq-q">Nên chọn lớp trực tuyến hay kèm riêng qua màn hình?</p>
<p>Nếu bạn mới bắt đầu và cần nhịp, chọn lớp trực tuyến theo lịch. Nếu bạn đã làm được vài món và đang kẹt ở một khâu, kèm riêng kết thúc nhanh hơn và tính theo số lần được chữa bài thì thường rẻ hơn.</p>

<hr class="hr">

<p>Nếu bạn đang phân vân giữa vài khoá từ xa, gửi cho chúng tôi mô tả từng lớp: số buổi, số người, số lần chữa bài và số bài nộp. Chúng tôi sẽ nói thẳng cái nào giữ chân bạn tốt hơn, kể cả khi câu trả lời là chưa nên học ở đâu cả. Muốn xem trước cách một chương trình chia bài theo tuần trông thế nào, mở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>, còn nếu bạn tới đây vì cần làm hình cho sản phẩm chứ không phải để học, phần <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> mô tả cách chúng tôi nhận việc.</p>
""",
    },
    {
    "slug": "khoa-hoc-dung-hinh-san-pham",
    "title": "Khoá học dựng hình sản phẩm: học gì để nhận việc",
    "desc": "Khoá học dựng hình sản phẩm nên dạy gì, khác lớp modeling chung ở đâu, và bảy câu lọc lớp trước khi đóng tiền. Kèm bảng so sánh và lộ trình tám tuần.",
    "tag": "Định hướng",
    "date": "2026-10-12",
    "date_vn": "12/10/2026",
    "read": "10 phút đọc",
    "thumb": "assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp",
    "faq": [
        ("Khoá học dựng hình sản phẩm có cần biết phần mềm CAD không?",
         "Không bắt buộc. Phần lớn việc thương mại bắt đầu từ ảnh chụp, bản vẽ kích thước hoặc mẫu thật, và bạn dựng lại trong Blender. Biết mở được file bước từ bên kỹ thuật là lợi thế, nhưng đó là kỹ năng thêm chứ không phải điều kiện vào nghề."),
        ("Học dựng hình sản phẩm bao lâu thì dựng được một món hoàn chỉnh?",
         "Ước lượng từ các nhóm chúng tôi đã kèm là khoảng sáu tới mười tuần với nhịp sáu tới mười giờ mỗi tuần, để dựng xong một món vừa phải và render ra ảnh đăng được. Con số này dao động mạnh theo độ phức tạp của món bạn chọn."),
        ("Máy yếu có học dựng hình sản phẩm được không?",
         "Được, vì khâu dựng khối và chỉnh lưới gần như không cần card đồ hoạ mạnh. Máy chỉ thành rào cản ở bước kết xuất. Nên kiểm tra cấu hình trước khi vào khoá thay vì nâng cấp giữa chừng."),
        ("Dựng hình sản phẩm và dựng hình nhân vật khác nhau nhiều không?",
         "Khác gần như toàn bộ phần kỹ thuật. Sản phẩm đòi bề mặt cứng, cạnh sắc, tỉ lệ đúng tới milimet và lưới sạch để đổ bóng không gợn. Nhân vật đòi lưới chảy theo chuyển động và kỹ năng điêu khắc. Chọn một hướng trước, học chéo sau."),
        ("Khoá học dựng hình sản phẩm có dạy luôn render không?",
         "Tuỳ nơi, và đây là chỗ nên hỏi kỹ. Một khoá chỉ dừng ở lưới sẽ để bạn cầm file không ai nhìn ra là đẹp hay xấu. Tối thiểu khoá nên dạy tới mức vật liệu cơ bản, một bộ đèn studio và một bản kết xuất đủ sạch để đưa vào portfolio."),
    ],
    "body": """
<p class="lead">Khoá học dựng hình sản phẩm khác lớp modeling chung ở một điểm quyết định: nó dạy bạn dựng theo một bản vẽ có kích thước thật, với sai số nhìn thấy được, chứ không phải dựng cho giống ảnh tham khảo. Đây là mảng dễ nhận việc nhất trong 3D tại Việt Nam, vì nhãn hàng nào cũng cần hình sản phẩm, và cũng là mảng bị dạy hời hợt nhiều nhất.</p>

<p>Bài này mô tả thứ một khoá dựng hình sản phẩm cần dạy, thứ tự học hợp lý, và cách hỏi để biết lớp bạn đang nhắm tới có làm được việc hay không. Chúng tôi nói cả phần bất lợi, kể cả phần bất lợi của mảng mà chính studio này đang làm.</p>

<h2>Khoá học dựng hình sản phẩm khác lớp modeling chung ở chỗ nào</h2>

<p>Nhiều người đăng ký một lớp modeling tổng quát rồi nhận ra nó không phục vụ được việc mình muốn làm. Khác biệt nằm ở ba chỗ, và cả ba đều là chỗ khách hàng soi.</p>

<h3>Tỉ lệ phải đúng, không phải trông giống</h3>
<p>Khi dựng một chai rượu hay một thiết bị điện tử, bạn đang dựng lại một vật đã tồn tại. Khách có món thật trong tay. Lệch tỉ lệ nắp, lệch độ dày vỏ, sai bán kính bo góc, tất cả đều bị phát hiện ngay trong vòng duyệt đầu tiên. Lớp modeling chung ít khi đặt bạn vào tình huống này vì bài tập của họ thường là vật tự nghĩ ra.</p>

<h3>Lưới phải sạch vì ánh sáng sẽ tố cáo</h3>
<p>Bề mặt cứng phản xạ gần như toàn bộ môi trường quanh nó. Một đoạn lưới xấu không lộ ra ở chế độ xem thường, nhưng lộ rõ thành vệt gợn khi bạn bật kết xuất và đặt một dải đèn dài. Đây là lý do phần lớn bài tập dựng hình sản phẩm của người mới trông sai mà không chỉ ra được sai ở đâu.</p>

<h3>Đầu ra là ảnh, không phải file</h3>
<p>Khách không mua file blend. Họ mua một tấm hình dùng được cho bao bì, sàn thương mại điện tử hoặc quảng cáo. Nghĩa là khoá nào dừng lại ở lúc lưới xong thì mới đi được nửa đường. Phần còn lại nằm ở vật liệu, đèn và kết xuất, và bạn có thể đối chiếu yêu cầu đó với bài <a href="blog-khoa-hoc-render.html">khoá học render</a>.</p>

<blockquote><p>Dựng hình sản phẩm không khó vì nó phức tạp. Nó khó vì sai số được nhìn thấy, và người nhìn là người đã cầm món đồ đó hằng ngày.</p></blockquote>

<h2>Bốn kỹ năng một khoá học dựng hình sản phẩm phải dạy</h2>

<p>Nếu chương trình thiếu một trong bốn phần này, bạn sẽ phải tự học bù sau khi đóng tiền.</p>

<h3>Một, đọc bản vẽ và dựng theo số đo</h3>
<p>Phần này nghe chán nhưng là phần phân biệt người làm được việc với người làm cho vui. Bạn cần quen với việc nhận một bản vẽ kích thước hoặc một bộ ảnh chụp sáu mặt, rồi dựng lại đúng tỉ lệ. Khoá tốt bắt bạn đo và đối chiếu, khoá yếu đưa sẵn ảnh tham chiếu đã căn chỉnh.</p>

<h3>Hai, topology cho bề mặt cứng</h3>
<p>Trọng tâm là kiểm soát cạnh và đổ bóng: khi nào dùng bộ chia mặt, khi nào bo cạnh thẳng, cách xử lý chỗ ba cạnh gặp nhau, cách tránh vệt gợn trên mặt cong. Đây là phần kỹ thuật dày nhất của mảng này. Một số công cụ rút ngắn được thao tác, xem phần đánh giá trong bài <a href="blog-add-on-hard-surface-blender.html">add-on hard surface cho Blender</a>, nhưng công cụ chỉ nhanh hơn khi bạn đã hiểu nguyên tắc bên dưới.</p>

<h3>Ba, chuẩn bị file để chịu được ánh sáng</h3>
<p>Gồm đặt gốc toạ độ, chuẩn tỉ lệ theo đơn vị thật, tách nhóm theo vật liệu, đặt tên có quy ước. Nghe như việc hành chính, nhưng chính nó quyết định bạn sửa một yêu cầu của khách trong mười phút hay trong ba tiếng. Mức độ tách nhóm cần tới đâu thì nhìn <a href="du-an-khoa-cua-thong-minh.html">bộ hình khoá cửa thông minh tách rời linh kiện</a> là rõ nhất: ảnh tách rời chỉ dựng được khi từng chi tiết đã nằm đúng nhóm ngay từ lúc modeling.</p>

<h3>Bốn, một quy trình ra ảnh tối thiểu</h3>
<p>Vật liệu cơ bản, một bộ đèn studio ba nguồn, một góc máy chuẩn và một bản kết xuất sạch. Không cần dạy sâu, nhưng phải dạy tới mức bạn tự ra được tấm hình để người khác đánh giá. Mức hoàn thiện mà một bài giao khách cần thì xem <a href="du-an-locphuc-10-nam.html">bộ hình kỷ niệm mười năm Lộc Phúc</a>, nơi cùng một món phải ra nhiều phương án ánh sáng cho bên duyệt chọn. Cách các khâu này nối vào nhau có mô tả trong trang <a href="khoa-hoc.html">khoá học 3D Blender</a> theo từng tuần. Còn muốn thấy khâu ra ảnh này nằm ở đâu trong một dự án có khách duyệt, xem <a href="blog-quy-trinh-mot-shot-tvc.html">quy trình dựng TVC 3D một shot sản phẩm</a>, trong đó bước ra ảnh chỉ là một trong chín bước.</p>

<h2>Bảng so sánh ba kiểu lớp dạy dựng hình sản phẩm</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Lớp modeling tổng quát</th><th>Khoá dựng hình sản phẩm chuyên sâu</th><th>Kèm riêng theo một món</th></tr></thead>
<tbody>
<tr><td>Bài tập dựa trên</td><td>Vật tự chọn, không có số đo</td><td>Bản vẽ và ảnh sản phẩm thật</td><td>Món bạn đang cần cho portfolio</td></tr>
<tr><td>Dạy topology bề mặt cứng</td><td>Chạm qua</td><td>Dạy thành chương riêng</td><td>Dạy đúng chỗ bạn đang sai</td></tr>
<tr><td>Có dạy tới bản kết xuất</td><td>Thường không</td><td>Có, ở mức tối thiểu dùng được</td><td>Có, theo yêu cầu của bạn</td></tr>
<tr><td>Số lần bài của bạn được chữa</td><td>Thấp, thường theo lượt</td><td>Trung bình, theo tuần</td><td>Cao nhất, mỗi buổi</td></tr>
<tr><td>Thời gian tới món hoàn chỉnh đầu tiên</td><td>Khó ước lượng</td><td>Khoảng sáu tới mười tuần</td><td>Khoảng ba tới sáu tuần</td></tr>
<tr><td>Chi phí tương đối</td><td>Thấp</td><td>Trung bình</td><td>Cao</td></tr>
<tr><td>Hợp với ai</td><td>Người chưa chọn hướng</td><td>Người đã chắc muốn làm sản phẩm</td><td>Người đang kẹt ở một khâu cụ thể</td></tr>
</tbody>
</table>
</div>

<p>Bảng này không nói kiểu nào tốt hơn. Nó chỉ ra lỗi chọn lớp phổ biến nhất: đăng ký một lớp tổng quát trong khi mục tiêu thật là đi làm mảng sản phẩm, rồi mất thêm vài tháng học bù. Nếu bạn còn đang phân vân giữa các hướng, bài <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> mô tả bức tranh rộng hơn trước khi bạn thu hẹp lại.</p>

<figure>
  <img src="assets/khoa-cua-thong-minh-tach-roi-linh-kien.webp" alt="Hình tách rời các linh kiện khoá cửa thông minh dựng bằng Blender, thân khoá, bàn phím cảm ứng và tay nắm xếp theo trục dọc" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Hình tách rời linh kiện trong dự án khoá cửa thông minh của LXAM Studio.</strong> Dạng hình này chỉ dựng được khi từng chi tiết đúng tỉ lệ và lưới đủ sạch, vì mọi khe hở và bo góc đều bị nhìn rõ ở cự ly gần.</figcaption>
</figure>

<h2>Lộ trình tám tuần hợp lý cho người mới</h2>

<p>Đây là thứ tự chúng tôi thấy ít gây nản nhất. Mỗi tuần kết thúc bằng một file lưu lại, không phải bằng một bài giảng đã xem.</p>

<h3>Tuần một và hai, làm chủ thao tác và dựng khối thô</h3>
<p>Mục tiêu không phải là đẹp, mà là dựng xong một món đơn giản có số đo đúng, ví dụ một hộp đựng hoặc một chai nước. Người mới hay bỏ qua giai đoạn này để nhảy vào món phức tạp, và đó là lý do họ kẹt ở tuần thứ năm. Nền tảng tối thiểu nằm trong bài <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a>.</p>

<h3>Tuần ba và bốn, cạnh sắc và đổ bóng</h3>
<p>Giai đoạn khó chịu nhất. Bạn sẽ dựng lại cùng một chi tiết nhiều lần chỉ để hết vệt gợn. Dấu hiệu bạn đang đi đúng là tự nhìn ra chỗ hỏng trước khi người dạy chỉ ra.</p>

<h3>Tuần năm và sáu, một món thật có nhiều bộ phận</h3>
<p>Chọn một món có vỏ, nút bấm, chi tiết kim loại và một phần trong suốt. Đây là lúc quy ước đặt tên và tách nhóm bắt đầu trả công cho bạn.</p>

<h3>Tuần bảy và tám, ra ảnh và dựng hồ sơ</h3>
<p>Vật liệu, đèn, kết xuất, và chọn ba góc máy. Kết thúc tám tuần bạn nên cầm được một món hoàn chỉnh đủ đăng. Dạng bài tập ở mức này trông ra sao thì xem trang <a href="hoc-vien.html">bài tập học viên</a>, còn mức thương mại thì xem <a href="du-an-san-pham.html">dự án dựng hình sản phẩm</a> của studio.</p>

<h2>Bảy câu hỏi lọc lớp trước khi đóng tiền</h2>

<p>Dùng được cho mọi nơi dạy. Chỗ tử tế trả lời thẳng cả những câu bất lợi cho họ.</p>

<ul>
<li>Bài tập dựa trên bản vẽ có kích thước thật hay chỉ dựa trên ảnh tham khảo?</li>
<li>Khoá có chương riêng về topology bề mặt cứng và xử lý đổ bóng không?</li>
<li>Trong cả khoá, file của riêng tôi được mở ra chữa bao nhiêu lần?</li>
<li>Khoá dừng ở lưới, hay dạy tới vật liệu, đèn và một bản kết xuất hoàn chỉnh?</li>
<li>Kết thúc khoá tôi cầm được bao nhiêu món đủ đưa vào portfolio?</li>
<li>Người chữa bài có đang làm dự án sản phẩm thật không, xem ở đâu?</li>
<li>Có dạy phần đặt tên, tách nhóm và chuẩn đơn vị để file bàn giao được không?</li>
</ul>

<p>Câu một và câu bốn lọc mạnh nhất. Nếu câu trả lời cho câu bốn là khoá chỉ dạy dựng hình, bạn vẫn có thể học, nhưng hãy tính luôn chi phí và thời gian học phần còn lại. Cách quy đổi học phí theo số lần được chữa bài nằm trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>.</p>

<h2>Khi nào khoá học dựng hình sản phẩm là lựa chọn sai</h2>

<p>Ba trường hợp nên chọn hướng khác, nói thẳng.</p>

<p>Nếu bạn muốn làm nhân vật, hoạt hình hoặc dựng cảnh phim, mảng này dạy gần như toàn bộ kỹ năng không dùng tới. Chọn nhầm hướng ở giai đoạn đầu tốn nhiều tháng. Bức tranh nghề và các nhánh có mô tả trong trang <a href="nghe-nghiep.html">nghề 3D artist</a>, kèm ghi chú rằng các mức thu nhập ở đó chỉ là khoảng ước lượng.</p>

<p>Nếu máy của bạn chưa chạy nổi khâu kết xuất, hãy kiểm tra trước thay vì nâng cấp giữa khoá, dùng bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> để biết mức nào là đủ.</p>

<p>Nếu mỗi tuần bạn chỉ còn dưới ba giờ rảnh, chưa nên đóng tiền. Không định dạng nào bù được việc không ngồi vào bàn. Trong lúc chờ, tải <a href="cam-nang.html">cẩm nang Blender miễn phí</a> và làm phần bài tập trong đó là đủ để giữ tay.</p>

<p>Nếu bạn đã dựng được vài món và chỉ kẹt ở một khâu cụ thể, một khoá dài là thừa. Trường hợp đó thuê <a href="blog-gia-su-blender.html">gia sư Blender</a> theo buổi gỡ nhanh hơn và tính ra thường rẻ hơn.</p>

<h2>Chọn khoá học dựng hình sản phẩm theo thứ bạn cầm được sau khoá</h2>

<p>Thứ đáng trả tiền trong một khoá học dựng hình sản phẩm không phải là số giờ bài giảng, mà là số lần bài của bạn được mở ra chữa, cộng với việc khoá có đưa bạn tới tận tấm ảnh hoàn chỉnh hay không. Nhìn theo đó thì việc chọn lớp gọn lại thành hai câu: lớp này bắt tôi dựng theo số đo thật chứ, và hết khoá tôi cầm được mấy món đăng lên được.</p>

<p>Nếu bạn muốn đối chiếu với một chương trình cụ thể, hai hệ ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a> ghi rõ bài nộp từng tuần và cách chữa bài. Còn nếu bạn tới đây vì cần hình cho sản phẩm của mình chứ không phải để học, phần <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a> mô tả cách chúng tôi nhận việc và cần gì từ phía bạn.</p>

<h2>Hỏi đáp</h2>

<p class="faq-q">Khoá học dựng hình sản phẩm có cần biết phần mềm CAD không?</p>
<p>Không bắt buộc. Phần lớn việc thương mại bắt đầu từ ảnh chụp, bản vẽ kích thước hoặc mẫu thật, và bạn dựng lại trong Blender. Biết mở được file bước từ bên kỹ thuật là lợi thế, nhưng đó là kỹ năng thêm chứ không phải điều kiện vào nghề.</p>

<p class="faq-q">Học dựng hình sản phẩm bao lâu thì dựng được một món hoàn chỉnh?</p>
<p>Ước lượng từ các nhóm chúng tôi đã kèm là khoảng sáu tới mười tuần với nhịp sáu tới mười giờ mỗi tuần, để dựng xong một món vừa phải và render ra ảnh đăng được. Con số này dao động mạnh theo độ phức tạp của món bạn chọn. Các mốc dài hơn có trong bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a>.</p>

<p class="faq-q">Máy yếu có học dựng hình sản phẩm được không?</p>
<p>Được, vì khâu dựng khối và chỉnh lưới gần như không cần card đồ hoạ mạnh. Máy chỉ thành rào cản ở bước kết xuất. Nên kiểm tra cấu hình trước khi vào khoá thay vì nâng cấp giữa chừng.</p>

<p class="faq-q">Dựng hình sản phẩm và dựng hình nhân vật khác nhau nhiều không?</p>
<p>Khác gần như toàn bộ phần kỹ thuật. Sản phẩm đòi bề mặt cứng, cạnh sắc, tỉ lệ đúng tới milimet và lưới sạch để đổ bóng không gợn. Nhân vật đòi lưới chảy theo chuyển động và kỹ năng điêu khắc. Chọn một hướng trước, học chéo sau.</p>

<p class="faq-q">Khoá học dựng hình sản phẩm có dạy luôn render không?</p>
<p>Tuỳ nơi, và đây là chỗ nên hỏi kỹ. Một khoá chỉ dừng ở lưới sẽ để bạn cầm file không ai nhìn ra là đẹp hay xấu. Tối thiểu khoá nên dạy tới mức vật liệu cơ bản, một bộ đèn studio và một bản kết xuất đủ sạch để đưa vào portfolio.</p>

<hr class="hr">

<p>Nếu bạn đang so vài lớp với nhau, gửi cho chúng tôi mô tả từng lớp: bài tập dựa trên gì, số buổi, số lần chữa bài và đầu ra cuối khoá. Chúng tôi sẽ nói thẳng lớp nào đưa bạn tới một món đăng được nhanh hơn, kể cả khi câu trả lời là chưa nên học ở đâu cả. Muốn xem trước cách một chương trình chia bài theo tuần, mở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>; muốn tự đi trước một đoạn, xem <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> bảy bước. Còn nếu bạn đã dựng được vài món và chỉ cần gom chúng thành hồ sơ nộp được, đọc bài <a href="blog-kem-1-1-lam-portfolio-3d.html">kèm 1 kèm 1 làm portfolio 3D</a>.</p>
""",
    },
    {
        "slug": "gia-su-blender",
        "title": "Gia sư Blender: khi nào cần và chọn thế nào",
        "desc": "Gia sư Blender khác lớp đông ở đâu, khi nào kèm riêng là đúng tiền, cách kiểm tra người dạy và năm câu hỏi lọc trước buổi đầu. Kèm bảng so sánh thẳng thắn.",
        "tag": "Định hướng",
        "date": "2026-10-14",
        "date_vn": "14/10/2026",
        "read": "10 phút đọc",
        "thumb": "assets/insta360-gimbal-hoc-vien-loc.jpg",
        "faq": [
            ('Gia sư Blender và lớp học kèm nhóm nhỏ khác nhau thế nào?',
             'Gia sư là một người dạy cho một người, toàn bộ buổi xoay quanh file của bạn. Nhóm nhỏ vẫn chạy theo một giáo trình chung, bạn được chữa bài nhiều hơn lớp đông nhưng vẫn phải chờ lượt. Nếu bạn đang kẹt ở một khâu rất riêng thì gia sư kết thúc nhanh hơn, còn nếu bạn mới bắt đầu và cần nhịp thì nhóm nhỏ hợp hơn.'),
            ('Mới học Blender hoàn toàn có nên thuê gia sư ngay không?',
             'Thường là chưa. Vài tuần đầu bạn chỉ cần làm quen giao diện và dựng vài khối đơn giản, phần đó tài liệu miễn phí dạy tốt và trả tiền cho nó là lãng phí. Gia sư phát huy tác dụng khi bạn đã có file của riêng mình và không hiểu vì sao nó chưa đẹp.'),
            ('Học với gia sư Blender bao nhiêu buổi là đủ?',
             'Ước lượng từ các nhóm chúng tôi đã kèm là sáu tới mười buổi cho một mục tiêu cụ thể, ví dụ hoàn thiện một món sản phẩm từ khối thô tới ảnh đăng được. Nếu quá mười lăm buổi mà chưa ra món nào hoàn chỉnh, vấn đề thường nằm ở mục tiêu quá rộng chứ không ở người dạy.'),
            ('Làm sao biết một gia sư Blender có thật sự làm nghề hay không?',
             'Hỏi xem một file gốc chứ không chỉ ảnh đã kết xuất. Người làm nghề mở file ra được, chỉ cho bạn cách đặt tên, cách gom bộ sưu tập và chỗ họ đã phải sửa lại. Ảnh đẹp có thể tải về từ bất cứ đâu, còn cấu trúc file thì không giả được.'),
            ('Học kèm riêng qua mạng có kém học trực tiếp không?',
             'Không kém, vì phần lớn thời gian là hai người cùng nhìn một màn hình. Điều kiện cần chỉ là gọi video ổn định và quyền điều khiển màn hình khi cần sửa trực tiếp. Phần nặng là kết xuất chạy trên máy bạn chứ không qua đường truyền.'),
        ],
        "body": """
<p class="lead">Gia sư Blender là hình thức một người dạy kèm riêng một người học, toàn bộ buổi học xoay quanh file bạn đang làm dở chứ không theo giáo trình chung. Nó đáng tiền khi bạn đã dựng được vài món nhưng không tự chỉ ra được chúng sai ở đâu. Nó lãng phí khi bạn mới mở phần mềm lần đầu, vì giai đoạn đó tài liệu miễn phí đã đủ.</p>

<p>Bài này nói rõ ranh giới giữa hai trường hợp đó, kèm cách kiểm tra một người dạy trước khi trả buổi đầu tiên. Chúng tôi không nêu mức giá của bất kỳ ai, kể cả của mình, vì giá thay đổi theo thời điểm và theo việc buổi học có chữa file thật hay không.</p>

<h2>Gia sư Blender khác lớp đông ở chỗ nào</h2>

<p>Khác biệt không nằm ở kiến thức. Phần lớn nội dung một gia sư nói ra, bạn đều tìm được trên mạng. Khác biệt nằm ở thứ tự: lớp đông đi theo thứ tự của giáo trình, gia sư đi theo thứ tự của chỗ bạn đang kẹt.</p>

<h3>Lớp đông dạy cái đa số cần</h3>
<p>Giáo trình được thiết kế cho người học trung bình. Nếu bạn đã mạnh phần dựng khối nhưng yếu ánh sáng, bạn vẫn ngồi hết các buổi dựng khối. Thời gian mất đi ở đó không nhỏ.</p>

<h3>Gia sư dạy cái riêng bạn thiếu</h3>
<p>Buổi học bắt đầu bằng việc mở file của bạn. Người dạy nhìn cấu trúc lưới, cách bạn đặt đèn, cách bạn tổ chức bộ sưu tập, rồi chỉ ra ba bốn chỗ làm hình xấu đi. Đó là việc không video nào làm được, vì video không biết bạn đã làm gì.</p>

<p>Nếu mục tiêu của bạn không phải học thêm kỹ thuật mà là ra được bộ hồ sơ đem đi xin việc, hình thức <a href="blog-kem-1-1-lam-portfolio-3d.html">kèm 1 kèm 1 làm portfolio 3D</a> đi theo một nhịp khác: chốt danh sách món trước, rồi mỗi buổi đẩy một món tiến thêm một bước.</p>

<blockquote><p>Thứ bạn mua ở một gia sư không phải bài giảng. Bài giảng Blender trên mạng đã quá nhiều và hầu hết miễn phí. Bạn mua khả năng chẩn đoán: có người nhìn file của bạn và nói đúng chỗ sai trong mười phút thay vì để bạn mò ba tuần.</p></blockquote>

<h2>Khi nào bạn thật sự cần một gia sư Blender</h2>

<p>Bốn tình huống dưới đây là lúc kèm riêng cho hiệu quả rõ rệt nhất, dựa trên các nhóm chúng tôi đã làm việc cùng.</p>

<p><strong style="color:#fff;">Bạn làm xong một món nhưng nó trông vẫn rẻ tiền.</strong> Đây là tình huống phổ biến nhất. Lưới đúng, vật liệu có vẻ ổn, nhưng ảnh cuối cùng thiếu sức nặng. Nguyên nhân thường nằm ở ánh sáng và bố cục, hai thứ rất khó tự thấy. Một buổi kèm có thể tiết kiệm cho bạn cả tháng thử sai.</p>

<p><strong style="color:#fff;">Bạn có hạn nộp thật và không được phép hỏng.</strong> Một khách hàng đầu tiên, một bài dự tuyển, một món cho hồ sơ xin việc. Lúc này thứ bạn cần là người đi cùng từng bước chứ không phải một khoá mười hai tuần.</p>

<p><strong style="color:#fff;">Bạn đã quen phần mềm khác và muốn chuyển sang.</strong> Người từng làm 3ds Max hoặc Cinema 4D không cần học lại tư duy 3D, chỉ cần ánh xạ thao tác và hiểu khác biệt về bộ kết xuất. Ngồi lớp người mới là phí thời gian rõ ràng.</p>

<p><strong style="color:#fff;">Bạn cần dựng đúng một loại món cho công việc.</strong> Ví dụ chỉ cần dựng được sản phẩm của chính công ty mình. Trường hợp này phần kèm riêng bám sát thực tế hơn hẳn, và nếu bạn muốn xem một chương trình bài bản hơn cho hướng này thì bài <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a> mô tả đủ các khâu cần có.</p>

<h2>Khi nào chưa nên thuê gia sư, nói thẳng</h2>

<p>Phần này đi ngược lợi ích của một nơi vừa dạy vừa nhận kèm riêng như chúng tôi, nhưng nói trước thì bạn đỡ mất tiền.</p>

<p>Nếu bạn chưa mở Blender lần nào, hãy dành hai tuần tự làm quen trước. Tải <a href="cam-nang.html">cẩm nang Blender miễn phí</a> và làm hết phần bài tập trong đó. Hai tuần này không tốn đồng nào và nó quyết định việc bạn có thật sự thích công việc này hay không. Kế hoạch chi tiết cho chặng này nằm trong bài <a href="blog-hoc-do-hoa-3d-tu-con-so-0.html">học đồ hoạ 3D từ con số 0</a>, gồm cả danh sách kiểm tra để tự biết đã qua chặng nền hay chưa.</p>

<p>Nếu mỗi tuần bạn chỉ còn dưới ba giờ rảnh, kèm riêng sẽ thành buổi nhắc bài. Người dạy giao việc, bạn không kịp làm, buổi sau lại ôn lại. Tiền chảy đi mà kỹ năng đứng yên.</p>

<p>Nếu bạn cần một môi trường có người cùng học để không bỏ cuộc, lớp mới là thứ bạn cần chứ không phải gia sư. Phần so sánh đầy đủ giữa hai lựa chọn nằm trong bài <a href="blog-tu-hoc-blender-hay-hoc-kem.html">tự học Blender hay học kèm</a>.</p>

<p>Nếu máy của bạn chưa kham nổi khâu kết xuất, hãy xử lý phần cứng trước. Học kèm trên một máy dựng xong không render được là trả tiền để nhìn vòng xoay chờ. Mức cấu hình đủ cho từng giai đoạn nằm trong bài <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a>.</p>

<h2>Bảng so sánh ba hình thức học theo thứ bạn thật sự nhận được</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Tự học qua video</th><th>Lớp có chữa bài nhóm</th><th>Gia sư kèm riêng</th></tr></thead>
<tbody>
<tr><td>Nội dung bám theo</td><td>Giáo trình của người quay</td><td>Giáo trình chung của lớp</td><td>File và mục tiêu của bạn</td></tr>
<tr><td>Tốc độ gỡ một chỗ kẹt cụ thể</td><td>Chậm, phụ thuộc may mắn tìm kiếm</td><td>Trung bình, phải chờ lượt</td><td>Nhanh nhất</td></tr>
<tr><td>Chi phí tính theo buổi</td><td>Gần bằng không</td><td>Trung bình</td><td>Cao nhất</td></tr>
<tr><td>Chi phí tính theo một lần được chữa file</td><td>Rất cao vì gần như không có</td><td>Trung bình</td><td>Thường thấp nhất</td></tr>
<tr><td>Rủi ro bỏ giữa chừng</td><td>Cao nhất</td><td>Trung bình</td><td>Thấp, vì có lịch hẹn riêng</td></tr>
<tr><td>Môi trường có bạn học</td><td>Không</td><td>Có</td><td>Không</td></tr>
<tr><td>Hợp nhất khi</td><td>Bạn đang làm quen giai đoạn đầu</td><td>Bạn cần nhịp và nền tảng</td><td>Bạn kẹt ở một khâu hoặc có hạn nộp</td></tr>
</tbody>
</table>
</div>

<p>Bảng này không chọn hộ bạn. Nó chỉ ra rằng ba hình thức giải ba bài toán khác nhau, và lỗi hay gặp là trả tiền cho hình thức đắt khi vấn đề chỉ cần hình thức rẻ, hoặc ngược lại. Cách quy mọi báo giá về một con số so sánh được nằm trong bài <a href="blog-hoc-phi-khoa-hoc-blender.html">học phí khoá học Blender</a>.</p>

<figure>
  <img src="assets/insta360-gimbal-hoc-vien-loc.jpg" alt="Render máy quay gimbal cầm tay chia đôi, nửa trái là bản kết xuất hoàn chỉnh, nửa phải là lưới wireframe xám của cùng mẫu" loading="lazy" width="1600" height="900">
  <figcaption><strong>Một bài học viên dựng trong quá trình kèm riêng tại LXAM Studio.</strong> Nửa lưới và nửa đã kết xuất đặt cạnh nhau là cách buổi kèm thường diễn ra: người dạy xem cấu trúc lưới trước, vì phần lớn lỗi ở ảnh cuối bắt nguồn từ chỗ không nhìn thấy.</figcaption>
</figure>

<h2>Cách kiểm tra một gia sư Blender trước khi trả buổi đầu</h2>

<p>Đây là danh sách bạn nên chạy qua với bất kỳ ai nhận kèm, kể cả với chúng tôi. Người làm nghề thật trả lời được hết, kể cả những câu bất lợi cho họ.</p>

<ul>
<li>Cho tôi xem một file gốc chứ không chỉ ảnh đã kết xuất, để tôi nhìn cách bạn tổ chức lưới và bộ sưu tập.</li>
<li>Bạn đang làm dự án thật nào trong sáu tháng qua, xem ở đâu?</li>
<li>Buổi học diễn ra thế nào: tôi làm và bạn sửa, hay bạn làm và tôi xem?</li>
<li>Giữa hai buổi tôi phải nộp gì, và bạn phản hồi trong bao lâu?</li>
<li>Sau sáu buổi, thứ cụ thể tôi cầm trong tay là gì?</li>
<li>Bạn có nhận chỉnh trực tiếp vào file của tôi không, hay chỉ hướng dẫn bằng lời?</li>
<li>Nếu tôi thấy không hợp sau hai buổi thì dừng thế nào?</li>
</ul>

<p>Câu đầu và câu áp chót là hai câu lọc mạnh nhất. Ảnh đẹp tải ở đâu cũng có, nhưng một file sạch thì không giả được. Còn người không dám đụng vào file của bạn thường là người chưa đủ tự tin với chính thao tác của mình. Dạng bằng chứng bạn nên đòi hỏi trông như trang <a href="hoc-vien.html">bài tập học viên</a> của chúng tôi, có cả bài tốt lẫn bài còn yếu kèm nhận xét.</p>

<h2>Một chu kỳ kèm riêng tám buổi trông như thế nào</h2>

<p>Đây là khung chúng tôi hay dùng khi người học đã có nền cơ bản và muốn ra một món sản phẩm hoàn chỉnh. Nó không phải chuẩn mực, chỉ là một ví dụ để bạn biết nên đòi hỏi mức rõ ràng nào.</p>

<p>Hai buổi đầu dành cho chẩn đoán và dựng khối. Người dạy xem lại toàn bộ thứ bạn đã làm, chốt một món để theo tới cùng, rồi cùng bạn dựng khối thô và kiểm tra tỉ lệ. Hai buổi tiếp là chỉnh lưới và cạnh, khâu quyết định việc đổ bóng có gợn hay không.</p>

<p>Buổi năm và sáu làm vật liệu và ánh sáng, thường là chỗ tiến bộ nhìn thấy rõ nhất. Hai buổi cuối dành cho kết xuất, hậu kỳ nhẹ và dựng trang trình bày món đó cho hồ sơ. Kết thúc chu kỳ bạn cầm một món đăng được, không phải tám bài tập rời rạc.</p>

<p>Nếu bạn muốn tự đi trước một đoạn rồi mới thuê kèm cho phần khó, thứ tự bảy kỹ năng trong bài <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a> cho biết bạn đang đứng ở đâu và còn thiếu bước nào.</p>

<h2>Gia sư Blender không thay được số giờ bạn ngồi vào bàn</h2>

<p>Đây là phần nhiều người không muốn nghe. Kèm riêng rút ngắn quãng mò mẫm, nó không rút ngắn quãng luyện tay. Một người dạy giỏi có thể chỉ cho bạn trong mười lăm phút thứ bạn tự tìm mất ba tuần, nhưng sau đó vẫn phải là bạn ngồi dựng lại cho tới khi thao tác thành phản xạ.</p>

<p>Cách dùng gia sư hiệu quả nhất, theo quan sát của chúng tôi, là xen kẽ chứ không liên tục. Học kèm một đợt ngắn để gỡ chỗ kẹt và nhận một bộ tiêu chuẩn, rồi tự làm vài tháng, rồi quay lại khi gặp bức tường mới. Chi phí thấp hơn nhiều so với kèm đều đặn, và kỹ năng bền hơn vì bạn tự giải quyết phần lớn vấn đề.</p>

<p>Nếu bạn đang cân nhắc giữa kèm riêng và một chương trình dài hơi, bài <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> phân tích kỹ hơn từng kiểu người học, còn mức thu nhập và nhu cầu tuyển của mảng này được mô tả theo khoảng trong trang <a href="nghe-nghiep.html">nghề 3D artist</a>, kèm ghi chú rõ đó là ước lượng chứ không phải số liệu chính thức.</p>

<h2>Hỏi đáp</h2>

<p class="faq-q">Gia sư Blender và lớp học kèm nhóm nhỏ khác nhau thế nào?</p>
<p>Gia sư là một người dạy cho một người, toàn bộ buổi xoay quanh file của bạn. Nhóm nhỏ vẫn chạy theo một giáo trình chung, bạn được chữa bài nhiều hơn lớp đông nhưng vẫn phải chờ lượt. Nếu bạn đang kẹt ở một khâu rất riêng thì gia sư kết thúc nhanh hơn, còn nếu bạn mới bắt đầu và cần nhịp thì nhóm nhỏ hợp hơn.</p>

<p class="faq-q">Mới học Blender hoàn toàn có nên thuê gia sư ngay không?</p>
<p>Thường là chưa. Vài tuần đầu bạn chỉ cần làm quen giao diện và dựng vài khối đơn giản, phần đó tài liệu miễn phí dạy tốt và trả tiền cho nó là lãng phí. Gia sư phát huy tác dụng khi bạn đã có file của riêng mình và không hiểu vì sao nó chưa đẹp.</p>

<p class="faq-q">Học với gia sư Blender bao nhiêu buổi là đủ?</p>
<p>Ước lượng từ các nhóm chúng tôi đã kèm là sáu tới mười buổi cho một mục tiêu cụ thể, ví dụ hoàn thiện một món sản phẩm từ khối thô tới ảnh đăng được. Nếu quá mười lăm buổi mà chưa ra món nào hoàn chỉnh, vấn đề thường nằm ở mục tiêu quá rộng chứ không ở người dạy.</p>

<p class="faq-q">Làm sao biết một gia sư Blender có thật sự làm nghề hay không?</p>
<p>Hỏi xem một file gốc chứ không chỉ ảnh đã kết xuất. Người làm nghề mở file ra được, chỉ cho bạn cách đặt tên, cách gom bộ sưu tập và chỗ họ đã phải sửa lại. Ảnh đẹp có thể tải về từ bất cứ đâu, còn cấu trúc file thì không giả được.</p>

<p class="faq-q">Học kèm riêng qua mạng có kém học trực tiếp không?</p>
<p>Không kém, vì phần lớn thời gian là hai người cùng nhìn một màn hình. Điều kiện cần chỉ là gọi video ổn định và quyền điều khiển màn hình khi cần sửa trực tiếp. Phần nặng là kết xuất chạy trên máy bạn chứ không qua đường truyền.</p>

<hr class="hr">

<p>Nếu bạn không chắc mình thuộc nhóm nên thuê kèm hay nên tự đi thêm một đoạn, gửi cho chúng tôi hai ba món bạn đã làm và một câu mô tả chỗ bạn thấy bí. Chúng tôi sẽ nói thẳng bạn đang thiếu gì, kể cả khi câu trả lời là chưa cần trả tiền cho ai cả. Muốn xem cách một chương trình chia bài và chữa bài theo tuần, hai hệ ở trang <a href="khoa-hoc.html">khoá học 3D Blender</a> ghi rõ đầu ra từng tuần.</p>
""",
    },
    {
        "slug": "kem-1-1-lam-portfolio-3d",
        "title": "Kèm 1 kèm 1 làm portfolio 3D: lộ trình sáu món",
        "desc": "Kèm 1 kèm 1 làm portfolio 3D khác lớp thường ở đâu, bộ hồ sơ cần mấy món, kèm bao lâu là đủ và khi nào chưa nên trả tiền. Kèm bảng so sánh thẳng thắn.",
        "tag": "Định hướng",
        "date": "2026-10-21",
        "date_vn": "21/10/2026",
        "read": "11 phút đọc",
        "thumb": "assets/khoa-cua-thong-minh-lap-tren-cua-thuc-te.webp",
        "faq": [
            ('Kèm 1 kèm 1 làm portfolio 3D khác lớp học 3D thường ở đâu?',
             'Lớp thường dạy kỹ năng theo giáo trình, bài tập là bài tập chung của lớp. Kèm riêng theo hồ sơ lấy đích đến là bộ món bạn sẽ đem đi xin việc, nên mọi buổi đều xoay quanh một món cụ thể trong bộ đó. Hệ quả là bạn học ít kỹ thuật hơn nhưng ra sản phẩm hoàn chỉnh nhanh hơn.'),
            ('Portfolio 3D cần mấy món thì đủ để nộp?',
             'Bốn tới sáu món hoàn chỉnh là khoảng hợp lý. Dưới bốn thì người xem không phân biệt được bạn làm được hay chỉ may mắn một lần. Trên tám thì gần như chắc chắn có món yếu kéo cả bộ xuống, vì người tuyển thường đánh giá theo món tệ nhất chứ không theo món đẹp nhất.'),
            ('Kèm 1 kèm 1 làm portfolio 3D mất bao lâu?',
             'Ước lượng từ các nhóm chúng tôi đã kèm là khoảng mười tới mười sáu tuần cho một bộ bốn tới sáu món, với nhịp tám tới mười hai giờ tự làm mỗi tuần. Con số dao động mạnh theo độ phức tạp món bạn chọn và theo việc bạn có nộp bài đúng hạn giữa hai buổi hay không.'),
            ('Chưa biết gì về Blender có nên kèm riêng để làm portfolio luôn không?',
             'Không nên. Giai đoạn làm quen giao diện và dựng khối cơ bản không cần người kèm, tài liệu miễn phí đủ dùng và trả tiền cho nó là lãng phí. Mốc hợp lý để bắt đầu kèm theo hồ sơ là khi bạn đã tự dựng xong ít nhất một món và tự thấy nó chưa đẹp nhưng không chỉ ra được vì sao.'),
            ('Portfolio 3D nên đưa ảnh kết xuất hay cả file gốc?',
             'Đưa ảnh trước, nhưng luôn chuẩn bị sẵn file gốc để mở khi được hỏi. Nhiều studio hỏi xem lưới và cách tổ chức bộ sưu tập ngay trong buổi phỏng vấn, vì ảnh đẹp có thể đến từ nhiều nguồn còn cấu trúc file thì không giả được.'),
        ],
        "body": """
<p class="lead">Kèm 1 kèm 1 làm portfolio 3D là hình thức học kèm riêng lấy đích đến là bộ hồ sơ bạn sẽ đem đi xin việc, chứ không phải lấy đích đến là học hết một giáo trình. Mỗi buổi xoay quanh một món trong bộ đó: chọn món, dựng, sửa, kết xuất, rồi đóng gói thành trang trình bày. Nó đáng tiền khi bạn đã dựng được vài thứ nhưng chưa có món nào đủ sạch để nộp.</p>

<p>Bài này nói rõ bộ hồ sơ cần mấy món, một chu kỳ kèm theo hồ sơ chia theo tuần trông thế nào, và ba tình huống mà chúng tôi khuyên bạn chưa nên trả tiền cho ai cả. Chúng tôi không nêu mức giá, vì giá thay đổi theo thời điểm và theo việc buổi học có chữa file thật hay không.</p>

<h2>Kèm 1 kèm 1 làm portfolio 3D là gì</h2>

<p>Khác biệt lớn nhất không nằm ở số người trong lớp. Nó nằm ở thứ được coi là đầu ra.</p>

<h3>Lớp thường lấy kỹ năng làm đầu ra</h3>
<p>Một khoá học 3D bình thường kết thúc khi bạn đi hết các chương: dựng khối, vật liệu, ánh sáng, kết xuất. Bài tập là bài tập của lớp, ai cũng làm giống nhau. Bạn ra khỏi khoá với nhiều kỹ năng rời và thường là không có món nào hoàn chỉnh của riêng mình.</p>

<h3>Kèm theo hồ sơ lấy bộ món làm đầu ra</h3>
<p>Buổi đầu không dạy gì. Buổi đầu là ngồi chọn bốn tới sáu món, dựa trên loại việc bạn muốn nhận. Từ buổi hai trở đi, mỗi buổi đều mở file của bạn và đẩy một món tiến thêm một bước. Kỹ thuật được dạy khi món đó cần tới, không dạy trước.</p>

<p>Nếu bạn muốn hiểu hình thức kèm riêng nói chung trước khi đọc tiếp, bài <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> mô tả cách một buổi diễn ra, còn bài <a href="blog-gia-su-blender.html">gia sư Blender</a> nói về cách kiểm tra người dạy. Bài này giả định bạn đã quyết định học kèm và chỉ bàn phần hồ sơ.</p>

<blockquote><p>Thị trường không chấm số giờ bạn học. Nó mở bốn năm hình, xem trong khoảng một phút, rồi quyết định. Mọi thứ bạn làm trong lúc kèm riêng nên được tính theo việc nó có làm một trong bốn năm hình đó tốt hơn hay không.</p></blockquote>

<h2>Portfolio 3D cần có gì</h2>

<p>Bốn tới sáu món hoàn chỉnh. Hoàn chỉnh nghĩa là có ảnh kết xuất sạch, có vài góc, có một ảnh lưới và một dòng mô tả bạn đã làm gì. Một món dở dang không tính, kể cả khi phần đã làm rất ấn tượng.</p>

<p>Bộ nên trải ra theo loại việc, không nên là bốn món cùng kiểu. Cấu hình chúng tôi thường dùng khi kèm:</p>

<ul>
<li>Một món sản phẩm cứng có nhiều chi tiết cơ khí, để chứng minh bạn kiểm soát được lưới và cạnh.</li>
<li>Một món sản phẩm mềm hoặc trong suốt, ví dụ chai, bao bì, vải, để chứng minh bạn hiểu vật liệu.</li>
<li>Một bối cảnh nhỏ có nhiều vật thể, để chứng minh bạn biết bố cục và quản lý tệp.</li>
<li>Một món chạy theo ảnh tham chiếu thật, dựng lại gần đúng, để chứng minh bạn làm được việc theo yêu cầu.</li>
<li>Tuỳ chọn thêm: một đoạn chuyển động ngắn vài giây, hoặc một ảnh tách lớp kỹ thuật.</li>
</ul>

<p>Đếm ngược cũng quan trọng. Trên tám món thì gần như chắc chắn có món yếu, và người xem hồ sơ thường nhớ món tệ nhất. Cắt bớt là việc khó nhưng thường nâng chất bộ hồ sơ nhanh hơn làm thêm.</p>

<figure>
  <img src="assets/vplas-exploded-view-blender.jpg" alt="Ảnh tách rời linh kiện của một thiết bị điện tử dựng bằng Blender, các bộ phận treo lơ lửng theo trục dọc trên nền tối" loading="lazy" width="1600" height="900">
  <figcaption><strong>Một ảnh tách lớp kỹ thuật trong dự án VPLAS của LXAM Studio.</strong> Dạng hình này nặng về tổ chức tệp hơn là về thẩm mỹ, nên nó là món chứng minh rất tốt trong hồ sơ: người xem biết ngay bạn có đặt tên và gom bộ sưu tập tử tế hay không.</figcaption>
</figure>

<h2>Lộ trình sáu món khi kèm riêng, chia theo tuần</h2>

<p>Đây là nhịp chúng tôi dùng cho phần lớn người học đi làm, giả định tám tới mười hai giờ tự làm mỗi tuần và một buổi kèm mỗi tuần hoặc mỗi hai tuần.</p>

<h3>Tuần một tới hai: chọn món và dựng khối món đầu</h3>
<p>Không mở phần mềm trong nửa buổi đầu. Việc của hai tuần này là chốt danh sách món và tìm ảnh tham chiếu cho từng món. Rất nhiều hồ sơ thất bại ở đây chứ không ở khâu kỹ thuật, vì chọn món quá khó rồi bỏ giữa chừng.</p>

<h3>Tuần ba tới sáu: hai món sản phẩm đầu tiên</h3>
<p>Mỗi món khoảng hai tuần. Buổi kèm tập trung vào lưới và cạnh ở món một, vào vật liệu ở món hai. Nếu bạn còn yếu khâu dựng hình, phần nền tảng trong bài <a href="blog-khoa-hoc-modeling-3d.html">khoá học modeling 3D</a> là chỗ bù trước khi vào giai đoạn này.</p>

<h3>Tuần bảy tới mười: bối cảnh và ánh sáng</h3>
<p>Giai đoạn này đổi tính chất. Bạn không thêm chi tiết nữa mà học cách làm hình có sức nặng. Phần lớn chỗ kẹt ở đây là ánh sáng, và nó đáng được đọc trước: bài <a href="blog-5-loi-lighting.html">năm lỗi lighting</a> liệt kê đúng những lỗi hay xuất hiện trong hồ sơ người mới.</p>

<h3>Tuần mười một tới mười sáu: món theo yêu cầu và đóng gói</h3>
<p>Món cuối nên là một món dựng lại theo ảnh tham chiếu do người kèm đưa, không do bạn chọn. Đó là bài kiểm tra gần nhất với việc thật. Sau đó là hai tuần đóng gói: chọn góc, dựng trang trình bày, viết mô tả từng món.</p>

<p>Khâu đóng gói bị coi nhẹ nhiều nhất và lại là khâu đổi kết quả nhiều nhất. Cùng một bộ file, cách trình bày tốt hay tệ chênh nhau rất xa ở vòng lọc hồ sơ.</p>

<h2>Bảng so sánh ba cách làm portfolio 3D</h2>

<div class="table-wrap">
<table>
<thead><tr><th>Tiêu chí</th><th>Tự làm theo video</th><th>Khoá học có bài tập</th><th>Kèm 1 kèm 1 theo hồ sơ</th></tr></thead>
<tbody>
<tr><td>Món trong hồ sơ là của ai</td><td>Thường trùng bài của video</td><td>Trùng bài tập của lớp</td><td>Do bạn chọn, không trùng ai</td></tr>
<tr><td>Số lần được chữa file</td><td>Gần như không</td><td>Có, phải chờ lượt</td><td>Nhiều nhất</td></tr>
<tr><td>Nguy cơ bỏ giữa chừng</td><td>Cao nhất</td><td>Trung bình</td><td>Thấp, vì có hạn nộp riêng</td></tr>
<tr><td>Thời gian ra bộ bốn tới sáu món</td><td>Rất khó dự đoán</td><td>Thường dài hơn một khoá</td><td>Ước lượng mười tới mười sáu tuần</td></tr>
<tr><td>Chi phí theo buổi</td><td>Gần bằng không</td><td>Trung bình</td><td>Cao nhất</td></tr>
<tr><td>Chi phí theo một món hoàn chỉnh</td><td>Rất cao nếu không ra món nào</td><td>Trung bình</td><td>Thường thấp nhất</td></tr>
<tr><td>Dạy kỹ năng rộng</td><td>Trung bình</td><td>Tốt nhất</td><td>Hẹp, chỉ dạy cái món cần</td></tr>
<tr><td>Hợp nhất khi</td><td>Bạn mới làm quen phần mềm</td><td>Bạn cần nền tảng và nhịp</td><td>Bạn có hạn nộp hoặc đã kẹt lâu</td></tr>
</tbody>
</table>
</div>

<p>Bảng này không chọn hộ bạn. Nó chỉ ra một điều: kèm riêng theo hồ sơ hẹp về kiến thức và đó là nhược điểm thật. Nếu bạn chưa có nền, học kèm theo hồ sơ sẽ cho bạn bốn món đẹp nhưng nhiều lỗ hổng kỹ thuật. Muốn xem cách hai hệ chia bài theo tuần và đầu ra từng tuần, mở trang <a href="khoa-hoc.html">khoá học 3D Blender</a>.</p>

<h2>Kèm riêng dựng hình sản phẩm ra việc nhanh nhất</h2>

<p>Trong các nhóm chúng tôi từng kèm, người chọn hướng sản phẩm thường nhận việc đầu tiên sớm hơn người chọn hướng nhân vật hoặc hướng phim. Lý do không phải vì sản phẩm dễ hơn, mà vì thị trường Việt Nam mua dạng hình này nhiều hơn.</p>

<p>Nhu cầu thật nằm ở ảnh bán hàng, ảnh bao bì, ảnh thiết bị và phối cảnh trưng bày. Đó là lý do chúng tôi hay khuyên người cần việc sớm nhắm hướng này trước, kể cả khi sở thích của họ là hướng khác. Nội dung một lớp hướng sản phẩm được mô tả trong bài <a href="blog-khoa-hoc-dung-hinh-san-pham.html">khoá học dựng hình sản phẩm</a>, còn dạng việc thật mà studio nhận thì nằm ở trang <a href="dich-vu.html">dịch vụ render 3D sản phẩm</a>.</p>

<h2>Danh sách kiểm tra trước buổi kèm đầu tiên</h2>

<p>Chạy qua danh sách này với bất kỳ ai nhận kèm hồ sơ, kể cả với chúng tôi. Người làm nghề trả lời được hết, kể cả câu bất lợi cho họ.</p>

<ul>
<li>Buổi đầu có chốt danh sách món không, hay bắt đầu dạy kỹ thuật ngay?</li>
<li>Người kèm cho xem một file gốc của chính họ chứ không chỉ ảnh đã kết xuất?</li>
<li>Giữa hai buổi tôi nộp gì, và nhận phản hồi trong bao lâu?</li>
<li>Có được quyền hỏi lại sau khi khoá kết thúc không, trong bao lâu?</li>
<li>Khâu đóng gói và viết mô tả món có nằm trong phạm vi kèm không?</li>
<li>Nếu tới buổi cuối mà tôi chưa xong bộ món thì xử lý thế nào?</li>
</ul>

<p>Câu cuối là câu quan trọng nhất và cũng là câu hay bị trả lời vòng vo. Một chương trình tử tế nói rõ trước rằng kết quả phụ thuộc vào số giờ bạn tự làm, và nói luôn cơ chế khi bạn trượt tiến độ.</p>

<h2>Khi nào chưa nên thuê kèm 1 kèm 1, nói thẳng</h2>

<p>Ba tình huống dưới đây, trả tiền bây giờ là lãng phí.</p>

<p><strong style="color:#fff;">Bạn chưa dựng xong món nào.</strong> Giai đoạn làm quen giao diện không cần người kèm. Hãy tự đi một tháng theo một lộ trình có thứ tự, ví dụ bảy bước trong bài <a href="blog-lo-trinh-tu-hoc-blender.html">lộ trình tự học Blender</a>, rồi mới tính chuyện thuê kèm.</p>

<p><strong style="color:#fff;">Bạn không có tám giờ mỗi tuần để tự làm.</strong> Kèm riêng không thay được số giờ ngồi vào bàn. Nếu lịch của bạn chỉ cho hai ba giờ một tuần, buổi kèm sẽ thành buổi nghe lại cùng một lời nhắc, và tiền đó nên để dành tới lúc rảnh hơn.</p>

<p><strong style="color:#fff;">Bạn chưa biết mình muốn nhận loại việc nào.</strong> Hồ sơ phải nhắm một hướng mới có sức. Nếu bạn còn phân vân giữa sản phẩm, nội thất, nhân vật và phim, hãy đọc phần hướng nghề trong <a href="cam-nang.html">cẩm nang học Blender</a> và chốt hướng trước, vì chọn sai hướng làm hỏng cả bộ món chứ không chỉ một món.</p>

<h2>Kèm 1 kèm 1 làm portfolio 3D không thay được số giờ của bạn</h2>

<p>Điều này cần nói thẳng ở cuối. Người kèm rút ngắn thời gian bạn đi sai đường, chỉ ra trong mười phút chỗ bạn có thể mò ba tuần. Nhưng toàn bộ số giờ dựng, sửa và kết xuất vẫn là của bạn. Mốc thời gian thực tế cho từng chặng nằm trong bài <a href="blog-hoc-blender-3d-bao-lau.html">học Blender 3D bao lâu</a>.</p>

<p>Nếu có ai hứa với bạn một bộ hồ sơ hoàn chỉnh mà không cần bạn bỏ ra hàng trăm giờ, đó là lời nên bị hỏi lại rất kỹ. Hồ sơ là bằng chứng về số giờ, nên nó không thể được mua tách khỏi số giờ đó.</p>

<h2>Hỏi đáp</h2>

<p class="faq-q">Kèm 1 kèm 1 làm portfolio 3D khác lớp học 3D thường ở đâu?</p>
<p>Lớp thường dạy kỹ năng theo giáo trình, bài tập là bài tập chung của lớp. Kèm riêng theo hồ sơ lấy đích đến là bộ món bạn sẽ đem đi xin việc, nên mọi buổi đều xoay quanh một món cụ thể trong bộ đó. Hệ quả là bạn học ít kỹ thuật hơn nhưng ra sản phẩm hoàn chỉnh nhanh hơn.</p>

<p class="faq-q">Portfolio 3D cần mấy món thì đủ để nộp?</p>
<p>Bốn tới sáu món hoàn chỉnh là khoảng hợp lý. Dưới bốn thì người xem không phân biệt được bạn làm được hay chỉ may mắn một lần. Trên tám thì gần như chắc chắn có món yếu kéo cả bộ xuống, vì người tuyển thường đánh giá theo món tệ nhất chứ không theo món đẹp nhất.</p>

<p class="faq-q">Kèm 1 kèm 1 làm portfolio 3D mất bao lâu?</p>
<p>Ước lượng từ các nhóm chúng tôi đã kèm là khoảng mười tới mười sáu tuần cho một bộ bốn tới sáu món, với nhịp tám tới mười hai giờ tự làm mỗi tuần. Con số dao động mạnh theo độ phức tạp món bạn chọn và theo việc bạn có nộp bài đúng hạn giữa hai buổi hay không.</p>

<p class="faq-q">Chưa biết gì về Blender có nên kèm riêng để làm portfolio luôn không?</p>
<p>Không nên. Giai đoạn làm quen giao diện và dựng khối cơ bản không cần người kèm, tài liệu miễn phí đủ dùng và trả tiền cho nó là lãng phí. Mốc hợp lý để bắt đầu kèm theo hồ sơ là khi bạn đã tự dựng xong ít nhất một món và tự thấy nó chưa đẹp nhưng không chỉ ra được vì sao.</p>

<p class="faq-q">Portfolio 3D nên đưa ảnh kết xuất hay cả file gốc?</p>
<p>Đưa ảnh trước, nhưng luôn chuẩn bị sẵn file gốc để mở khi được hỏi. Nhiều studio hỏi xem lưới và cách tổ chức bộ sưu tập ngay trong buổi phỏng vấn, vì ảnh đẹp có thể đến từ nhiều nguồn còn cấu trúc file thì không giả được.</p>

<hr class="hr">

<p>Nếu bạn muốn biết bộ món hiện tại của mình còn thiếu gì, gửi cho chúng tôi ba bốn hình bạn đang có và một câu nói rõ bạn muốn nhận loại việc nào. Chúng tôi sẽ nói thẳng nên bỏ món nào và thêm món nào, kể cả khi câu trả lời là bạn chưa cần thuê kèm. Muốn xem cách hai hệ chia bài và chữa bài theo tuần, trang <a href="khoa-hoc.html">khoá học 3D Blender</a> ghi rõ đầu ra từng tuần.</p>
""",
    },
]



# ---------------------------------------------------------------- SEO: muc luc + bai lien quan
def _slugify(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = t.replace("đ", "d").replace("Đ", "D").lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:60] or "muc"


def with_toc(body):
    """Them id cho moi h2 va tra ve (body moi, khoi muc luc)."""
    items, used = [], set()
    def rep(m):
        inner = m.group(1)
        sl = _slugify(inner)
        n, base = 2, sl
        while sl in used:
            sl = "%s-%d" % (base, n); n += 1
        used.add(sl)
        items.append((sl, re.sub(r"<[^>]+>", "", inner)))
        return '<h2 id="%s">%s</h2>' % (sl, inner)
    body = re.sub(r"<h2>(.*?)</h2>", rep, body, flags=re.S)
    if len(items) < 3:
        return body, ""
    li = "".join('<li><a href="#%s">%s</a></li>' % (sl, html.escape(t)) for sl, t in items)
    toc = ('<nav class="toc" aria-label="Mục lục bài viết">'
           '<p class="toc-h">Trong bài này</p><ol>%s</ol></nav>' % li)
    return body, toc


# Hai bai viet tay khong sinh tu POSTS. Khai bao o day de chung xuat hien
# trong danh sach blog.html va sitemap, tranh thanh trang mo coi.
EXTRA_POSTS = [
    {
        "slug": "render-nhanh-hon-blender-cycles",
        "title": "Cách render nhanh hơn trong Blender Cycles",
        "desc": "Mười cách cắt thời gian render Cycles mà không làm hình xấu đi: noise threshold, denoise, bounce, volumetric, OptiX và những thứ không nên đụng vào.",
        "tag": "Kỹ thuật",
        "date": "2026-09-10",
        "date_vn": "10/09/2026",
        "read": "9 phút đọc",
        "thumb": "assets/vplas-chi-tiet-cong-sac-render.jpg",
    },
    {
        "slug": "blender-hay-3dsmax-c4d",
        "title": "Blender hay 3ds Max, C4D? So sánh cho người mới",
        "desc": "So sánh Blender, 3ds Max, Cinema 4D và Maya theo mục tiêu nghề nghiệp tại Việt Nam, phần kỹ năng chuyển được giữa các phần mềm và cách chọn đỡ mất thời gian.",
        "tag": "Định hướng",
        "date": "2026-09-10",
        "date_vn": "10/09/2026",
        "read": "8 phút đọc",
        "thumb": "assets/hero-poster.jpg",
    },
]


def brand_title(t):
    """Giu the title duoi 60 ky tu: du cho thi gan thuong hieu day, khong du thi gan ngan hoac bo."""
    for suf in (" | LXAM Studio", " | LXAM"):
        if len(t) + len(suf) <= 60:
            return t + suf
    return t


def related_html(p):
    same = [x for x in POSTS if x is not p and x["tag"] == p["tag"]]
    other = [x for x in POSTS if x is not p and x["tag"] != p["tag"]]
    picks = (same + other)[:3]
    if not picks:
        return ""
    cards = "".join(
        '<a class="rel-c" href="blog-%s.html"><img src="%s" alt="%s" loading="lazy" width="640" height="360">'
        '<span class="rel-t">%s</span><span class="rel-k">%s</span></a>'
        % (x["slug"], x["thumb"], html.escape(x["title"]), html.escape(x["title"]), x["read"])
        for x in picks)
    return ('<section class="rel" aria-label="Bài viết liên quan">'
            '<p class="rel-h">Đọc tiếp</p><div class="rel-g">%s</div></section>' % cards)


POST_TPL = """
<main>
  <article class="prose">
    <div class="wrap-narrow">
      <a href="blog.html" style="display:inline-block;font-size:13px;color:#9a8f84;text-decoration:none;margin-bottom:26px;">← Tất cả bài viết</a>
      <span class="tag">{tag}</span>
      <h1 style="margin-top:18px;font-size:clamp(26px,4.2vw,44px);">{title}</h1>
      <p class="post-meta" style="margin-bottom:34px;">{date_vn} · {read}</p>
      <img src="{thumb}" alt="{title_plain}" width="1280" height="720" fetchpriority="high" decoding="async" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:4px;margin:0 0 40px;">
      {toc}
      {body}
      {sources}
      {related}
      <hr class="hr">
      <div class="card" style="text-align:center;border-color:rgba(255,122,26,.28);background:rgba(255,122,26,.05);">
        <h3 style="margin-bottom:12px;">Muốn được sửa bài trực tiếp?</h3>
        <p style="margin:0 auto 22px;max-width:460px;">Coaching 1:1 online, đồng hành trọn một năm. Để lại thông tin, tôi xem qua và tư vấn bạn nên bắt đầu từ đâu.</p>
        <a class="lxcta" href="lo-trinh.html#dangky">Đăng ký tư vấn</a>
      </div>
    </div>
  </article>
</main>
"""


def blog_index():
    cards = []
    allp = sorted(POSTS + EXTRA_POSTS, key=lambda x: x["date"], reverse=True)
    for p in allp:
        cards.append(f"""      <a class="post-card" href="blog-{p['slug']}.html">
        <div class="thumb"><img src="{p['thumb']}" alt="{html.escape(p['title'])}" width="640" height="360" loading="lazy" decoding="async"></div>
        <div class="body">
          <span class="tag" style="align-self:flex-start;">{p['tag']}</span>
          <h3 style="margin:6px 0 0;">{html.escape(p['title'])}</h3>
          <p style="font-size:14.5px;line-height:1.7;margin:0;flex:1;">{html.escape(p['desc'])}</p>
          <p class="post-meta" style="margin:6px 0 0;">{p['date_vn']} · {p['read']}</p>
        </div>
      </a>""")
    return f"""
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow">Blog</p>
      <h1>Ghi chép từ<br>bàn làm việc</h1>
      <p class="lead" style="max-width:700px;">Những thứ tôi rút ra khi làm job thật và khi sửa bài cho học viên. Không có bài nào ở đây là lý thuyết chép lại, nếu tôi chưa từng vấp phải nó, tôi không viết.</p>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="grid3">
{chr(10).join(cards)}
      </div>
    </div>
  </section>
</main>
"""


# ---------------------------------------------------------------- STUDENT AREA
HOCVIEN_BODY = f"""
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow">Khu học viên</p>
      <h1>Không gian riêng<br>của học viên LXAM</h1>
      <p class="lead" style="max-width:720px;">Nơi tập trung toàn bộ tài nguyên đi kèm khoá học: bài giảng, file dự án, thư viện asset, lịch buổi kèm và khu nộp bài để được sửa.</p>
      <div style="display:inline-flex;align-items:center;gap:10px;margin-top:6px;padding:11px 20px;border-radius:999px;border:1px dashed rgba(255,122,26,.4);background:rgba(255,122,26,.05);">
        <span style="width:7px;height:7px;border-radius:50%;background:#ff7a1a;display:block;"></span>
        <span style="font-size:13.5px;color:#e2dad2;">Hệ thống đăng nhập đang được hoàn thiện, học viên hiện tại nhận tài nguyên qua nhóm kín và email.</span>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>Bên trong có gì</h2>
      <div class="grid3" style="margin-top:32px;">
        <div class="card">
          <h3>Bài giảng đã ghi</h3>
          <p style="margin:0;">Toàn bộ buổi học được ghi lại, chia theo từng kỹ năng trong lộ trình. Xem lại bất cứ lúc nào, không giới hạn số lần.</p>
        </div>
        <div class="card">
          <h3>File dự án gốc</h3>
          <p style="margin:0;">File .blend của các shot dùng trong bài giảng, mở ra xem trực tiếp cách setup đèn, node vật liệu và tổ chức scene.</p>
        </div>
        <div class="card">
          <h3>Thư viện tài nguyên</h3>
          <p style="margin:0;">HDRI, texture, preset render và các asset dùng chung, được chọn lọc để bạn không mất thời gian đi tìm.</p>
        </div>
        <div class="card">
          <h3>Nộp bài &amp; nhận sửa</h3>
          <p style="margin:0;">Khu nộp bài theo từng module. Mỗi bài được sửa kèm ảnh so sánh trước/sau và ghi chú cụ thể phải chỉnh gì.</p>
        </div>
        <div class="card">
          <h3>Lịch buổi kèm 1:1</h3>
          <p style="margin:0;">Xem lịch, đặt buổi và theo dõi số buổi còn lại trong gói của bạn.</p>
        </div>
        <div class="card">
          <h3>Cẩm nang &amp; tài liệu</h3>
          <p style="margin:0;">Cẩm nang Blender từ Basic lên Master cùng các bảng tra cứu dùng khi làm việc thật: checklist lighting, quy trình render, mẫu báo giá.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="grid2" style="gap:44px;align-items:start;">
        <div>
          <p class="eyebrow">Truy cập</p>
          <h2>Bạn đang là học viên?</h2>
          <p>Điền form bên cạnh, tôi sẽ gửi lại đường dẫn nhóm kín và toàn bộ tài nguyên của gói bạn đang học, thường trong vòng 24 giờ.</p>
          <p>Chưa học nhưng muốn tìm hiểu? Xem trước <a href="khoa-hoc.html" style="color:#ff7a1a;">các gói khoá học</a> hoặc đọc <a href="blog.html" style="color:#ff7a1a;">blog</a>, phần lớn kiến thức nền tôi để công khai.</p>
          <div style="margin-top:26px;display:flex;flex-direction:column;gap:12px;">
            <a href="https://www.facebook.com/lxamstudio/" target="_blank" rel="noopener" style="font-size:14px;color:#cfc6bd;text-decoration:none;">Fanpage Studio ↗</a>
            <a href="tel:0942890363" style="font-size:14px;color:#cfc6bd;text-decoration:none;">Hotline 0942 890 363</a>
          </div>
        </div>
        <div class="card">
          <form id="hvform" novalidate>
            <label for="hv-name" style="display:block;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#9a8f84;margin-bottom:8px;">Họ và tên</label>
            <input id="hv-name" name="name" required autocomplete="name" placeholder="Nguyễn Văn A" style="width:100%;padding:13px 15px;border-radius:4px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);color:#f2ebe4;font-size:15px;font-family:inherit;margin-bottom:18px;">
            <label for="hv-email" style="display:block;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#9a8f84;margin-bottom:8px;">Email</label>
            <input id="hv-email" name="email" type="email" required autocomplete="email" inputmode="email" placeholder="ban@email.com" style="width:100%;padding:13px 15px;border-radius:4px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);color:#f2ebe4;font-size:15px;font-family:inherit;margin-bottom:18px;">
            <label for="hv-phone" style="display:block;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#9a8f84;margin-bottom:8px;">Số điện thoại</label>
            <input id="hv-phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="09xx xxx xxx" style="width:100%;padding:13px 15px;border-radius:4px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);color:#f2ebe4;font-size:15px;font-family:inherit;margin-bottom:18px;">
            <label for="hv-goi" style="display:block;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#9a8f84;margin-bottom:8px;">Bạn đang học gói nào</label>
            <select id="hv-goi" name="goi" style="width:100%;padding:13px 15px;border-radius:4px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.04);color:#f2ebe4;font-size:15px;font-family:inherit;margin-bottom:24px;appearance:none;"><option value="" style="background:#0d0d0d;">Chọn gói</option><option style="background:#0d0d0d;">Tự học có chữa bài</option><option style="background:#0d0d0d;">Lớp 8 tuần</option><option style="background:#0d0d0d;">Kèm riêng 1:1</option><option style="background:#0d0d0d;">Chưa chắc</option></select>
            <button type="submit" class="lxcta" style="width:100%;border:0;padding:15px;font-size:15px;font-family:inherit;cursor:pointer;">Gửi yêu cầu truy cập</button>
            <p id="hvmsg" style="display:none;margin:18px 0 0;font-size:14.5px;color:#ff7a1a;text-align:center;"></p>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>
<script>
(function(){{
  var ENDPOINT='{ENDPOINT}';
  var f=document.getElementById('hvform'), msg=document.getElementById('hvmsg');
  if(!f) return;
  f.addEventListener('submit', function(e){{
    e.preventDefault();
    var g=function(n){{ var el=f.querySelector('[name="'+n+'"]'); return el?el.value.trim():''; }};
    if(!g('name')||!g('email')||!g('phone')){{
      msg.style.display='block'; msg.style.color='#ff6b5a';
      msg.textContent='Bạn điền giúp mình tên, email và số điện thoại nhé.';
      return;
    }}
    var d=new URLSearchParams();
    d.append('name',g('name')); d.append('email',g('email'));
    d.append('phone',g('phone')); d.append('fb','');
    d.append('pkg','Yêu cầu truy cập khu học viên · '+(g('goi')||'chưa chọn gói'));
    d.append('src',location.href);
    var sent=false;
    try{{ if(navigator.sendBeacon) sent=navigator.sendBeacon(ENDPOINT,d); }}catch(err){{}}
    if(!sent){{ try{{ fetch(ENDPOINT,{{method:'POST',mode:'no-cors',body:d,keepalive:true}}); }}catch(err){{}} }}
    f.reset();
    msg.style.display='block'; msg.style.color='#ff7a1a';
    msg.textContent='Đã nhận. Mình sẽ gửi đường dẫn qua email trong vòng 24 giờ.';
  }});
}})();
</script>
"""


def sources_html(items):
    if not items:
        return ""
    lis = "".join(
        '<li><a href="%s" target="_blank" rel="noopener" style="color:#ff7a1a;">%s</a></li>'
        % (u, html.escape(t)) for t, u in items
    )
    return ('<hr class="hr">'
            '<h2 style="font-size:clamp(19px,2.2vw,26px);">Nguồn tham khảo</h2>'
            '<p style="font-size:14.5px;color:#9a8f84;">Bài viết là phân tích và quan điểm riêng của LXAM Studio, '
            'dựa trên thông tin từ các nguồn dưới đây. Bấm vào để đọc bản gốc.</p>'
            '<ul style="margin-top:14px;">%s</ul>' % lis)


def jsonld_post(p):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["desc"],
        "image": "https://lxamstudio.com/" + p["thumb"],
        "datePublished": p["date"],
        "dateModified": p.get("updated", p["date"]),
        "inLanguage": "vi-VN",
        "mainEntityOfPage": {"@type": "WebPage",
                             "@id": "https://lxamstudio.com/blog-%s.html" % p["slug"]},
        "author": {"@type": "Organization", "name": "LXAM Studio",
                   "url": "https://lxamstudio.com/"},
        "publisher": {"@type": "Organization", "name": "LXAM Studio",
                      "logo": {"@type": "ImageObject",
                               "url": "https://lxamstudio.com/assets/2792c6e0.png"}},
    }
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ",
             "item": "https://lxamstudio.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog",
             "item": "https://lxamstudio.com/blog.html"},
            {"@type": "ListItem", "position": 3, "name": p["title"],
             "item": "https://lxamstudio.com/blog-%s.html" % p["slug"]},
        ],
    }
    out = ['<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False),
           '<script type="application/ld+json">%s</script>' % json.dumps(crumbs, ensure_ascii=False)]
    if p.get("faq"):
        faq = {"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q,
                               "acceptedAnswer": {"@type": "Answer", "text": a}}
                              for q, a in p["faq"]]}
        out.append('<script type="application/ld+json">%s</script>' % json.dumps(faq, ensure_ascii=False))
    return "\n".join(out)


def jsonld_simple(kind, name, desc, url):
    import json
    return '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": kind, "name": name,
        "description": desc, "url": url, "inLanguage": "vi-VN",
        "publisher": {"@type": "Organization", "name": "LXAM Studio",
                      "url": "https://lxamstudio.com/"},
    }, ensure_ascii=False)


def main():
    write("ve-chung-toi.html",
          head("Về LXAM Studio | Studio visual 3D Việt Nam",
               "LXAM Studio: studio visual 3D tại Việt Nam làm TVC, render sản phẩm và animation kỹ thuật, đồng thời đào tạo Blender 1:1. Founder, hệ triết lý và quan điểm nghề.",
               "about",
               canonical="ve-chung-toi.html",
               og_image="assets/a26a7e39.jpg",
               jsonld=ABOUT_LD)
          + ABOUT_BODY + FOOTER)

    write("blog.html",
          head("Blog 3D và Blender | LXAM Studio",
               "Ghi chép về Blender, lighting, render và nghề 3D thương mại từ bàn làm việc LXAM Studio: lộ trình học, lỗi thường gặp và quy trình job thật.",
               "blog",
               canonical="blog.html",
               og_image=POSTS[0]["thumb"],
               jsonld=jsonld_simple("Blog", "Blog LXAM Studio",
                                    "Bài viết về Blender, lighting, render và nghề 3D thương mại",
                                    "https://lxamstudio.com/blog.html"))
          + blog_index() + FOOTER)

    for p in POSTS:
        body_html_, toc_ = with_toc(p["body"])
        body = POST_TPL.format(
            tag=p["tag"], title=html.escape(p["title"]),
            title_plain=html.escape(p["title"]),
            date_vn=(p["date_vn"] + " · Cập nhật " + p["updated_vn"]) if p.get("updated_vn") else p["date_vn"],
            read=p["read"],
            thumb=p["thumb"], body=body_html_, toc=toc_,
            related=related_html(p),
            sources=sources_html(p.get("sources")),
        )
        write("blog-%s.html" % p["slug"],
              head(brand_title(p["title"]), p["desc"], "blog",
                   canonical="blog-%s.html" % p["slug"],
                   og_image=p["thumb"],
                   og_type="article", published=p["date"],
                   jsonld=jsonld_post(p))
              + body + FOOTER)

    write("hoc-vien.html",
          head("Khu học viên | LXAM Studio",
               "Khu học viên LXAM Studio: bài giảng đã ghi, file .blend dự án gốc, thư viện asset dùng được cho job thật, khu nộp bài để được sửa và lịch buổi kèm 1 kèm 1.",
               "hocvien",
               canonical="hoc-vien.html",
               jsonld=jsonld_simple("WebPage", "Khu học viên LXAM Studio",
                                    "Tài nguyên dành cho học viên LXAM Studio",
                                    "https://lxamstudio.com/hoc-vien.html"))
          + HOCVIEN_BODY + FOOTER)

    # sitemap
    P9 = ["cam-nang.html", "lo-trinh.html", "lo-trinh-3d-automotive.html", "lo-trinh-3d-ai.html"]
    P8 = ["dich-vu.html", "khoa-hoc.html", "du-an-event.html", "du-an-chivas-18.html", "du-an-chivas-18-chai-xviii.html", "du-an-chivas-15-trung-bay.html", "du-an-trien-lam-axe.html",
          "du-an-automotive.html", "du-an-mercedes-g63-tvc.html", "du-an-porsche-911.html",
          "du-an-mclaren-765lt.html", "du-an-aston-martin-dbx.html", "du-an-volvo-s90.html",
          "du-an-san-pham.html", "du-an-vplas.html", "du-an-jhm-masonry-hanger.html",
          "du-an-khoa-cua-thong-minh.html", "du-an-jewelry.html", "du-an-locphuc-10-nam.html",
          "du-an-locphuc-bo-suu-tap.html", "du-an-hoc-vien.html",
          "nghe-nghiep.html", "ve-chung-toi.html", "blog.html"]
    urls = [""] + P9 + P8 + ["hoc-vien.html"] + ["blog-%s.html" % p["slug"] for p in POSTS] \
           + ["blog-%s.html" % p["slug"] for p in EXTRA_POSTS]
    # lastmod chi gan cho trang ma ta biet chac ngay doi: cac bai blog.
    lastmod = {}
    for p_ in POSTS + EXTRA_POSTS:
        lastmod["blog-%s.html" % p_["slug"]] = p_.get("updated") or p_["date"]

    rows = []
    for u in urls:
        pri = "1.0" if u == "" else ("0.9" if u in P9 else ("0.8" if u in P8 else "0.7"))
        freq = "weekly" if u in ("", "blog.html") else "monthly"
        lm = lastmod.get(u)
        lm_tag = "<lastmod>%s</lastmod>" % lm if lm else ""
        rows.append('  <url><loc>https://lxamstudio.com/%s</loc>%s'
                    '<changefreq>%s</changefreq><priority>%s</priority></url>' % (u, lm_tag, freq, pri))
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(rows) + "\n</urlset>\n")


if __name__ == "__main__":
    main()
