class ListProduct: 
  __list_product = [] 

  def __init__(self) -> None:
    pass

  def get_list_product(self) -> list:
    return self.__list_product
  def set_list_product(self, list_product) -> None: 
    self.__list_product = list_product