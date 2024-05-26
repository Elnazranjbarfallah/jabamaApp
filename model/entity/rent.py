from model.entity import *



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

    # def __init__(self, id, house, price, start_date_time):
    #     self.id = id
    #     self.house = house
    #     self.price = price
    #     self.start_date_time = start_date_time

    # todo : getter / setter (validation)