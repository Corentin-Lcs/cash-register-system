#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import TableManager
import Ticket
import Item
import Stock
import Order

#################################################################################################
#                                        CLASS CUSTOMER                                         #
#################################################################################################

class Customer:

    #-------------------------------------------------------------------------------------------#
    # Function      : __init__                                                                  #
    #                                                                                           #
    # Description   : Initialize an instance of Customer                                        #
    #-------------------------------------------------------------------------------------------#
    def __init__(self, _id, _name, _email, _phone_nb, _ticket):
        self.id = _id
        self.name = _name
        self.email = _email
        self.phone_nb = _phone_nb
        self.ticket = _ticket

    #-------------------------------------------------------------------------------------------#
    # Function      : ask_shopping                                                              #
    #                                                                                           #
    # Description   : Ask the customer if he wants to start shopping                            #
    #-------------------------------------------------------------------------------------------#
    def ask_shopping(self):
        answer = input("Souhaitez-vous commencer vos courses ? (oui / non)  ")
        # Choose "no"
        if(answer == "non"):
            print("\nFin du programme")
            return False
        # Choose "yes"
        elif(answer == "oui"):
            # Did not choose a tva
            if(not self.choose_tva()):
                self.ask_shopping()
            # Choose a tva
            else:
                return True
        # Ask again
        else:
            self.ask_shopping()

    #-------------------------------------------------------------------------------------------#
    # Function      : choose_tva                                                                #
    #                                                                                           #
    # Description   : Let the customer choose a tva or go back to ask_shopping                  #
    #-------------------------------------------------------------------------------------------#
    def choose_tva(self):
        # Ask a tva
        print("Comment voulez-vous faire vos courses ?")
        print("  1. En magasin sans assistance           (TVA = 5%)")
        print("  2. Commande preparee sans livraison     (TVA = 11%)")
        print("  3. Commande preparee et livree          (TVA = 20%)")
        print("  4. Retourner a l'accueil")

        answer = input("\n")

        # If the answer is 1, 2, 3 or 4
        if(len(answer) == 1 and answer[0] >= '1' and answer[0] <= '4'):
            # Return to the homepage
            if(answer[0] == '4'):
                return False
            # Choose a tva
            else:
                if(answer[0] == '1'):
                    self.ticket.tva = 0.05
                elif(answer[0] == '2'):
                    self.ticket.tva = 0.11
                else:
                    self.ticket.tva = 0.2
                return True
        # Ask again
        else:
            self.choose_tva()

    #-------------------------------------------------------------------------------------------#
    # Function      : choose_category                                                           #
    #                                                                                           #
    # Description   : Let the customer choose a category or complete their order                #
    #-------------------------------------------------------------------------------------------#
    def choose_category(self, cursor, stock):
        categories = Item.list_categories()
        nb_categories = len(categories)

        print("\n\nChoisissez une categorie :")
        for i in range(nb_categories):
            print(str(i + 1) + ". " + categories[i].name)

        print(str(nb_categories + 1) + ". " + "Finaliser la commande")

        # Transform the answer to a string so that this function work even if the number of categories exceed 9
        answer = int(input("\n"))

        # If the customer choose a category
        if(answer > 0 and answer <= nb_categories):
            self.choose_item( cursor, stock, categories[answer - 1])
        # If the customer choose to finalize their order
        elif(answer == nb_categories + 1):
            self.end_shopping(cursor)
        # If the customer enter a wrong number
        else:
            self.choose_category(cursor, stock)

    #--------------------------------------------------------------------------------------------------------#
    # Function      : choose_item                                                                            #
    #                                                                                                        #
    # Description   : Let the customer choose an item within the category or choose another category         #
    #--------------------------------------------------------------------------------------------------------#
    def choose_item(self, cursor, stock, category):
        # Get indexes of items in the category
        items_index = stock.get_items_index_from_category(cursor, category)
        nb_items = len(items_index)

        print("\n\nChoisissez un article :")
        for i in range(nb_items):
            print(str(i + 1) + ". " + stock.items[items_index[i]].name)
            print("   -> "+ str(stock.nb[items_index[i]]) + " disponible(s)")
            print("   -> prix unitaire : " + str(stock.items[items_index[i]].cost))
        
        print(str(nb_items + 1) + ". Choisir une autre categorie")

        answer = int(input("\n"))

        # If the customer choose an item
        if(answer > 0 and answer <= nb_items):
            self.choose_quantity(cursor, stock, items_index[answer - 1], stock.nb[items_index[answer - 1]], category)
        # If the customer want to select another category
        elif(answer == nb_items + 1):
            self.choose_category(cursor, stock)
        # If the customer enter a wrong number
        else:
            self.choose_item(cursor, stock, category)

    #-------------------------------------------------------------------------------------------#
    # Function      : choose_quantity                                                           #
    #                                                                                           #
    # Description   : Let the customer choose the quantity he order                             #
    #-------------------------------------------------------------------------------------------#
    def choose_quantity(self, cursor, stock, index, quantity_max, category):
        answer = int(input("\n\nChoisissez une quantite (" + str(quantity_max) + " max)    "))

        # If the customer choose a possible quantity
        if(answer > 0 and answer <= quantity_max):
            Order.make_order(cursor, self, stock, index, answer)
            self.choose_item(cursor, stock, category)
        # If the customer choose not to order the item
        elif(answer == 0):
            self.choose_item(cursor, stock, category)
        # If the customer enter a wrong number
        else:
            self.choose_quantity(cursor, stock, index, quantity_max, category)
    
    #-------------------------------------------------------------------------------------------#
    # Function      : start_shopping                                                            #
    #                                                                                           #
    # Description   : Start the shopping process                                                #
    #-------------------------------------------------------------------------------------------#
    def start_shopping(self, cursor, stock):
        self.choose_category(cursor, stock)

    #-------------------------------------------------------------------------------------------#
    # Function      : end_shopping                                                              #
    #                                                                                           #
    # Description   : End the purchase process                                                  #
    #                 Add the final ticket to the ticket table                                  #
    #                 Print the ticket                                                          #
    #-------------------------------------------------------------------------------------------#
    def end_shopping(self, cursor):
        TableManager.insert_ticket(cursor, self.ticket)

        print("\n\n\n")
        print("Merci d'avoir utilise nos services")
        print("Impression du ticket...")
        print("\n------------------------------------------------------------------------------------")
        print("Bienvenue " + self.name)
        print(self.phone_nb)
        print(self.email)
        print("Ticket n°" + str(self.ticket.id) + "\n")

        for order in self.ticket.orders:
            print(order.item.name + " x" + str(order.quantity) + " : " + str(order.item.cost * order.quantity) + " euro(s)\n")

        print("Prix : " + str(self.ticket.total_cost))
        print("TVA : " + str(self.ticket.tva) + "\n")

        print("Prix TVA : " + str(self.ticket.get_final_cost()))
        print("\n------------------------------------------------------------------------------------")
        
#-----------------------------------------------------------------------------------------------#
# Function      : identification                                                                #
#                                                                                               #
# Description   : Add the customer information to the customers table                           #
#-----------------------------------------------------------------------------------------------#
def identification(cursor):
    # Ask the info of the customer
    print("Identifiez-vous")
    _id = TableManager.count_customers(cursor) + 1
    _name = input("Name : ")
    _email = input("Email : ")
    _phone_nb = input("Phone Number : ")
    _ticket = Ticket.Ticket(_id)

    # Add the customer to the table customers
    _customer = Customer(_id, _name, _email, _phone_nb, _ticket)
    TableManager.insert_customer(cursor, _customer)
    print()

    return _customer