import unittest
from client.src.requests_handler import search_song, search_artist

class TestClient(unittest.TestCase):
    def test_search_song(self):
        result = search_song("Havana")
        self.assertIn("lyric", result)
    
    def test_search_artist(self):
        result = search_artist("Camila Cabello")
        self.assertIn("full_name", result)

if __name__ == "__main__":
    unittest.main()
