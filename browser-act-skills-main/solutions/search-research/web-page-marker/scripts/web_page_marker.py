import sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
print(r"""
(function() {
  try {
    const url = 'https://example.com';
    const title = document.title || '';
    const body = document.body;
    if (!body) return JSON.stringify({ error: true, message: 'No document body found' });
    
    const clone = body.cloneNode(true);
    
    const removals = clone.querySelectorAll('script, style, nav, header, footer, iframe, ' +
      '.sidebar, .nav, .footer, .header, .menu, .ad, .advertisement, .social-share, ' +
      '.comments, .comment, noscript, svg, [role="navigation"], [role="banner"], ' +
      '[role="contentinfo"], [aria-hidden="true"]');
    removals.forEach(el => el.remove());
    
    const text = clone.textContent.replace(/\s+/g, ' ').trim();
    const maxLen = 100000;
    const content = text.length > maxLen ? text.slice(0, maxLen) + '\n\n[truncated...]' : text;
    
    return JSON.stringify({
      title: title,
      url: url,
      content: content,
      truncated: text.length > maxLen
    });
  } catch(e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
""")
