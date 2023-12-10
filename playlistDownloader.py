from pytube import Playlist

def download_playlist(playlist_url, output_path='.'):
    try:
        playlist = Playlist(playlist_url)
        playlist_title = playlist.title()
        
        print(f"Downloading Playlist: {playlist_title}")
        
        for video in playlist.videos:
            video_title = video.title
            print(f"Downloading Video: {video_title}")
            video.streams.get_highest_resolution().download(output_path)
            print(f"Downloaded: {video_title}")

        print(f"Playlist Downloaded Successfully: {playlist_title}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    playlist_url = 'https://www.youtube.com/playlist?list=PLillGF-RfqbY3c2r0htQyVbDJJoBFE6Rb'
    output_path = 'E:\Abdify'
    
    download_playlist(playlist_url, output_path)
