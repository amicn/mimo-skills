import sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
print(r"""
(function() {
  try {
    const organic = [];
    document.querySelectorAll('div.g, div[data-hveid]').forEach((el, i) => {
      const titleEl = el.querySelector('h3');
      const linkEl = el.querySelector('a[href^="http"]');
      const descEl = el.querySelector('div[data-sncf], span.aCOpRe, div.VwiC3b');
      if (titleEl) {
        organic.push({
          position: i + 1,
          type: 'organic',
          title: titleEl.textContent.trim(),
          url: linkEl ? linkEl.href : null,
          displayedUrl: el.querySelector('cite')?.textContent?.trim() || null,
          description: descEl ? descEl.textContent.trim() : null
        });
      }
    });

    const paid = [];
    document.querySelectorAll('div.uEierd, div[data-text-ad]').forEach((el, i) => {
      const titleEl = el.querySelector('span[role="heading"], div[role="heading"]');
      const linkEl = el.querySelector('a[href^="http"]');
      if (titleEl) {
        paid.push({
          adPosition: i + 1,
          type: 'paid',
          title: titleEl.textContent.trim(),
          url: linkEl ? linkEl.href : null,
          description: el.querySelector('.v1i0ed, div[aria-level]')?.textContent?.trim() || null
        });
      }
    });

    const related = [];
    document.querySelectorAll('div.s75Ojd a, a[jsname]').forEach(el => {
      if (el.href && el.textContent.trim()) {
        related.push({ title: el.textContent.trim(), url: el.href });
      }
    });

    const paa = [];
    document.querySelectorAll('div[jsname] span, div.wWOJcd').forEach(el => {
      const txt = el.textContent.trim();
      if (txt && txt.endsWith('?')) paa.push({ question: txt });
    });

    const aiOverview = document.querySelector('[data-attrid="wa-kp"]')?.textContent?.trim() ||
                       document.querySelector('div[class*="kp-blk"]')?.textContent?.trim() || null;

    const resultsTotal = document.querySelector('#result-stats')?.textContent?.trim() || null;

    return JSON.stringify({
      organicResults: organic,
      paidResults: paid,
      relatedQueries: [...new Map(related.map(r => [r.title, r])).values()],
      peopleAlsoAsk: [...new Map(paa.map(p => [p.question, p])).values()],
      aiOverview: aiOverview,
      resultsTotal: resultsTotal
    }, null, 2);
  } catch(e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
""")
