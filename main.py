import os, platform
from multiprocessing import cpu_count
from query_database import *

def init_console() -> None:
  os.system('cls')
  print(platform.processor())
  print(f'Number of CPU threads: {cpu_count()}')
  print()
if(__name__ == '__main__'):
  init_console()
  test_cate_list()
  test_product_list()