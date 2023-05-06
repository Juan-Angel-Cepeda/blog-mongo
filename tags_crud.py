import pymongo as mongo

def find_articles_by_tag(tag):
    connection = mongo.MongoClient("mongodb://localhost:27017")
    blog_connection = connection.blog
    users = blog_connection.users
    all_users = users.find()

    articles_with_tag = []
    for user in all_users:
        username = user.get("user")
        articles = user.get("articles", [])
        for article in articles:
            if tag in article.get("tags", []):
                article["username"] = username
                articles_with_tag.append(article)

    return articles_with_tag