### read
### read r,
### write w,
### append, a
### read and write , r+

# by default it is going to be read.
# file = open("./myfile.txt","r")
# file = open("./myfile.txt","w")
# file = open("./myfile.txt","a")
# file = open("./myfile.txt","r+")

# print(file.name)
# print(file.mode)
# print(file.read())

# file.close()

# pythin introduced the suite(block) of the file.
# instead of oening and closing file all the time...add()
with open("/Users/sarahdadoun/Desktop/COMPUTER_SCIENCE/semester-3-2021/Scripting-language/in-class/readFile/myfile.txt","r") as file:
    
    ## 1) Read File in 1 shot
    # file_content = file.read()
    # print(file_content)
    
    ## 2) Read File line by line and store content in form of list (\n --> enter)
    # lines = file.readlines()
    # print(len(lines))
    # for line in lines:
    #     print(line, end=" ")
    
    # f_content = file.read(100)
    # print(f_content)
    
    # f_content = file.read(100)
    # print(f_content)
    
    # chunk = 150
    # f_content = file.read(chunk)
    # print(f_content)
    # while len(f_content) > 0 :
    #     print(f_content)
    #     f_content = file.read(chunk)
    
    
    # print("\n\nThis is the end of the file.")
    
    chunk = 200
    f = file.read(chunk)
    print(f.tell()) # where is the position of the 
    file.seek(0)    # tells the reader to go to position 0
    
    