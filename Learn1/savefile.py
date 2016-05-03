fileName = 'demo.txt'
WRITE = 'w'
APPEND = 'a'

data = input('Please enter file info')

file = open(fileName, mode = APPEND)
file.write(data)
file.close()
