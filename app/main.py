from app.core import get_genres, recommend_book
def run():
	print("--- DevOps система рекомендаций книг ---")
	try:
		genres = get_genres()
		print(f"Доступные жанры: {', '.join(genres)}")
		user_genre = input("Введите интересующий вас жанр: ")
		book = recommend_book(user_genre)
		print(f"\nРекомендуемая книга: \"{book['title']}\" (Автор: {book['author']})")
	except (FileNotFoundError, ValueError) as e:
		print(f"\nОшибка системы: {e}")
if __name__ == "__main__":
	run()