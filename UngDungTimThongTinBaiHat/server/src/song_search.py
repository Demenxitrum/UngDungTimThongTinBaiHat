def find_song(song_name):
    songs = {
        "Havana": {"lyric": "Havana, ooh na-na", "composer": "Camila Cabello", "video_url": "https://www.youtube.com/watch?v=HCjNJDNzw8Y"},
        "Shape of You": {"lyric": "The club isn't the best place to find a lover", "composer": "Ed Sheeran", "video_url": "https://www.youtube.com/watch?v=JGwWNGJdvx8"}
    }
    song_info = songs.get(song_name, None)
    if song_info:
        return {"song": song_name, **song_info}
    else:
        return {"error": "Không tìm thấy bài hát"}
