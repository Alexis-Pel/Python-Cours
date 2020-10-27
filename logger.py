from datetime import datetime

dateTimeObj = datetime.now()


# Place une ligne au début de chaques logs
def first_log():
    with open('phonebook.log', 'a') as f:
        f.write("##################################################################" + "\n")


# écrit dans le fichier log
def log(write):
    with open('phonebook.log', 'a') as f:
        f.write('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) + " : " + write)
        f.write("\n")


# Affiche les logs dans le terminal
def dump_log():
    try:
        f = open('phonebook.log', 'r')
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
        f.close()
    except FileNotFoundError as e:
        print(e)
