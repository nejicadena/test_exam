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


class UserList(Resource):
    @classmethod
    def post(cls):
   
        error_occurred = False
        schema = CommonUtils.load_json_file("./schemas/user_list.json")
        try:
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except ValidationError as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True

        try:
            data_email = {}
            data_token = request.headers.get("Authorization")
            data_email = jwt.decode(data_token.replace("EX-",""), options={"verify_signature": False})
        except (jwt.exceptions.DecodeError , AttributeError) as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True
        print(data_email)
        if not error_occurred and data_email:
            try:
                user_service = UsersService()
                
                recordsPermissions = user_service.get_user(data)
                records = {"UserList": recordsPermissions}
                
            except UsersServiceException as exeption:
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"

        if error_occurred:
            records = {"error": True, "message": message}

        return Response(json.dumps(records), mimetype="application/json", status=200)


class PostList(Resource):
    @classmethod
    def post(cls):
   
        error_occurred = False
        schema = CommonUtils.load_json_file("./schemas/post_list.json")
        try:
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except ValidationError as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True

        try:
            data_email = {}
            data_token = request.headers.get("Authorization")
            data_email = jwt.decode(data_token.replace("EX-",""), options={"verify_signature": False})
        except (jwt.exceptions.DecodeError , AttributeError) as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True
        print(data_email)
        if not error_occurred and data_email:
            try:
                user_service = UsersService()
                
                recordsPermissions = user_service.get_post(data)
                records = {"UserList": recordsPermissions}
                
            except UsersServiceException as exeption:
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"

        if error_occurred:
            records = {"error": True, "message": message}

        return Response(json.dumps(records), mimetype="application/json", status=200)


class CommetsList(Resource):
    @classmethod
    def post(cls):
        error_occurred = False
        schema = CommonUtils.load_json_file("./schemas/comment_list.json")
        try:
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except ValidationError as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True

        try:
            data_email = {}
            data_token = request.headers.get("Authorization")
            data_email = jwt.decode(data_token.replace("EX-",""), options={"verify_signature": False})
        except (jwt.exceptions.DecodeError , AttributeError) as exeption:
            logging.error("EX %s ", exeption)
            message = "ERROR_OCCURRED"
            error_occurred = True
        print(data_email)
        if not error_occurred and data_email:
            try:
                user_service = UsersService()
                
                recordsPermissions = user_service.get_commet(data)
                records = {"UserList": recordsPermissions}
                
            except UsersServiceException as exeption:
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "ERROR_OCCURRED"

        if error_occurred:
            records = {"error": True, "message": message}

        return Response(json.dumps(records), mimetype="application/json", status=200)