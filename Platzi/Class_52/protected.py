#protected methods/variables is just for FYI, here is a protected/private
class BaseClass:
  def __init__(self):
    self._protected_variable = 'Protected'

  def _protected_method(self):
    print('Protected method...')

base = BaseClass()
print(base._protected_variable) 
base._protected_method()