from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from jabama.model.entity.base import Base
from jabama.model.entity.person import Person


class House(Base):
    __tablename__ = "house"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    meterage = Column(Integer)
    finall_adress = Column(String)
    plate = Column(String(5))
    number_of_rooms = Column(Integer, default=0)
    elevator = Column(Boolean, default=False)
    parking = Column(Boolean, default=False)
    warehouse = Column(Boolean, default=False)
    price = Column(String)
    owner_id = Column(Integer, ForeignKey("person.id"))
    owner = relationship(Person)

    def __init__(self, id, name, city, meterage, finall_adress, plate, number_of_rooms, elevator, parking,warehouse, price,owner_id,owner):
        self.id = id
        self.name = name
        self.city = city
        self.meterage = meterage
        self.finall_adress = finall_adress
        self.plate = plate
        self.number_of_rooms = number_of_rooms
        self.elevator = elevator
        self.parking = parking
        self.warehouse = warehouse
        self.price = price
        self.owner_id =owner_id
        self.owner =owner