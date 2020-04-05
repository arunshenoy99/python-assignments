with open('demo.txt', mode='r') as f:
    file_lines = f.readlines()
    for i in range(0, len(file_lines)):
        if file_lines[i][-1] == '\n':
            file_lines[i] = file_lines[i][:-1]
    print(file_lines)
    f.close()