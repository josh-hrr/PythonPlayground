class BaseClass:
  def __init__(self):
    self.__private_variable = 'Private'

  def __private_method(self):
    print('Private method...')

  def public_method(self):
    self.__private_method()

base = BaseClass()
base.public_method()
#print(base.__private_variable) #throws an error, private does not exists.