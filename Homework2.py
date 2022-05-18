# 1

class Fruit:
    def __init__(self, name="", weight=0):
        self._name = name
        self._weight = weight

    def __add__(self, other):
        new_weight = self._weight + other._weight
        return new_weight

    def __eq__(self, other):
        if self._name == other._name:
            print("SAME FRUITS!!!")
        else:
            print("DIFFERENT FRUITS!!!")


first = Fruit("Apple", 6)
second = Fruit("Apple", 4)
third = Fruit("Banana", 2)

print(first + second)
print(first == second)



# 2

import sqlite3
connection = sqlite3.connect("morty.db")
cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS dog_info (
                                             name TEXT,
                                             age INTEGER,
                                             colour TEXT )''')
cursor.execute(''' INSERT INTO dog_info VALUES ("labrador", 2, "brown")''')
cursor.execute(''' INSERT INTO dog_info VALUES ("husky", 1, "grey")''')
cursor.execute(''' INSERT INTO dog_info VALUES ("doberman", 3, "black")''')


connection.commit()

select_query = ''' SELECT * FROM dog_info '''
cursor.execute(select_query)
print(cursor.fetchall())