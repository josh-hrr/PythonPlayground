
#explicit import
'''
from package.mod_1 import func_1, func_2
from package.mod_2 import func_3, func_4

print(func_1())
print(func_4())

'''

#using a namespace that imports the packages to use them as follows:
import package
print(package.URL)
print(package.mod_1.func_1())
