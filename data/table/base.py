from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from abc import abstractmethod
# Create a class for mapping to database
class Base(declarative_base()):
    __abstract__ = True
    # Connect to database
    engine = create_engine("sqlite:///objects.db")

    # Update or create(if not exist) table to database
    @classmethod
    def update_table(cls):
        cls.metadata.create_all(cls.engine)

    # Get session for query
    @classmethod
    def get_session(cls):
        Session = sessionmaker(bind=cls.engine)
        session = Session()
        return session

    @classmethod
    @abstractmethod
    def get_columns_name(cls):
        pass