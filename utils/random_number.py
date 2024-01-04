import random

class RandomNumber: 
  def __init__(self) -> None:
    pass 

  def get_random(self) -> int: 
    self.__r1 = random.randint(1, 5)

    return self.__r1