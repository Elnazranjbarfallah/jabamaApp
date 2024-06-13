from model.entity import *
import re


class Rent(Base):
    __tablename__ = "rent"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Integer)
    start_date_time = Column(DateTime)
    end_date_time = Column(DateTime)
    house_id = Column(Integer, ForeignKey("house.id"))
    house = relationship("House")
    renter_id = Column(Integer, ForeignKey("person.id"))
    renter = relationship("Person")

    def __init__(self, id, price, start_date_time, end_date_time, house_id, house, renter_id,renter):
         self.id = id
         self.price = price
         self.start_date_time = start_date_time
         self.end_date_time = end_date_time
         self.house_id = house_id
         self.house = house
         self.renter_id =renter_id
         self.renter = renter


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if re.match("^[0-9_ \s]+$", id):
            self.id = id

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
    def house_id(self):
        return self._house_id

    @house_id.setter
    def house_id(self, house_id):
        if re.match("^[0-9_ \s]+$", house_id):
            self.house_id = house_id

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if re.match(r"^[A-Za-z\s]+$", house, re.I):
            self._house = house
        else:
            raise ValueError("invalid house format")

    @property
    def renter_id(self):
        return self._renter_id

    @renter_id.setter
    def renter_id(self, house_id):
        if re.match("^[0-9_ \s]+$", house_id):
            self.house_id = renter_id

    @property
    def renter(self):
        return self._renter

    @renter.setter
    def renter(self, renter):
        if re.match(r"^[A-Za-z\s]+$", renter, re.I):
            self._renter = renter
        else:
            raise ValueError("invalid renter format")