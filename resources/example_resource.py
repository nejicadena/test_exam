from flask import Response, request
from flask_restful import Resource
import logging
import json
from jsonschema import validate, ValidationError
from utility.common_utils import CommonUtils
from services.services import UsersService, UsersServiceException


class CreateComent(Resource):
    @classmethod
    def post(cls):
       
        error_occurred = False
        schema = CommonUtils.load_json_file("./schemas/create_comment.json")
        try:
            data = request.get_json(force=True, silent=True)
            validate(data, schema)
        except ValidationError as exeption:
            logging.error("EX %s ", exeption)
            message = "CAMPOS NO VALIDOS"
            error_occurred = True
        
        if not error_occurred:
            try:
                user_service = UsersService()
                recordsConsulta = user_service.create_commet(data)
                records = {"Consulta": recordsConsulta}
            except UsersServiceException as exeption:
                logging.error("EX %s ", exeption)
                error_occurred = True
                message = "Error"
        
        if error_occurred:
            records = {"error": True, "message": message}
        return Response(json.dumps(records), mimetype="application/json", status=200)