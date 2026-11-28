# -*- coding: utf-8 -*-
"""Trang he 3D Automotive ban gon (11/2026).
Chi giu thu nguoi xem can de quyet: lo trinh 2 chang, 3 goi hoc phi, dieu khoan tom tat, form.
Chu tieng Anh dung BrownSport, chu tieng Viet dung Be Vietnam Pro / Unbounded (co dau)."""

AV_CSS = """
<style>
  @font-face{font-family:'BrownSport';src:url("assets/brown-italic.woff2") format('woff2');font-style:italic;font-weight:400;font-display:swap;}
  @font-face{font-family:'BrownSport';src:url("assets/brown.woff2") format('woff2');font-style:normal;font-weight:400;font-display:swap;}
  .av{font-family:'Be Vietnam Pro',system-ui,sans-serif;}
  .av-en{font-family:'BrownSport',sans-serif;font-style:italic;font-weight:400;}
  .av-k{font-family:'BrownSport',sans-serif;font-size:12px;letter-spacing:2.4px;text-transform:uppercase;color:var(--ac);margin:0 0 14px;}
  .av-h2{font-family:'Unbounded',sans-serif;font-weight:500;text-transform:none;letter-spacing:-.01em;
         font-size:clamp(24px,2.8vw,38px);line-height:1.15;margin:0 0 clamp(22px,3vw,36px);color:#fff;}
  .av-sec{padding:clamp(64px,8vw,120px) 0 0;}

  /* HERO */
  .av-hero{position:relative;margin-top:clamp(20px,3vw,40px);border-radius:14px;overflow:hidden;min-height:clamp(440px,58vw,640px);
           display:flex;align-items:flex-end;isolation:isolate;}
  .av-hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 50%;z-index:-2;}
  .av-hero::before{content:"";position:absolute;inset:0;z-index:-1;
    background:linear-gradient(90deg,rgba(0,0,0,.86) 0%,rgba(0,0,0,.55) 42%,rgba(0,0,0,0) 72%),
               linear-gradient(0deg,rgba(0,0,0,.75) 0%,rgba(0,0,0,0) 45%);}
  .av-hi{padding:clamp(22px,4.4vw,64px);max-width:none;width:100%;box-sizing:border-box;min-width:0;}
  .av-bc{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#cfc6bd;margin:0 0 16px;}
  .av-bc a{color:inherit;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35);}
  .av-h1{font-family:'BrownSport',sans-serif;font-style:italic;font-weight:400;text-transform:uppercase;
         font-size:clamp(34px,6vw,88px);line-height:.92;white-space:nowrap;margin:0 0 18px;color:#fff;}
  .av-lead{font-size:clamp(16px,1.5vw,19px);line-height:1.55;color:#eee6de;margin:0 0 24px;max-width:46ch;}
  .av-facts{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 28px;padding:0;list-style:none;}
  .av-facts li{padding:8px 14px;border-radius:999px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.16);
               font-size:13.5px;color:#fff;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);}
  .av-facts b{color:var(--ac);font-weight:600;}
  .av-btns{display:flex;flex-wrap:wrap;gap:12px;align-items:center;}
  .av-b{display:inline-flex;align-items:center;gap:10px;padding:15px 26px;border-radius:999px;background:var(--ac);color:#000;
        font-weight:700;font-size:15px;text-decoration:none;transition:transform .25s,background .25s;}
  .av-b:hover{transform:translateY(-2px);background:#ff9447;}
  .av-g{display:inline-flex;align-items:center;padding:14px 22px;border-radius:999px;border:1px solid rgba(255,255,255,.4);
        color:#fff;font-weight:500;font-size:14.5px;text-decoration:none;transition:border-color .25s,color .25s;}
  .av-g:hover{border-color:var(--ac);color:var(--ac);}

  /* LO TRINH */
  .av-path{display:grid;grid-template-columns:1fr 1fr;gap:clamp(14px,1.8vw,22px);position:relative;}
  .av-st{display:flex;flex-direction:column;border-radius:10px;overflow:hidden;background:#0d0d0d;border:1px solid var(--line);}
  .av-st img{width:100%;height:auto;aspect-ratio:4/3;object-fit:cover;object-position:50% 30%;display:block;transition:transform 1.2s cubic-bezier(.2,.7,.2,1);}
  .av-st:hover img{transform:scale(1.03);}
  .av-st>div{padding:clamp(20px,2.4vw,30px);}
  .av-tag{display:inline-block;font-family:'BrownSport',sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;
          padding:4px 10px;border-radius:999px;border:1px solid var(--ac);color:var(--ac);margin:0 0 12px;}
  .av-st.mx .av-tag{background:var(--ac);color:#000;}
  .av-st h3{font-family:'Unbounded',sans-serif;font-weight:600;text-transform:none;font-size:clamp(18px,1.6vw,22px);
            line-height:1.2;margin:0 0 14px;color:#fff;letter-spacing:-.01em;}
  .av-chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px;padding:0;list-style:none;}
  .av-chips li{font-size:13px;padding:6px 11px;border-radius:6px;background:#181818;color:#e6ddd4;}
  .av-out{font-size:14.5px;line-height:1.5;color:#d9cfc5;margin:0;}
  .av-out b{color:#fff;font-weight:600;}
  .av-more{margin-top:14px;border-top:1px solid var(--line);}
  .av-more summary{cursor:pointer;list-style:none;padding:14px 0 4px;font-size:13.5px;font-weight:600;color:var(--ac);}
  .av-more summary::-webkit-details-marker{display:none;}
  .av-more summary::after{content:" +";}
  .av-more[open] summary::after{content:" −";}
  .av-more dl{margin:8px 0 0;display:grid;grid-template-columns:auto 1fr;gap:8px 14px;font-size:13.5px;line-height:1.5;}
  .av-more dt{color:#fff;font-weight:600;white-space:nowrap;}
  .av-more dd{margin:0;color:var(--muted);}

  /* DAI NGHE THUAT */
  .av-art{padding:clamp(70px,9vw,130px) 0 0;overflow:hidden;}
  .av-art-in{display:flex;gap:.6em;white-space:nowrap;width:max-content;animation:avMq 28s linear infinite;
             font-family:'BrownSport',sans-serif;font-style:italic;text-transform:uppercase;line-height:1;
             font-size:clamp(54px,10vw,150px);color:transparent;-webkit-text-stroke:1px rgba(255,122,26,.55);}
  .av-art-in span::after{content:"  ·";}
  @keyframes avMq{to{transform:translateX(-50%);}}
  @media (prefers-reduced-motion:reduce){.av-art-in{animation:none;}}

  /* HOC PHI */
  .av-pr{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,20px);align-items:stretch;}
  .av-p{position:relative;display:flex;flex-direction:column;padding:clamp(22px,2.4vw,32px);border-radius:8px;
        background:#0d0d0d;border:1px solid var(--line);}
  .av-p.hot{border-color:rgba(255,122,26,.6);background:linear-gradient(180deg,rgba(255,122,26,.12),rgba(255,122,26,0) 55%),#0d0d0d;}
  .av-p .av-badge{position:absolute;top:-12px;left:22px;padding:4px 11px;border-radius:999px;background:var(--ac);color:#000;
                  font-size:11.5px;font-weight:700;}
  .av-p h3{font-family:'Unbounded',sans-serif;font-weight:600;text-transform:none;font-size:17px;margin:0 0 16px;color:#fff;}
  .av-price{font-family:'Unbounded',sans-serif;font-weight:600;font-size:clamp(34px,3.4vw,46px);line-height:1;color:#fff;margin:0 0 6px;}
  .av-price small{font-size:.42em;font-weight:500;color:var(--muted);margin-right:6px;}
  .av-note{font-size:13px;color:var(--muted);margin:0 0 20px;min-height:1.4em;}
  .av-p ul{list-style:none;margin:0 0 24px;padding:20px 0 0;border-top:1px solid var(--line);display:grid;gap:11px;}
  .av-p li{display:flex;gap:10px;font-size:14.5px;line-height:1.45;color:#e6ddd4;}
  .av-p li::before{content:"✓";color:var(--ac);font-weight:700;flex:0 0 auto;}
  .av-p .av-cta{margin-top:auto;display:flex;justify-content:center;padding:14px 18px;border-radius:999px;
                border:1px solid rgba(255,255,255,.25);color:#fff;text-decoration:none;font-weight:600;font-size:14.5px;
                transition:background .25s,border-color .25s,color .25s;}
  .av-p .av-cta:hover{border-color:var(--ac);color:var(--ac);}
  .av-p.hot .av-cta{background:var(--ac);border-color:var(--ac);color:#000;}
  .av-p.hot .av-cta:hover{background:#ff9447;color:#000;}
  .av-extra{display:flex;flex-wrap:wrap;gap:10px 28px;margin:22px 0 0;font-size:14px;color:#d9cfc5;}
  .av-extra b{color:var(--ac);font-weight:600;}

  .av-trust{list-style:none;margin:0;padding:22px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
            display:flex;flex-wrap:wrap;gap:10px 30px;font-size:14px;color:#d9cfc5;}
  .av-trust li::before{content:"✓ ";color:var(--ac);font-weight:700;}
  .av-trust li.sw{margin-left:auto;}
  .av-trust li.sw::before,.av-trust li:nth-child(4)::before{content:"";}
  .av-trust a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35);}
  .av-trust a:hover{color:var(--ac);border-color:var(--ac);}
  @media (max-width:700px){.av-trust{flex-direction:column;}.av-trust li.sw{margin-left:0;}}
  /* DIEU KHOAN + HOP VOI AI */
  .av-two{display:grid;grid-template-columns:1fr 1fr;gap:clamp(14px,1.8vw,22px);}
  .av-box{padding:clamp(22px,2.6vw,34px);border-radius:8px;background:#0d0d0d;border:1px solid var(--line);}
  .av-box h3{font-family:'Unbounded',sans-serif;font-weight:500;text-transform:none;font-size:18px;margin:0 0 16px;color:#fff;}
  .av-box ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;}
  .av-box li{display:flex;gap:10px;font-size:14.5px;line-height:1.5;color:#d9cfc5;}
  .av-box li::before{content:"";flex:0 0 6px;height:6px;margin-top:.6em;border-radius:50%;background:var(--ac);}
  .av-box p{font-size:14px;color:var(--muted);margin:16px 0 0;line-height:1.55;}
  .av-box a{color:#fff;}
  .av-box a:hover{color:var(--ac);}

  @media (max-width:900px){
    .av-path,.av-pr,.av-two{grid-template-columns:1fr;}
    .av-pr{gap:24px;}
    .av-hero{min-height:560px;}
    .av-hero img{object-position:70% 50%;}
    .av-hero::before{background:linear-gradient(0deg,rgba(0,0,0,.92) 0%,rgba(0,0,0,.55) 55%,rgba(0,0,0,.1) 100%);}
  }
  @media (max-width:600px){ .av-h1{white-space:normal;font-size:clamp(34px,11vw,52px);} }
  @media (max-width:520px){
    .av-btns .av-b,.av-btns .av-g{flex:1 1 100%;justify-content:center;}
  }
</style>
"""


def _more(rows):
    return ('<details class="av-more"><summary>Xem chi tiết nội dung</summary><dl>%s</dl></details>'
            % "".join("<dt>%s</dt><dd>%s</dd>" % r for r in rows))


AV_BASIC_MORE = _more([
    ("Modeling", "extrude, bevel, bridge, boolean; dựng sản phẩm đúng tỉ lệ, đúng form"),
    ("Shading", "Geometry Node, vật liệu PBR"),
    ("Lighting", "các loại đèn, hướng sáng"),
    ("Camera", "bố cục khung hình, góc máy"),
    ("Render", "resolution, denoise, compositing, tối ưu CPU và GPU"),
])
AV_MASTER_MORE = _more([
    ("Modeling", "hard-surface nâng cao, dựng xe Lamborghini Veneno"),
    ("Concept", "sketch, kịch bản, storyboard"),
    ("Rigging", "rig xe bằng LC Addon"),
    ("Animation", "keyframe, tư duy điện ảnh"),
    ("VFX · SFX", "khí động học, hiệu ứng ánh sáng, âm thanh, nhạc nền"),
    ("Render", "ánh sáng điện ảnh, grading, render bản cuối"),
])


def body_auto_v2(reg_form_html, ai_href):
    return AV_CSS + """
<main class="av">
  <section style="padding:0;">
    <div class="wrap">
      <div class="av-hero">
        <img src="assets/slide-mercedes-g63.webp" alt="Mercedes G63 dựng và render 3D trong TVC của LXAM Studio" width="1440" height="900" fetchpriority="high">
        <div class="av-hi">
          <p class="av-bc"><a href="lo-trinh.html">Lộ trình học</a> · Hệ 01</p>
          <h1 class="av-h1">3D Automotive</h1>
          <p class="av-lead">Từ thao tác đầu tiên trong Blender tới một TVC ô tô do chính tay bạn dựng.</p>
          <ul class="av-facts">
            <li><b>6 đến 9</b> tháng</li>
            <li>Đầu ra: <b>1 TVC ô tô</b></li>
          </ul>
          <div class="av-btns">
            <a class="av-b" href="#dangky" data-he="Hệ 3D Automotive" data-goi="">Giữ chỗ, nhận tư vấn →</a>
            <a class="av-g" href="#hocphi">Xem học phí</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="automotive" class="av-sec">
    <div class="wrap">
      <p class="av-k">Step 01 · Roadmap</p>
      <h2 class="av-h2">Hai chặng, đi từ nền tới TVC.</h2>
      <div class="av-path">
        <article class="av-st">
          <img src="assets/st-auto-basic.webp" alt="Cận cảnh đèn pha Mercedes G63 dựng 3D, chặng Basic hệ Automotive" width="960" height="720" loading="lazy" decoding="async">
          <div>
            <span class="av-tag">Basic</span>
            <h3>Automotive Beginner</h3>
            <p class="av-out"><b>Đầu ra:</b> tự dựng và render một sản phẩm hoàn chỉnh, đủ đưa vào portfolio.</p>
            %s
          </div>
        </article>
        <article class="av-st mx">
          <img src="assets/st-auto-master.webp" alt="Mercedes G63 lao qua cảnh cháy nổ trong TVC 3D, chặng Master hệ Automotive" width="960" height="720" loading="lazy" decoding="async">
          <div>
            <span class="av-tag">Master</span>
            <h3>Automotive Masterclass</h3>
            <p class="av-out"><b>Đầu ra:</b> một TVC ô tô từ concept tới bản dựng cuối. Đã gồm toàn bộ chặng Basic.</p>
            %s
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="av-art" aria-hidden="true"><div class="av-art-in"><span>Make every frame art</span><span>Make every frame art</span></div></section>

  <section id="hocphi" class="av-sec">
    <div class="wrap">
      <p class="av-k">Step 02 · Pricing</p>
      <h2 class="av-h2">Chọn cách bạn muốn đi.</h2>
      <div class="av-pr">
        <div class="av-p">
          <h3>Basic quay sẵn</h3>
          <p class="av-price">2,5tr</p>
          <p class="av-note">Học theo nhịp của bạn</p>
          <ul>
            <li>Bài giảng quay sẵn, xem lại không giới hạn</li>
            <li>Tặng 2 buổi chữa bài trực tiếp Chủ nhật</li>
          </ul>
          <a class="av-cta" href="#dangky" data-he="Hệ 3D Automotive" data-goi="tuhoc">Chọn gói này</a>
        </div>
        <div class="av-p hot">
          <span class="av-badge">Nhiều người chọn</span>
          <h3>Lớp 8 tuần</h3>
          <p class="av-price">12tr</p>
          <p class="av-note">Chia 2 mốc, mỗi mốc 6tr</p>
          <ul>
            <li>Có lịch, có deadline, không bỏ giữa chừng</li>
            <li>Tặng 8 buổi chữa bài 1:1</li>
          </ul>
          <a class="av-cta" href="#dangky" data-he="Hệ 3D Automotive" data-goi="lop8tuan">Chọn gói này</a>
        </div>
        <div class="av-p">
          <span class="av-badge">Đi xa nhất</span>
          <h3>Coaching Basic lên Master</h3>
          <p class="av-price"><small>từ</small>15tr</p>
          <p class="av-note">Basic 15tr · Master 20tr · Trọn lộ trình 30tr</p>
          <ul>
            <li>Kèm 1:1 tới lúc bạn giỏi thì thôi</li>
            <li>Sửa trực tiếp trên file của bạn</li>
          </ul>
          <a class="av-cta" href="#dangky" data-he="Hệ 3D Automotive" data-goi="kemrieng">Chọn gói này</a>
        </div>
      </div>
      <div class="av-extra">
        <span>Đóng trước 50%%: <b>tặng thêm 6 tháng coaching</b></span>
        <span>Chỉ thiếu một mảng? Học lẻ <b>5tr / kỹ năng</b></span>
      </div>
    </div>
  </section>

  <section class="av-sec" style="padding-bottom:clamp(64px,8vw,120px);">
    <div class="wrap">
      <ul class="av-trust">
        <li>Bảo hành kiến thức trọn đời</li>
        <li>Bảo lưu khi bận việc</li>
        <li>Tư vấn trước khi đóng tiền</li>
        <li><a href="dieu-khoan.html">Điều khoản →</a></li>
        <li class="sw"><a href="%s">Cần hình nhanh để bán hàng? Hệ 3D × A.I →</a></li>
      </ul>
    </div>
  </section>
""" % (AV_BASIC_MORE, AV_MASTER_MORE, ai_href) + reg_form_html + "</main>\n"


AI_BASIC_MORE = _more([
    ("Modeling", "hard-surface, sản phẩm, form chuẩn"),
    ("Material", "hiểu vật liệu để render ra hình bán được"),
    ("Lighting", "ánh sáng, mood, góc máy"),
    ("Render", "setup scene sạch, tối ưu workflow"),
    ("Tư duy hình", "bố cục, storytelling cơ bản"),
])
AI_ADV_MORE = _more([
    ("Prompt", "diễn đạt để AI hiểu đúng ý tưởng"),
    ("Góc máy · ánh sáng", "kiểm soát mood, cảm giác điện ảnh với AI"),
    ("Workflow 3D × AI", "lấy render làm gốc, để AI nhân ra nhiều phiên bản"),
    ("Công cụ", "Nano Banana Pro, Seedance, Kling 3.0"),
])


def body_ai_v2(reg_form_html, auto_href):
    return AV_CSS + """
<main class="av">
  <section style="padding:0;">
    <div class="wrap">
      <div class="av-hero">
        <img src="assets/ac-bg.webp" alt="Chân dung robot mặt người, hình đại diện hệ 3D × A.I của LXAM Academy" width="1392" height="936" fetchpriority="high" style="object-position:80%% 35%%;">
        <div class="av-hi">
          <p class="av-bc"><a href="lo-trinh.html">Lộ trình học</a> · Hệ 02</p>
          <h1 class="av-h1">3D × A.I</h1>
          <p class="av-lead">Vững 3D trước, rồi để AI nhân một sản phẩm thành hàng chục hình.</p>
          <ul class="av-facts">
            <li><b>4</b> tháng</li>
            <li>Từ con số 0</li>
          </ul>
          <div class="av-btns">
            <a class="av-b" href="#dangky" data-he="Hệ 3D × A.I" data-goi="">Giữ chỗ, nhận tư vấn →</a>
            <a class="av-g" href="#hocphi">Xem học phí</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section id="ai" class="av-sec">
    <div class="wrap">
      <p class="av-k">Step 01 · Roadmap</p>
      <h2 class="av-h2">3 tháng 3D, 1 tháng AI.</h2>
      <div class="av-path">
        <article class="av-st">
          <img src="assets/st-ai-basic.webp" alt="Chi tiết mạch cơ khí trên mũ robot, chặng 3D Basic hệ 3D × A.I" width="960" height="720" loading="lazy" decoding="async">
          <div>
            <span class="av-tag">3D Basic</span>
            <h3>Blender Foundation</h3>
            <p class="av-out"><b>Đầu ra:</b> tự dựng và render được một sản phẩm hoàn chỉnh.</p>
            %s
          </div>
        </article>
        <article class="av-st mx">
          <img src="assets/st-ai-adv.webp" alt="Khuôn mặt robot người, chặng A.I Advance hệ 3D × A.I" width="960" height="720" loading="lazy" decoding="async">
          <div>
            <span class="av-tag">A.I Advance</span>
            <h3>AI × Visual</h3>
            <p class="av-out"><b>Đầu ra:</b> từ 1 sản phẩm ra 5 đến 10 biến thể chất lượng cao, nhanh.</p>
            %s
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="av-art" aria-hidden="true"><div class="av-art-in"><span>Make every frame art</span><span>Make every frame art</span></div></section>

  <section id="hocphi" class="av-sec">
    <div class="wrap">
      <p class="av-k">Step 02 · Pricing</p>
      <h2 class="av-h2">Chọn cách bạn muốn đi.</h2>
      <div class="av-pr">
        <div class="av-p">
          <h3>Basic quay sẵn</h3>
          <p class="av-price">2,5tr</p>
          <p class="av-note">Học theo nhịp của bạn</p>
          <ul>
            <li>Bài giảng quay sẵn, xem lại không giới hạn</li>
            <li>Tặng 2 buổi chữa bài trực tiếp Chủ nhật</li>
          </ul>
          <a class="av-cta" href="#dangky" data-he="Hệ 3D × A.I" data-goi="tuhoc">Chọn gói này</a>
        </div>
        <div class="av-p hot">
          <span class="av-badge">Nhiều người chọn</span>
          <h3>Lớp 8 tuần</h3>
          <p class="av-price">12tr</p>
          <p class="av-note">Chia 2 mốc, mỗi mốc 6tr</p>
          <ul>
            <li>Có lịch, có deadline, không bỏ giữa chừng</li>
            <li>Tặng 8 buổi chữa bài 1:1</li>
          </ul>
          <a class="av-cta" href="#dangky" data-he="Hệ 3D × A.I" data-goi="lop8tuan">Chọn gói này</a>
        </div>
        <div class="av-p">
          <span class="av-badge">Đi xa nhất</span>
          <h3>Coaching 3D lên A.I</h3>
          <p class="av-price"><small>từ</small>15tr</p>
          <p class="av-note">3D Basic 15tr · A.I Advance 10tr · Trọn hệ 22tr</p>
          <ul>
            <li>Kèm 1:1 tới lúc bạn giỏi thì thôi</li>
            <li>Sửa trực tiếp trên file của bạn</li>
          </ul>
          <a class="av-cta" href="#dangky" data-he="Hệ 3D × A.I" data-goi="kemrieng">Chọn gói này</a>
        </div>
      </div>
      <div class="av-extra">
        <span>Đóng trước 50%%: <b>tặng thêm 6 tháng coaching</b></span>
        <span>Chỉ thiếu một mảng? Học lẻ <b>5tr / kỹ năng</b></span>
      </div>
    </div>
  </section>

  <section class="av-sec" style="padding-bottom:clamp(64px,8vw,120px);">
    <div class="wrap">
      <ul class="av-trust">
        <li>Bảo hành kiến thức trọn đời</li>
        <li>Bảo lưu khi bận việc</li>
        <li>Tư vấn trước khi đóng tiền</li>
        <li><a href="dieu-khoan.html">Điều khoản →</a></li>
        <li class="sw"><a href="%s">Muốn làm nghề dựng? Hệ 3D Automotive →</a></li>
      </ul>
    </div>
  </section>
""" % (AI_BASIC_MORE, AI_ADV_MORE, auto_href) + reg_form_html + "</main>\n"
