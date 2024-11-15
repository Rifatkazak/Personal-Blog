import json
from flask import Flask, jsonify, request

app = Flask(__name__)
DATA_FILE = 'articles.json'

# JSON dosyasını yükleme fonksiyonu
def load_articles():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# JSON dosyasına kaydetme fonksiyonu
def save_articles(articles):
    with open(DATA_FILE, 'w') as file:
        json.dump(articles, file, indent=4)

# Anasayfa: Tüm makaleleri listeler
@app.route('/articles', methods=['GET'])
def list_articles():
    articles = load_articles()
    return jsonify(articles)

# Belirli bir makaleyi görüntüleme
@app.route('/articles/<int:article_id>', methods=['GET'])
def view_article(article_id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return jsonify(article)
    return jsonify({"message": "Article not found"}), 404

# Yeni makale ekleme
@app.route('/admin/add-article', methods=['POST'])
def add_article():
    articles = load_articles()
    new_article = request.json
    new_article["id"] = articles[-1]["id"] + 1 if articles else 1  # Otomatik ID atama
    articles.append(new_article)
    save_articles(articles)
    return jsonify({"message": "Article added successfully", "article": new_article}), 201

# Makale düzenleme
@app.route('/admin/edit-article/<int:article_id>', methods=['PUT'])
def edit_article(article_id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == article_id), None)
    if not article:
        return jsonify({"message": "Article not found"}), 404

    update_data = request.json
    article.update(update_data)
    save_articles(articles)
    return jsonify({"message": "Article updated successfully", "article": article})

# Makale silme
@app.route('/admin/delete-article/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == article_id), None)
    if not article:
        return jsonify({"message": "Article not found"}), 404

    articles = [a for a in articles if a['id'] != article_id]
    save_articles(articles)
    return jsonify({"message": "Article deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
