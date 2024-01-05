from data.mysql_connector import DbConnection
from model.product import Product

class ListProduct: 
  __list_product = [] 
  __db_cnx = None
  __db_cursor = None
  
  def __init__(self) -> None:
    self.__db_cnx = DbConnection()
    self.__db_cursor = self.__db_cnx.get_cursor()

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

  def __str__(self) -> str:
    item_count = len(self.__list_product)
    if(item_count == 0):
      return 'ListProduct[]'
    result = 'ListProduct [\n'
    count = 0
    for item in self.__list_product:
      count += 1
      if(count == len(self.__list_product)):
        result += f'\t{item} \n'
        result += ']'
      else:
        result += f'\t{item}, \n'

    return result