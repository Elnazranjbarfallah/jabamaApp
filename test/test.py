from controller.person_controller import PersonController
from model.da.da import DataAccess
from model.entity import *

# owner = Person()
# owner.name = "ali"
# owner.family = "alipour"
# owner.city = "Tehran"
# owner.role = "OWNER"
#
# renter = Person()
# renter.name = "reza"
# renter.family = "rezaii"
# renter.city = "Tehran"
# renter.role = "RENTER"
#
# p_da = DataAccess(Person)
# p_da.save(owner)
# p_da.save(renter)


print(PersonController.save("ali", "alipour", "OWNER"))
print(PersonController.save("reza", "rezaii", "RENTER"))

# owner = p_da.find_by_id(1)
# renter = p_da.find_by_id(2)


# house = House()
# house.name = "V1"
# house.price = 10000
# house.city = "Tehran"
# house.owner = owner
#
# h_da = DataAccess(House)
# h_da.save(house)
#
# house = h_da.find_by_id(1)
#
# rent = Rent()
# rent.house = house
# rent.renter = renter
#
# r_da = DataAccess(Rent)
# r_da.save(rent)
#
# print(r_da.find_by_id(1))


# from jabama.model.entity.house import House
# from jabama.model.entity.person import Person
# from jabama.model.entity.rent import Rent
# from jabama.model.da.da import DataAccess
# from jabama.model.entity.person import Person
#
# person_da = DataAccess(Person)
# house_da = DataAccess(House)
#
# book_writer = Person(None, "ahmad", "messbah")
#
# book = Book(None, "Python12", book_writer)
#
#
# # print(person_da.save(person))
#
# # print(person)
#
# book_da.save(book)
# # print(book)
#
#
# # print(person_da.find_all())
# # print(person_da.find_by_id(2))
# # print(person_da.find_by(Person.id > 3))
