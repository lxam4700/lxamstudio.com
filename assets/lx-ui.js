/* LXAM UI: nut cuon len dau trang + thanh dang ky co dinh (mobile).
   Tu chen style va markup, khong phu thuoc lx.css. */
(function () {
  if (window.__lxui) return;
  window.__lxui = 1;

  var CSS = [
    '.lxui-top{position:fixed;right:clamp(14px,2.4vw,26px);bottom:clamp(14px,2.4vw,26px);',
    'width:46px;height:46px;border-radius:50%;z-index:70;display:flex;align-items:center;justify-content:center;',
    'border:1px solid rgba(255,255,255,.2);background:rgba(0,0,0,.82);color:#ece4db;',
    '-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);cursor:pointer;padding:0;',
    'opacity:0;visibility:hidden;transform:translateY(10px);',
    'transition:opacity .25s ease,transform .25s ease,visibility .25s,border-color .2s ease;}',
    '.lxui-top.on{opacity:1;visibility:visible;transform:none;}',
    '.lxui-top:hover{border-color:rgba(255,122,26,.65);color:#fff;}',
    '.lxui-top:focus-visible{outline:2px solid #ff7a1a;outline-offset:3px;}',
    '.lxui-top svg{width:17px;height:17px;display:block;}',

    '.lxui-bar,.lxui-top{font-family:\'Be Vietnam Pro\',system-ui,-apple-system,sans-serif;}',
    '.lxui-bar{position:fixed;left:0;right:0;bottom:0;z-index:69;display:none;',
    'gap:10px;align-items:center;padding:10px clamp(12px,4vw,18px) calc(10px + env(safe-area-inset-bottom));',
    'background:#000000;box-shadow:0 -14px 30px rgba(0,0,0,.55);',
    'border-top:1px solid rgba(255,255,255,.12);',
    'transform:translateY(110%);transition:transform .28s ease;}',
    '.lxui-bar.on{transform:none;}',
    '.lxui-bar .lxui-txt{flex:1;min-width:0;}',
    '.lxui-bar .lxui-t1{font-family:\'Unbounded\',sans-serif;font-size:11.5px;font-weight:600;color:#fff;line-height:1.35;',
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}',
    '.lxui-bar .lxui-t2{font-size:11px;color:#9a9088;line-height:1.35;margin-top:2px;',
    'white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}',
    '.lxui-cta{flex:0 0 auto;display:inline-flex;align-items:center;justify-content:center;',
    'padding:12px 20px;border-radius:999px;font-size:13.5px;font-weight:600;text-decoration:none;',
    'color:#140c06;background:#ff7a1a;white-space:nowrap;}',
    '.lxui-cta:focus-visible{outline:2px solid #fff;outline-offset:2px;}',

    '@media (max-width:820px){',
    '  .lxui-bar{display:flex;}',
    '  body{padding-bottom:74px;}',
    '  .lxui-top{bottom:calc(74px + env(safe-area-inset-bottom));width:42px;height:42px;}',
    '}',
    '@media (prefers-reduced-motion:reduce){',
    '  .lxui-top,.lxui-bar{transition:none;}',
    '}'
  ].join('');

  var st = document.createElement('style');
  st.textContent = CSS;
  document.head.appendChild(st);

  // --- nut cuon len dau trang -------------------------------------------
  var top = document.createElement('button');
  top.type = 'button';
  top.className = 'lxui-top';
  top.setAttribute('aria-label', 'Lên đầu trang');
  top.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M12 19V5"></path><path d="M5 12l7-7 7 7"></path></svg>';
  top.addEventListener('click', function () {
    var soft = !window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: soft ? 'smooth' : 'auto' });
  });

  // --- thanh dang ky co dinh --------------------------------------------
  var onPage = document.getElementById('dangky');
  var bar = document.createElement('div');
  bar.className = 'lxui-bar';
  bar.innerHTML =
    '<div class="lxui-txt">' +
    '<div class="lxui-t1">Khoá Blender 3D tại LXAM</div>' +
    '<div class="lxui-t2">Ba cách học, xem học phí rồi ghi danh</div>' +
    '</div>' +
    '<a class="lxui-cta" href="' + (onPage ? '#dangky' : 'lo-trinh.html#dangky') + '">Đăng ký →</a>';

  function mount() {
    document.body.appendChild(bar);
    document.body.appendChild(top);
    onScroll();
  }

  // an thanh dang ky khi form ghi danh dang hien tren man hinh
  var formVisible = false;
  if (onPage && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      formVisible = es[0].isIntersecting;
      apply();
    }, { threshold: 0 }).observe(onPage);
  }

  var y = 0;
  function apply() {
    top.classList.toggle('on', y > 700);
    bar.classList.toggle('on', y > 400 && !formVisible);
  }
  var tick = false;
  function onScroll() {
    y = window.pageYOffset || document.documentElement.scrollTop || 0;
    if (tick) return;
    tick = true;
    requestAnimationFrame(function () { tick = false; apply(); });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
