from django.db import models
import sqlite3

class User(models.Model):
    ID = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    userAvailability = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ID)

    @staticmethod
    def addUser(ID, password, username):
        return UserGateway.addUser(ID, password, username)

    @staticmethod
    def checkUserAvailability(userAvailability):
        return UserGateway.checkUserAvailability(userAvailability)

class Article(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField()
    publicationDate = models.DateField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def filterTitle(title):
        return ArticleGateway.filterArticle(title)


class DB:
    @staticmethod
    def prepare(query):
        conn = sqlite3.connect('database.db')
        return conn.cursor(), conn

class UserGateway:
    def __init__(self, ID, password, username, user_availability):
        self.ID = ID
        self.password = password
        self.username = username
        self.user_availability = user_availability

    def update(self):
        update_statement = "UPDATE users SET password = ?, username = ?, userAvailability = ? WHERE ID = ?"
        cursor, conn = DB.prepare(update_statement)
        cursor.execute(update_statement, (self.password, self.username, self.user_availability, self.ID))
        conn.commit()
        conn.close()

    def insert(self):
        insert_statement = "INSERT INTO users VALUES (?, ?, ?, ?)"
        cursor, conn = DB.prepare(insert_statement)
        cursor.execute(insert_statement, (self.ID, self.password, self.username, self.user_availability))
        conn.commit()
        conn.close()

class ArticleGateway:
    def __init__(self, author, content, publication_date, title):
        self.author = author
        self.content = content
        self.publication_date = publication_date
        self.title = title

    def update(self):
        update_statement = "UPDATE articles SET author = ?, content = ?, publicationDate = ?, title = ? WHERE ID = ?"
        cursor, conn = DB.prepare(update_statement)
        cursor.execute(update_statement, (self.author, self.content, self.publication_date, self.title))
        conn.commit()
        conn.close()

    def insert(self):
        insert_statement = "INSERT INTO articles VALUES (?, ?, ?, ?)"
        cursor, conn = DB.prepare(insert_statement)
        cursor.execute(insert_statement, (self.author, self.content, self.publication_date, self.title))
        conn.commit()
        conn.close()

    def filter_article(self, title):
        filter_statement = "SELECT * FROM articles WHERE title = ?"
        cursor, conn = DB.prepare(filter_statement)
        cursor.execute(filter_statement, (title,))
        result = cursor.fetchall()
        conn.close()
        return result


