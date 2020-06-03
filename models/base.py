
from peewee import *

from utils.database.mysql import MysqlPool

class BaseModel(Model):

    class Meta:
        # table_name = 'users'
        database = MysqlPool().get_conn
        legacy_table_names = False
