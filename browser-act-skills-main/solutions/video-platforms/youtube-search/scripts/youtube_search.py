import argparse
import sys
import urllib.parse

def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description='YouTube search results extractor')
    parser.add_argument('keywords', help='Search keywords')
    parser.add_argument('video_type', nargs='?', default='Videos', 
                        choices=['Videos', 'Shorts', 'Channels', 'Playlists'],
                        help='Result type tab')
    parser.add_argument('max_results', nargs='?', type=int, default=100,
                        help='Maximum number of results')
    args = parser.parse_args()

    encoded = urllib.parse.quote(args.keywords)
    search_url = f'https://www.youtube.com/results?search_query={encoded}'

    js = f"""
    (function() {{
      try {{
        const type = '{args.video_type}';
        const maxResults = {args.max_results};
        const searchUrl = '{search_url}';
        
        // Try to get data from ytInitialData
        const initialData = window.ytInitialData;
        if (!initialData) return JSON.stringify({{ error: true, message: 'ytInitialData not found' }});
        
        const results = [];
        const contents = initialData?.contents?.twoColumnSearchResultsRenderer?.primaryContents?.sectionListRenderer?.contents || [];
        
        for (const section of contents) {
          const items = section?.itemSectionRenderer?.contents || [];
          for (const item of items) {{
            const video = item.videoRenderer;
            const channel = item.channelRenderer;
            const playlist = item.playlistRenderer;
            const shelf = item.shelfRenderer;
            
            if (video && (type === 'Videos' || type === 'Shorts')) {{
              results.push({{
                type: 'video',
                title: video.title?.runs?.[0]?.text || '',
                url: video.videoId ? `https://www.youtube.com/watch?v=${{video.videoId}}` : '',
                view_count: video.viewCount?.simpleText || video.shortViewCount?.simpleText || '',
                published_at: video.publishedTimeText?.simpleText || '',
                channel_name: video.ownerText?.runs?.[0]?.text || '',
                channel_url: video.ownerText?.runs?.[0]?.navigationEndpoint?.browseEndpoint?.browseId 
                  ? `https://www.youtube.com/channel/${{video.ownerText.runs[0].navigationEndpoint.browseEndpoint.browseId}}`
                  : '',
                length: video.lengthText?.simpleText || '',
                thumbnail: video.thumbnail?.thumbnails?.[0]?.url || ''
              }});
            }}
            
            if (channel && type === 'Channels') {{
              results.push({{
                type: 'channel',
                title: channel.title?.simpleText || '',
                url: channel.channelId ? `https://www.youtube.com/channel/${{channel.channelId}}` : '',
                subscriber_count: channel.subscriberCountText?.simpleText || '',
                video_count: channel.videoCountText?.runs?.[0]?.text || '',
                description: channel.descriptionSnippet?.runs?.[0]?.text || ''
              }});
            }}
            
            if (playlist && type === 'Playlists') {{
              results.push({{
                type: 'playlist',
                title: playlist.title?.simpleText || '',
                url: playlist.playlistId ? `https://www.youtube.com/playlist?list=${{playlist.playlistId}}` : '',
                video_count: playlist.videoCount?.runs?.[0]?.text || '',
                channel_name: playlist.ownerText?.runs?.[0]?.text || ''
              }});
            }}
          }}
        }
        
        return JSON.stringify({{ results: results.slice(0, maxResults), total: results.length }}, null, 2);
      }} catch(e) {{
        return JSON.stringify({{ error: true, message: e.message }});
      }}
    }})()
    """
    print(js)

if __name__ == '__main__':
    main()
