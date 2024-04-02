import pandas as pd
from tqdm import tqdm
from faker import Faker
import faker_commerce
from utils.random_number import RandomNumber

class MockProductData:
  __fake = None
  __max_range = None
  __generated_products = None
  
  def __init__(self, max_range) -> None:
    self.__fake = Faker()
    self.__fake.add_provider(faker_commerce.Provider)
    self.__max_range = max_range
  
  def get_max_range(self) -> int:
    return self.__max_range
  def get_item_count(self) -> int: 
    return len(self.__generated_products)
  def get_generated_products(self) -> list:
    return self.__generated_products
  def set_generated_products(self, generated_products) -> list: 
    self.__generated_products = generated_products 
