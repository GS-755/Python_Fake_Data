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
  def set_pending_list(self, pending_list) -> None:
    self.__pending_list = pending_list 
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
      pro.set_id_pro(item[0])
      pro.set_name_pro(item[1])
      pro.set_qty_pro(item[2])
      pro.set_price_pro(item[3])
      pro.set_desc_pro(item[4])
      pro.set_id_cate(item[5])
      list_product.append(pro)
    self.__db_cursor.close()
    self.__db_cnx.close_connection()

    return list_product
  
  def db_insert_data(self, item) -> None:
    query = f''' INSERT INTO Products VALUES (
                  {item.get_id_pro()}, 
                  '{item.get_name_pro()}', 
                  {item.get_qty_pro()}, 
                  {item.get_price_pro()}, 
                  '{item.get_desc_pro()}', 
                  {item.get_id_cate()}
                );
            '''
    self.__init__()
    self.__db_cnx = DbConnection()
    self.__db_cursor = self.__db_cnx.get_cursor()
    self.__db_cursor.execute(query)
    self.__db_cursor.close()
    self.__db_cnx.close_connection()
  def insert_multiple_data(self, arrays):
    query = 'INSERT INTO Products VALUES('
    count = 1
    size = len(arrays)
    for item in arrays:
      if(count != size):
        query += f'{item.get_id_pro()}, \'{item.get_name_pro()}\', {item.get_qty_pro()}, {item.get_price_pro()}, \'{item.get_desc_pro()}\', {item.get_id_cate()}), ('
      else:
        query += f'{item.get_id_pro()}, \'{item.get_name_pro()}\', {item.get_qty_pro()}, {item.get_price_pro()}, \'{item.get_desc_pro()}\', {item.get_id_cate()});'
      count += 1 
    self.__init__()
    self.__db_cursor.execute(query)
    print('OK!', end = '')
    self.__db_cnx.commit_change()
    print('Commited to MySQL Database!')
    self.__db_cursor.close()
    self.__db_cnx.close_connection()

  def db_wipe(self) -> None:
    query = ('DELETE FROM Products;')
    self.__init__()
    self.__db_cursor.execute(query)
    self.__db_cursor.close()
    self.__db_cnx.close_connection()
    print('Wiped the products table successfully!')
  
  def insert_pending(self, item) -> None:
    self.__list_product.append(item)

  def print_pending(self) -> str:
    result = FormatExportString.execute('PendingProducts', self.__pending_list)

    return result
  def __str__(self) -> str:
    result = FormatExportString.execute('ListProduct', self.__list_product)

    return result