import phonebook
import logger

logger.first_log("##################################################################")
nom = "Alexis"
phone = "0974"
Favori = False
contact = phonebook.create_contact(nom, phone, Favori)

nom = "Bob"
phone = "0874"
Favori = True
contact = phonebook.create_contact(nom, phone, Favori)
phonebook.print_all()