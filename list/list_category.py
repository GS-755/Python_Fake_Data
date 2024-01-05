from data.mysql_connector import DbConnection
from model.category import Category
from utils.format_export_string import FormatExportString

class ListCategory: 
  __list_cate = [] 
  __db_cnx = None
  __db_cursor = None

  def __init__(self) -> None:
    self.__db_cnx = DbConnection()
    self.__db_cursor = self.__db_cnx.get_cursor()

  def get_list_cate(self) -> list:
    return self.__list_cate
  def set_list_cate(self, list_cate) -> None: 
    self.__list_cate = list_cate

  def db_query(self) -> list:
    list_cate = []
    query = ('SELECT * FROM Category;')
    self.__db_cursor.execute(query)
    tmp_result = self.__db_cursor.fetchall()
    for item in tmp_result:
      cate = Category()
      cate.set_id_cate(item[0])
      cate.set_name_cate(item[1])
      list_cate.append(cate)
    self.__db_cursor.close()
    self.__db_cnx.close_connection()

    return list_cate
  
  def __str__(self) -> str:
    result = FormatExportString.execute('ListCategory', self.__list_cate)

    return result
