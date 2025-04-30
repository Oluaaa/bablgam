def log_for(logfile, date_str):
    name = 'log_for_' + date_str[:] + '.txt'
    with (
        open(name, 'w', encoding='utf-8') as file1,
        open(logfile, 'r', encoding='utf-8') as file2
    ):
        file2_reed = file2.readlines()
        for i in file2_reed:
            if date_str in i:
                file1.write(i[11:])


with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())
