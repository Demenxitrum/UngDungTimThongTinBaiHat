def find_artist(artist_name):
    artists = {
        "Camila Cabello": {"full_name": "Karla Camila Cabello Estrabao", "birthdate": "March 3, 1997", "hometown": "Cojímar, Cuba"},
        "Ed Sheeran": {"full_name": "Edward Christopher Sheeran", "birthdate": "February 17, 1991", "hometown": "Halifax, West Yorkshire, England"}
    }
    artist_info = artists.get(artist_name, None)
    if artist_info:
        return {"artist": artist_name, **artist_info}
    else:
        return {"error": "Không tìm thấy ca sĩ"}
