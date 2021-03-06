import os
import toml
from sqlalchemy import text
from . import mysql_db
from . import sql_path

class SwapModel:
    def __init__(self):
        self.sql_path = os.path.join(sql_path,'swap.sql.toml')
        self.sql_dict = toml.load(self.sql_path)
        for k,v in self.sql_dict.items():
            object.__setattr__(self,k,text(v))

    def query_hour(self,now_time,next_time):
        return mysql_db.engine.execute(self.swap_hour_query,
                                       now_time=now_time,next_time=next_time).fetchall()


    def query_day(self,now_time,next_time):
        return mysql_db.engine.execute(self.swap_day_query,
                                       now_time=now_time,next_time=next_time).fetchall()


    def query_month(self,now_time,next_time):
        return mysql_db.engine.execute(self.swap_month_query,
                                       now_time=now_time,next_time=next_time).fetchall()