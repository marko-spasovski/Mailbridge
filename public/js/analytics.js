// Microsoft Clarity (usage analytics for the UX course). The standard Clarity snippet, kept in its own
// file because the CSP blocks inline scripts. The CSP allows *.clarity.ms for scripts and data.
(() => {
  // Not on local addresses: development and the browser tests must not send sessions to Clarity
  // (and Firefox rejects Clarity's cookies on 127.0.0.1, which the tests count as errors).
  if (['localhost', '127.0.0.1', '[::1]'].includes(location.hostname)) return;
  const projectId = 'zb5jhevix7';
  /** @type {any} */
  const win = window;
  if (!win.clarity) {
    // Calls made before the Clarity script arrives are queued and replayed once it loads.
    win.clarity = (...args) => {
      win.clarity.q = win.clarity.q || [];
      win.clarity.q.push(args);
    };
  }
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.clarity.ms/tag/${projectId}`;
  const first = document.getElementsByTagName('script')[0];
  if (first?.parentNode) first.parentNode.insertBefore(script, first);
  else document.head.append(script);
})();
