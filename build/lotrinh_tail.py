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
        ("khoa-hoc.html", "Khóa học", None),
        (PAGES["hub"], "Lộ trình &amp; học phí", "hub"),
        ("index.html#portfolio", "Portfolio", None),
        ("ve-chung-toi.html", "Về chúng tôi", None),
        ("blog.html", "Blog", None),
        ("hoc-vien.html", "Khu học viên", None),
    ]
    out = ""
    for href, label, key in items:
        cls = ' class="is-active"' if key == "hub" and active in ("hub", "auto", "ai") else ""
        out += '<a href="%s"%s>%s</a>' % (href, cls, label)
    return out


DRAWER = (
    '<a href="khoa-hoc.html">Khóa học</a>'
    '<a href="%s">Hệ 3D Automotive</a>'
    '<a href="%s">Hệ 3D × A.I</a>'
    '<a href="index.html#portfolio">Portfolio</a>'
    '<a href="cam-nang.html">Cẩm nang</a>'
    '<a href="ve-chung-toi.html">Về chúng tôi</a>'
    '<a href="blog.html">Blog</a>'
    '<a href="hoc-vien.html">Khu học viên</a>'
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
          <div style="padding:10px;border-radius:20px;background:linear-gradient(135deg,var(--ac),var(--ac-red));box-shadow:0 18px 50px rgba(226,45,15,.34);">
            <img src="assets/cef4dd06.webp" alt="Mã QR chuyển khoản Techcombank LXAM Studio" style="width:min(260px,62vw);height:auto;display:block;border-radius:13px;" width="700" height="788" loading="lazy" decoding="async">
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
      <p class="eyebrow"><a href="lo-trinh.html" style="color:inherit;text-decoration:none;">Lộ trình học</a> — Hệ 01</p>
      <h1>Hệ 3D Automotive</h1>
      <p class="lead" style="max-width:740px;">Lộ trình 3D truyền thống, đi từ thao tác đầu tiên trong Blender đến một
      TVC ô tô hoàn chỉnh. Dành cho người muốn làm nghề bằng chính tay mình — dựng, chiếu sáng, render, dựng phim.</p>
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
     "Bạn sẵn sàng bỏ 3–4 tháng để có kỹ năng dùng được nhiều năm."]
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
      <p class="eyebrow"><a href="lo-trinh.html" style="color:inherit;text-decoration:none;">Lộ trình học</a> — Hệ 02</p>
      <h1>Hệ 3D × A.I</h1>
      <p class="lead" style="max-width:740px;">Dành cho người cần AI trong công việc hình ảnh: marketing, thương mại
      điện tử, content sản phẩm. Vẫn học 3D trước — vì AI chỉ nghe lời người biết mình muốn gì — rồi mới ghép AI
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
      hoặc để lại thông tin bên dưới — tôi xem qua rồi nói thẳng bạn nên vào hệ nào.</p>
    </div>
  </section>
""" % (
    hub_card(PAGES["auto"], "01", "Hệ 01 · 3D Automotive", "3–4 tháng",
             "Làm nghề 3D bằng tay mình",
             "Từ thao tác đầu tiên trong Blender tới một TVC ô tô hoàn chỉnh.",
             ["Modeling · Lighting · Rendering · Animation",
              "Hard-surface nâng cao, car modeling Lamborghini Veneno",
              "Đầu ra là một TVC ô tô do bạn tự dựng",
              "Học phí từ 2,5tr tuỳ cách học"],
             "assets/lo-trinh-automotive-masterclass.jpg",
             "Hệ 3D Automotive — lộ trình Blender tới TVC ô tô tại LXAM Academy", False),
    hub_card(PAGES["ai"], "02", "Hệ 02 · 3D × A.I", "4 tháng",
             "Đưa AI vào quy trình hình ảnh",
             "Học 3D nền tảng trước, rồi ghép AI vào để nhân sản lượng lên.",
             ["3 tháng 3D Basic, 1 tháng A.I Advance",
              "Tư duy prompt, góc máy và ánh sáng với AI",
              "Nano Banana Pro · Seedance · Kling 3.0",
              "Học phí từ 2,5tr tuỳ cách học"],
             "assets/lo-trinh-ai-advance.jpg",
             "Hệ 3D × A.I — khoá AI cho người làm hình ảnh tại LXAM Academy", True),
) + reg_form(
    "Chưa biết chọn hệ nào?",
    "Để lại thông tin, tôi gọi tư vấn và nói thẳng bạn nên vào hệ nào — trước khi bạn đóng bất kỳ khoản nào."
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
    if(!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email)) return fail('Email trông chưa đúng — kiểm tra lại giúp mình.');

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
        <a href="khoa-hoc.html">Khóa học</a>
        <a href="lo-trinh-3d-automotive.html">Hệ 3D Automotive</a>
        <a href="lo-trinh-3d-ai.html">Hệ 3D × A.I</a>
        <a href="index.html#portfolio">Portfolio</a>
        <a href="cam-nang.html">Cẩm nang</a>
        <a href="ve-chung-toi.html">Về chúng tôi</a>
        <a href="blog.html">Blog</a>
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
    {"@type": "ItemList", "name": "Hệ 3D Automotive — LXAM Academy", "itemListElement": [
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
    {"@type": "ItemList", "name": "Hệ 3D × A.I — LXAM Academy", "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": course(
            "3D Basic — Blender Foundation",
            "3 tháng nền tảng: modeling hard-surface, material & lighting, rendering, tư duy hình ảnh.",
            PAGES["ai"], 3)},
        {"@type": "ListItem", "position": 2, "item": course(
            "A.I Advance — AI × Visual",
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
     "Lộ trình học — LXAM Studio",
     "Hai hệ đào tạo riêng tại LXAM Academy: 3D Automotive (Blender tới TVC ô tô) và 3D × A.I cho người cần AI trong công việc hình ảnh.",
     JSONLD_HUB, "lo-trinh-automotive-masterclass.jpg", BODY_HUB, "hub"),
    (PAGES["auto"],
     "Hệ 3D Automotive — Học phí & lộ trình | LXAM",
     "Lộ trình Blender từ con số 0 tới TVC ô tô hoàn chỉnh. Nội dung từng tháng, ba cách học và học phí từ 2,5tr.",
     JSONLD_AUTO, "lo-trinh-automotive-masterclass.jpg", BODY_AUTO, "auto"),
    (PAGES["ai"],
     "Hệ 3D × A.I — Học phí & lộ trình | LXAM",
     "3 tháng 3D nền tảng cộng 1 tháng A.I Advance: prompt, ánh sáng với AI, workflow 3D × AI. Học phí từ 2,5tr.",
     JSONLD_AI, "lo-trinh-ai-advance.jpg", BODY_AI, "ai"),
]

for fname, title, desc, ld, og, body, active in OUT:
    html = head(title, desc, fname, ld, og, active) + body + FOOTER
    with open(os.path.join(SITE, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %-28s %6d B" % (fname, len(html.encode("utf-8"))))
