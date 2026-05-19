import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class ItemBasedRecommender:
    def __init__(self):
        self.user_item_matrix = pd.DataFrame()
        self.similarity_matrix = pd.DataFrame()

    def fit(self, df: pd.DataFrame):
        self.user_item_matrix = df.pivot_table(
            index='user_id',
            columns='item_id',
            values='rating'
        ).fillna(0)

        sim_data = cosine_similarity(self.user_item_matrix.T)

        book_ids = self.user_item_matrix.columns
        self.similarity_matrix = pd.DataFrame(
            sim_data,
            index=book_ids,
            columns=book_ids
        )

    def get_user_ratings(self):
        return self.user_item_matrix

    def get_similarity_matrix(self):
        return self.similarity_matrix
