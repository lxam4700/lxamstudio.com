#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh trang hub cho từng khu portfolio."""

import os, json, datetime

SITE = "/home/claude/site"
YEAR = datetime.date.today().year
URL = "https://lxamstudio.com/"

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


# ---------------------------------------------------------------- DU LIEU
KHU = [
    {
        "slug": "event",
        "ten": "Event &amp; Kích hoạt thương hiệu",
        "tieu_de": "Dự án Event &amp; kích hoạt thương hiệu",
        "desc_meta": ("Dự án event của LXAM Studio: phối cảnh 3D dựng trước để duyệt, và ảnh ghi nhận "
                      "triển lãm sau khi thi công: Chivas Regal 18, AXEHIBITION."),
        "lead": ("Việc của khu này có hai nửa. Nửa trước là phối cảnh 3D dựng khi mặt bằng còn trống, "
                 "để bên thương hiệu duyệt và bên thi công đo. Nửa sau là ảnh chụp lại khi mọi thứ đã "
                 "đứng thật, thứ duy nhất chứng minh bản dựng có ra được đời thực hay không."),
        "title_seo": "Dự án Event | Portfolio LXAM Studio",
        "og": "card-khu-event.webp",
        "items": [
            ("Chivas Regal 18 × Touliver", "Phối cảnh 3D · Duyệt trước thi công",
             "card-chivas18.webp", "du-an-chivas-18.html"),
            ("AXEHIBITION: Hương trong “Ảnh”", "Triển lãm · Ảnh ghi nhận",
             "card-axehibition.webp", "du-an-trien-lam-axe.html"),
            ("Chivas Regal 18 · Chai XVIII", "Render sản phẩm · Key visual",
             "card-chivas18-chai.webp", "du-an-chivas-18-chai-xviii.html"),
            ("Chivas Regal 15 · Trưng bày", "Phối cảnh vật phẩm · Event",
             "card-chivas15.webp", "du-an-chivas-15-trung-bay.html"),
            ("PS Krypton · Launching Stunt", "Phối cảnh 3D · Kích hoạt", None, None),
        ],
    },
    {
        "slug": "automotive",
        "ten": "Automotive",
        "tieu_de": "Dự án Automotive",
        "desc_meta": ("Dự án 3D automotive của LXAM Studio: dựng và render xe ở chuẩn quảng cáo "
                      "bằng Blender: sơn, phản chiếu, kính, bối cảnh."),
        "lead": ("Mảng khó nhất trong hình tĩnh: bề mặt sơn phải đúng, phản chiếu phải hợp lý, "
                 "và chiếc xe phải đứng được trong bối cảnh mà không lộ ghép. Đây là những dự án "
                 "xe LXAM Studio đã dựng và render bằng Blender."),
        "og": "pf-2cdbf5f9.webp",
        "items": [
            ("Mercedes-AMG G63 · TVC", "Cinematic · VFX · Dựng phim",
             "card-mercedes-g63.webp", "du-an-mercedes-g63-tvc.html"),
            ("Porsche 911 · Pit lane", "Key Visual · Lighting",
             "card-porsche-911.webp", "du-an-porsche-911.html"),
            ("McLaren 765LT · Horizon", "Key Visual · Hardsurface",
             "card-mclaren.webp", "du-an-mclaren-765lt.html"),
            ("Aston Martin DBX", "Key Visual · Concept",
             "card-aston-martin-dbx.webp", "du-an-aston-martin-dbx.html"),
            ("Volvo S90", "Chiến dịch · Studio Light",
             "card-volvo-s90.webp", "du-an-volvo-s90.html"),
        ],
    },
    {
        "slug": "san-pham",
        "ten": "Sản phẩm &amp; Kỹ thuật",
        "tieu_de": "Dự án sản phẩm &amp; kỹ thuật",
        "desc_meta": ("Dự án 3D sản phẩm và kỹ thuật: dựng hình hard-surface, phối cảnh lắp ráp, "
                      "cắt lớp cấu tạo và animation kỹ thuật bằng Blender."),
        "lead": ("Nhóm việc studio nhận nhiều nhất: dựng lại sản phẩm đúng tỉ lệ từ bản vẽ kỹ thuật, "
                 "tách lớp cấu tạo, mô phỏng lắp ráp và vận hành. Khách dùng cho catalogue, "
                 "hồ sơ kỹ thuật và quảng cáo."),
        "og": "pf-2afcaceb.webp",
        "items": [
            ("Thiết bị VPLAS · Exploded", "Hardsurface · Product", "pf-2afcaceb.webp", "du-an-vplas.html"),
            ("JHM Masonry Hanger · TVC", "Technical · Animation", "pf-jhm.webp", "du-an-jhm-masonry-hanger.html"),
            ("Engine · Động cơ", "Mechanical · Lighting", "pf-b64a4cd7.webp", None),
            ("Khoá cửa thông minh", "Product · Interior", "card-digital-lock.webp", "du-an-khoa-cua-thong-minh.html"),
            ("Z113 · Dàn phóng phản lực", "Environment · FX", "z113-dan-phong-phan-luc-render-blender.jpg", None),
            ("Insta360 · Pocket Gimbal", "Hardsurface · Bài học viên Lộc", "insta360-gimbal-hoc-vien-loc.jpg", None),
        ],
    },
    {
        "slug": "jewelry",
        "ten": "Jewelry Branding",
        "tieu_de": "Dự án Jewelry Branding",
        "desc_meta": ("Dự án Jewelry Branding của LXAM Studio: key visual và bộ hình chiến dịch cho "
                      "thương hiệu trang sức, dựng bằng 3D để kiểm soát ánh sáng và chất liệu."),
        "lead": ("Một thương hiệu trang sức bán bằng hình trước khi bán bằng món hàng. Khu này là phần hình đó: "
                 "key visual, phối cảnh triển lãm và bộ hình chiến dịch dựng bằng 3D, để cả bộ giữ được một chất ánh sáng "
                 "và một chất kim loại duy nhất, thay vì mỗi buổi chụp ra một kiểu. Trang sức bị soi ở cự ly rất gần, "
                 "nên sai sót về khúc xạ đá hay độ bóng kim loại lộ ngay."),
        "title_seo": "Dự án Jewelry Branding | Portfolio LXAM",
        "og": "card-locphuc-10-nam.webp",
        "items": [
            ("Lộc Phúc Fine Jewelry · Triển lãm 10 năm", "Phối cảnh 3D · Duyệt trước thi công",
             "card-locphuc-10-nam.webp", "du-an-locphuc-10-nam.html"),
            ("Nhẫn kim cương · Key visual", "Macro · Khúc xạ &amp; caustics", None, None),
            ("Dây chuyền &amp; mặt dây", "Studio light · Kim loại quý", None, None),
            ("Đồng hồ cao cấp", "Hardsurface · Macro", None, None),
            ("Bộ sưu tập · Lookbook 3D", "Chiến dịch · Đồng bộ bộ hình", None, None),
            ("Đá màu &amp; chế tác", "Vật liệu · Cắt lớp", None, None),
        ],
    },
]

PAGE_CSS = """
<style>
  .pgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:22px;margin-top:36px;}
  .pitem{
    display:block;text-decoration:none;color:inherit;
    border:1px solid var(--line);border-radius:4px;overflow:hidden;
    background:linear-gradient(180deg,rgba(255,255,255,.025),rgba(255,255,255,0));
    transition:transform .25s ease,border-color .25s ease;
  }
  a.pitem:hover{transform:translateY(-4px);border-color:rgba(255,122,26,.5);}
  .pthumb{aspect-ratio:16/10;overflow:hidden;background:#050505;border-bottom:1px solid var(--line);}
  .pthumb img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .5s ease;}
  a.pitem:hover .pthumb img{transform:scale(1.04);}
  .pbody{padding:22px 24px;display:flex;align-items:flex-start;justify-content:space-between;gap:14px;}
  .pname{
    font-family:'Unbounded',sans-serif;font-size:16px;font-weight:600;
    color:#fff;line-height:1.4;margin:0 0 7px;
  }
  .ptag{font-size:11.5px;letter-spacing:1.5px;text-transform:uppercase;color:var(--ac);margin:0;}
  .pgo{
    flex:0 0 auto;font-family:'Unbounded',sans-serif;font-size:10.5px;font-weight:600;
    letter-spacing:1.4px;text-transform:uppercase;color:var(--ac);white-space:nowrap;padding-top:3px;
  }
  .psoon{
    flex:0 0 auto;font-size:11.5px;letter-spacing:1px;text-transform:uppercase;
    color:var(--faint);white-space:nowrap;padding-top:4px;
  }
  .pthumb-empty{display:flex;align-items:center;justify-content:center;
    background:repeating-linear-gradient(135deg,rgba(255,255,255,.028) 0 12px,rgba(255,255,255,0) 12px 24px);}
  .pthumb-empty span{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--faint);}
  .khu-nav{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px;}
  .khu-nav a{
    display:inline-flex;align-items:center;padding:12px 22px;border-radius:999px;
    border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.04);
    color:#cfc6bd;font-size:14px;font-weight:500;text-decoration:none;
  }
  .khu-nav a.on{border-color:var(--ac);background:rgba(255,122,26,.12);color:#fff;}
  .khu-nav a:hover{border-color:rgba(255,122,26,.55);color:#fff;}
  @media (max-width:760px){ .pgrid{grid-template-columns:1fr;} }
</style>
"""

ALL = [("Event &amp; Kích hoạt", "du-an-event.html"),
       ("Automotive", "du-an-automotive.html"),
       ("Sản phẩm &amp; Kỹ thuật", "du-an-san-pham.html"),
       ("Jewelry Branding", "du-an-jewelry.html")]


def khu_nav(cur):
    # chi hien khu da co trang, khong de link chet
    co = [(t, h) for t, h in ALL if os.path.exists(os.path.join(SITE, h)) or h.endswith(cur + '.html')]
    return '<div class="khu-nav">%s</div>' % "".join(
        '<a href="%s"%s>%s</a>' % (h, ' class="on"' if h.endswith(cur + '.html') else "", t)
        for t, h in co)


def item_html(ten, tag, img, href):
    thumb = ('<div class="pthumb"><img src="assets/%s" alt="%s, dự án 3D của LXAM Studio" '
             'loading="lazy" width="1600" height="1000"></div>' % (img, ten.replace('"', ''))
             ) if img else '<div class="pthumb pthumb-empty"><span>Ảnh đang chuẩn bị</span></div>'
    inner = ('%s'
             '<div class="pbody"><div><p class="pname">%s</p><p class="ptag">%s</p></div>%s</div>'
             % (thumb, ten, tag,
                '<span class="pgo">Xem dự án →</span>' if href
                else '<span class="psoon">Đang cập nhật</span>'))
    if href:
        return '<a class="pitem" href="%s">%s</a>' % (href, inner)
    return '<div class="pitem">%s</div>' % inner


def head(title, desc, canonical, jsonld, og):
    links, drawer = nav_html("pf")
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
    <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ</a>
    <button class="lxburger" id="lxburger" aria-label="Menu" aria-expanded="false">≡</button>
  </div>
</nav>
<div class="lxdrawer" id="lxdrawer">
  %s
  <a class="lxcta" href="lo-trinh.html#dangky">Giữ chỗ →</a>
</div>
""" % (title, desc, title, desc, URL, og, URL, canonical, URL, canonical,
       jsonld, PAGE_CSS, links, drawer)


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
      <p>Studio visual 3D tại Việt Nam, làm TVC, render sản phẩm và animation kỹ thuật bằng Blender. Đồng thời đào tạo Blender 3D từ con số 0.</p>
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
        <a href="hoc-vien.html">Khu học viên</a>
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


for k in KHU:
    fname = "du-an-%s.html" % k["slug"]
    ld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": k["tieu_de"].replace("&amp;", "&"),
         "description": k["desc_meta"], "url": URL + fname, "inLanguage": "vi-VN",
         "isPartOf": {"@id": URL + "#studio"}},
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "name": t.replace("&amp;", "&"),
             "item": (URL + h) if h else None}
            for i, (t, tag, img, h) in enumerate(k["items"])]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": URL},
            {"@type": "ListItem", "position": 2, "name": "Portfolio", "item": URL + "index.html#portfolio"},
            {"@type": "ListItem", "position": 3, "name": k["tieu_de"].replace("&amp;", "&"), "item": URL + fname},
        ]},
    ]}, ensure_ascii=False)
    title = k.get("title_seo") or ("%s | Portfolio LXAM Studio" % k["tieu_de"].replace("&amp;", "&"))
    body = """
<main>
  <section style="padding-bottom:0;">
    <div class="wrap">
      <p class="eyebrow"><a href="index.html#portfolio" style="color:inherit;text-decoration:none;">Portfolio</a></p>
      <h1>%s</h1>
      <p class="lead" style="max-width:760px;">%s</p>
      %s
    </div>
  </section>

  <section>
    <div class="wrap">
      <div class="pgrid">%s</div>
    </div>
  </section>

  <section style="padding-top:0;">
    <div class="wrap">
      <div class="card" style="text-align:center;padding:clamp(30px,4.5vw,56px);border-color:rgba(255,122,26,.28);background:rgba(255,122,26,.05);">
        <h2 style="margin-bottom:12px;">Cần một dự án như thế này?</h2>
        <p style="max-width:560px;margin:0 auto 26px;">Gửi brief hoặc bản vẽ, chúng tôi báo lại thời gian và chi phí. Muốn tự làm được thì xem hai hệ đào tạo.</p>
        <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
          <a class="lxcta" href="index.html#lienhe" style="padding:15px 30px;font-size:15px;">Liên hệ báo giá →</a>
          <a class="lxcta-ghost" href="lo-trinh.html">Xem khoá học</a>
        </div>
      </div>
    </div>
  </section>
</main>
""" % (k["tieu_de"], k["lead"], khu_nav(k["slug"]),
       "".join(item_html(*it) for it in k["items"]))
    html = head(title, k["desc_meta"], fname, ld, k["og"]) + body + FOOTER
    with open(os.path.join(SITE, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %-26s %6d B | %d du an | title %d | desc %d"
          % (fname, len(html.encode("utf-8")), len(k["items"]),
             len(title), len(k["desc_meta"])))
