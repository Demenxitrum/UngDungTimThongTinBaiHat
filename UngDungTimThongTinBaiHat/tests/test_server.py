import unittest
from server.src.song_search import find_song
from server.src.artist_search import find_artist

class TestServer(unittest.TestCase):
    def test_find_song(self):
        result = find_song("Havana")
        self.assertIn("lyric", result)

    def test_find_artist(self):
        result = find_artist("Camila Cabello")
        self.assertIn("full_name", result)

if __name__ == "__main__":
    unittest.main()
