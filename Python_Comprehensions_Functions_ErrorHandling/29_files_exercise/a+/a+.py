with open('text.txt', 'a+') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    
    file.seek(0)
    content = file.read()
    print("Content of the file after writing:")
    print(content)
    
    file.write("This is an additional line.\n")
    
    file.seek(0)
    updated_content = file.read()
    print("\nUpdated content of the file:")
    print(updated_content)