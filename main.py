import os, platform
from time import sleep
from list.users.list_ttnguoidung import generate_users
from multiprocessing import cpu_count, Pool

NUM_DATA = 1001

def init_console() -> None:
  os.system('cls')
  print(f'Generic CPU name: {platform.processor()}')
  print(f'Number of CPU threads: {cpu_count()}')
  print()

def fake_tt_nguoidung(num_user) -> None: 
  print('\nFake du lieu bang tt_nguoi_dung: \n')
  generated_users = generate_users(num_user)
  for item in generated_users: 
    print(item.export_insert_clause())
    f = open('log\\tt_nguoi_dung.sql', 'a', encoding='utf-8')
    f.write(f'{item.export_insert_clause()}\n')
    f.close()
    print()
  print()

if(__name__ == '__main__'):
  init_console()
  with Pool(12) as p:
    fake_tt_nguoidung(NUM_DATA)
