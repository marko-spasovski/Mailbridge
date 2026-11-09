// Microsoft Clarity (usage analytics for the UX course). The standard Clarity snippet, kept in its own
// file because the CSP blocks inline scripts. The CSP allows *.clarity.ms for scripts and data.
(() => {
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
