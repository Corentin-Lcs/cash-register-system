#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import mysql.connector
import TableManager
import Customer
import Ticket
import Item
import Stock
import Order

#################################################################################################
#                                              MAIN                                             #
#################################################################################################

def main():
    # Create the cursor to access the database
    connector = mysql.connector.connect(host="localhost",user="root")
    _cursor = connector.cursor(buffered = True)
    TableManager.create_bdd(_cursor)
    _cursor.execute("USE caisse_enregistreuse")

    # Create tables
    TableManager.create_all_tables(_cursor)

    # Clear all tables
    # TableManager.clear_all_tables(_cursor)

    # Clear main tables
    TableManager.clear_main_tables(_cursor)

    # Create an instance of stock
    _stock = Stock.Stock()

    # Fill the table's stock with the item in stock_test
    _stock.load_stock(_cursor, Stock.stock_test)

    # Load table stock
    _stock.get_stock_from_table(_cursor)

    # Identification
    _customer = Customer.identification(_cursor)

    # Ask if the customer wants to start shopping
    if(_customer.ask_shopping()):
        # Start the shopping process
        _customer.start_shopping(_cursor, _stock)

    return 0

#################################################################################################
#                                             LAUNCH                                            #
#################################################################################################

# Launch the main function
main()