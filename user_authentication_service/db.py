#!/usr/bin/env python3
"""
Module for database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from user import Base, User

class DB:
    """
    Database class
    """
    def __init__(self) -> None:
        """
        New databse
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds user to database
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        print(f"Debug - User ID: {new_user.id}")
        return new_user
