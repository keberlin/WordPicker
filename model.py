from sqlalchemy import String

from database import db


class SowpodsModel(db.Model):
    __tablename__ = "sowpods"
    # __table_args__ = {"schema":"wordpicker"}

    word = db.Column("word", String, primary_key=True, nullable=False)
