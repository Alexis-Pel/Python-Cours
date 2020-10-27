import logger

# Créer le contact
def create_contact(name, phone, is_favorite):
    contact = {
        'name': name,
        'phone': phone,
        'is_favorite': is_favorite,
    }
    add_contact(contact)
    return contact


def new_contact():
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

# Ajout du contact dans l'annuaire
def add_contact(c):
    logger.log("ADD CONTACT \n")
    phone = c['phone']
    name = c['name']
    annuaire[phone] = c
    annuaire_name[name] = c
    logger.log(f"name : {name} / phone : {phone}\n")


# Prend et trie que les noms
def get_names():
    names = []
    for n in annuaire:
        names.append(annuaire[n]["name"])

    names.sort()
    return names


# Affiche touts les contacts
def display_all():
    logger.log("DISPLAY ALL : \n")
    for n in annuaire:
        print(f"{n} => {annuaire[n]}")
        logger.log(f"{n} => {annuaire[n]}")
    logger.log("\n")


# Permet de trouver le contact avec son numéro ou son nom
def get_contact(search):
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


# Affiche les noms des contacts, puis l'annuaire et ensuite la recherche
def print_all():
    print(get_names())
    display_all()
    search = input("Recherche : ")
    print(f"{get_contact(search)}")


annuaire = {}
annuaire_name = {}
