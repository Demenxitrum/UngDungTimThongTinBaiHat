from flask import Flask, request, jsonify
from song_search import find_song
from artist_search import find_artist

app = Flask(__name__)

@app.route("/search/song", methods=["GET"])
def search_song():
    song_name = request.args.get('name')
    result = find_song(song_name)
    return jsonify(result)

@app.route("/search/artist", methods=["GET"])
def search_artist():
    artist_name = request.args.get('name')
    result = find_artist(artist_name)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
