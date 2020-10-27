import phonebook
import logger
import sys
logger.first_log()

nom = "Alexis"
phone = "08"
is_favorite = False;
contact = phonebook.create_contact(nom, phone, is_favorite)
phonebook.add_contact(contact)

nom = "bob"
phone = "09"
is_favorite = False;
contact = phonebook.create_contact(nom, phone, is_favorite)
phonebook.add_contact(contact)

arg = sys.argv

if '-log' in arg:
    logger.dump_log()

if '-display' in arg:
    display = arg.index("-display")
    display = display + 1
    for n in range(display, len(arg)):
        try:
            phone = arg[n]
            print(phonebook.get_contact(phone))
        except IndexError:
            print("Veuillez indiquer le numéro ou le nom que vous souhaitez rechercher")


# phonebook.new_contact()
# phonebook.print_all()

