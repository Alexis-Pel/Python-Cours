import phonebook
import logger
import error
logger.first_log()


nom = "Alexis"
phone = "09"
Favori = False
contact = phonebook.create_contact(nom, phone, Favori)

nom = "Bob"
phone = "08"
Favori = True
contact = phonebook.create_contact(nom, phone, Favori)
phonebook.print_all()