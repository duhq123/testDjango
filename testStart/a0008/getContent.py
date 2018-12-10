
import os, csv

if __name__ == '__main__':
    file = open('/Users/edz/Downloads/sub-clause3.csv', 'r')


    file_name = 'sub-clause5.csv'
    target = os.path.join('/Users/edz/Desktop', file_name)
    with open(target, 'w+') as f1:
        writer = csv.writer(f1)

        for line in file:
            # print(line)
            line = line.split(',')[1].strip()
            print(line)
            if line is not  None:
                writer.writerow([line])
