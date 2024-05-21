from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from jabama.model.entity.base import Base


class DataAccess:
    def __init__(self, class_name):
        connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
        if not database_exists(connection_string):
            create_database(connection_string)

        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.class_name = class_name

    def save(self, entity):
        session = self.Session()
        session.add(entity)
        session.commit()
        # todo : has error
        # return entity

    def edit(self, entity):
        session = self.Session()
        session.merge(entity)
        session.commit()

    def remove(self, id):
        session = self.Session()
        entity = session.get(self.class_name, id)
        session.delete(entity)
        session.commit()

    def find_all(self):
        session = self.Session()
        entity_list = session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        session = self.Session()
        entity = session.get(self.class_name, id)
        return entity


    # todo : has Error
    def find_by(self, find_statement):
        session = self.Session()
        entity = session.query(self.class_name, find_statement).all()
        return entity
