import cassandra_operations
import mongoDB_operations
from mongoDB_operations import DB_operation
from cassandra_operations import DB_operation


class DB_management:

    def __init__(self, db_type):
        self.db_type = db_type

    def assign_DB(self):
        """
        This function checks whether db_type is 'mongoDB' or 'cassandra' and thus creates a DB object.
        :return: DB object
        """

        if(self.db_type == 'mongo_DB'):
            db_obj = mongoDB_operations.DB_operation()
            return db_obj

        elif(self.db_type == 'cassandra'):
            db_obj = cassandra_operations.DB_operation()
            return db_obj

