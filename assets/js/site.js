/* Act_ive De_sk — studioPalmes demo build
   Stage 0 direction preview behaviour. Defensive: every feature is gated on
   capability detection and the page is fully usable with this file absent. */
(function () {
  'use strict';

  var reduceMotion =
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Scroll reveals --------------------------------------------------- */
  var revealables = document.querySelectorAll('.reveal');

  if (!revealables.length) {
    // nothing to do
  } else if (reduceMotion || typeof window.IntersectionObserver !== 'function') {
    for (var i = 0; i < revealables.length; i++) {
      revealables[i].classList.add('is-visible');
    }
  } else {
    var observer = new window.IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.08 }
    );

    for (var j = 0; j < revealables.length; j++) {
      observer.observe(revealables[j]);
    }
  }

  /* --- Rise demo -------------------------------------------------------- */
  var stage = document.querySelector('[data-rise-stage]');
  var toggle = document.querySelector('[data-rise-toggle]');
  var stateLabel = document.querySelector('[data-rise-state]');

  if (stage && toggle) {
    var setState = function (standing) {
      stage.classList.toggle('is-standing', standing);
      toggle.setAttribute('aria-pressed', standing ? 'true' : 'false');
      toggle.textContent = standing ? 'Lower the desk' : 'Raise the desk';
      if (stateLabel) stateLabel.textContent = standing ? 'Standing' : 'Seated';
    };

    setState(false);

    toggle.addEventListener('click', function () {
      setState(!stage.classList.contains('is-standing'));
    });
  }

  /* --- Year stamp ------------------------------------------------------- */
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
