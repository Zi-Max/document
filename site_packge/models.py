"""Define site database"""
from site_packge import db


class Category(db.Model):
    """Define Category table (html, css, js,...)"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    sub_categories = db.relationship("SubCategory", backref="category", lazy=True)


class SubCategory(db.Model):
    """Define subcategories table (html bascis, html forms, ...)"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    index = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)


class Article(db.Model):
    """Define Article table that contains the content"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sub_category_id = db.Column(
        db.Integer, db.ForeignKey("sub_category.id"), nullable=False
    )
