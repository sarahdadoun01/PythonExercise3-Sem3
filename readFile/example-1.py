from random import randint # generates a random integer

names = [
    'Oliver',
    'Elijah',
    'William',
    'James',
    'Benjamin',
    'Ethan',
    'Henry',
    'Jacob',
    'Lucas',
    'Alexander',
    'Joe'
]

def txtGenerator(word):
    randPosition = randint(0, len(names)-1) # max of random number is length of list 'NAMES'
    return f"{word} {names[randPosition]}"

np = int(input("How many paragraphs you need? "))

with open('/Users/sarahdadoun/Desktop/COMPUTER_SCIENCE/semester-3-2021/Scripting-language/in-class/readFile/myfile.txt') as rf:
    list_of_words = rf.read().split()
    for n in range(np):
        new_generated_list = list(map(txtGenerator, list_of_words))
        #print(new_generated_list)
    with open('/Users/sarahdadoun/Desktop/COMPUTER_SCIENCE/semester-3-2021/Scripting-language/in-class/readFile/new_file.txt', 'a') as wf:
        wf.write(''.join(new_generated_list) + '\n\n')
        
        