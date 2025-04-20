import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database


def start_session(filepath, Base):
    engine = start_engine(filepath, Base)
    return engine, Session(engine)


def start_engine(filepath, Base):
    uri = "sqlite:///" + os.path.abspath(filepath)
    engine = create_engine(uri)
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)
    return engine
