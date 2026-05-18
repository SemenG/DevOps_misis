import csv
import os
import random


def load_books():
	books = []
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	csv_path = os.path.join(base_dir, "books.csv")
	if not os.path.exists(csv_path):
		raise FileNotFoundError("Файл данных books.csv не найден")
	with open(csv_path, mode="r", encoding="utf-8") as f:
		reader = csv.DictReader(f)
		for row in reader:
			books.append(row)
	return books


def get_genres():
	books = load_books()
	return list(set(book["genre"] for book in books))


def recommend_book(genre):
	genre = genre.lower().strip()
	books = load_books()
	filtered_books = [b for b in books if b["genre"].lower() == genre]
	if not filtered_books:
		raise ValueError("Такой жанр не найден в базе данных")
	return random.choice(filtered_books)
