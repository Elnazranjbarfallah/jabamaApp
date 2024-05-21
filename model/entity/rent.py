from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from jabama.model.entity.base import Base
from jabama.model.entity.person import Person
from jabama.model.entity.house import House


class Rent(Base):
    __tablename__ = "rent"
    id = Column(Integer, primary_key=True, autoincrement=True)
    house = Column(String(20), nullable=False)
    price = Column(Integer)
    date_time = Column(DateTime)

    house_id = Column(Integer, ForeignKey("house.id"))
    house = relationship(House)

    renter_id = Column(Integer, ForeignKey("person.id"))
    renter = relationship(Person)

    def __init__(self, id, house, price, date_time):
        self.id = id
        self.house = house
        self.price = price
        self.date_time = date_time
