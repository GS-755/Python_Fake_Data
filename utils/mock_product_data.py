import pandas as pd
from tqdm import tqdm
from faker import Faker
import faker_commerce
from model.product import Product
from list.list_product import ListProduct
from utils.random_number import RandomNumber

class MockProductData:
  __fake = None
  __max_range = None
  __generated_products = None
  
  def __init__(self, max_range) -> None:
    self.__fake = Faker()
    self.__fake.add_provider(faker_commerce.Provider)
    self.__max_range = max_range
    self.__generated_products = ListProduct()
  
  def create_dataset(self):
    generated_products = []
    data = pd.DataFrame()
    for i in tqdm(range(self.__max_range), desc = 'Creating mock Product list...'):
      item = Product() 
      item.set_id_pro(int(i))
      item.set_name_pro(self.__fake.ecommerce_name())
      item.set_qty_pro(RandomNumber.randomize(10, 199))
      item.set_price_pro(RandomNumber.randomize(50000, 550000))
      item.set_desc_pro('Description')
      item.set_id_cate(RandomNumber.randomize(1, 5))
      
      data.loc[i, 'NamePro'] = item.get_name_pro()
      data.loc[i, 'Qty'] = item.get_qty_pro()
      data.loc[i, 'Price'] = item.get_price_pro()
      data.loc[i, 'ProDesc'] = item.get_desc_pro()
      data.loc[i, 'IdCate'] = item.get_id_cate()
      generated_products.append(item)

    return generated_products
  
  def get_max_range(self) -> int:
    return self.__max_range
  def get_item_count(self) -> int: 
    return len(self.__generated_products)
  def get_generated_products(self) -> list:
    return self.__generated_products
  def set_generated_products(self, generated_products) -> list: 
    self.__generated_products = generated_products 