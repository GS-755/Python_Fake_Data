import os
from dotenv import load_dotenv, find_dotenv

class DbSettings: 
  __host = None
  __usr_name = None 
  __password = None
  __db_name = None

  def __init__(self) -> None:
    pass

  def get_host(self) -> str: 
    return self.__host
  def get_usr_name(self) -> str: 
    return self.__usr_name
  def get_password(self) -> str: 
    return self.__password
  def get_db_name(self) -> str: 
    return self.__db_name
  def set_host(self, host) -> None:
    self.__host = host
  def set_usr_name(self, usr_name) -> None:
    self.__usr_name = usr_name
  def set_password(self, password) -> None:
    self.__password = password
  def set_db_name(self, db_name) -> None: 
    self.__db_name = db_name
  
  def grab_dotenv(self) -> None:
    load_dotenv(find_dotenv())
    self.set_host(os.getenv('DB_HOST'))
    self.set_usr_name(os.getenv('DB_USRNAME'))
    self.set_password(os.getenv('DB_PASSWORD'))
    self.set_db_name(os.getenv('DB_NAME'))
