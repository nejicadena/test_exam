from services.sql_services import MySQLService, MySQLServiceException
from time import sleep
import json
import requests



class UsersServiceException(Exception):
    pass


class UsersService:
    def __init__(self):
        try:
            self.mysql_service = MySQLService()
        except MySQLServiceException as error:
            raise UsersServiceException(error) from error
        
    def insert_user(self, first_name, last_name, password, email, ):
        print(1)
        query = (
            "INSERT INTO `user` (userName, userLastName, userPassword, userEmail "
            ") values(%s, %s, %s, %s)"
        )
        try:
            idRecord = self.mysql_service.insert_single_record(
                query, [
                    first_name,
                    last_name,
                    password,
                    email,
                ]
            )
        except MySQLServiceException as error:
            raise UsersServiceException(error) from error
        print(idRecord)
        return idRecord
        
    def get_user_by_email(self, email):
  

        query = (
            "SELECT id, UserEmail, userPassword  "
            "FROM `user` "
            "WHERE userEmail = %s ; "
        )
        parameters = (email,)
        try:
            records = self.mysql_service.fetch_records(query, parameters)
            if records:
                records = records[0]
            else:
                records = {}
        except MySQLServiceException as error:
            raise UsersServiceException(error) from error
        return records
    
    def get_commet(self, data):
      
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/comments')
            
            if response.status_code == 200:
                
                data = response.json()
                print(data)
                return data
            else:
               
                print(f'Error: {response.status_code}')
        except requests.RequestException as e:
            print(f'Error de conexión: {str(e)}')
        except Exception as e:
            print(f'Ocurrió un error: {str(e)}')
    
    def get_post(self, data):
      
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/posts')
            
            if response.status_code == 200:
                
                data = response.json()
                print(data)
                return data
            else:
               
                print(f'Error: {response.status_code}')
        except requests.RequestException as e:
            print(f'Error de conexión: {str(e)}')
        except Exception as e:
            print(f'Ocurrió un error: {str(e)}')
    
    def get_user(self, data):
      
        try:
            response = requests.get('https://jsonplaceholder.typicode.com/users')
            
            if response.status_code == 200:
                
                data = response.json()
                print(data)
                return data
            else:
               
                print(f'Error: {response.status_code}')
        except requests.RequestException as e:
            print(f'Error de conexión: {str(e)}')
        except Exception as e:
            print(f'Ocurrió un error: {str(e)}')