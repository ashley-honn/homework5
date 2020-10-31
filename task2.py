#Read the file book.txt and write the output in summary.txt
FILENAME = 'book.txt'
OUTPUT_FILE = 'summary.txt'
READ_MODE = 'f'
WRITE_MODE = 'w'

f = open("summary.txt", "r+")

for i in range(1):
     f.write("A %d\r\n" % (i))
     f.write("B %d\r\n" % (i))
     f.write("C %d\r\n" % (i))
     f.write("D %d\r\n" % (i))
     f.write("E %d\r\n" % (i))

w = open("book.txt", "w+")

for i in range(1):
    w.write("It doesn't have all the letters\n")