from operator import pos
from flask import Flask, json, jsonify, request
from sqlite3 import Connection as SQLite3Connection
from datetime import date, datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.operators import json_getitem_op
import random

from linked_list import LinkedList
from hash_table import HashTable
from binary_search_tree import BST


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
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email'],
        address=data['address'],
        phone=data['phone'],
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User Created"}), 200


@app.route("/user/descending_id", methods=['GET'])
def get_all_users_descending():
    users = User.query.all()
    ll = LinkedList()
    for user in users:
        ll.insert_beginning({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })

    return jsonify(ll.to_array()), 200


@app.route("/user/ascending_id", methods=['GET'])
def get_all_users_ascending():
    users = User.query.all()
    ll = LinkedList()
    for user in users:
        ll.insert_end({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })

    return jsonify(ll.to_array()), 200


@app.route("/user/<user_id>", methods=['GET'])
def get_one_user(user_id):
    users = User.query.all()
    ll = LinkedList()
    for user in users:
        ll.insert_end({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        })
    # print(user_id, type(user_id))
    return ll.get_user_by_id(user_id)


@app.route("/user/<user_id>", methods=['DELETE'])
def delete_user_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    # print("user deleted")
    return jsonify({}), 200


# Blogpost routes
@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
    user = User.query.filter_by(id=user_id).first()
    data = request.get_json()
    if not user:
        return jsonify({"message": "User does not exist"}), 404
    ht = HashTable(5)

    ht.add_data("title", data['title'])
    ht.add_data("body", data['body'])
    ht.add_data("date", now)
    ht.add_data("user_id", user_id)

    new_blogpost = BlogPost(title=ht.get_value('title'),
                            body=ht.get_value('body'),
                            date=ht.get_value('date'),
                            user_id=ht.get_value('user_id'))
    db.session.add(new_blogpost)
    db.session.commit()
    return jsonify({"message": "Blog Post added Successfully"}), 200


@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def get_one_blog_posts(blog_post_id):
    blog_posts = BlogPost.query.all()
    random.shuffle(blog_posts)

    bst = BST()

    for post in blog_posts:
        bst.insert({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id,
        })

    post = bst.search(blog_post_id)

    if not post:
        return jsonify({"message": "Blog Post not found"}), 404

    return jsonify(post), 200


@app.route("/blog_post/all", methods=['GET'])
def get_all_blog_post():
    posts = BlogPost.query.all()
    lst = []
    for post in posts:
        lst.append({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id,
        })
    return jsonify(lst), 200


@app.route("/blog_post/<blog_post_id>", methods=['DELETE'])
def delete_blog_post(blog_post_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)