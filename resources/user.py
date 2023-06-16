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
    
        error_occurred = False
        try:
            schema = CommonUtils.load_json_file("./schemas/login.json")
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except (ValidationError, FileNotFoundError) as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True

        if not error_occurred:
            try:
                user_service = UsersService()
                values = user_service.get_user_by_email(data.get('email'))
                if values:
                    password = data.get('password')
                    passworddb = values.get('userPassword')
                    if password == passworddb:
                        token = jwt.encode(
                            {   
                                "id": values.get('id'),
                                "email": data.get('email'),
                                "exp": datetime.datetime.utcnow() + datetime.timedelta(
                                    minutes=int(10)
                                )
                            }, "TEST-SECRET", algorithm="HS512"
                        )
                        records = {
                            "token": f"EX-{token}"
                        }
                    else:
                        print(2)
                        error_occurred = True
                        message = "ERROR_OCCURRED"
                else:
                    print(3)
                    error_occurred = True
                    message = "ERROR_OCCURRED"
            except (
                UsersServiceException, TypeError, json.decoder.JSONDecodeError,
                FileNotFoundError, ValueError
            ) as exeption:
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"

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
            schema = CommonUtils.load_json_file("./schemas/signup.json")
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
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"

        if not error_occurred:
            try:
                print(1)
                d = user_service.insert_user(
                    data.get('first_name'),
                    data.get('last_name'),
                    data.get('password'),
                    data.get('email'),
                )
                print("d")
                print(d)
                records = {
                    "data":d
                    }
                print(2)
            except (UsersServiceException) as exeption:
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"
            
        if error_occurred:
            records = {"error": True, "message": message}

        return Response(json.dumps(records), mimetype="application/json", status=200)


