from data.mysql_connector import DbConnection
from model.product import Product
from utils.format_export_string import FormatExportString

class ListProduct: 
  __list_product = [] 
  __pending_list = []
  __db_cnx = None
  __db_cursor = None
  
  def __init__(self) -> None:
    self.__db_cnx = DbConnection()
    self.__db_cursor = self.__db_cnx.get_cursor()

  def get_pending_list(self) -> list: 
    return self.__pending_list
  def get_list_product(self) -> list:
    return self.__list_product
  def set_list_product(self, list_product) -> None: 
    self.__list_product = list_product
  
  def db_query(self) -> list:
    list_product = []
    query = ('SELECT * FROM Products;')
    self.__db_cursor.execute(query)
    tmp_result = self.__db_cursor.fetchall()
    for item in tmp_result:
      pro = Product()
      pro.set_id_pro = item[0]
      pro.set_name_pro = item[1]
      pro.set_qty_pro = item[2]
      pro.set_price_pro = item[3]
      pro.set_desc_pro = item[4]
      pro.set_id_cate = item[5]
      list_product.append(pro)
    self.__db_cursor.close()
    self.__db_cnx.close_connection()

    return list_product
  
  def insert_pending(self, item) -> None:
    self.__list_product.append(item)

  def print_pending(self) -> str:
    result = FormatExportString.execute('PendingProducts', self.__pending_list)

    return result
  def __str__(self) -> str:
    result = FormatExportString.execute('ListProduct', self.__list_product)

    return result