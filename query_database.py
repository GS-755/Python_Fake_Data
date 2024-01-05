from list.list_category import ListCategory
from list.list_product import ListProduct

def test_cate_list() -> None: 
  obj = ListCategory()
  obj.set_list_cate(obj.db_query())
  print(obj.__str__())
def test_product_list() -> None: 
  obj = ListProduct()
  obj.set_list_product(obj.db_query())
  print(obj.__str__())