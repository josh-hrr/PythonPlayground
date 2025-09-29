with open('text.txt', 'r+') as file:
    content = file.read()
    print("Current content of the file:")
    print(content)
    
    file.write("\nAppended line 1.")
    file.write("\nAppended line 2.")
    
    file.seek(0)
    updated_content = file.read()
    print("\nUpdated content of the file:")
    print(updated_content)