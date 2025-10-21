# file_path = r"C:\Users\khan\Desktop\learn_pyhton_basics\final_handling\data.txt"

# with open(file_path, "w") as f:
#     f.write("my 2nd python file\n")
#     f.write("I make this file\n")
    
fd1 = open('faisal.txt',"w")
rv = fd1.write('Python is awesome!')
print("Number of bytes written in the file", rv)
fd1.close()
fd1 = open('faisal.txt')
print(fd1.read())
fd1.close()