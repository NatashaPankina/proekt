import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Level(SqlAlchemyBase):
    __tablename__ = 'levels'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    olympiads = orm.relationship("Olympiad", back_populates='level')