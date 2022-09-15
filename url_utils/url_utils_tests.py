
import url_utils
import unittest

class TestUrlMethods(unittest.TestCase):

    def test_should_return_true_for_valid_url(self):
        self.assertEqual(url_utils.is_url("https://shorturl.click/ANSS9"), True)
        self.assertEqual(url_utils.is_url("http://shorturl.at/uHTXZ"), True)
        self.assertEqual(url_utils.is_url("shorturl.at/uHTXZ"), True)
        self.assertEqual(url_utils.is_url("shorturl.click/ANSS9"), True)

    def test_should_return_correct_url_from_shortener(self):
        self.assertEqual(url_utils.get_url_from_shortener("https://shorturl.click/ANSS9"),"https://www.youtube.com/watch?v=xEaPh7yvxHo&feature=emb_title")
        self.assertEqual(url_utils.get_url_from_shortener("http://shorturl.at/uHTXZ"),"https://www.youtube.com/watch?v=vNjNtaCLJN4")

if __name__ == '__main__':
    unittest.main()        