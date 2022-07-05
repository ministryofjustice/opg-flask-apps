import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

postgres_uri = "postgresql://{}:{}@{}/{}".format(
    os.getenv("POSTGRES_USERNAME"),
    os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_HOSTNAME"),
    os.getenv("POSTGRES_NAME"),
)


class Database:
    def __init__(self, database_uri):
        self.engine = create_engine(database_uri, echo=True)
        self.sessionClass = sessionmaker(bind=self.engine)

    def query(self, *args, **kwargs):
        session = self.sessionClass()
        return session.query(*args, **kwargs)

    def raw_query(self, sql: str):
        with self.engine.begin() as conn:
            return conn.execute(sql, {})

    def add(self, obj):
        session = self.sessionClass()
        session.add(obj)
        return session.commit()

    def delete(self, modelClass, id):
        session = self.sessionClass()
        obj = session.query(modelClass).filter(modelClass.id == id).first()
        session.delete(obj)
        return session.commit()
