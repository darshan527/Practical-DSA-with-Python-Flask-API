from flask import Flask, jsonify, request
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime

#main App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQL_TRACKMODIFICATION"] = 0
