def create_contact(name, phone, is_favorite):
    contact = {
        'name': name,
        'phone': phone,
        'is_favorite': is_favorite,
    }
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


def display_all():
    for n in annuaire:
        print(annuaire[n])


def get_contact(search):
    if search.isnumeric():
        return annuaire[search]
    else:
        return annuaire_name[search]


# def new_contact():
#     nom = input("Nom du Contact")
#     phone = input("Numéro de téléphone")
#     Favori = input("Favori ?")
#     if Favori == "o":
#         Favori = True,
#     elif Favori == "n":
#         Favori = False,
#     else:
#         print("ERREUR")
#         new_contact()
#     return nom, phone, Favori
#
# nom, phone, Favori = new_contact()
annuaire = {}
annuaire_name = {}

nom = "Alexis"
phone = "0974"
Favori = False
contact = create_contact(nom, phone, Favori)
add_contact(contact)

nom = "Bob"
phone = "0874"
Favori = True
contact = create_contact(nom, phone, Favori)
add_contact(contact)

print(get_names())
display_all()
print(f"Résultat de la recherche : {get_contact('0874')}")