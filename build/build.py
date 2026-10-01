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
<link rel="stylesheet" href="assets/lx.css?v=den2">
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
    <img src="assets/2792c6e0.png" alt="LXAM" class="lxlogo-icon">
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
        <img src="assets/2792c6e0.png" alt="LXAM" style="width:40px;height:40px;">
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

  <section>
    <div class="wrap">
      <div class="grid2" style="gap:48px;align-items:start;">
        <div>
          <p class="eyebrow">Câu chuyện</p>
          <h2>Bắt đầu từ năm ba đại học,<br>với Blender và một cái máy vừa đủ</h2>
        </div>
        <div>
          <p>Tôi vào nghề sớm hơn dự định, năm ba đại học, công cụ trong tay chỉ có Blender và vài phần mềm Adobe. Không có studio đứng sau, không có ai cầm tay chỉ việc. Mọi thứ học được đều đến từ việc nhận job, làm hỏng, sửa, rồi làm lại cho tới khi khách gật đầu.</p>
          <p>Mười năm sau, tôi dẫn dắt một team Multimedia trong phòng Marketing, đồng thời vận hành LXAM Studio nhận các dự án TVC và hình ảnh thương mại. Hai vai trò đó nuôi nhau: cái nhìn của người duyệt bài giúp tôi biết một portfolio thiếu gì, còn việc trực tiếp làm job giúp tôi không dạy những thứ đã lỗi thời.</p>
          <p>Điều khiến tôi mở lớp không phải vì thiếu khoá học Blender trên mạng, có quá nhiều là đằng khác. Mà vì gần như không khoá nào trả lời được câu hỏi thật sự khó: <strong style="color:#fff;">làm sao đi từ chỗ biết dùng phần mềm đến chỗ có người trả tiền cho sản phẩm của bạn.</strong></p>
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
        <div class="grid2" style="gap:16px;">
          <img src="assets/a26a7e39.jpg" alt="Dự án TVC ô tô" width="1200" height="900" loading="lazy" style="border-radius:4px;width:100%;aspect-ratio:4/3;object-fit:cover;">
          <img src="assets/card-chivas18.webp" alt="Phối cảnh 3D triển lãm Chivas Regal 18" width="1600" height="1000" loading="lazy" style="border-radius:4px;width:100%;aspect-ratio:4/3;object-fit:cover;">
          <img src="assets/b64a4cd7.jpg" alt="Dự án hard-surface" width="1200" height="900" loading="lazy" style="border-radius:4px;width:100%;aspect-ratio:4/3;object-fit:cover;">
          <img src="assets/4c9ff169.jpg" alt="Dự án render thương mại" width="1200" height="900" loading="lazy" style="border-radius:4px;width:100%;aspect-ratio:4/3;object-fit:cover;">
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


# ---------------------------------------------------------------- BLOG POSTS
POSTS = [
    {
        "slug": "lo-trinh-tu-hoc-blender",
        "title": "Lộ trình tự học Blender: 7 kỹ năng, và thứ tự bạn không nên đảo",
        "desc": "Phần lớn người mới bỏ Blender không phải vì khó, mà vì học sai thứ tự. Đây là trình tự 7 kỹ năng và lý do từng bước phải đứng ở vị trí đó.",
        "tag": "Lộ trình",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "8 phút đọc",
        "thumb": "assets/2cdbf5f9.jpg",
        "body": """
<p class="lead">Tôi gặp câu hỏi này gần như mỗi tuần: "Em nên học gì trước?". Câu trả lời ngắn là modeling. Câu trả lời dài, và hữu ích hơn, là vì sao thứ tự lại quan trọng đến thế.</p>

<p>Blender là phần mềm hiếm hoi làm được gần như mọi khâu trong một pipeline 3D. Đó vừa là điểm mạnh vừa là cái bẫy: người mới mở lên, thấy hai chục tab, và bắt đầu học theo thứ tự ngẫu nhiên của video YouTube được đề xuất. Ba tháng sau họ biết dựng một cái ghế, biết bấm nút render, nhưng không giải thích được vì sao ảnh của mình trông rẻ tiền.</p>

<h2>Vì sao thứ tự quan trọng</h2>

<p>Mỗi kỹ năng trong 3D đều đứng trên vai kỹ năng trước nó. Bạn không thể đánh giá vật liệu của mình đúng hay sai nếu ánh sáng đang sai. Bạn không thể sửa ánh sáng nếu hình khối đã lệch. Học đảo thứ tự nghĩa là bạn liên tục sửa triệu chứng thay vì sửa nguyên nhân, và đó là lý do người ta bỏ cuộc, chứ không phải vì Blender khó.</p>

<blockquote><p>Một cái model sai tỉ lệ, lighting đẹp cỡ nào cũng không cứu được. Nhưng một cái model đúng, chỉ cần một nguồn sáng tử tế là đã dùng được.</p></blockquote>

<h2>Bảy kỹ năng, theo đúng thứ tự</h2>

<h3>1. Modeling: dựng hình</h3>
<p>Đây là nền. Không phải để bạn dựng được thứ phức tạp, mà để bạn đọc được hình khối: tỉ lệ, topology, đâu là bề mặt cong thật và đâu là cong giả. Người dựng hình tốt tiết kiệm được hàng giờ ở mọi khâu phía sau.</p>
<p><strong style="color:#fff;">Dấu hiệu bạn đã qua bước này:</strong> nhìn một vật thể ngoài đời, bạn phác được trong đầu nó gồm mấy khối cơ bản và nối với nhau ra sao.</p>

<h3>2. Materials: vật liệu</h3>
<p>Vật liệu là nơi người mới hay đốt thời gian nhất mà thu về ít nhất, vì họ chỉnh nó dưới ánh sáng sai. Học đủ để hiểu ba thông số thật sự quan trọng là base color, roughness và metallic, rồi đi tiếp. Phần còn lại quay lại sau khi biết lighting.</p>

<h3>3. Lighting: ánh sáng</h3>
<p>Đây là bước tạo ra khác biệt lớn nhất giữa ảnh nghiệp dư và ảnh thương mại, và cũng là bước bị bỏ qua nhiều nhất. Ánh sáng quyết định người xem nhìn vào đâu, cảm thấy gì, và tin sản phẩm đó đắt hay rẻ.</p>
<p>Nếu bạn chỉ có thời gian để giỏi một kỹ năng duy nhất trong bảy cái này, chọn cái này.</p>

<h3>4. Rendering: kết xuất</h3>
<p>Không phải học bấm nút render, mà học đọc kết quả: nhiễu đến từ đâu, vì sao cảnh này lâu bất thường, khi nào nên dùng Cycles và khi nào EEVEE là đủ. Hiểu render giúp bạn tiết kiệm hàng chục giờ chờ máy mỗi tháng.</p>

<h3>5. Hard-surface: bề mặt cứng</h3>
<p>Đến đây bạn mới nên đụng vào sản phẩm công nghiệp: máy móc, thiết bị, xe cộ. Hard-surface đòi hỏi kỷ luật về topology và bevel mà ba bước đầu đã rèn cho bạn. Vào sớm hơn, bạn sẽ chỉ tạo ra những khối méo mà không biết vì sao nó méo.</p>

<h3>6. Animation: chuyển động</h3>
<p>Chuyển động là ngôn ngữ riêng, không phải phần mở rộng của dựng hình. Timing, easing, và quan trọng nhất là biết khi nào <em>không</em> nên cho vật thể chuyển động. Một shot sản phẩm đứng yên với camera trôi chậm thường thuyết phục hơn một shot mọi thứ đều quay.</p>

<h3>7. VFX &amp; hậu kỳ</h3>
<p>Bước cuối, và là bước dễ bị lạm dụng nhất. Hậu kỳ để nâng một shot đã tốt lên, không phải để cứu một shot hỏng. Nếu bạn thấy mình đang kéo curve rất nhiều để ảnh "đỡ tệ", vấn đề nằm ở khâu ba hoặc khâu một.</p>

<hr class="hr">

<h2>Mất bao lâu?</h2>

<p>Câu trả lời thành thật: tuỳ vào việc bạn có được sửa bài hay không. Tự học, phần lớn người ta mất một đến hai năm để đi hết bảy bước này, và đa số dừng ở bước ba. Có người sửa bài đều đặn, quãng đường đó rút xuống đáng kể, không phải vì bạn học nhanh hơn, mà vì bạn không mất sáu tháng đi sai đường rồi mới phát hiện.</p>

<p>Nếu bạn đã đi được tới bước ba rồi đứng yên, đó đúng là lúc hình thức <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> phát huy, vì cái bạn thiếu không còn là bài giảng mà là người chẩn đoán đúng chỗ kẹt.</p>

<p>Nếu bạn đang tự học và thấy mình mắc kẹt ở đâu đó trong bảy bước trên, cứ nhắn cho tôi mô tả chỗ kẹt. Tôi trả lời được thì trả lời, không thì chỉ bạn chỗ tìm. Không cần đăng ký gì cả.</p>
""",
    },
    {
        "slug": "5-loi-lighting",
        "title": "5 lỗi lighting khiến render của bạn trông rẻ tiền",
        "desc": "Không phải do máy yếu hay thiếu plugin. Năm lỗi ánh sáng dưới đây gặp ở gần như mọi bài tự học, và cái nào cũng sửa được trong một buổi.",
        "tag": "Kỹ thuật",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "6 phút đọc",
        "thumb": "assets/2afcaceb.jpg",
        "body": """
<p class="lead">Khi ai đó gửi tôi một bài render và hỏi "sao nhìn nó chưa đã", tám trên mười lần vấn đề nằm ở ánh sáng, không phải model, không phải vật liệu, và gần như không bao giờ là do card đồ hoạ.</p>

<p>Dưới đây là năm lỗi tôi gặp nhiều nhất. Không cái nào cần plugin trả phí để sửa.</p>

<h2>1. Dùng đúng một HDRI và gọi đó là lighting</h2>

<p>HDRI cho bạn ánh sáng môi trường tử tế trong ba mươi giây, nên rất dễ dừng lại ở đó. Vấn đề là HDRI chiếu đều từ mọi phía. Nó xoá đi cái bạn cần nhất: hướng. Không có hướng thì không có khối, không có khối thì vật thể trông như dán lên nền.</p>

<p><strong style="color:#fff;">Sửa:</strong> giữ HDRI làm nền, hạ cường độ xuống còn khoảng một phần ba, rồi thêm một area light làm nguồn chính. Chỉ một đèn thôi. So sánh trước/sau, bạn sẽ thấy vật thể đột nhiên có trọng lượng.</p>

<h2>2. Đèn quá nhỏ so với vật thể</h2>

<p>Đây là lỗi âm thầm nhất. Nguồn sáng nhỏ tạo bóng đổ sắc cạnh và highlight nhỏ như đầu kim, thứ ngoài đời chỉ xuất hiện dưới nắng gắt hoặc đèn flash trần. Sản phẩm chụp studio luôn dùng nguồn lớn, vì nguồn lớn cho chuyển sáng mềm dọc theo bề mặt cong, và chính cái chuyển đó nói cho mắt người biết vật thể làm bằng gì.</p>

<p><strong style="color:#fff;">Sửa:</strong> phóng area light của bạn to lên. To hơn nữa. Quy tắc thô: nguồn chính nên lớn ít nhất bằng vật thể, thường là gấp hai đến ba lần.</p>

<blockquote><p>Nếu highlight trên bề mặt kim loại của bạn là một chấm nhỏ thay vì một vệt dài, đèn của bạn đang quá nhỏ.</p></blockquote>

<h2>3. Không có gì để phản chiếu</h2>

<p>Kim loại và nhựa bóng không tự đẹp, chúng đẹp nhờ những gì xung quanh phản chiếu vào. Render một chiếc đồng hồ trong không gian trống, bề mặt của nó sẽ chỉ có màu xám chết. Studio thật luôn đầy vật thể: hắt sáng, cờ đen, tường, trần.</p>

<p><strong style="color:#fff;">Sửa:</strong> đặt vài mặt phẳng lớn quanh vật thể, một trắng để hắt sáng, một đen để tạo mảng tối tương phản trên cạnh. Tắt bóng đổ của chúng nếu cần. Chi phí render gần như bằng không, khác biệt thì thấy ngay.</p>

<h2>4. Sáng đều tuyệt đối, không có vùng tối</h2>

<p>Người mới sợ vùng tối, nên thêm fill light cho tới khi mọi ngóc ngách đều nhìn rõ. Kết quả là ảnh phẳng lì. Vùng tối không phải chỗ thiếu thông tin. Nó là chỗ mắt người nghỉ, và là thứ làm vùng sáng trở nên sáng.</p>

<p><strong style="color:#fff;">Sửa:</strong> tắt hết đèn phụ, chỉ để nguồn chính. Nhìn kỹ. Rồi thêm lại từng đèn một, mỗi lần tự hỏi "đèn này đang giải quyết vấn đề gì?". Đèn nào không trả lời được thì xoá.</p>

<h2>5. Chỉnh màu ở khâu hậu kỳ để cứu ánh sáng sai</h2>

<p>Kéo contrast và saturation trong Compositor cho tới khi ảnh "đỡ tệ" là dấu hiệu bạn đang vá triệu chứng. Hậu kỳ nên là bước tinh chỉnh cuối, không phải bước cứu hộ. Nếu bạn phải kéo mạnh tay, quay lại sửa đèn, nhanh hơn nhiều.</p>

<hr class="hr">

<h2>Cách tự kiểm tra trong ba mươi giây</h2>

<p>Đổi toàn bộ vật liệu trong cảnh sang một chất xám trung tính rồi render nháp. Nếu ảnh xám đó đã đọc được hình khối và có chiều sâu, ánh sáng của bạn ổn, phần còn lại là chuyện vật liệu. Nếu ảnh xám trông phẳng và nhạt, không vật liệu nào cứu được nó.</p>

<p>Bài kiểm tra này tôi dùng cho gần như mọi shot, và nó bắt lỗi sớm hơn bất kỳ thứ gì khác.</p>

<p>Năm lỗi trên đều sửa được một mình. Thứ khó tự sửa là thói quen đọc ảnh, và đó là phần một <a href="blog-khoa-hoc-render.html">khoá học render</a> có người nhận xét từng vòng làm tốt hơn hẳn video hướng dẫn.</p>
""",
    },
    {
        "slug": "quy-trinh-mot-shot-tvc",
        "title": "Từ file Blender đến TVC: quy trình một shot sản phẩm chạy thật",
        "desc": "Toàn bộ các bước một shot sản phẩm đi qua trong dự án thương mại, kể cả những khâu không ai quay video hướng dẫn: brief, duyệt, và sửa theo ý khách.",
        "tag": "Nghề",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "7 phút đọc",
        "thumb": "assets/0954717e.jpg",
        "body": """
<p class="lead">Phần lớn hướng dẫn trên mạng dừng lại ở lúc bấm render. Trong một dự án thật, đó mới là khoảng giữa. Bài này đi hết một shot sản phẩm từ lúc nhận brief đến lúc file cuối được duyệt.</p>

<h2>Bước 1: Đọc brief, và hỏi lại</h2>

<p>Brief đến từ khách hầu như luôn thiếu thứ quan trọng nhất: shot này dùng ở đâu. Cùng một sản phẩm, dựng cho banner web khác hẳn dựng cho màn LED ngoài trời hay cho video dọc trên điện thoại. Tỉ lệ khung, khoảng cách nhìn, thời lượng người xem dừng lại, ba thứ đó quyết định gần như mọi lựa chọn phía sau.</p>

<p>Câu tôi luôn hỏi trước khi mở Blender: đăng ở đâu, khung hình gì, và có chữ đè lên không. Câu thứ ba cứu tôi vô số lần, vì bố cục đẹp mà chừa sai chỗ cho chữ thì phải dựng lại.</p>

<h2>Bước 2: Dựng khối thô và chốt góc máy trước</h2>

<p>Trước khi model chi tiết, tôi dựng khối thô rồi chốt camera. Lý do đơn giản: chi tiết ở mặt không lên hình là chi tiết vứt đi. Chốt góc máy sớm giúp biết chính xác cần làm kỹ chỗ nào.</p>

<p>Ở bước này tôi gửi khách ảnh xám khối thô. Nghe thì thô sơ, nhưng nó ngăn được thảm hoạ lớn nhất: làm xong hết rồi khách mới nói "anh muốn nhìn từ bên kia".</p>

<blockquote><p>Duyệt bố cục ở giai đoạn khối xám mất của bạn một ngày. Duyệt ở giai đoạn đã render mất của bạn một tuần.</p></blockquote>

<h2>Bước 3: Lighting trước, vật liệu sau</h2>

<p>Tôi dựng ánh sáng khi mọi thứ còn là chất xám trung tính. Ánh sáng đúng ở trạng thái xám thì gần như chắc chắn đúng khi có vật liệu. Làm ngược lại, tức chỉnh vật liệu dưới ánh sáng tạm, là tự tạo việc cho mình hai lần.</p>

<h2>Bước 4: Vật liệu, và kiềm chế</h2>

<p>Sản phẩm thương mại thường đơn giản hơn người ta tưởng: vài chất liệu sạch, đúng độ nhám, đúng màu thương hiệu. Cám dỗ lớn nhất là thêm trầy xước, bụi, vân tay cho "thật". Với sản phẩm bán hàng, những thứ đó thường làm hại, khách muốn hàng mới tinh.</p>

<h2>Bước 5: Render theo lớp, không render một cục</h2>

<p>Tách render ra thành các pass riêng: sản phẩm, nền, bóng đổ, phản chiếu. Lý do không phải kỹ thuật mà là thực tế: khi khách nói "nền tối hơn chút", bạn chỉnh trong ba phút thay vì render lại bốn tiếng.</p>

<p>Đây là khâu tách người làm nghề với người làm bài tập rõ nhất. Người mới render ra một file duy nhất và cầu trời khách duyệt.</p>

<h2>Bước 6: Hậu kỳ nhẹ tay</h2>

<p>Ghép pass, cân bằng tổng thể, thêm chút bloom nếu cảnh cần, xuất đúng không gian màu nơi sẽ đăng. Nếu ở bước này tôi phải kéo mạnh tay, tôi quay lại bước 3. Luôn nhanh hơn.</p>

<h2>Bước 7: Vòng sửa, và cách sống sót</h2>

<p>Sẽ có sửa. Luôn luôn. Điều bạn kiểm soát được là chi phí của mỗi vòng sửa, và nó được quyết định từ bước 5: file có tách lớp gọn gàng thì một vòng sửa là buổi chiều, file gộp một cục thì là hai ngày.</p>

<p>Một thói quen nhỏ giúp rất nhiều: mỗi lần gửi duyệt, đánh số phiên bản và ghi lại đúng một dòng đã đổi những gì. Khi khách bảo "quay lại bản hôm trước", bạn có bản hôm trước thật.</p>

<hr class="hr">

<p>Không bước nào ở trên đòi hỏi kỹ thuật cao siêu. Chúng chỉ đòi hỏi bạn biết trước điều gì sắp xảy ra, thứ mà học một mình thì phải trả giá bằng vài dự án hỏng mới rút ra được.</p>
""",
    },
    {
        "slug": "kho-hau-truong-overgrown-blender-studio",
        "title": "Blender Studio mở kho hậu trường OVERGROWN: file production thật, học được gì từ đó",
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
        "title": "Add-on hard-surface cho Blender: cái nào đáng cài, cái nào bỏ qua",
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

<p>Muốn biết hard-surface nằm ở đâu trong lộ trình học, xem <a href="blog-lo-trinh-tu-hoc-blender.html">bài về 7 kỹ năng</a>. Nó là bước thứ năm, và có lý do nó không đứng sớm hơn.</p>
""",
    },
    {
        "slug": "sau-node-va-mot-hanh-lang",
        "title": "Sáu node và một hành lang: bài học dựng không khí từ Backrooms của Blender Guru",
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
<p>Hai thứ này thêm ở khâu compositing, nhưng chỉ hiệu quả khi ánh sáng bên dưới đã đúng. Nếu bạn thấy mình dựa vào grain để cảnh đỡ giả, vấn đề nằm ở đèn. Tôi có viết kỹ hơn trong <a href="blog-5-loi-lighting.html">bài về 5 lỗi lighting</a>.</p>

<h2>Bài tập</h2>

<p>Lấy một không gian bạn từng dựng thủ công và tự hỏi: nếu chỉ được dùng năm node, phần nào của cảnh này thật sự cần thiết? Trả lời được câu đó, bạn tiết kiệm được vài chục giờ cho mọi dự án sau.</p>
""",
    },
    {
        "slug": "hoc-blender-3d-bao-lau",
        "title": "Học Blender 3D bao lâu thì nhận được job đầu tiên?",
        "desc": "Mốc thời gian thực tế để đi từ mở Blender lần đầu tới lúc có khách trả tiền, chia theo từng giai đoạn, và điều gì quyết định bạn nhanh hay chậm.",
        "tag": "Định hướng",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "8 phút đọc",
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
        ],
        "body": """
<p class="lead">Đây là câu hỏi tôi nhận nhiều nhất, và cũng là câu bị trả lời ẩu nhất. "Ba tháng là làm được" nghe thì dễ chốt đơn, nhưng không đúng. Dưới đây là mốc thời gian thật, kèm điều kiện đi kèm.</p>

<h2>Câu trả lời ngắn</h2>

<p>Với người học đều <strong style="color:#fff;">10 đến 15 giờ mỗi tuần</strong> và có người sửa bài: khoảng <strong style="color:#fff;">4 đến 6 tháng</strong> để có portfolio đủ nhận job nhỏ, <strong style="color:#fff;">10 đến 14 tháng</strong> để nhận được job thương mại tử tế.</p>

<p>Tự học hoàn toàn, không ai sửa: cộng thêm gấp đôi tới gấp ba. Không phải vì bạn học chậm hơn, mà vì bạn mất nhiều tháng đi sai hướng rồi mới nhận ra.</p>

<h2>Bốn giai đoạn, và dấu hiệu bạn đã qua</h2>

<h3>Tháng 1 đến 2: làm quen công cụ</h3>
<p>Bạn dựng được vật thể đơn giản, biết di chuyển trong viewport không phải nghĩ, hiểu modifier cơ bản. Đây là giai đoạn dễ chịu nhất và cũng gây ảo tưởng nhất, vì nhiều người tưởng mình đã học được nghề.</p>
<p><strong style="color:#fff;">Dấu hiệu qua:</strong> bạn dựng được một vật ngoài đời mà không cần xem hướng dẫn từng bước.</p>

<h3>Tháng 3 đến 5: hình bắt đầu "trông được"</h3>
<p>Ánh sáng và vật liệu vào cuộc. Đây là chỗ khoảng cách giữa người có người kèm và người tự học mở ra lớn nhất, vì bạn không tự thấy được ánh sáng của mình sai ở đâu khi chưa có ai chỉ.</p>
<p><strong style="color:#fff;">Dấu hiệu qua:</strong> bạn nhìn render của mình và nói được cụ thể chỗ nào chưa ổn, chứ không chỉ cảm giác "chưa đã".</p>

<figure>
  <img src="assets/vplas-render-san-pham-blender.jpg" alt="Render sản phẩm thiết bị y tế VPLAS dựng bằng Blender, bề mặt kim loại, ánh sáng studio nền tối" loading="lazy" width="1600" height="900">
  <figcaption><strong>Shot sản phẩm trong dự án VPLAS của LXAM Studio.</strong> Chỉ một nguồn sáng chính và vài mặt hắt, cái khó không nằm ở số lượng đèn mà ở việc đặt đúng chỗ để bề mặt kim loại có chuyển sáng.</figcaption>
</figure>

<h3>Tháng 6 đến 10: làm được sản phẩm hoàn chỉnh</h3>
<p>Bạn xử lý được hard-surface, biết tổ chức scene cho dự án nhiều shot, render ra file dùng được chứ không phải file phải sửa lại. Đây là lúc portfolio bắt đầu có sức nặng.</p>
<p><strong style="color:#fff;">Dấu hiệu qua:</strong> bạn hoàn thành một dự án từ đầu tới cuối mà không bỏ dở giữa chừng.</p>

<h3>Tháng 10 trở đi: làm được job thật</h3>
<p>Khác biệt ở giai đoạn này không còn là kỹ thuật. Là biết đọc brief, biết báo giá, biết xử lý khi khách đổi ý ở phút cuối, biết chia file để sửa nhanh. Tôi có viết riêng về <a href="blog-quy-trinh-mot-shot-tvc.html">quy trình một shot chạy thật</a>.</p>

<h2>Ba thứ quyết định bạn nhanh hay chậm</h2>

<h3>1. Có được sửa bài hay không</h3>
<p>Đây là biến số lớn nhất, hơn cả tài năng hay số giờ ngồi máy. Người tự học có thể ngồi sáu tháng với một thói quen sai mà không biết. Người được sửa bài mất một buổi để bỏ thói quen đó.</p>

<h3>2. Làm dự án hay làm bài tập</h3>
<p>Bài tập có đáp án sẵn, làm xong thấy vui rồi thôi. Dự án có ràng buộc thật: deadline, yêu cầu, người duyệt, và ép bạn giải quyết vấn đề chưa ai dạy. Một dự án hoàn chỉnh dạy nhiều hơn hai mươi bài tập.</p>

<h3>3. Đều đặn hơn là dồn dập</h3>
<p>10 giờ mỗi tuần trong sáu tháng ăn đứt 40 giờ một tuần rồi nghỉ hai tháng. Kỹ năng 3D là kỹ năng vận động, mắt và tay cần lặp lại thường xuyên mới giữ được.</p>

<blockquote><p>Thứ khiến người ta bỏ Blender hiếm khi là độ khó. Thường là sáu tháng không thấy mình tiến bộ, vì không ai nói cho họ biết họ đang sai ở đâu.</p></blockquote>

<h2>Vài câu hỏi hay gặp</h2>

<p class="faq-q">Không biết vẽ có học được không?</p>
<p>Được. 3D thương mại, từ sản phẩm, hard-surface tới kiến trúc, không đòi hỏi kỹ năng vẽ tay. Mảng cần vẽ là character và concept stylized, không phải hướng duy nhất của nghề.</p>

<p class="faq-q">Học Blender rồi có phải học thêm 3ds Max hay Maya?</p>
<p>Không, trừ khi bạn nhắm vào một studio bắt buộc dùng phần mềm đó. Blender làm được trọn pipeline sản phẩm và TVC. Nắm chắc một công cụ hơn là biết lõm bõm ba cái.</p>

<p class="faq-q">Trên 30 tuổi bắt đầu có muộn không?</p>
<p>Không. Khách hàng nhìn portfolio, không nhìn tuổi. Người đi làm chuyển ngành thường còn có lợi thế: đã quen deadline và làm việc với khách, hai thứ dân mới ra trường phải học lại từ đầu.</p>

<p class="faq-q">Cần máy mạnh không?</p>
<p>Lúc bắt đầu thì không. Tôi có viết riêng một bài về <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> và khi nào thật sự cần nâng cấp.</p>

<hr class="hr">

<p>Nếu bạn đang tự học và không chắc mình đang ở giai đoạn nào, gửi tôi vài bài render, tôi xem qua và nói thẳng bạn đang mắc ở đâu, kể cả khi câu trả lời là bạn chưa cần học khoá nào cả.</p>
""",
    },
    {
        "slug": "cau-hinh-may-hoc-blender",
        "title": "Cấu hình máy tính học Blender 3D: mua gì, và khi nào chưa cần nâng cấp",
        "desc": "Hướng dẫn chọn cấu hình máy học Blender theo từng giai đoạn: CPU, GPU, RAM, SSD, và lý do máy yếu không phải thứ đang cản bạn.",
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

<p>Ở giai đoạn này cảnh của bạn nhẹ, render nháp vài phút là xong. Nâng cấp máy lúc này giống mua giày chạy marathon khi mới tập đi bộ.</p>

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

<p>Tóm lại: bắt đầu bằng máy đang có. Khi nào bạn thấy mình <em>chờ</em> nhiều hơn <em>làm</em>, lúc đó nâng cấp, và nâng GPU trước. Còn nếu vấn đề là hình chưa đẹp thì máy mới không giải quyết được; cái cần xem lại là <a href="blog-5-loi-lighting.html">ánh sáng</a>.</p>
""",
    },
    {
        "slug": "tu-hoc-blender-hay-hoc-kem",
        "title": "Tự học Blender hay học khoá có người kèm? So sánh thẳng thắn",
        "desc": "Tự học Blender hoàn toàn miễn phí và nhiều người thành công. Vậy khi nào bỏ tiền học kèm là hợp lý, khi nào là lãng phí, phân tích từ người đang dạy.",
        "tag": "Định hướng",
        "date": "2026-09-07",
        "date_vn": "07/09/2026",
        "read": "8 phút đọc",
        "thumb": "assets/vplas-exploded-view-blender.jpg",
        "body": """
<p class="lead">Tôi đang bán khoá học, nên bạn có quyền nghi ngờ bài này. Vì vậy tôi bắt đầu bằng phần bất lợi cho mình: rất nhiều người tự học Blender thành công, hoàn toàn miễn phí, và bạn có thể là một trong số đó.</p>

<h2>Tự học được gì</h2>

<p>Blender là phần mềm miễn phí có cộng đồng dạy học tốt nhất trong ngành 3D. Tài nguyên chất lượng cao, miễn phí, nhiều tới mức không xem hết. Riêng khoản tài liệu, bạn không thiếu gì.</p>

<p>Người tự học tốt thường có ba đặc điểm: kỷ luật ngồi đều mà không cần ai nhắc, khả năng tự đánh giá bài mình khá chính xác, và kiên nhẫn với việc thử sai. Nếu bạn có đủ ba thứ đó, tự học là lựa chọn đúng, và tôi nói thật lòng.</p>

<h2>Tự học mắc ở đâu</h2>

<p>Vấn đề của tự học không nằm ở thiếu thông tin. Nằm ở ba chỗ khác:</p>

<h3>Không biết mình sai ở đâu</h3>
<p>Đây là cái kẹt lớn nhất. Bạn nhìn render của mình, thấy "chưa đã", nhưng không chỉ ra được vì sao. Không chỉ ra được thì không sửa được, và bạn lặp lại cùng một lỗi qua hàng chục bài.</p>

<h3>Không biết thứ tự học</h3>
<p>YouTube gợi ý theo lượt xem, không theo trình độ của bạn. Nhiều người học vật liệu nâng cao trước khi biết đặt đèn, rồi kết luận mình không có năng khiếu. Tôi có viết riêng về <a href="blog-lo-trinh-tu-hoc-blender.html">thứ tự 7 kỹ năng</a> và vì sao đảo thứ tự lại hại.</p>

<h3>Không ai dạy phần ngoài phần mềm</h3>
<p>Báo giá thế nào, nhận brief ra sao, file phải chia thế nào để sửa nhanh, trình bày một shot ra sao để người duyệt hiểu ngay. Không có video nào dạy mấy thứ này, vì chúng đến từ việc làm job thật và va vấp.</p>

<figure>
  <img src="assets/vplas-exploded-view-blender.jpg" alt="Ảnh render tách rời linh kiện thiết bị VPLAS dựng bằng Blender, hard-surface, bo mạch, vỏ kim loại" loading="lazy" width="1600" height="900">
  <figcaption><strong>Shot tách rời linh kiện, dự án VPLAS.</strong> Loại shot này không khó về kỹ thuật. Khó ở chỗ sắp xếp sao cho người xem đọc được thứ tự lắp ráp. Đây là quyết định thẩm mỹ, và là thứ khó tự học nhất.</figcaption>
</figure>

<h2>So sánh trực tiếp</h2>

<div class="table-wrap">
<table>
<thead><tr><th></th><th>Tự học</th><th>Có người kèm</th></tr></thead>
<tbody>
<tr><td>Chi phí</td><td>Gần như 0</td><td>Vài triệu đến vài chục triệu</td></tr>
<tr><td>Thời gian tới portfolio dùng được</td><td>Thường 1 đến 2 năm</td><td>Thường 6 đến 12 tháng</td></tr>
<tr><td>Rủi ro lớn nhất</td><td>Đi sai hướng nhiều tháng mà không biết</td><td>Chọn nhầm người dạy</td></tr>
<tr><td>Phần kỹ năng nghề</td><td>Phải tự va vấp mà học</td><td>Được truyền lại trực tiếp</td></tr>
<tr><td>Phù hợp với</td><td>Người kỷ luật cao, không gấp</td><td>Người cần đi nhanh, hoặc đã mắc kẹt</td></tr>
</tbody>
</table>
</div>

<h2>Khi nào bỏ tiền học là hợp lý</h2>

<ul>
<li>Bạn đã tự học vài tháng và <strong style="color:#fff;">cảm thấy đứng yên</strong>, làm được thêm thứ mới nhưng chất lượng không nhích.</li>
<li>Bạn cần <strong style="color:#fff;">đi nhanh vì lý do cụ thể</strong>: chuyển nghề, có deadline, đang cần portfolio để ứng tuyển.</li>
<li>Bạn biết mình <strong style="color:#fff;">không giữ được kỷ luật khi học một mình</strong>, điều này không có gì đáng xấu hổ, đa số là vậy.</li>
</ul>

<h2>Khi nào chưa nên</h2>

<ul>
<li>Bạn <strong style="color:#fff;">chưa mở Blender bao giờ</strong>. Học miễn phí một tháng trước đã, để chắc mình thật sự thích công việc này.</li>
<li>Bạn kỳ vọng khoá học <strong style="color:#fff;">thay bạn luyện tập</strong>. Không có khoá nào làm được điều đó.</li>
<li>Học phí <strong style="color:#fff;">ảnh hưởng tới sinh hoạt của bạn</strong>. Nghề này không đi đâu mất; học sau vẫn kịp.</li>
</ul>

<blockquote><p>Tiền học không mua kỹ năng. Nó mua thời gian, cụ thể là mấy tháng bạn sẽ mất để tự nhận ra điều một người có kinh nghiệm chỉ trong mười phút.</p></blockquote>

<h2>Nếu chọn học, hỏi ba câu này trước</h2>

<ol>
<li><strong style="color:#fff;">Người dạy có đang làm job thật không?</strong> Người chỉ dạy mà không làm sẽ dạy những thứ đúng của năm năm trước.</li>
<li><strong style="color:#fff;">Bài của tôi được sửa như thế nào?</strong> "Có hỗ trợ" là câu vô nghĩa. Hỏi cụ thể: sửa mấy lần, ai sửa, phản hồi dạng gì.</li>
<li><strong style="color:#fff;">Kết thúc khoá tôi cầm về cái gì?</strong> Câu trả lời tốt là một danh sách sản phẩm cụ thể, không phải một danh sách bài giảng.</li>
</ol>

<p>Ba câu này áp dụng cho mọi khoá học, kể cả của tôi. Nếu ai không trả lời được rõ ràng, đó là câu trả lời rồi. Bộ tiêu chí đầy đủ hơn nằm ở bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">khoá học Blender 3D ở Việt Nam</a>, gồm cả cách bóc học phí thành từng khoản để so cho công bằng.</p>

<hr class="hr">

<p>Muốn xem cách LXAM Studio làm việc trước khi quyết định gì, phần <a href="ve-chung-toi.html">về chúng tôi</a> nói rõ triết lý dạy, còn <a href="blog.html">blog</a> là nơi tôi để công khai phần lớn kiến thức nền, đọc miễn phí, không cần đăng ký.</p>
""",
    },
    {
        "slug": "khoa-hoc-blender-3d-o-viet-nam",
        "title": "Khoá học Blender 3D ở Việt Nam: chọn sao cho khỏi phí tiền",
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

<p>Cách so sánh công bằng nhất là bỏ qua con số tổng và tách học phí thành bốn khoản: giờ giảng, số lần bài được chữa, tài nguyên đi kèm và hỗ trợ sau khoá. Hai nơi cùng báo một mức giá có thể chênh nhau nhiều lần ở khoản thứ hai.</p>

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
        "title": "Học kèm 1 kèm 1 Blender: khi nào đáng tiền, khi nào phí",
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

<h2>Cách thử một gia sư Blender trước khi trả tiền</h2>

<p>Xin một buổi thử, mang theo một bài bạn làm và đang không ưng. Đừng hỏi họ dạy gì, hãy đưa bài và xem họ phản ứng thế nào. Danh sách dưới là những thứ cần kiểm trong đúng buổi đó.</p>

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
        "desc": "Kế hoạch ba tháng đầu cho người học đồ hoạ 3D bằng Blender: học gì trước, bỏ qua gì, luyện bao nhiêu mỗi tuần và dấu hiệu cho thấy bạn đi đúng hướng.",
        "tag": "Bắt đầu",
        "date": "2026-09-26",
        "date_vn": "26/09/2026",
        "read": "7 phút đọc",
        "thumb": "assets/jhm-khoi-kinh-ky-thuat.webp",
        "body": """
<p class="lead">Người mới thường hỏi nên học phần mềm nào. Câu hỏi đó ít quan trọng hơn bạn nghĩ. Ba tháng đầu quyết định bạn ở lại hay bỏ cuộc, và nó phụ thuộc vào thứ tự học chứ không phải công cụ.</p>

<h2>Chọn phần mềm trong năm phút</h2>

<p>Nếu bạn bắt đầu từ con số 0 và tự trả tiền cho mọi thứ, chọn Blender. Miễn phí, chạy được trên máy phổ thông, làm được cả model, dựng cảnh, ánh sáng, hoạt hình và hậu kỳ trong một chỗ. Khi đi làm cần phần mềm khác, bạn học thêm trong vài tuần vì nguyên lý giống nhau.</p>

<p>Máy móc cũng vậy, đừng nâng cấp vội. Mình đã viết riêng về <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> và khi nào máy thật sự là thứ đang cản bạn.</p>

<h2>Tháng đầu: làm quen và giữ nhịp</h2>

<p>Mục tiêu tháng này không phải làm ra hình đẹp. Là ngồi xuống đều đặn và không sợ phần mềm nữa.</p>

<ul>
<li><strong style="color:#fff;">Thao tác cơ bản:</strong> xoay cảnh, di chuyển, phóng to, chọn đối tượng, lưu file cho gọn.</li>
<li><strong style="color:#fff;">Model khối đơn giản:</strong> cái ly, cái loa, cái điều khiển. Vật gì trên bàn cũng được.</li>
<li><strong style="color:#fff;">Một nguồn sáng duy nhất:</strong> tập nhìn bóng đổ trước khi nghĩ tới ba đèn.</li>
<li><strong style="color:#fff;">Nhịp luyện:</strong> bốn tới năm buổi mỗi tuần, mỗi buổi một tiếng, hơn hẳn ngồi tám tiếng vào chủ nhật.</li>
</ul>

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

<p>Đến lúc bạn có vài bài nộp mà vẫn không tự biết bài nào yếu ở đâu, hình thức <a href="blog-hoc-blender-kem-1-1.html">học kèm 1 kèm 1 Blender</a> là bước hợp lý tiếp theo, vì giai đoạn này cái thiếu là người chẩn đoán chứ không phải thêm bài giảng.</p>

<hr class="hr">

<p>Nếu muốn đi theo lộ trình có người chữa bài thay vì tự mò, xem <a href="khoa-hoc.html">khoá học Blender 3D</a> của LXAM Academy. Còn nếu muốn tự học trước, tải <a href="cam-nang.html">cẩm nang miễn phí</a> và đọc <a href="blog-hoc-blender-3d-bao-lau.html">học Blender bao lâu thì nhận job đầu tiên</a>.</p>
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

<p>Một cách so sánh công bằng hơn giá mỗi buổi: lấy học phí chia cho số lần bài của bạn được người có nghề xem tận nơi. Con số đó mới phản ánh thứ bạn thật sự mua. Bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">chọn khoá học Blender 3D ở Việt Nam</a> có bảng dịch các kiểu nói về học phí sang nghĩa thật của chúng.</p>

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
<p>Làm trọn một dự án cá nhân từ đầu tới cuối, rồi mới tính chuyện chuyên sâu theo hướng sản phẩm, automotive hay sự kiện. Chọn hướng quá sớm khi chưa hoàn thành cái gì trọn vẹn là lỗi phổ biến nhất ở giai đoạn này.</p>

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
<p>Render có một trình tự sửa khá cố định: bố cục trước, ánh sáng sau, vật liệu tiếp theo, hậu kỳ cuối cùng. Người mới hay làm ngược, kéo hậu kỳ để cứu ánh sáng hỏng. Năm lỗi hay gặp nhất trong nhóm này tôi đã viết riêng ở bài <a href="blog-5-loi-lighting.html">5 lỗi lighting khiến render trông rẻ tiền</a>.</p>

<figure>
  <img src="assets/aston-dbx-goc-ben-dai-sang.webp" alt="Xe Aston Martin DBX màu xanh ngọc dựng và render 3D bằng Blender, chụp nghiêng trên nền vải xanh đậm với một dải sáng trắng chạy ngang sàn phía sau xe" loading="lazy" width="1800" height="1013">
  <figcaption><strong>Một key visual automotive dựng hoàn toàn bằng Blender.</strong> Thứ làm tấm này đứng được không phải model xe, mà là dải sáng chạy dọc thân và khoảng tối giữ cho nền không giành mất chú ý. Đó chính là phần một khoá học render phải dạy.</figcaption>
</figure>

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

<p>Một cách so sánh công bằng hơn giá mỗi buổi: lấy học phí chia cho số lần bài của bạn được người trong nghề xem tận nơi. Bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">chọn khoá học Blender 3D ở Việt Nam</a> có bảng dịch các kiểu nói về học phí sang nghĩa thật của chúng, dùng lại được cho khoá render.</p>

<h2>Danh sách kiểm tra trước khi đóng tiền</h2>

<ol>
<li><strong style="color:#fff;">Xem bài render của học viên, không phải bài của giảng viên.</strong> Bài học viên cho biết khoá dạy được gì.</li>
<li><strong style="color:#fff;">Hỏi tuần đầu tiên nộp gì.</strong> Không trả lời cụ thể được nghĩa là chưa có lịch bài nộp.</li>
<li><strong style="color:#fff;">Hỏi ai sửa bài.</strong> Người dạy và người sửa nhiều khi không phải một người.</li>
<li><strong style="color:#fff;">Hỏi một bài được nhận xét mấy vòng.</strong> Với render, dưới hai vòng là gần như không đủ.</li>
<li><strong style="color:#fff;">Đưa cấu hình máy của bạn và hỏi thẳng.</strong> Câu trả lời tử tế sẽ nói rõ phần nào chạy được, phần nào phải giảm chất lượng khi luyện.</li>
<li><strong style="color:#fff;">Hỏi khoá dạy theo mảng nào.</strong> Sản phẩm, kiến trúc và automotive đòi hỏi cách sáng khác nhau, khoá dạy chung chung thường không đi sâu được mảng nào.</li>
</ol>

<p>Nếu bạn lo máy mình không theo nổi phần luyện render, đọc <a href="blog-cau-hinh-may-hoc-blender.html">cấu hình máy học Blender</a> trước, trong đó có mốc cụ thể cho biết khi nào nâng cấp mới thật sự có nghĩa.</p>

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

<p>Nếu bạn chưa mở Blender bao giờ, ba kiểu đầu đều dùng được, kiểu thứ tư thì chưa. Còn nếu bạn đã dựng được vài vật nhưng ảnh ra vẫn nhìn rẻ tiền, vấn đề của bạn nằm ở ánh sáng và vật liệu chứ không nằm ở dựng hình, và một <a href="blog-khoa-hoc-render.html">khoá học render</a> đúng nghĩa sẽ hiệu quả hơn là học lại từ đầu.</p>

<h2>Khoá học 3D online hay khoá học 3D tại TPHCM</h2>

<p>Câu hỏi này bị hỏi nhiều hơn mức nó đáng. Hình thức lớp không quyết định bạn giỏi hay không. Thứ quyết định là số vòng bài của bạn được sửa và mức độ thẳng thắn của người sửa.</p>

<h3>Khi nào online là lựa chọn tốt hơn</h3>
<p>Bài nộp trong nghề này là file và ảnh, gửi đi trong vài giây. Người sửa mở file của bạn ra là thấy ngay bạn dựng sai ở đâu, không cần ngồi cạnh. Nếu bạn đã có máy chạy được và tự ngồi vào bàn được, khoá học 3D online tiết kiệm cho bạn hàng giờ đi lại mỗi tuần, và thời gian đó đổ vào luyện tập thì có lợi hơn nhiều.</p>

<h3>Khi nào nên chịu khó tới lớp</h3>
<p>Nếu bạn từng mua hai ba khoá online rồi bỏ dở, đừng mua khoá thứ tư. Vấn đề của bạn không phải nội dung mà là sự có mặt. Một lớp có địa điểm cụ thể ở TPHCM, có giờ cố định và có người nhìn thấy bạn vắng, giải quyết đúng chỗ đó. Đây là lý do duy nhất đáng để chọn học trực tiếp, và nó là lý do chính đáng.</p>

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

<p>Một cách so sánh công bằng hơn giá mỗi buổi: lấy học phí chia cho số lần bài của bạn được người trong nghề xem tận nơi. Cách đọc các kiểu nói về học phí, kể cả những lời hứa nên bỏ qua, mình viết kỹ trong bài <a href="blog-khoa-hoc-blender-3d-o-viet-nam.html">khoá học Blender 3D ở Việt Nam</a>.</p>

<blockquote><p>Bạn không mua số buổi học. Bạn mua số lần có người nhìn vào bài của bạn và nói thẳng nó sai ở đâu. Mọi con số khác trên tờ báo giá đều là phụ.</p></blockquote>

<h2>Ba bài nên đọc trước khi chọn khoá học 3D Blender</h2>

<p>Tuỳ bạn đang đứng ở đâu, một trong ba bài dưới sẽ hợp hơn hai bài còn lại. Đọc đúng bài rồi hãy quyết định.</p>

<h3>Nếu bạn chưa từng mở Blender</h3>
<p>Đọc <a href="blog-khoa-hoc-blender-3d-cho-nguoi-moi.html">khoá học Blender 3D cho người mới</a>. Bài đó mô tả tám tuần đầu nên dạy gì, tuần nào nộp bài gì, và sáu câu nên hỏi trước khi đóng tiền. Nó cũng nói rõ những thứ một khoá cho người mới không nên nhồi vào, ví dụ hoạt hình nhân vật hay mô phỏng vải, vì đưa vào sớm chỉ làm bạn rối.</p>

<h3>Nếu bạn dựng được hình nhưng ảnh chưa đẹp</h3>
<p>Đọc <a href="blog-khoa-hoc-render.html">khoá học render</a>. Bài đó phân tích một khoá render phải có bốn phần nào, nên học Cycles hay Eevee trước, và năm dấu hiệu nhận ra một khoá chỉ dạy thao tác chứ không dạy cách chẩn đoán. Đây là giai đoạn nhiều người kẹt lâu nhất mà lại hay chọn sai khoá nhất.</p>

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
      <img src="{thumb}" alt="{title_plain}" style="width:100%;aspect-ratio:16/9;object-fit:cover;border-radius:4px;margin:0 0 40px;">
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
    for p in POSTS:
        cards.append(f"""      <a class="post-card" href="blog-{p['slug']}.html">
        <div class="thumb"><img src="{p['thumb']}" alt="{html.escape(p['title'])}"></div>
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
        "dateModified": p["date"],
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
               "LXAM Studio: studio visual 3D tại Việt Nam làm TVC, render sản phẩm và animation kỹ thuật, đồng thời đào tạo Blender 1:1. Câu chuyện và quan điểm nghề.",
               "about",
               canonical="ve-chung-toi.html",
               og_image="assets/a26a7e39.jpg",
               jsonld=jsonld_simple("AboutPage", "Về LXAM Studio",
                                    "Studio 3D và đào tạo Blender tại Việt Nam",
                                    "https://lxamstudio.com/ve-chung-toi.html"))
          + ABOUT_BODY + FOOTER)

    write("blog.html",
          head("Blog | LXAM Studio",
               "Ghi chép về Blender, lighting, render và nghề 3D thương mại từ bàn làm việc của LXAM Studio.",
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
            date_vn=p["date_vn"], read=p["read"],
            thumb=p["thumb"], body=body_html_, toc=toc_,
            related=related_html(p),
            sources=sources_html(p.get("sources")),
        )
        write("blog-%s.html" % p["slug"],
              head(p["title"] + " | LXAM Studio", p["desc"], "blog",
                   canonical="blog-%s.html" % p["slug"],
                   og_image=p["thumb"],
                   og_type="article", published=p["date"],
                   jsonld=jsonld_post(p))
              + body + FOOTER)

    write("hoc-vien.html",
          head("Khu học viên | LXAM Studio",
               "Không gian riêng của học viên LXAM Studio: bài giảng, file dự án, thư viện asset, nộp bài và lịch buổi kèm 1:1.",
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
          "nghe-nghiep.html", "ve-chung-toi.html", "blog.html"]
    urls = [""] + P9 + P8 + ["hoc-vien.html"] + ["blog-%s.html" % p["slug"] for p in POSTS] \
           + ["blog-render-nhanh-hon-blender-cycles.html", "blog-blender-hay-3dsmax-c4d.html"]
    rows = []
    for u in urls:
        pri = "1.0" if u == "" else ("0.9" if u in P9 else ("0.8" if u in P8 else "0.7"))
        freq = "weekly" if u in ("", "blog.html") else "monthly"
        rows.append('  <url><loc>https://lxamstudio.com/%s</loc>'
                    '<changefreq>%s</changefreq><priority>%s</priority></url>' % (u, freq, pri))
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(rows) + "\n</urlset>\n")


if __name__ == "__main__":
    main()
