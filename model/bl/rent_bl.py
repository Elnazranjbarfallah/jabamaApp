from controller.exceptions.exceptions import HouseNotFoundError
from model.da.da import DataAccess
from model.entity.rent import Rent

rent_da = DataAccess(Rent)


class RentBl:
    @staticmethod
    def save(rent):
        return rent_da.save(rent)

    @staticmethod
    def edit(rent):
        if rent_da.find_by_rent_id(rent.rent_id):
            return rent_da.edit(rent)
        else:
            raise HouseNotFoundError()

    @staticmethod
    def remove(renter_id):
        renter = rent_da.find_by_renter_id(renter_id)
        if renter:
            return rent_da.remove(renter)
        else:
            raise HouseNotFoundError()

    @staticmethod
    def find_all():
        rent_list = rent_da.find_all()
        if rent_list:
            return rent_list
        else:
            raise HouseNotFoundError()

    @staticmethod
    def find_by_id(person_id):
        renter = rent_da.find_by_renter_id(person_id)
        if renter:
            return renter
        else:
            raise HouseNotFoundError()

