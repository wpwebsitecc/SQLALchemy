from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book: Mapped[str] = mapped_column(String, unique=True)
    author: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://new-books-collection.db"
