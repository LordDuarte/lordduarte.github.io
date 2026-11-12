/* Céu estrelado e grama em pixel art (canvas). Sem dependências. */
(function () {
  function R(g, x, y, w, h, c) { g.fillStyle = c; g.fillRect(x | 0, y | 0, w | 0, h | 0); }
  function rnd(s) { return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }

  var sky = document.getElementById('sky');
  if (sky) {
    var sg = sky.getContext('2d'), stars = [];
    var size = function () {
      var s = 4;
      sky.width = Math.ceil(innerWidth / s);
      sky.height = Math.ceil(innerHeight / s);
      var r = rnd(7); stars = [];
      for (var i = 0; i < 70; i++) stars.push({ x: r() * sky.width | 0, y: r() * sky.height | 0, t: r() * 6, b: r() < 0.25 });
    };
    var draw = function (t) {
      var bands = ['#150c2b', '#1a0f36', '#1f1445', '#241752'];
      for (var i = 0; i < bands.length; i++) R(sg, 0, i * sky.height / 4, sky.width, sky.height / 4 + 1, bands[i]);
      stars.forEach(function (s) {
        var col = Math.floor(t / 500 + s.t) % 4 === 0 ? '#8f7fc4' : '#e8b830';
        R(sg, s.x, s.y, 1, 1, col);
        if (s.b) { R(sg, s.x - 1, s.y, 3, 1, col); R(sg, s.x, s.y - 1, 1, 3, col); }
      });
    };
    size(); draw(0);
    addEventListener('resize', function () { size(); draw(0); });
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
      (function loop(t) { draw(t); setTimeout(function () { requestAnimationFrame(loop); }, 250); })(0);
    }
  }

  var gr = document.getElementById('grass');
  if (gr) {
    var g = gr.getContext('2d'), r = rnd(3);
    gr.width = 260; gr.height = 6;
    R(g, 0, 3, 260, 3, '#4a8a34'); R(g, 0, 5, 260, 1, '#35652a');
    for (var x = 0; x < 260; x++) {
      var h = r() < 0.5 ? 1 : (r() < 0.5 ? 2 : 3);
      R(g, x, 3 - h, 1, h, r() < 0.3 ? '#a8d86a' : '#6ab04c');
    }
  }
})();
