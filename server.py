from flask import Flask, jsonify, request
from sqlite3 import Connection as SQLite3Connection
from datetime import date, datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy


# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


#main App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

db = SQLAlchemy(app)
now = datetime.now()


# Models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(10))
    posts = db.relationship("BlogPost")


class BlogPost(db.Model):
    __tablename__ = "blog_post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


@app.route("/user", methods=['POST'])
def create_user():
    pass


@app.route("/user/descending_id", methods=['POST'])
def get_all_users_descending():
    pass


@app.route("/user/ascending_id", methods=['POST'])
def get_all_users_ascending():
    pass


@app.route("/user/<user_id>", methods=['GET'])
def get_one_use(user_id):
    pass


@app.route("/user/<user_id>", methods=['DELETE'])
def delete_user_id(user_id):
    pass


# Blogpost routes
@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    pass


@app.route("/blog_post/<user_id>", methods=['GET'])
def get_all_blog_post(user_id):
    pass


@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def get_one_blog_post(blog_post_id):
    pass


@app.route("/blog_post/<blog_post_id>", methods=['DELETE'])
def delete_blog_post(blog_post_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)