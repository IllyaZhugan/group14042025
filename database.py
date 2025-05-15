import os
import json
import constants


def setup_database() -> None:
    """be sure database exists"""
    database_name = constants.DATABASE_NAME
   if os.path.exists(database_name):
       return

with open(database_name, mode="w", encoding="utf-8") as database_file:
    json.dump([], database_file)

pass