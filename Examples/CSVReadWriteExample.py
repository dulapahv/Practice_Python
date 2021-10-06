import csv

def readCSV():
    with open('CloseFriends.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} likes the movie {row[1]} , and like the animal {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


def writeCSV():
    import csv

    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Dulapah Vibulsanti', 'Manager', 'March'])
        employee_writer.writerow(['Sitthapong Jitsuparp', 'CEO', 'August'])

#writeCSV()
readCSV()