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

    # def __init__(self, id, name, city, area, final_address, plate, number_of_rooms, elevator, parking,warehouse, price,owner_id,owner):
    #     self.id = id
    #     self.name = name
    #     self.city = city
    #     self.area = area
    #     self.final_address = final_address
    #     self.plate = plate
    #     self.number_of_rooms = number_of_rooms
    #     self.elevator = elevator
    #     self.parking = parking
    #     self.warehouse = warehouse
    #     self.price = price
    #     self.owner_id =owner_id
    #     self.owner =owner

    # todo : getter / setter (validation)