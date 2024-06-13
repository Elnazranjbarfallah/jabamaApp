from model.bl.rent_bl import RentBl
from model.entity.rent import Rent
from model.tools.decorators import exception_handling

class RentController:
    @staticmethod
    @exception_handling
    def save(price, start_date_time, end_date_time, house_id, house , renter_id, renter):
        rent = Rent( price, start_date_time, end_date_time, house_id, house , renter_id, renter)
        return True, RentBl.save(rent)

    @staticmethod
    @exception_handling
    def edit(id, price, start_date_time, end_date_time, house , renter, status=True):
        person = Rent(id, price, start_date_time, end_date_time, house , renter, status)
        return True, RentBl.edit(person)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, RentBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, RentBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, RentBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_price(price):
        return True, RentBl.find_by_price(price)
