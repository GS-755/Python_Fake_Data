class Category: 
  __id_cate = None 
  __name = None 

  def __init__(self) -> None:
    pass

  def get_id_cate(self) -> int: 
    return self.__id_cate
  def get_name_cate(self) -> str:
    return self.__name
  def set_id_cate(self, id_cate) -> None: 
    self.__id_cate = id_cate 
  def set_name_cate(self, name) -> None: 
    self.__name = name

  def __str__(self) -> str:
    return f'Category[IdCate: {self.get_id_cate()}, Name: {self.get_name_cate()}]' 