#scores file for students 
FILENAME = 'scores.txt'
WRITE_MODE = 'w'

with open(FILENAME, WRITE_MODE) as scores_file:
    scores_file.write('Alice 69\n')

    name = 'Bob'
    score = 89
    scores_file.write(f'{name} {score}\n')

    scores_file.write('Cindy 79\n')


#define the average for 3 students
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

#font will be red 
print("\033[31mThe class average is\033[0m", cal_average([89,69,79]), '\033[31mfor 3 students.\033[0m')

#output file
OUTPUT_FILE = 'log.txt'
READ_MODE = 'r'

# log.txt file
with open(OUTPUT_FILE, WRITE_MODE) as output_file:
    output_file.write('Bad score value for Boy, ignored.\n')
    output_file.write('Bad score value for Eric, ignored.\n')
    output_file.write('The class average is 79 for 3 students.\n')
