
from peewee import *

from utils.database.mysql import MysqlPoolSync

class BaseModel(Model):

    class Meta:
        # table_name = 'users'
        database = MysqlPoolSync().get_conn
        legacy_table_names = False
