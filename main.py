import os, platform
from list.users.list_ttnguoidung import generate_users
from multiprocessing import cpu_count

NUM_USERS = 100000000

def init_console() -> None:
  os.system('cls')
  print(f'Generic CPU name: {platform.processor()}')
  print(f'Number of CPU threads: {cpu_count()}')
  print()
def fake_tt_nguoidung(num_user) -> None: 
  print('\nFake du lieu bang tt_nguoi_dung')
  users = generate_users(num_user)
  for item in users: 
    print(item.export_insert_clause())
  print()
if(__name__ == '__main__'):
  init_console()
  fake_tt_nguoidung(NUM_USERS)
