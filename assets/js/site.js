/* Act_ive De_sk — studioPalmes rebuild
   One script, no dependencies. Every behaviour is progressive: with this file
   absent or scripting disabled the page is complete, readable and navigable. */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion =
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var clamp = function (n, min, max) { return n < min ? min : n > max ? max : n; };

  /* ---------- Reveals ---------------------------------------------------- */
  var revealables = document.querySelectorAll('.reveal, .reveal-group');

  if (reduceMotion || typeof window.IntersectionObserver !== 'function') {
    Array.prototype.forEach.call(revealables, function (el) { el.classList.add('is-visible'); });
  } else {
    var revealObserver = new window.IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        });
      },
      { rootMargin: '0px 0px -10% 0px', threshold: 0.06 }
    );
    Array.prototype.forEach.call(revealables, function (el) { revealObserver.observe(el); });
  }

  /* ---------- Scroll-driven layer --------------------------------------- */
  /* One rAF loop drives the progress bar, the nav state and the desk raise.
     Nothing else listens to scroll. */
  var nav = document.querySelector('[data-nav]');
  var progress = document.querySelector('[data-progress]');
  var riseTrack = document.querySelector('[data-rise-track]');
  var stages = document.querySelectorAll('[data-rise-stages] .rise__stage');
  var heightOut = document.querySelector('[data-height]');
  var ticking = false;
  var currentStage = -1;

  var isDesktopRise = function () {
    return !reduceMotion && window.matchMedia('(min-width: 62rem)').matches;
  };

  var update = function () {
    ticking = false;
    var y = window.pageYOffset || root.scrollTop || 0;

    if (progress) {
      var scrollable = root.scrollHeight - window.innerHeight;
      progress.style.setProperty('--sp', scrollable > 0 ? clamp(y / scrollable, 0, 1) : 0);
    }

    if (nav) nav.classList.toggle('is-scrolled', y > 40);

    if (riseTrack && isDesktopRise()) {
      var rect = riseTrack.getBoundingClientRect();
      var distance = rect.height - window.innerHeight;
      var p = distance > 0 ? clamp(-rect.top / distance, 0, 1) : 0;
      var active = rect.top <= 0 && rect.bottom >= window.innerHeight;

      root.style.setProperty('--p', p.toFixed(4));
      document.body.classList.toggle('is-rising', active);

      if (heightOut) {
        heightOut.lastChild.nodeValue =
          Math.round(580 + (1230 - 580) * p).toLocaleString('en-GB') + 'mm';
      }

      // Copy stages: sit → transition → stand
      var index = p < 0.33 ? 0 : p < 0.72 ? 1 : 2;
      if (index !== currentStage) {
        currentStage = index;
        Array.prototype.forEach.call(stages, function (stage, i) {
          stage.classList.toggle('is-current', i === index);
        });
      }
    }
  };

  var onScroll = function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(update);
  };

  if (typeof window.requestAnimationFrame === 'function') {
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    update();
  }

  // Below the desktop breakpoint, and with reduced motion, the desk is simply
  // shown standing — no pin, no scrub.
  if (!isDesktopRise()) {
    root.style.setProperty('--p', '1');
    Array.prototype.forEach.call(stages, function (stage) { stage.classList.add('is-current'); });
  }

  /* ---------- Mobile drawer ---------------------------------------------- */
  var menuBtn = document.querySelector('[data-menu]');
  var drawer = document.querySelector('[data-drawer]');

  if (menuBtn && drawer) {
    var setMenu = function (open) {
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      drawer.classList.toggle('is-open', open);
      document.body.classList.toggle('is-locked', open);
    };

    menuBtn.addEventListener('click', function () {
      setMenu(menuBtn.getAttribute('aria-expanded') !== 'true');
    });

    // Any navigation closes it, as does Escape or growing past the breakpoint.
    drawer.addEventListener('click', function (event) {
      if (event.target.closest('a')) setMenu(false);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && menuBtn.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        menuBtn.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.matchMedia('(min-width: 64rem)').matches) setMenu(false);
    }, { passive: true });
  }

  /* ---------- Count-ups -------------------------------------------------- */
  var counters = document.querySelectorAll('[data-count]');

  var renderCount = function (el, value) {
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    el.textContent = prefix + value.toLocaleString('en-GB') + suffix;
  };

  var runCount = function (el) {
    var target = parseFloat(el.getAttribute('data-count')) || 0;
    if (reduceMotion || typeof window.requestAnimationFrame !== 'function') {
      renderCount(el, target);
      return;
    }
    var duration = 1400;
    var start = null;
    var step = function (now) {
      if (start === null) start = now;
      var t = clamp((now - start) / duration, 0, 1);
      var eased = 1 - Math.pow(1 - t, 3);
      renderCount(el, Math.round(target * eased));
      if (t < 1) window.requestAnimationFrame(step);
    };
    window.requestAnimationFrame(step);
  };

  if (counters.length) {
    if (typeof window.IntersectionObserver !== 'function') {
      Array.prototype.forEach.call(counters, function (el) {
        renderCount(el, parseFloat(el.getAttribute('data-count')) || 0);
      });
    } else {
      var countObserver = new window.IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            runCount(entry.target);
            countObserver.unobserve(entry.target);
          });
        },
        { threshold: 0.4 }
      );
      Array.prototype.forEach.call(counters, function (el) { countObserver.observe(el); });
    }
  }

  /* ---------- Finish selector -------------------------------------------- */
  var preview = document.querySelector('[data-finish-preview]');
  var swatches = document.querySelectorAll('[data-swatches] .swatch');
  var finishName = document.querySelector('[data-finish-name]');
  var finishTier = document.querySelector('[data-finish-tier]');
  var frameButtons = document.querySelectorAll('[data-frame]');

  var track = function (name, detail) {
    if (typeof window.plausible === 'function') window.plausible(name, { props: detail });
    /* Meta Pixel insertion point — add fbq('trackCustom', name, detail) here. */
  };

  if (preview && swatches.length) {
    Array.prototype.forEach.call(swatches, function (button) {
      button.addEventListener('click', function () {
        Array.prototype.forEach.call(swatches, function (other) {
          other.setAttribute('aria-pressed', other === button ? 'true' : 'false');
        });
        preview.style.setProperty('--desk-top', button.getAttribute('data-colour'));
        preview.style.setProperty('--desk-top-deep', button.getAttribute('data-deep'));
        if (finishName) finishName.textContent = button.getAttribute('data-name');
        if (finishTier) finishTier.textContent = button.getAttribute('data-tier');
        track('finish_selected', { finish: button.getAttribute('data-name') });
      });
    });

    // Match the initial pressed swatch so the preview and the label agree.
    var initial = document.querySelector('[data-swatches] .swatch[aria-pressed="true"]');
    if (initial) {
      preview.style.setProperty('--desk-top', initial.getAttribute('data-colour'));
      preview.style.setProperty('--desk-top-deep', initial.getAttribute('data-deep'));
    }
  }

  if (preview && frameButtons.length) {
    Array.prototype.forEach.call(frameButtons, function (button) {
      button.addEventListener('click', function () {
        Array.prototype.forEach.call(frameButtons, function (other) {
          other.setAttribute('aria-pressed', other === button ? 'true' : 'false');
        });
        preview.style.setProperty('--frame', button.getAttribute('data-frame'));
      });
    });
  }

  /* ---------- Conversion events ------------------------------------------ */
  var tracked = document.querySelectorAll('[data-event]');
  Array.prototype.forEach.call(tracked, function (el) {
    el.addEventListener('click', function () { track(el.getAttribute('data-event'), {}); });
  });

  var telLinks = document.querySelectorAll('a[href^="tel:"]');
  Array.prototype.forEach.call(telLinks, function (el) {
    el.addEventListener('click', function () { track('call_tap', {}); });
  });

  /* ---------- Forms ------------------------------------------------------ */
  /* No form provider is configured yet. Rather than ship a form that silently
     does nothing, submissions are validated here and handed to the visitor's
     mail client, with the address also shown in plain text on the page.
     PROVIDER INSERTION POINT: set FORM_ENDPOINT to a Formspree / Web3Forms URL
     (or the client's Mailchimp endpoint) and the fetch path below takes over. */
  var FORM_ENDPOINT = '';
  var ENQUIRY_ADDRESS = 'hello@activedesk.co.uk';

  var setStatus = function (form, message, ok) {
    var status = form.querySelector('[data-form-status]');
    if (!status) return;
    status.textContent = message;
    status.style.color = ok ? 'var(--ink-soft)' : 'var(--accent-deep)';
  };

  var firstInvalid = function (form) {
    var fields = form.querySelectorAll('input, select, textarea');
    for (var i = 0; i < fields.length; i++) {
      var field = fields[i];
      if (field.type === 'hidden' || field.tabIndex === -1) continue;
      if (typeof field.checkValidity === 'function' && !field.checkValidity()) return field;
    }
    return null;
  };

  var handleForm = function (form, subject, buildBody) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      // Honeypot: a filled hidden field means a bot. Fail quietly.
      var trap = form.querySelector('input[name="company-url"]');
      if (trap && trap.value) return;

      var invalid = firstInvalid(form);
      if (invalid) {
        setStatus(form, 'Please check the highlighted field and try again.', false);
        invalid.focus();
        return;
      }

      var data = {};
      Array.prototype.forEach.call(form.querySelectorAll('[name]'), function (field) {
        if (field.name !== 'company-url') data[field.name] = field.value;
      });

      if (FORM_ENDPOINT) {
        setStatus(form, 'Sending…', true);
        window
          .fetch(FORM_ENDPOINT, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
            body: JSON.stringify(data)
          })
          .then(function (response) {
            if (!response.ok) throw new Error('Request failed');
            form.reset();
            setStatus(form, 'Thank you — your enquiry is with us and we will come back to you.', true);
          })
          .catch(function () {
            setStatus(
              form,
              'Something went wrong sending that. Please email ' + ENQUIRY_ADDRESS + ' instead.',
              false
            );
          });
        return;
      }

      window.location.href =
        'mailto:' + ENQUIRY_ADDRESS +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(buildBody(data));
      setStatus(form, 'Opening your email app. If nothing happens, write to ' + ENQUIRY_ADDRESS + '.', true);
    });
  };

  var enquiryForm = document.querySelector('[data-enquiry]');
  if (enquiryForm) {
    handleForm(enquiryForm, 'Website enquiry', function (data) {
      return (
        'Name: ' + (data.name || '') + '\n' +
        'Email: ' + (data.email || '') + '\n' +
        'Company: ' + (data.company || '') + '\n' +
        'Enquiry type: ' + (data.enquiry || '') + '\n\n' +
        (data.message || '')
      );
    });
  }

  var newsletterForm = document.querySelector('[data-newsletter]');
  if (newsletterForm) {
    handleForm(newsletterForm, 'Newsletter sign-up', function (data) {
      return 'Please add this address to the Act_ive De_sk newsletter: ' + (data.email || '');
    });
  }

  /* ---------- Year stamp -------------------------------------------------- */
  var years = document.querySelectorAll('[data-year]');
  Array.prototype.forEach.call(years, function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
