### CREATE a new file by looping each line in the myfile.txt


with open('/Users/sarahdadoun/Desktop/COMPUTER_SCIENCE/semester-3-2021/Scripting-language/in-class/readFile/myfile.txt') as read_file:
    with open('/Users/sarahdadoun/Desktop/COMPUTER_SCIENCE/semester-3-2021/Scripting-language/in-class/readFile/myfile_cp.txt', 'w') as write_file:
        for line in read_file: #for each line in the read file
            write_file.write(line)
            
    with open('/Users/sarahdadoun/Desktop/COMPUTER_SCIENCE/semester-3-2021/Scripting-language/in-class/readFile/myfile_cp.txt', 'a') as append_file:
        append_file.write("\n\nThis is the end of the file >>>>>")