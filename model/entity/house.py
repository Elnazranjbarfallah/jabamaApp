import re
from model.entity import *


class House(Base):
    __tablename__ = "house"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    area = Column(Integer)
    final_address = Column(String(100))
    plate = Column(String(5))
    number_of_rooms = Column(Integer, default=0)
    elevator = Column(Boolean, default=False)
    parking = Column(Boolean, default=False)
    warehouse = Column(Boolean, default=False)
    price = Column(Integer)

    owner_id = Column(Integer, ForeignKey("person.id"))
    owner = relationship("Person")

    def __init__(self, id, name, city, area, final_address, plate, number_of_rooms, elevator, parking,warehouse, price,owner_id,owner):
         self.id = id
         self.name = name
         self.city = city
         self.area = area
         self.final_address = final_address
         self.plate = plate
         self.number_of_rooms = number_of_rooms
         self.elevator = elevator
         self.parking = parking
         self.warehouse = warehouse
         self.price = price
         self.owner_id = owner_id
         self.owner = owner


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
    def name(self):
        return self._city
    @city.setter
    def name(self, city):
        if re.match(r"^[A-Za-z\s]+$", city, re.I):
            self._city = city
        else:
            raise ValueError("invalid city format")


    @property
    def area(self):
        return self._area
    @id.setter
    def area(self, area):
        if re.match("^[0-9_ \s]+$", area):
            self.area = area
        else:
            raise ValueError("invalid area format")
    @property
    def final_address(self):
        return self._final_address

    @id.setter
    def final_address(self, final_address):
        if re.match("^[A-Za-z0-9_ \s]+$", final_address):
            self.final_address = final_address
        else:
            raise ValueError("invalid address format")

 #addres
    @property
    def plate(self):
        return self._plate
    @id.setter
    def plate(self, plate):
        if re.match("^[0-9_ \s]+$", plate):
            self.plate = plate
        else:
            raise ValueError("invalid plate format")


    @property
    def number_of_rooms(self):
        return self._number_of_rooms

    @id.setter
    def number_of_rooms(self, number_of_rooms):
        if re.match("^[0-9_ \s]+$", number_of_rooms):
            self.number_of_rooms = number_of_rooms
        else:
            raise ValueError("invalid number of rooms format")


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if not price > 1000000000 and price < 100:
            self._price = price
        else:
            return ValueError("invalid price format")


    @property
    def owner_id(self):
        return self._owner_id
    @owner_id.setter
    def owner_id(self, owner_id):
        if re.match("^[0-9_ \s]+$", owner_id):
            self._owner_id = owner_id
        else:
            raise ValueError("invalid owner_id")

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if re.match(r"^[A-Za-z\s]+$", name, re.I):
            self._owner = owner
        else:
            raise ValueError("invalid owner")