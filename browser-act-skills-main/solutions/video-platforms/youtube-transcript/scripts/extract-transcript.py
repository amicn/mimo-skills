import sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
print(r"""
(function() {
  try {
    const segments = [];
    
    const selectors = [
      'div[role="button"][tabindex="0"] yt-formatted-string',
      'div.segment yt-formatted-string',
      'ytd-transcript-segment-renderer .segment-text',
      'ytd-transcript-segment-renderer yt-formatted-string',
      '.segment-text',
      '[class*="segment"] [class*="text"]'
    ];
    
    let foundSegments = [];
    for (const sel of selectors) {
      const els = document.querySelectorAll(sel);
      if (els.length > 0) {
        foundSegments = Array.from(els);
        break;
      }
    }
    
    const transcriptRenderer = document.querySelector('ytd-transcript-renderer');
    if (transcriptRenderer) {
      const items = transcriptRenderer.querySelectorAll('ytd-transcript-segment-renderer');
      items.forEach((item, i) => {
        const textEl = item.querySelector('.segment-text, yt-formatted-string');
        const timeEl = item.querySelector('.segment-timestamp, .time-container');
        segments.push({
          segment_index: i,
          text: textEl ? textEl.textContent.trim() : '',
          timestamp: timeEl ? timeEl.textContent.trim() : ''
        });
      });
    }
    
    if (segments.length === 0 && window.ytInitialPlayerResponse) {
      const captions = window.ytInitialPlayerResponse?.captions?.playerCaptionsTracklistRenderer;
      if (captions) {
        return JSON.stringify({ 
          error: false, 
          message: 'Transcript panel not yet opened',
          available_captions: (captions.captionTracks || []).map(t => ({
            language: t.name?.simpleText || t.languageCode,
            languageCode: t.languageCode,
            vssId: t.vssId
          }))
        });
      }
    }
    
    if (segments.length === 0) {
      return JSON.stringify({ error: true, message: 'No transcript segments found. The transcript panel may not be open.' });
    }
    
    return JSON.stringify({ 
      segments: segments,
      total_segments: segments.length,
      full_text: segments.map(s => s.text).join(' ')
    }, null, 2);
  } catch(e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
""")
