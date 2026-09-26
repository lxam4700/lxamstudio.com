#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh trang nghe-nghiep.html: cơ hội nghề nghiệp với 3D."""

import os, json, datetime

SITE = "/home/claude/site"
YEAR = datetime.date.today().year
URL = "https://lxamstudio.com/"

TITLE = "Cơ hội nghề nghiệp với 3D: học xong làm gì | LXAM"
DESC = ("Học 3D xong làm nghề gì: product artist, lighting & rendering, animation TVC, "
        "automotive CGI, AI visual. Ai tuyển và portfolio cần gì để được gọi.")

# ---------------------------------------------------------------- NAV
NAV_ITEMS = [
    ("ve-chung-toi.html", "Về chúng tôi", "ve"),
    ("index.html#portfolio", "Portfolio", "pf"),
    ("blog.html", "Blog", "blog"),
    ("hoc-vien.html", "Khu học viên", "hv"),
    ("index.html#lienhe", "Liên hệ", "lh"),
    ("khoa-hoc.html", "Khóa học", "kh"),
    ("nghe-nghiep.html", "Cơ hội nghề nghiệp", "nn"),
]
DRAWER_EXTRA = ("cam-nang.html", "Cẩm nang", "cn")
DRAWER_TAIL = ("lo-trinh.html", "Lộ trình &amp; học phí", "lt")


def nav_html(active):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' class="is-active"' if k == active else "", t)
                    for h, t, k in NAV_ITEMS)
    items = NAV_ITEMS[:2] + [DRAWER_EXTRA] + NAV_ITEMS[2:] + [DRAWER_TAIL]
    drawer = "".join('<a href="%s">%s</a>' % (h, t) for h, t, k in items)
    return links, drawer


# ---------------------------------------------------------------- ROLES
ROLES = [
    {
        "n": "01", "name": "3D Product / Hardsurface Artist",
        "line": "Dựng hình sản phẩm cho quảng cáo và catalogue",
        "day": "Nhận bản vẽ kỹ thuật hoặc ảnh chụp, dựng lại sản phẩm trong 3D đúng tỉ lệ, "
               "tách lớp vật liệu, xuất hình ở nhiều góc cho marketing dùng.",
        "who": "Nhãn hàng tiêu dùng, thiết bị điện tử, nội thất, thương mại điện tử.",
        "port": "Ba đến năm sản phẩm khác chất liệu, từ kim loại, nhựa trong, vải tới gỗ, "
                "mỗi cái có ảnh tổng thể và ảnh cận chi tiết.",
        "track": ("Hệ 3D Automotive, chặng Basic", "lo-trinh-3d-automotive.html"),
    },
    {
        "n": "02", "name": "Lighting & Rendering Artist",
        "line": "Người quyết định khung hình trông đắt hay rẻ",
        "day": "Nhận scene đã dựng, set đèn, chỉnh vật liệu, canh máy, render và hậu kỳ màu. "
               "Cùng một model, người này làm ra chênh lệch lớn nhất về chất lượng cuối.",
        "who": "Studio quảng cáo, agency, công ty kiến trúc, đội in-house của nhãn hàng.",
        "port": "Cùng một sản phẩm render ở ba mood khác nhau, kèm ảnh breakdown "
                "cho thấy bạn kiểm soát ánh sáng chứ không ăn may.",
        "track": ("Hệ 3D Automotive, chặng Basic", "lo-trinh-3d-automotive.html"),
    },
    {
        "n": "03", "name": "3D Animator / Motion Artist",
        "line": "Làm sản phẩm chuyển động thành phim",
        "day": "Dựng storyboard, rig, đặt keyframe, thêm hiệu ứng và âm thanh, "
               "rồi dựng thành một TVC hoàn chỉnh có nhịp.",
        "who": "Nhà sản xuất TVC, agency quảng cáo, đội content của thương hiệu lớn.",
        "port": "Một phim 30 đến 60 giây trọn vẹn, có mở đầu và kết, không phải một chuỗi shot rời.",
        "track": ("Hệ 3D Automotive, chặng Masterclass", "lo-trinh-3d-automotive.html"),
    },
    {
        "n": "04", "name": "Automotive / CGI Visual Artist",
        "line": "Mảng khó nhất, và trả cao nhất trong nhóm hình tĩnh",
        "day": "Dựng và render xe ở chuẩn quảng cáo: bề mặt sơn, phản chiếu, kính, "
               "đặt xe vào bối cảnh thật sao cho không lộ ghép.",
        "who": "Hãng xe và đại lý, studio CGI quốc tế, khách nước ngoài thuê từ xa.",
        "port": "Hai đến ba chiếc xe hoàn chỉnh, có cả ảnh studio và ảnh ngoại cảnh.",
        "track": ("Hệ 3D Automotive, chặng Masterclass", "lo-trinh-3d-automotive.html"),
    },
    {
        "n": "05", "name": "AI Visual Specialist",
        "line": "Vị trí mới, ít người làm được tử tế",
        "day": "Dùng 3D dựng phần cần chính xác, dùng AI nhân bối cảnh và biến thể, "
               "rồi ghép lại thành bộ hình nhất quán cho cả chiến dịch.",
        "who": "Đội marketing, sàn thương mại điện tử, agency performance, brand chạy nhiều SKU.",
        "port": "Một sản phẩm, mười biến thể bối cảnh, nhìn như cùng một buổi chụp.",
        "track": ("Hệ 3D × A.I", "lo-trinh-3d-ai.html"),
    },
]

WHERE = [
    ("Studio quảng cáo &amp; agency", "Nơi tuyển nhiều nhất. Vào được thì học nhanh vì làm nhiều dạng job."),
    ("Đội in-house của nhãn hàng", "Lịch ổn định hơn, làm sâu một ngành hàng. Hợp người muốn đi đường dài."),
    ("Công ty kỹ thuật &amp; sản xuất", "Cần hình lắp ráp, cắt lớp, mô phỏng vận hành. Ít người làm nên ít cạnh tranh."),
    ("Freelance &amp; khách nước ngoài", "Tính theo dự án hoặc theo shot. Cần portfolio đủ mạnh để khách tin trước khi gặp mặt."),
]

PORTFOLIO_RULES = [
    ("Ít mà chắc", "Năm tác phẩm hoàn chỉnh thắng hai mươi bài dở dang. Người xem dừng ở tác phẩm yếu nhất của bạn, không phải tác phẩm mạnh nhất."),
    ("Có breakdown", "Wireframe, layout đèn, các bước hậu kỳ. Đây là thứ phân biệt người hiểu nghề với người tải preset."),
    ("Đúng mảng bạn muốn làm", "Nộp vào chỗ làm xe thì đừng gửi portfolio toàn nhân vật. Nhà tuyển dụng không tự suy ra giúp bạn."),
    ("Nói được vì sao", "Buổi phỏng vấn nào cũng hỏi tại sao đặt đèn ở đó, tại sao chọn góc đó. Trả lời được mới qua."),
]


def role_card(r):
    tname, thref = r["track"]
    return """
      <article class="role">
        <div class="role-num">%s</div>
        <div class="role-body">
          <h3>%s</h3>
          <p class="role-line">%s</p>
          <dl class="role-dl">
            <div><dt>Việc hằng ngày</dt><dd>%s</dd></div>
            <div><dt>Ai tuyển</dt><dd>%s</dd></div>
            <div><dt>Portfolio cần có</dt><dd>%s</dd></div>
          </dl>
          <a class="role-track" href="%s">Học ở %s →</a>
        </div>
      </article>""" % (r["n"], r["name"], r["line"], r["day"], r["who"], r["port"], thref, tname)


PAGE_CSS = """
<style>
  .lead-block{max-width:780px;}
  .role{
    display:grid;grid-template-columns:78px minmax(0,1fr);gap:26px;
    padding:32px 0;border-top:1px solid var(--line);
  }
  .role:first-of-type{border-top:0;}
  .role-num{
    font-family:'Unbounded',sans-serif;font-size:clamp(28px,3.4vw,42px);font-weight:700;
    color:transparent;-webkit-text-stroke:1px rgba(255,122,26,.55);line-height:1;padding-top:4px;
  }
  .role h3{margin:0 0 6px;font-size:clamp(19px,2.2vw,26px);}
  .role-line{font-size:14px;letter-spacing:.4px;color:var(--ac);margin:0 0 20px;font-weight:500;}
  .role-dl{margin:0 0 20px;display:grid;gap:14px;}
  .role-dl dt{
    font-family:'Unbounded',sans-serif;font-size:10px;font-weight:600;letter-spacing:1.8px;
    text-transform:uppercase;color:var(--dim);margin-bottom:5px;
  }
  .role-dl dd{margin:0;font-size:15px;line-height:1.7;color:#c9c0b7;}
  .role-track{
    display:inline-flex;align-items:center;gap:8px;
    font-family:'Unbounded',sans-serif;font-size:11.5px;font-weight:600;
    letter-spacing:1.4px;text-transform:uppercase;color:var(--ac);text-decoration:none;
    border-bottom:1px solid rgba(255,122,26,.4);padding-bottom:3px;
  }
  .role-track:hover{color:#fff;border-color:#fff;}
  .where{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:30px;}
  .where .card h3{font-size:16px;margin:0 0 8px;}
  .where .card p{margin:0;font-size:14.5px;line-height:1.7;}
  .rules{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:30px;}
  .rule strong{
    display:block;font-family:'Unbounded',sans-serif;font-size:15px;font-weight:600;
    color:#fff;margin-bottom:8px;line-height:1.4;
  }
  .rule p{margin:0;font-size:14.5px;line-height:1.7;color:#b8afa6;}
  .note-box{
    margin-top:34px;padding:24px 28px;border-radius:4px;
    border:1px dashed rgba(255,255,255,.18);background:rgba(255,255,255,.02);
  }
  .note-box p{margin:0;font-size:15px;line-height:1.75;color:#b8afa6;}
  .note-box strong{color:#ece4db;}
  .hire{
    margin-top:34px;padding:26px 30px;border-radius:4px;
    border:1px solid rgba(255,122,26,.26);background:rgba(255,122,26,.05);
  }
  .hire h3{margin:0 0 10px;font-size:clamp(18px,2.2vw,24px);}
  .hire p{margin:0 0 6px;font-size:15px;line-height:1.75;color:#c9c0b7;}
  @media (max-width:820px){
    .role{grid-template-columns:1fr;gap:12px;}
    .role-num{padding-top:0;}
    .where,.rules{grid-template-columns:1fr;}
  }
</style>
"""

JSONLD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "name": TITLE, "description": DESC,
     "url": URL + "nghe-nghiep.html", "inLanguage": "vi-VN",
     "isPartOf": {"@id": URL + "#studio"}},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": URL},
        {"@type": "ListItem", "position": 2, "name": "Cơ hội nghề nghiệp",
         "item": URL + "nghe-nghiep.html"},
    ]},
]}, ensure_ascii=False)

links, drawer = nav_html("nn")

HEAD = """<!DOCTYPE html>
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
<meta property="og:image" content="%sassets/lo-trinh-automotive-masterclass.jpg">
<meta property="og:url" content="%snghe-nghiep.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="%snghe-nghiep.html">
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
    <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ</a>
    <button class="lxburger" id="lxburger" aria-label="Menu" aria-expanded="false">≡</button>
  </div>
</nav>
<div class="lxdrawer" id="lxdrawer">
  %s
  <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ →</a>
</div>
""" % (TITLE, DESC, TITLE, DESC, URL, URL, URL, JSONLD, PAGE_CSS, links, drawer)

BODY = """
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow">Cơ hội nghề nghiệp</p>
      <h1>Học 3D xong<br>thì làm nghề gì</h1>
      <div class="lead-block">
        <p class="lead">Câu hỏi này đáng được trả lời bằng tên vị trí cụ thể, không phải bằng
        lời hứa. Dưới đây là năm hướng đi mà người học 3D ở Việt Nam thật sự đi vào, mỗi hướng
        kèm việc bạn làm hằng ngày, ai đang tuyển, và portfolio phải có gì thì mới được gọi.</p>
        <p>Chúng tôi viết phần này từ chỗ đứng của một studio đang nhận job: những vị trí ở đây
        là những vị trí chúng tôi từng thuê, từng cộng tác, hoặc từng thấy khách hàng tuyển.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Năm hướng đi</p>
      <h2>Vị trí và việc thật</h2>
      %s
    </div>
  </section>

  <section style="background:rgba(255,255,255,.014);border-top:1px solid var(--line);border-bottom:1px solid var(--line);">
    <div class="wrap">
      <p class="eyebrow">Nơi tuyển</p>
      <h2>Bốn cửa vào nghề</h2>
      <p style="max-width:700px;">Không phải ai cũng bắt đầu ở studio. Bốn cửa dưới đây khác nhau
      về tốc độ học, độ ổn định và kiểu người hợp với nó.</p>
      <div class="where">
        %s
      </div>
      <div class="note-box">
        <p><strong>Về thu nhập:</strong> chúng tôi không đăng con số ước lượng, vì mức trả
        chênh nhau rất xa theo nơi làm, mảng việc và chất lượng portfolio, một con số trung bình
        chỉ làm bạn hiểu sai. Cách tính thì đơn giản: đi làm công ty tính theo tháng, freelance
        tính theo dự án hoặc theo shot. Trong buổi tư vấn, chúng tôi nói thẳng mức mà người ở
        trình độ của bạn đang được trả, dựa trên job studio đang nhận.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <p class="eyebrow">Điều kiện cần</p>
      <h2>Portfolio thế nào thì được gọi</h2>
      <p style="max-width:700px;">Trong nghề này không ai hỏi bằng cấp. Người ta mở portfolio,
      xem hai phút, rồi quyết định. Bốn điều dưới đây quyết định hai phút đó.</p>
      <div class="rules">
        %s
      </div>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="wrap">
      <div class="card" style="padding:clamp(30px,4.5vw,52px);">
        <p class="eyebrow">Đi tiếp thế nào</p>
        <h2 style="margin-bottom:14px;">Chọn hướng rồi chọn hệ</h2>
        <p style="max-width:660px;">Bốn hướng đầu nằm trong <strong style="color:#ece4db;">hệ 3D Automotive</strong>,
        chặng Basic cho hình tĩnh, chặng Masterclass cho phim và xe. Hướng thứ năm nằm trong
        <strong style="color:#ece4db;">hệ 3D × A.I</strong>. Nếu chưa rõ mình hợp hướng nào,
        để lại thông tin, chúng tôi xem qua rồi nói thẳng.</p>
        <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:26px;">
          <a class="lxcta" href="lo-trinh.html" style="padding:15px 30px;font-size:15px;">Xem hai hệ đào tạo →</a>
          <a class="lxcta-ghost" href="lo-trinh.html#dangky">Đăng ký tư vấn hướng đi</a>
        </div>
      </div>

      <div class="hire">
        <h3>Tuyển dụng tại LXAM Studio</h3>
        <p>Studio nhận job quanh năm, và khi cần thêm người thì tìm trước trong số học viên đã học
        qua, vì chúng tôi biết rõ họ làm được gì, quen quy trình nào, và bàn giao file ra sao.</p>
        <p>Hiện chưa có vị trí tuyển cố định. Nếu bạn muốn cộng tác theo dự án, gửi portfolio kèm
        lời nhắn qua <a href="index.html#lienhe" style="color:var(--ac);">phần liên hệ</a>, có job
        hợp tay nghề thì chúng tôi liên lạc.</p>
      </div>
    </div>
  </section>
</main>
""" % (
    "".join(role_card(r) for r in ROLES),
    "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (h, t) for h, t in WHERE),
    "".join('<div class="rule"><strong>%s</strong><p>%s</p></div>' % (h, t) for h, t in PORTFOLIO_RULES),
)

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
        <a href="nghe-nghiep.html">Cơ hội nghề nghiệp</a>
        <a href="blog.html">Blog</a>
        <a href="cam-nang.html">Cẩm nang</a>
        <a href="hoc-vien.html">Khu học viên</a>
        <a href="lo-trinh.html">Lộ trình &amp; học phí</a>
        <a href="khoa-hoc.html">Khóa học</a>
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
    <span>&copy; %d LXAM Studio. All rights reserved.</span>
    <span>3D &middot; Modeling &middot; Lighting &middot; Rendering &middot; Animation &middot; TVC &middot; AI</span>
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
<script src="assets/lx-ui.js?v=den2" defer></script>
</body></html>
""" % YEAR

html = HEAD + BODY + FOOTER
with open(os.path.join(SITE, "nghe-nghiep.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("wrote nghe-nghiep.html  %d B | title %d | desc %d"
      % (len(html.encode("utf-8")), len(TITLE), len(DESC)))
