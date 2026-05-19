def get_top_recommendations(user_id: int, model, top_n: int = 5) -> list:

    user_item_matrix = model.get_user_ratings()
    similarity_matrix = model.get_similarity_matrix()

    if user_id not in user_item_matrix.index:
        popular = user_item_matrix.mean(axis=0).sort_values(ascending=False)
        return popular.head(top_n).index.tolist()

    user_ratings = user_item_matrix.loc[user_id]

    predicted_scores = similarity_matrix.dot(user_ratings)

    already_read = user_ratings[user_ratings > 0].index

    recommendations = predicted_scores.drop(already_read, errors='ignore')

    top_items = recommendations.sort_values(ascending=False).head(top_n)

    return top_items.index.tolist()