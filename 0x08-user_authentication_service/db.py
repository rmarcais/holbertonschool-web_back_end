"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User

from typing import TypeVar


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar("User"):
        """Saves a user to the database"""
        user = User()
        user.email = email
        user.hashed_password = hashed_password

        session = self._session

        session.add(user)
        session.commit()

        return user

    def find_user_by(self, **kwargs) -> TypeVar("User"):
        """
        Returns the first row found in the users table
        as filtered by the arguments kwargs
        """
        session = self._session
        try:
            query = session.query(User).filter_by(**kwargs)
            if not query.first():
                raise NoResultFound
        except InvalidRequestError:
            raise
        return query.first()
