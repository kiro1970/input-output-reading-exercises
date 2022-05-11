with open('Sample-text-file-10kb.txt', 'r') as sample:

    a = 0
    for line in sample:
        print(line)
        words = line.split()
        a += len(words)
    print(f'Number of words in file: {a}')
