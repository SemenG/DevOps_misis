import os
import random
import pandas as pd


class DataLoader:
    def __init__(self, file_path: str = "app/data/books.csv"):
        self.file_path = file_path
        self.raw_lines = []

    def load_data(self) -> pd.DataFrame:
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.raw_lines = f.readlines()
            total_books = len(self.raw_lines) - 1 if len(self.raw_lines) > 1 else 1
            random.seed(42)
            data_rows = []

            for user_id in range(1, 11):
                book_pool = list(range(total_books))
                rated_books = random.sample(book_pool, 20)

                for item_id in rated_books:
                    rating = random.randint(3, 5)
                    data_rows.append({"user_id": user_id, "item_id": item_id, "rating": rating})
            return pd.DataFrame(data_rows)

        return pd.DataFrame([
            {"user_id": 1, "item_id": 0, "rating": 5},
            {"user_id": 1, "item_id": 1, "rating": 3},
            {"user_id": 2, "item_id": 0, "rating": 4},
        ])

    def get_book_info(self, item_id: int) -> str:

        line_idx = item_id + 1

        if 0 <= line_idx < len(self.raw_lines):
            # Разбиваем строку по запятой
            parts = self.raw_lines[line_idx].strip().split(',')
            if len(parts) >= 2:
                title = parts[0]
                author = parts[1]
                return f"<strong>«{title}»</strong> — {author}"

        return f"Книга №{item_id}"
