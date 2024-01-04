class Product: 
  __id_pro = None 
  __name_pro = None 
  __qty = None 
  __price = None 
  __pro_desc = None 
  __id_cate = None 

  def __init__(self) -> None:
    pass
  
  def get_id_pro(self) -> int: 
    return self.__id_pro
  def get_name_pro(self) -> str: 
    return self.__name_pro
  def get_qty_pro(self) -> int: 
    return self.__qty
  def get_price_pro(self) -> float: 
    return self.__price
  def get_desc_pro(self) -> str: 
    return self.__pro_desc
  def get_id_cate(self) -> int: 
    return self.__id_cate
  
  def __str__(self) -> str:
    return f'''Product[
      ID: {self.get_id_pro}, 
      Name: {self.get_name_pro}, 
      Qty: {self.get_qty_pro}, 
      Price: {self.get_price_pro}, 
      Desc: {self.get_desc_pro}, 
      IDCate: {self.get_id_cate}]
    '''