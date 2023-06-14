import logging
from mysql.connector import pooling
from utility.common_utils import CommonUtils


class MySQLServiceException(Exception):
    pass


class MySQLService:
    class __MySQLService:
        def __init__(self):
            env_var = CommonUtils()
            try:
                self.pool = pooling.MySQLConnectionPool(
                    pool_name="comments",
                    pool_size=10,
                    pool_reset_session=True,
                    host= env_var.load_enviroment_env("MYSQL_LOCALHOST"),
                    user= env_var.load_enviroment_env("MYSQL_USER"),
                    passwd= env_var.load_enviroment_env("MYSQL_PASSWORD"),
                    db= env_var.load_enviroment_env("MYSQL_DB"),
                    port= env_var.load_enviroment_env("MYSQL_PORT")
                )
            except Exception as exeption:
                logging.error("Error while connecting to MySQL. %s", exeption)
                raise MySQLServiceException(exeption) from exeption

    instance = None

    def __init__(self):
        MySQLService.instance = MySQLService.__MySQLService()

    @classmethod
    def fetch_all_records(cls, query):
        """
        Function to fetch the records from a table
        Args:
            query (str): Query to be executed
            parameters (list): Parameters to be used for the where clause
        Raises:
            error: If there is a problem with the query
        Returns:
            [list]: A list with the records fetched
        """
        connection = MySQLService.instance.pool.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            connection.close()
        except (Exception) as exeption:
            logging.error(
                "Error trying to execute this query %s. %s",
                query, exeption
            )
            raise MySQLServiceException(exeption) from exeption
        return records
    
    @classmethod
    def fetch_records(cls, query, parameters):
        """
        Function to fetch the records from a table
        Args:
            query (str): Query to be executed
            parameters (list): Parameters to be used for the where clause
        Raises:
            error: If there is a problem with the query
        Returns:
            [list]: A list with the records fetched
        """
        connection = MySQLService.instance.pool.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, parameters)
            records = cursor.fetchall()
            cursor.close()
        except (Exception) as exeption:
            logging.error(
                "Error trying to execute this query %s and these parameters %s. %s",
                query, parameters, exeption
            )
            raise MySQLServiceException(exeption) from exeption

        return records
        
    @classmethod
    def insert_single_record(cls, query, parameters):
        """
        Function to insert into a table
        Args:
            query (str): Query to be executed
            parameters (list): Parameters to be used for the where clause
        Raises:
            error: If there is a problem with the query
        Returns:
            [list]: A list with the values fetched
        """
        connection = MySQLService.instance.pool.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, parameters)
            id_record = cursor.lastrowid
            connection.commit()
            cursor.close()
        except (Exception) as exeption:
            logging.error(
                "Error trying to execute this query %s and these parameters %s. "
                "%s", query, parameters, exeption
            )
            raise MySQLServiceException(exeption) from exeption

        return id_record