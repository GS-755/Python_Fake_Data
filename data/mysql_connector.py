import mysql.connector
from config.settings import DbSettings

class DbConnection:
  __config = None 
  __db_connection = None
  __cursor = None 

  def __init__(self) -> None: 
    self.__config = DbSettings()
    self.__config.grab_dotenv()
    self.__db_connection = mysql.connector.connect(
      user = self.get_config().get_usr_name(), 
      password = self.get_config().get_password(), 
      host = self.get_config().get_host(), 
      database = self.get_config().get_db_name()
    )
    self.__cursor = self.__db_connection.cursor()

  def get_config(self) -> DbSettings: 
    return self.__config
  def get_connection(self): 
    return self.__db_connection
  def get_cursor(self): 
    return self.__cursor
  def close_connection(self) -> None: 
    self.__db_connection.close()
  def commit_change(self) -> None: 
    self.__db_connection.commit()