import sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
print(r"""
(function() {
  try {
    const type = 'Videos';
    const maxResults = 100;
    const searchUrl = 'https://www.youtube.com/results?search_query=example';
    
    const initialData = window.ytInitialData;
    if (!initialData) return JSON.stringify({ error: true, message: 'ytInitialData not found' });
    
    const results = [];
    const contents = initialData?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents || [];
    
    for (const section of contents) {
      const items = section?.itemSectionRenderer?.contents || [];
      for (const item of items) {
        const video = item.videoRenderer;
        const channel = item.channelRenderer;
        const playlist = item.playlistRenderer;
        const shelf = item.shelfRenderer;
        
        if (video && (type === 'Videos' || type === 'Shorts')) {
          results.push({
            type: 'video',
            title: video.title?.runs?.[0]?.text || '',
            url: video.videoId ? `https://www.youtube.com/watch?v=${video.videoId}` : '',
            view_count: video.viewCount?.simpleText || video.shortViewCount?.simpleText || '',
            published_at: video.publishedTimeText?.simpleText || '',
            channel_name: video.ownerText?.runs?.[0]?.text || '',
            channel_url: video.ownerText?.runs?.[0]?.navigationEndpoint?.browseEndpoint?.browseId 
              ? `https://www.youtube.com/channel/${video.ownerText.runs[0].navigationEndpoint.browseEndpoint.browseId}`
              : '',
            length: video.lengthText?.simpleText || '',
            thumbnail: video.thumbnail?.thumbnails?.[0]?.url || ''
          });
        }
        
        if (channel && type === 'Channels') {
          results.push({
            type: 'channel',
            title: channel.title?.simpleText || '',
            url: channel.channelId ? `https://www.youtube.com/channel/${channel.channelId}` : '',
            subscriber_count: channel.subscriberCountText?.simpleText || '',
            video_count: channel.videoCountText?.runs?.[0]?.text || '',
            description: channel.descriptionSnippet?.runs?.[0]?.text || ''
          });
        }
        
        if (playlist && type === 'Playlists') {
          results.push({
            type: 'playlist',
            title: playlist.title?.simpleText || '',
            url: playlist.playlistId ? `https://www.youtube.com/playlist?list=${playlist.playlistId}` : '',
            video_count: playlist.videoCount?.runs?.[0]?.text || '',
            channel_name: playlist.ownerText?.runs?.[0]?.text || ''
          });
        }
      }
    }
    
    return JSON.stringify({ results: results.slice(0, maxResults), total: results.length }, null, 2);
  } catch(e) {
    return JSON.stringify({ error: true, message: e.message });
  }
})()
""")
