# Interface (Using Abstract Base Classes - ABC)
# •	17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`.
#  Implement this in `SQLDatabase` and `NoSQLDatabase`.

from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self,data):
        pass
    @abstractmethod
    def update(self,data):
        pass
    @abstractmethod
    def delete(self,data):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self,data):
        print(f"Inserting {data} into SQL DataBase")
    def update(self,data):
        print(f"Updating {data} into SQL DataBase")
    def delete(self,data):
        print(f"Deleting {data} into SQL DataBase")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self,data):
        print(f"Inserting {data} into No SQL DataBase")
    def update(self,data):
        print(f"Updating {data} into No SQL DataBase")
    def delete(self,data):
        print(f"Deleting {data} into No SQL DataBase")

print("SQL database")
sql=SQLDatabase()
sql.insert(15)
sql.update(15)
sql.delete(15)
print()
print("NoSQL database")
nosql=NoSQLDatabase()
nosql.insert(30)
nosql.update(30)
nosql.delete(30)