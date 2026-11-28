# -*- coding: utf-8 -*-
"""Khu goi dich vu Thue studio (11/2026): 3 goi, bam Lien he bao gia thi so ra thong tin lien he."""

PKGS = [
    ("event", "Event &amp; Activation", "Sự kiện và trải nghiệm thương hiệu",
     "axehibition-toan-canh-khoi-dau-nguoi.webp", "Không gian triển lãm Axehibition do LXAM Studio thiết kế",
     ["Thiết kế và thi công sự kiện", "Booth triển lãm", "Activation thương hiệu", "Decor mặt bằng, sân khấu"]),
    ("print", "Brand &amp; Print", "Nhận diện và ấn phẩm",
     "chivas15-tent-card-mo-mat-truoc.webp", "Ấn phẩm tent card Chivas Regal 15 do LXAM Studio thiết kế",
     ["Logo, bộ nhận diện", "Banner, backdrop", "Standee, POSM", "Catalogue, poster, ấn phẩm in"]),
    ("tvc", "3D TVC", "Phim quảng cáo 3D chuyên nghiệp",
     "mercedes-g63-canh-mo-trong-duong-ham.webp", "Mercedes G63 trong TVC 3D do LXAM Studio thực hiện",
     ["Kịch bản, storyboard", "Dựng 3D sản phẩm, xe", "Animation, VFX", "Dựng phim, âm thanh, bàn giao"]),
]

PROJ = {
    "event": ([("pj-chivas18.webp", "Chivas 18 × Touliver", "Phối cảnh sự kiện", "du-an-chivas-18.html"),
               ("pj-axe.webp", "AXEHIBITION", "Triển lãm hương", "du-an-trien-lam-axe.html"),
               ("pj-chivas15.webp", "Chivas Regal 15", "Photobooth, trưng bày", "du-an-chivas-15-trung-bay.html"),
               ("pj-locphuc10.webp", "Lộc Phúc 10 năm", "Jewelry exhibition", "du-an-locphuc-10-nam.html")],
              ("du-an-event.html", "Xem tất cả dự án Event")),
    "print": ([("pj-tentcard.webp", "Chivas Regal 15", "Tent card, POSM", "du-an-chivas-15-trung-bay.html"),
               ("pj-chivas18chai.webp", "Chivas Regal 18", "Key visual chai XVIII", "du-an-chivas-18-chai-xviii.html"),
               ("pj-locphucbst.webp", "Lộc Phúc", "Key visual bộ sưu tập", "du-an-locphuc-bo-suu-tap.html"),
               ("pj-aston.webp", "Aston Martin DBX", "Key visual", "du-an-aston-martin-dbx.html")],
              ("du-an-san-pham.html", "Xem thêm dự án sản phẩm")),
}

CSS = """
<style>
  @font-face{font-family:'BrownSport';src:url("assets/brown-italic.woff2") format('woff2');font-style:italic;font-weight:400;font-display:swap;}
  .pk{padding:clamp(56px,7vw,100px) 0 0;}
  .pk-k{font-family:'BrownSport',sans-serif;font-style:italic;font-size:12px;letter-spacing:2.4px;text-transform:uppercase;color:var(--ac);margin:0 0 14px;}
  .pk-h{font-family:'Unbounded',sans-serif;font-weight:500;text-transform:none;letter-spacing:-.01em;font-size:clamp(26px,3.2vw,44px);line-height:1.12;margin:0 0 10px;color:#fff;}
  .pk-s{font-size:clamp(15px,1.3vw,17px);color:var(--muted);margin:0 0 clamp(28px,3.4vw,44px);}
  .pk-g{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(12px,1.6vw,20px);align-items:start;}
  .pk-c{border-radius:12px;overflow:hidden;background:#0d0d0d;border:1px solid var(--line);transition:border-color .3s,box-shadow .4s;}
  .pk-c:hover,.pk-c.open{border-color:rgba(255,122,26,.6);box-shadow:0 22px 50px -26px rgba(255,122,26,.4);}
  .pk-im{position:relative;aspect-ratio:4/3;overflow:hidden;}
  .pk-im img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.2s cubic-bezier(.2,.7,.2,1);}
  .pk-c:hover .pk-im img{transform:scale(1.04);}
  .pk-im::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(13,13,13,.95) 100%);}
  .pk-n{position:absolute;z-index:1;left:clamp(20px,2.2vw,28px);right:16px;bottom:14px;margin:0;
        font-family:'BrownSport',sans-serif;font-style:italic;font-weight:400;text-transform:uppercase;line-height:.95;
        font-size:clamp(28px,2.6vw,38px);color:#fff;text-shadow:0 2px 20px rgba(0,0,0,.6);}
  .pk-bd{padding:6px clamp(20px,2.2vw,28px) clamp(20px,2.2vw,28px);}
  .pk-t{font-size:15px;color:var(--ac);font-weight:600;margin:0 0 16px;}
  .pk-ul{list-style:none;margin:0 0 20px;padding:0;display:grid;gap:9px;}
  .pk-ul li{display:flex;gap:10px;font-size:14.5px;line-height:1.45;color:#e6ddd4;}
  .pk-ul li::before{content:"";flex:0 0 6px;height:6px;margin-top:.55em;border-radius:50%;background:var(--ac);}
  .pk-b{width:100%;display:flex;justify-content:center;align-items:center;gap:10px;padding:14px 18px;border-radius:999px;cursor:pointer;
        font:inherit;font-weight:700;font-size:15px;border:0;background:var(--ac);color:#000;transition:background .25s;}
  .pk-b:hover{background:#ff9447;}
  .pk-b i{font-style:normal;display:inline-block;transition:transform .3s;}
  .pk-c.open .pk-b i{transform:rotate(180deg);}
  .pk-ct{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s cubic-bezier(.2,.7,.2,1);}
  .pk-c.open .pk-ct{grid-template-rows:1fr;}
  .pk-ct>div{overflow:hidden;}
  .pk-ct ul{list-style:none;margin:14px 0 0;padding:0;display:grid;gap:8px;}
  .pk-ct a{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:13px 16px;border-radius:10px;
           background:#161616;border:1px solid var(--line);color:#fff;text-decoration:none;font-size:14.5px;transition:border-color .25s,color .25s;}
  .pk-ct a:hover{border-color:var(--ac);color:var(--ac);}
  .pk-ct a span{color:var(--muted);font-size:12.5px;}
  .pk-im{cursor:pointer;}
  .pk-see{position:absolute;z-index:2;top:14px;right:14px;padding:6px 12px;border-radius:999px;font-size:12.5px;font-weight:600;
          background:rgba(0,0,0,.55);color:#fff;border:1px solid rgba(255,255,255,.25);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);
          transition:background .25s,color .25s;}
  .pk-im:hover .pk-see,.pk-c.show .pk-see{background:var(--ac);color:#000;border-color:var(--ac);}
  .pk-c.show{border-color:var(--ac);}
  .pk-pj{display:grid;grid-template-rows:0fr;transition:grid-template-rows .55s cubic-bezier(.2,.7,.2,1);}
  .pk-pj.on{grid-template-rows:1fr;}
  .pk-pj>div{overflow:hidden;}
  .pk-pin{margin-top:clamp(14px,1.6vw,20px);padding:clamp(18px,2.4vw,30px);border-radius:12px;background:#0d0d0d;border:1px solid rgba(255,122,26,.35);}
  .pk-ph{display:flex;justify-content:space-between;align-items:baseline;gap:14px;margin:0 0 18px;}
  .pk-ph b{font-family:'BrownSport',sans-serif;font-style:italic;font-weight:400;text-transform:uppercase;font-size:clamp(20px,2vw,26px);color:#fff;}
  .pk-ph a{font-size:14px;color:var(--ac);text-decoration:none;white-space:nowrap;}
  .pk-ph a:hover{text-decoration:underline;}
  .pk-pg{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}
  .pk-it{display:block;text-decoration:none;color:#fff;border-radius:8px;overflow:hidden;background:#151515;}
  .pk-it img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;transition:transform 1s cubic-bezier(.2,.7,.2,1);}
  .pk-it:hover img{transform:scale(1.05);}
  .pk-it span{display:block;padding:10px 12px 12px;font-size:14px;font-weight:600;line-height:1.3;}
  .pk-it small{display:block;font-weight:400;font-size:12.5px;color:var(--muted);margin-top:2px;}
  .pk-rl{position:relative;border-radius:10px;overflow:hidden;aspect-ratio:1280/540;background:#000;isolation:isolate;transform:translateZ(0);-webkit-mask-image:-webkit-radial-gradient(white,black);}
  .pk-rl img,.pk-rl video{position:absolute;inset:-2px;width:calc(100% + 4px);height:calc(100% + 4px);max-width:none;object-fit:cover;transform:scale(1.02);}
  @media (max-width:900px){ .pk-pg{grid-template-columns:1fr 1fr;} .pk-rl{aspect-ratio:16/10;} }
  .pk-ft{margin:clamp(20px,2.4vw,28px) 0 0;font-size:14px;color:var(--muted);}
  @media (max-width:900px){ .pk-g{grid-template-columns:1fr;} }
</style>
"""


def studio_packages():
    cards = ""
    for key, name, sub, img, alt, items in PKGS:
        li = "".join("<li>%s</li>" % x for x in items)
        subj = "Bao%20gia%20goi%20" + key
        cards += """
      <article class="pk-c" id="goi-%s">
        <div class="pk-im" role="button" tabindex="0" data-pj="%s" aria-controls="pj-%s"><span class="pk-see">Xem dự án ↓</span><img src="assets/%s" alt="%s" width="1800" height="1200" loading="lazy" decoding="async"><h3 class="pk-n">%s</h3></div>
        <div class="pk-bd">
          <p class="pk-t">%s</p>
          <ul class="pk-ul">%s</ul>
          <button class="pk-b" type="button" aria-expanded="false" aria-controls="ct-%s">Liên hệ báo giá <i>↓</i></button>
          <div class="pk-ct" id="ct-%s"><div><ul>
            <li><a href="tel:0942890363">Gọi 0942 890 363 <span>Hotline</span></a></li>
            <li><a href="mailto:anhminhlexuan@gmail.com?subject=%s">anhminhlexuan@gmail.com <span>Gửi brief</span></a></li>
            <li><a href="https://m.me/lxamstudio" target="_blank" rel="noopener">Nhắn fanpage LXAM Studio <span>Messenger ↗</span></a></li>
          </ul></div></div>
        </div>
      </article>""" % (key, key, key, img, alt, name, sub, li, key, key, subj)
    panels = ""
    for key, name, *_ in PKGS:
        if key == "tvc":
            body = ('<div class="pk-rl"><img src="assets/reel-poster.webp" alt="" width="1280" height="541" loading="lazy" decoding="async">'
                    '<video id="pkV" muted loop playsinline preload="none" data-src="assets/reel.mp4" poster="assets/reel-poster.webp" aria-label="Showreel LXAM Studio"></video></div>')
            more = ("du-an-mercedes-g63-tvc.html", "Xem TVC Mercedes G63")
        else:
            items, more = PROJ[key]
            body = '<div class="pk-pg">%s</div>' % "".join(
                '<a class="pk-it" href="%s"><img src="assets/%s" alt="%s, dự án %s của LXAM Studio" width="800" height="600" loading="lazy" decoding="async"><span>%s<small>%s</small></span></a>'
                % (h, im, t, d.lower(), t, d) for im, t, d, h in items)
        panels += ('<div class="pk-pj" id="pj-%s"><div><div class="pk-pin"><div class="pk-ph"><b>%s</b><a href="%s">%s →</a></div>%s</div></div></div>'
                   % (key, name, more[0], more[1], body))
    return CSS + """
<section id="goi" class="pk">
  <div class="wrap">
    <p class="pk-k">Studio packages</p>
    <h2 class="pk-h">Thuê studio theo gói.</h2>
    <p class="pk-s">Ba gói làm trọn từ ý tưởng tới bàn giao. Bấm vào hình để xem dự án đã làm.</p>
    <div class="pk-g">%s
    </div>
    %s
    <p class="pk-ft">Cần kết hợp nhiều gói cho một chiến dịch? Gọi thẳng, mình gộp lại thành một báo giá.</p>
  </div>
</section>
<script>
(function(){
  var v=document.getElementById('pkV');
  function vid(on){ if(!v) return; if(on){ if(!v.src) v.src=v.dataset.src; v.muted=true; var p=v.play(); if(p&&p.catch) p.catch(function(){}); } else if(v.src) v.pause(); }
  function pj(key){
    var open=document.getElementById('pj-'+key), was=open.classList.contains('on');
    document.querySelectorAll('.pk-pj').forEach(function(x){ x.classList.remove('on'); });
    document.querySelectorAll('.pk-c').forEach(function(c){ c.classList.remove('show'); });
    document.querySelectorAll('.pk-see').forEach(function(x){ x.textContent='Xem dự án ↓'; });
    vid(false);
    if(was) return;
    open.classList.add('on');
    var c=document.getElementById('goi-'+key); c.classList.add('show'); c.querySelector('.pk-see').textContent='Đóng ↑';
    if(key==='tvc') vid(true);
    setTimeout(function(){ open.scrollIntoView({behavior:'smooth',block:'nearest'}); },250);
  }
  document.querySelectorAll('.pk-im').forEach(function(m){
    m.addEventListener('click',function(){ pj(m.dataset.pj); });
    m.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); pj(m.dataset.pj); } });
  });
  document.querySelectorAll('.pk-b').forEach(function(b){
    b.addEventListener('click',function(){
      var c=b.closest('.pk-c'), on=!c.classList.contains('open');
      c.classList.toggle('open',on); b.setAttribute('aria-expanded',on?'true':'false');
    });
  });
})();
</script>""" % (cards, panels)
