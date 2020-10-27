from datetime import datetime
dateTimeObj = datetime.now()


def first_log(write):
    with open('phonebook.log', 'a') as f:
        f.write(write + "\n")


def log(write):
    with open('phonebook.log', 'a') as f:
        f.write('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) + " : " + write)
        f.write("\n")


def dump_log():
    f = open('phonebook.log', 'r')
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()
