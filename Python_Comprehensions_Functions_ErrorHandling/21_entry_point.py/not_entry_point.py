import entry_point  

print("This is not the entry point module")
entry_point.run()

print(__name__)             #__name__ : name of the module, if module is executed directly, the __name__ is equal to "main"
print(entry_point.__name__) #__name__ : name of the module, if imported, it has the module name.
