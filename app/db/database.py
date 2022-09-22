import os
from dotenv import load_dotenv
from typing import Callable, Iterator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import StaticPool

load_dotenv()

engine = create_engine(
    os.getenv('DB_URL'),
    poolclass=StaticPool,
    connect_args={},
)

Base = declarative_base()

session_factory: Callable[[], Session] = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)


def get_session() -> Iterator[Session]:
    db_session: Session = session_factory()

    try:
        yield db_session
        db_session.commit()

    finally:
        db_session.close()
