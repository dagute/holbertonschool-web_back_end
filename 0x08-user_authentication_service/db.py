#!/usr/bin/env python3
""" Database module"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import TypeVar, Any
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class"""
    def __init__(self):
        """Constructor"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """session"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add the user"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ returns the first row found in the
        users table as filtered by the method’s
        input arguments"""
        if not kwargs:
            raise InvalidRequestError
        column_names = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in column_names:
                raise InvalidRequestError
        query = self._session.query(User).filter_by(**kwargs).first()
        if query is None:
            raise NoResultFound
        return query

    def update_user(self, user_id: int, **kwargs) -> None:
        """Uses find_user_by to locate the user"""
        user = self.find_user_by(id=user_id)
        column_names = User.__table__.columns.keys()
        for key, val in kwargs.items():
            setattr(user, key, val)
        self._session.commit()
        for key in kwargs.keys():
            if key not in column_names:
                raise ValueError
