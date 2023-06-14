import json
import logging
from json import JSONDecodeError
import os
from os.path import join, dirname
from dotenv import load_dotenv,  dotenv_values

class CommonUtils:
    @staticmethod
    def load_json_file(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as fp:
                return json.loads(fp.read())
        except (FileNotFoundError, JSONDecodeError) as exeption:
            logging.error("Ex %s ", exeption)
            raise exeption
    
    @staticmethod
    def load_enviroment_env(env):

        dotenv_path = join("./static/", '.env')
        config_env = dotenv_values(dotenv_path)
        values_env = config_env[env]
        return values_env
        