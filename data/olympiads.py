import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Olympiad(SqlAlchemyBase):
    __tablename__ = 'olympiads'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    level_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("levels.id"), nullable=False)
    level = orm.relationship("Level")
    students = orm.relationship("Student", back_populates='olympiad')