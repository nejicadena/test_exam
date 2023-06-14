import base64
import datetime
import json
import logging
import os
import random
import string
from flask import Response, request
from flask_restful import Resource
from jsonschema import validate, ValidationError
import jwt
from services.services import UsersService, UsersServiceException
from utility.common_utils import CommonUtils


class User(Resource):
    @classmethod
    def post(cls):
        """
        Method to login app
        Args:
            user_name (string): Parameters required for user insertion, unique value constraint
        Returns:
            The user_id is returned in json format
        """
        error_occurred = False
        try:
            schema = CommonUtils.load_json_file("schemas/login.json")
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except (ValidationError, FileNotFoundError) as exeption:
            logging.error("CARTEC %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True

        if not error_occurred:
            try:
                user_service = UsersService()
                values = user_service.get_user_by_email_token(data.get('email'))
                if values:
                    password = CommonUtils.decrypt_password(data.get('password'))
                    passworddb = CommonUtils.decrypt_password(values.get('userPassword'))
                    if password == passworddb:
                        if values.get('activateUser') == 1:
                            secretKey = CommonUtils.get_environment_variable('SECRTE_KEY_JWT')
                            jwt_secret = CommonUtils.get_secret_key(secretKey)
                            permissions_user = user_service.get_permmission_user(data.get('email'))
                            token = jwt.encode(
                                {   
                                    "id": values.get('id'),
                                    "email": data.get('email'),
                                    "exp": datetime.datetime.utcnow() + datetime.timedelta(
                                        minutes=int(os.environ.get('JWT_EXPIRATION_TIME'))
                                    )
                                }, jwt_secret.get('key'), algorithm="HS512"
                            )
                            records = {
                                "token": f"CARTEC-{token}",
                                "permissions": permissions_user
                            }
                        else:
                            print(1)
                            error_occurred = True
                            message = ERROR_OCCURRED_USER_NOT_ACTIVATION
                    else:
                        print(2)
                        error_occurred = True
                        message = ERROR_OCCURRED
                else:
                    print(3)
                    error_occurred = True
                    message = ERROR_OCCURRED
            except (
                UsersServiceException, TypeError, json.decoder.JSONDecodeError,
                FileNotFoundError, ValueError
            ) as exeption:
                logging.error("CARTEC %s ", exeption)
                error_occurred = True
                message = ERROR_OCCURRED

        if error_occurred:
            records = {"error": True, "message": message}

        return Response(json.dumps(records), mimetype="application/json", status=200)


class UserRegister(Resource):
    @classmethod
    def post(cls):
        """
        Method to user register app
        Args:
            user_name (string): Parameters required for user insertion, unique value constraint
        Returns:
            The user_id is returned in json format
        """
        error_occurred = False
    
        user_service = UsersService()
        
        try:
            schema = CommonUtils.load_json_file("schemas/sing_up.json")
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except (ValidationError, FileNotFoundError) as exeption:
            logging.error("Ex %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True

        if not error_occurred:
            try:
                values = user_service.get_user_by_email(data.get('email'))
                if values:
                    error_occurred = True
                    message = "ERROR_OCCURRED"
            except (UsersServiceException) as exeption:
                logging.error("CARTEC %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"

        if not error_occurred:
            try:
                tokenActivacionUser = ''.join(
                    random.choice(string.ascii_lowercase + string.digits) for i in range(10)
                )
                user_service.insert_user(
                    data.get('first_name'),
                    data.get('last_name'),
                    data.get('password'),
                    data.get('email'),
                    datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                    tokenActivacionUser,
                )
            except (UsersServiceException) as exeption:
                logging.error("CARTEC %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"
            
        if error_occurred:
            records = {"error": True, "message": message}

        return Response(json.dumps(records), mimetype="application/json", status=200)


