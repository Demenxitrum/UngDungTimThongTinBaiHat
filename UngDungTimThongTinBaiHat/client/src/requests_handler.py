import requests

SERVER_URL = "http://localhost:5000"  # Địa chỉ server

def search_song(song_name):
    try:
        response = requests.get(f"{SERVER_URL}/search/song", params={'name': song_name})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Không tìm thấy bài hát."}
    except Exception as e:
        return {"error": str(e)}

def search_artist(artist_name):
    try:
        response = requests.get(f"{SERVER_URL}/search/artist", params={'name': artist_name})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Không tìm thấy ca sĩ."}
    except Exception as e:
        return {"error": str(e)}