

with open('text.txt', 'w') as out_file:
    a = input("Enter you text: ")
    while a != "":
        out_file.write(a)
        out_file.write('\n')
        a = input("Enter you text: ")


with open('text.txt', 'r') as in_file:
    a = 0
    for line in in_file.readlines():
        a += 1
        print(f'Line {a}: {line}')
