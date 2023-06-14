from services.sql_services import MySQLService, MySQLServiceException
from time import sleep
import json



class UsersServiceException(Exception):
    pass


class UsersService:
    def __init__(self):
        try:
            self.mysql_service = MySQLService()
        except MySQLServiceException as error:
            raise UsersServiceException(error) from error

    def create_commet(self, data):
        """
        Method to get
        Args:
            email (str): The email of user
        Raises:
            UsersServiceException: If an error occurred with the database
        Returns:
            The user object if exists, if not returns empty object
        """
        query_type_user = (
            "INSERT INTO comments(idUser, idFile, commets) "
            "VALUES (%s,%s,%s); "
        )
        try:
            self.mysql_service.insert_single_record(query_type_user, (data.get("idUser"),data.get("idFile"),data.get("comment")))
        except MySQLServiceException as error:
            raise UsersServiceException(error) from error

        return "Ok"
    
    def get_commet(self, data):
        """
        Method to get
        Args:
            email (str): The email of user
        Raises:
            UsersServiceException: If an error occurred with the database
        Returns:
            The user object if exists, if not returns empty object
        """
        query = (
        "SELECT * FROM comments "
        "WHERE idFile = %s;"
        )
        try:
            records = self.mysql_service.fetch_records(query, (data.get("idFile"),))
        except MySQLServiceException as error:
            raise UsersServiceException(error) from error

        return records