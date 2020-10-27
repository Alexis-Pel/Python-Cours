def create_contact(name, phone, is_favorite):
    contact = {
        'name': name,
        'phone': phone,
        'is_favorite': is_favorite,
    }
    add_contact(contact)
    return contact


# Ajout du contact dans l'annuaire
def add_contact(c):
    phone = c['phone']
    name = c['name']
    annuaire[phone] = c
    annuaire_name[name] = c


# Prend et trie que les noms
def get_names():
    names = []
    for n in annuaire:
        names.append(annuaire[n]["name"])

    names.sort()
    return names


# Affiche touts les contacts
def display_all():
    for n in annuaire:
        print(f"{n} => {annuaire[n]}")


# Permet de trouver le contact avec son numéro ou son nom
def get_contact(search):
    if search.find('.'):
        search = search.replace('.', "")
    if search.isnumeric():
        return annuaire[search]
    else:
        return annuaire_name[search]


# Affiche les noms des contacts, puis l'annuaire et ensuite la recherche
def print_all():
    print(get_names())
    display_all()
    search = input("Recherche : ")
    print(f"{get_contact(search)}")


annuaire = {}
annuaire_name = {}