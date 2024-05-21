from sqlalchemy import Column, Integer, String, Boolean

from jabama.model.entity.base import Base

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    role = Column(String(10))
    status = Column(Boolean, default=True)


    def __init__(self, id, name, family,city, role, status=True):
        self.id = id
        self.name = name
        self.family = family
        self.city = city
        self.role = role
        self.status = status