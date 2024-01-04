import os, platform
from multiprocessing import cpu_count
from data.mysql_connector import DbConnection 
import mysql.connector
from mysql.connector import errorcode

def init_console() -> None:
  os.system('cls')
  print(platform.processor())
  print(f'Number of CPU threads: {cpu_count()}')
  print()