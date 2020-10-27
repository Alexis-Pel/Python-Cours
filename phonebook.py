import logger


def create_contact(name, phone, is_favorite):
    """
    Permet de créer le contact
    :param name: Nom du contact
    :param phone: Le numéro de téléphone du contact
    :param is_favorite: Le contact est en favoris ou non
    :return: le dictionnaire contact avec les paramètres
    """
    contact = {
        'name': name,
        'phone': phone,
        'is_favorite': is_favorite,
    }
    add_contact(contact)
    return contact


def new_contact():
    """
    Demande a l'utilisateur d'entrer les paramètres du nouveau contact
    :return: Rien
    """
    nom = input("Nom : ")
    phone = input("Phone : ")
    favori = input("Favori ?(o)(n) ")
    Favori = False
    if favori == 'o':
        Favori = True
    else:
        Favori == False

    create_contact(nom, phone, Favori)
    new = input("Nouveau contact ? (o / n)")
    if new == 'o':
        new_contact()


def add_contact(c):
    """
    Ajout du contact dans l'annuaire
    :param c: Le dictionnaire de create_contact
    :return: Rien
    """
    logger.log("ADD CONTACT \n")
    phone = c['phone']
    name = c['name']
    annuaire[phone] = c
    annuaire_name[name] = c
    logger.log(f"name : {name} / phone : {phone}\n")
    return None


def get_names():
    """
    Prend et trie que les noms
    :return: Les noms enregistrés
    """
    names = []
    for n in annuaire:
        names.append(annuaire[n]["name"])
    names.sort()
    return names


def display_all():
    """
    Affiche touts les contacts
    :return: Rien
    """
    logger.log("DISPLAY ALL : \n")
    for n in annuaire:
        print(f"{n} => {annuaire[n]}")
        logger.log(f"{n} => {annuaire[n]}")
    logger.log("\n")
    return None


def get_contact(search):
    """
    Permet de trouver le contact avec son numéro ou son nom
    :param search: Le numéro ou le nom que l'utilisateur recherche
    :return: Rien
    """
    logger.log("GET CONTACT \n")
    try:
        if search.find('.'):
            search = search.replace('.', "")
        if search.isnumeric():
            a = annuaire[search]
            logger.log(str(a))
            return annuaire[search]
        else:
            a = annuaire_name[search]
            logger.log(str(a))
            return annuaire_name[search]
    except KeyError as e:
        print(e)
        return None


def print_all():
    """
    Affiche les noms des contacts, puis l'annuaire et ensuite propose la recherche
    :return: Rien
    """
    print(get_names())
    display_all()
    search = input("Recherche : ")
    print(f"{get_contact(search)}")
    return None


annuaire = {}
annuaire_name = {}
