from model.entity import *


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    city = Column(String(20), nullable=True)
    role = Column(String(10))
    status = Column(Boolean, default=True)


    def __init__(self,  name, family, role):
        # self.id = id
        self.name = name
        self.family = family

        self.role = role


    # todo : getter / setter (validation)