import argparse
import sys

def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description='Extract webpage as markdown')
    parser.add_argument('target_url', help='The full URL to extract content from')
    args = parser.parse_args()

    js = f"""
    (function() {{
      try {{
        const url = '{args.target_url}';
        const title = document.title || '';
        const body = document.body;
        if (!body) return JSON.stringify({{ error: true, message: 'No document body found' }});
        
        // Clone body to avoid modifying the page
        const clone = body.cloneNode(true);
        
        // Remove non-content elements
        const removals = clone.querySelectorAll('script, style, nav, header, footer, iframe, ' +
          '.sidebar, .nav, .footer, .header, .menu, .ad, .advertisement, .social-share, ' +
          '.comments, .comment, noscript, svg, [role="navigation"], [role="banner"], ' +
          '[role="contentinfo"], [aria-hidden="true"]');
        removals.forEach(el => el.remove());
        
        // Get clean text
        const text = clone.textContent.replace(/\\s+/g, ' ').trim();
        const maxLen = 100000;
        const content = text.length > maxLen ? text.slice(0, maxLen) + '\\n\\n[truncated...]' : text;
        
        return JSON.stringify({{
          title: title,
          url: url,
          content: content,
          truncated: text.length > maxLen
        }});
      }} catch(e) {{
        return JSON.stringify({{ error: true, message: e.message }});
      }}
    }})()
    """
    print(js)

if __name__ == '__main__':
    main()
