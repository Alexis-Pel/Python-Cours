from datetime import datetime

dateTimeObj = datetime.now()


def first_log():
    """
    Place une ligne au début de chaques logs
    :return: Rien
    """
    with open('phonebook.log', 'a') as f:
        f.write("##################################################################" + "\n")
    return None


def log(write):
    """
    écrit dans le fichier log
    :param write: Ce qui a à écrire dans le fichier phonebook.log
    :return: Rien
    """
    with open('phonebook.log', 'a') as f:
        f.write('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) + " : " + write)
        f.write("\n")
    return None


def dump_log():
    """
    Affiche les logs dans le terminal
    :return: Rien
    """
    try:
        f = open('phonebook.log', 'r')
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
        f.close()
    except FileNotFoundError as e:
        print(e)
    return None
