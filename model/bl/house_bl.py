from controller.exceptions.exceptions import OwnerNotFoundError
from model.bl import *
from model.da.da import DataAccess
from model.entity.house import House

house_da = DataAccess(House)


class HousetBl:
    @staticmethod
    def save(house):
        return house_da.save(house)

    @staticmethod
    def edit(house):
        if house_da.find_by_house_id(house.rent_id):
            return house_da.edit(house)
        else:
            raise OwnerNotFoundError()

    @staticmethod
    def remove(house_id):
        house = house_da.find_by_house_id(house_id)
        if house:
            return house_da.remove(house)
        else:
            raise OwnerNotFoundError()

    @staticmethod
    def find_all():
        house_list = house_da.find_all()
        if house_list:
            return house_list
        else:
            raise OwnerNotFoundError()

    @staticmethod
    def find_by_owner_id(owner_id):
        house = house_da.find_by_owner_id(owner_id)
        if house:
            return house
        else:
            raise OwnerNotFoundError()

