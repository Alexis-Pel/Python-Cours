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
    annuaire[phone] = c


def get_names():
    names = []
    for n in annuaire:
        names.append(annuaire[n]["name"])

    names.sort()
    return names



my_name = 'Alexis'
my_phone = '06'
my_favorite = True
annuaire = {}

contact = create_contact("Bob", "08", False)
add_contact(contact)

contact = create_contact("Zulu", "09", True)
add_contact(contact)

contact = create_contact(my_name, my_phone, my_favorite)
add_contact(contact)




print(annuaire)
print(get_names())
