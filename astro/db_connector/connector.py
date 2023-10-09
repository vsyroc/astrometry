import mysql.connector

from decouple import config
from astro.core.logger_settings import logger


db_host = config('host')
db_user = config('user')
db_password = config('password')
db_name = config('name')
db_port = config('port')


class DBHConnector:
    def __init__(self):
        try:
            self.dbh = mysql.connector.Connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name,
                port=db_port,
                auth_plugin='mysql_native_password'
            )

            self.dbh.autocommit = True
            self.cursor = self.dbh.cursor(buffered=True)
            logger.info('Connected to db.')
        except Exception as e:
            logger.error(f'Connection failed. {e}')

    def get_sql_query(self, sql_request: str, values: tuple = None, multy: bool = False):
        if not isinstance(sql_request, str):
            logger.error('SQL request is not string.')
            return None
        self.cursor.execute(sql_request, values, multi=multy)
        return self.cursor.fetchall()

    def push_sql_query(self, sql_request: str, values: tuple = None, multy=False):
        if not isinstance(sql_request, str):
            logger.error('SQL request is not string.')
            return None
        self.cursor.execute(sql_request, values, multi=multy)

    def close_connection(self):
        try:
            self.dbh.close()
            logger.info('Connection closed')
        except:
            logger.error('Connection didn\'t close.')
