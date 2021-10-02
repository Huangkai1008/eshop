from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_session_factory(database_url: str) -> sessionmaker:
    engine = create_engine(database_url)
    session_factory = sessionmaker(
        autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
    )
    return session_factory


def get_session(session_factory: sessionmaker) -> Iterator:
    session = scoped_session(session_factory)
    yield session
    session.close()
