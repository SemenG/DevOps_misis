from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.data.books import DataLoader
from app.model.item_based import ItemBasedRecommender
from app.inference.recommend import get_top_recommendations

app = FastAPI(docs_url=None, redoc_url=None)

loader = DataLoader(file_path="app/data/books.csv")
recommender = ItemBasedRecommender()
df_train = loader.load_data()
recommender.fit(df_train)


@app.get("/", response_class=HTMLResponse)
def get_simple_form(user_id: int = None, top_n: int = 5):
    result_html = ""

    if user_id is not None:
        recs = get_top_recommendations(user_id=user_id, model=recommender, top_n=top_n)


        list_items = ""
        for item_id in recs:
            book_text = loader.get_book_info(item_id)
            list_items += f"<li>{book_text}</li>"

        result_html = f"""
        <h3>Рекомендации для Пользователя {user_id}:</h3>
        <ol>
            {list_items}
        </ol>
        """


    html_content = f"""
    <html>
        <head>
            <title>Рекомендации</title>
        </head>
        <body>
            <h2>Система рекомендаций книг</h2>
            <form method="get" action="/">
                <label>ID Пользователя: </label>
                <input type="number" name="user_id" value="{user_id if user_id else 1}" required><br><br>

                <label>Количество рекомендаций: </label>
                <input type="number" name="top_n" value="{top_n}" min="1" max="20" required><br><br>

                <button type="submit">Получить</button>
            </form>
            <hr>
            {result_html}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)