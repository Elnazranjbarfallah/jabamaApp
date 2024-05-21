from jabama.model.entity.house import House
from jabama.model.entity.person import Person
from jabama.model.entity.rent import Rent
from jabama.model.da.da import DataAccess
from jabama.model.entity.person import Person

person_da = DataAccess(Person)
house_da = DataAccess(House)

book_writer = Person(None, "ahmad", "messbah")

book = Book(None, "Python12", book_writer)


# print(person_da.save(person))

# print(person)

book_da.save(book)
# print(book)


# print(person_da.find_all())
# print(person_da.find_by_id(2))
# print(person_da.find_by(Person.id > 3))
