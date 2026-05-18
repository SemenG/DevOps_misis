import unittest
from app.core import get_genres, recommend_book
class TestBookRecommendation(unittest.TestCase):
	def test_get_genres_is_not_empty(self):
		genres = get_genres()
		self.assertTrue(len(genres) > 0)
		self.assertIn("фантастика", genres)
	def test_recommend_book_correct_genre(self):
		book = recommend_book("детектив")
		self.assertEqual(book["genre"], "детектив")
		self.assertIn("title", book)
		self.assertIn("author", book)
	def test_recommend_book_case_insensitive(self):
		book = recommend_book("  ФАНТАСТИКА  ")
		self.assertEqual(book["genre"], "фантастика")
	def test_recommend_book_invalid_genre(self):
		with self.assertRaises(ValueError):
			recommend_book("кулинария")
if __name__ == "__main__":
	unittest.main()