#!/usr/bin/env python3
"""
Hash Pwd and Auth utilities
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """
    Generates new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user by email and password.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email=email,
                                         hashed_password=hashed_password)

            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Credentials validation
        """
        try:
            user_info = self._db.find_user_by(email=email)
            password_bytes = password.encode("utf-8")
            return bcrypt.checkpw(password_bytes, user_info.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Session ID
        """
        try:
            user_info = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user_info.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Find user by session ID
        """
        if session_id is None:
            return None
        try:
            found_user = self._db.find_user_by(session_id=session_id)
            return found_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy Session
        """
        try:
            destroyed_sesh = self._db.find_user_by(id=user_id)
            destroyed_sesh.session_id = None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email:str) -> str:
        """
        Generates reset password token
        """
        try:
            registered_user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        
        reset_token = _generate_uuid()
        self._db.update_user(registered_user.id, reset_token=reset_token)
        return reset_token
