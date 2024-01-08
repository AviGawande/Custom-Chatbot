file_path = 'input.txt'

# here we are writing into the file
with open(file_path,'w') as file:
    file.write('Hello Abhishek!!')
    file.write("How are you??")
print("Your Content has been successfully Added..")


# here we are opening the file
with open(file_path,'r') as file:
    file_content = file.read()
    print("File Content:",file_content)


