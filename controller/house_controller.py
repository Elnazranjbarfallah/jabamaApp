from model.bl.house_bl import HousetBl
from model.entity.house import House
from model.tools.decorators import exception_handling


class HouseController:
    @staticmethod
    @exception_handling
    def save(name, city, area, final_address, plate, number_of_rooms, elevator, parking, warehouse, price, owner_id,
             owner):
        house = House(name, city, area, final_address, plate, number_of_rooms, elevator, parking, warehouse, price,
                      owner_id, owner)
        return True, HouseBl.save(house)

    @staticmethod
    @exception_handling
    def edit(name, city, area, final_address, plate, number_of_rooms, elevator, parking, warehouse, price, owner_id,
             owner, status=True):
        house = House(id, name, city, area, final_address, plate, number_of_rooms, elevator, parking, warehouse, price,
                      owner_id, owner, status)
        return True, HouseBl.edit(house)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, HouseBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, HouseBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, HouseBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_owner_id(owner_id):
        return True, HouseBl.find_by_owner_id(owner_id)
