'''

__name__ concept: 
__name__ is a special variable in Python that indicates how a file is being used. 
If the file is executed directly, __name__ is set to '__main__'. 
If the file is imported as a module, __name__ is set to the module's name (the filename without the .py extension). 
This allows Python files to be used both as reusable modules and as standalone programs

'''

print(f"[a.py] Valor de __name__: {__name__}")

if __name__ == "__main__":
    print("[a.py] Ejecutado directamente")
else:
    print("[a.py] Importado como módulo")
