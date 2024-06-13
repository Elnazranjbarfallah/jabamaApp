from model.entity import *
import re

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    role = Column(String(10))
    status = Column(Boolean, default=True)


    def __init__(self,  name, family, role):
        self.name = name
        self.family = family
        self.role = role



    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if re.match("^[0-9_ \s]+$", id):
            self.id = id
        else:
            raise ValueError("invalid id format")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match(r"^[A-Za-z\s]+$", name, re.I):
            self._name = name
        else:
            raise ValueError("invalid name format")

    @property
    def family(self):
        return self._family

    @name.setter
    def family(self, family):
        if re.match(r"^[A-Za-z\s]+$", family, re.I):
            self._family = family
        else:
            raise ValueError("invalid family format")


