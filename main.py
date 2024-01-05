import os, platform
from tqdm import tqdm
from multiprocessing import cpu_count
from query_database import *
from utils.mock_product_data import MockProductData
from model.product import Product

from query_database import *

def init_console() -> None:
  os.system('cls')
  print(f'Generic CPU name: {platform.processor()}')
  print(f'Number of CPU threads: {cpu_count()}')
  print()
def make_publish_random_data(size) -> None: 
  list_product = ListProduct()
  list_product.db_wipe()
  mock_data = MockProductData(size)
  mock_data.set_generated_products(mock_data.create_dataset())
  print('\nPublishing to MySQL Instance...')
  list_product.insert_multiple_data(mock_data.get_generated_products())
  print()

if(__name__ == '__main__'):
  init_console()
  make_publish_random_data(1000)