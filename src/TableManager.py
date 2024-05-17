#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import mysql.connector
import Customer
import Ticket
import Item
import Stock
import Order

#################################################################################################
#                                           ALL TABLES                                          #
#################################################################################################

#-----------------------------------------------------------------------------------------------#
# Function      : create_all_tables                                                             #
#                                                                                               #
# Description   : Create all tables                                                             #
#-----------------------------------------------------------------------------------------------#
def create_all_tables(cursor):
    create_customers_table(cursor)
    create_tickets_table(cursor)
    create_stock_table(cursor)
    create_orders_table(cursor)

#-----------------------------------------------------------------------------------------------#
# Function      : clear_all_tables                                                              #
#                                                                                               #
# Description   : Clear all tables                                                              #
#-----------------------------------------------------------------------------------------------#
def clear_all_tables(cursor):
    clear_customers_table(cursor)
    clear_tickets_table(cursor)
    clear_stock_table(cursor)
    clear_orders_table(cursor)

def create_bdd(cursor):
    cursor.execute("CREATE DATABASE caisse_enregistreuse")

#################################################################################################
#                                          MAIN TABLES                                          #
#################################################################################################

#-----------------------------------------------------------------------------------------------#
# Function      : clear_main_tables                                                             #
#                                                                                               #
# Description   : Clear main tables (everything except stock)                                   #
#-----------------------------------------------------------------------------------------------#
def clear_main_tables(cursor):
    clear_customers_table(cursor)
    clear_tickets_table(cursor)
    clear_orders_table(cursor)

#################################################################################################
#                                        CUSTOMERS TABLE                                        #
#################################################################################################

#-----------------------------------------------------------------------------------------------#
# Function      : count_customers                                                               #
#                                                                                               #
# Description   : Return the number of customers in the table                                   #
#-----------------------------------------------------------------------------------------------#
def count_customers(cursor):
    cursor.execute("SELECT COUNT(*) FROM customers")
    return cursor.fetchone()[0]

#-----------------------------------------------------------------------------------------------#
# Function      : create_customers_table                                                        #
#                                                                                               #
# Description   : Create customers table                                                        #
#-----------------------------------------------------------------------------------------------#
def create_customers_table(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS customers (
                        customer_id             INT PRIMARY KEY,
                        customer_name           NVARCHAR(100),
                        customer_email          NVARCHAR(100),
                        customer_phone_nb       NVARCHAR(100),
                        ticket_id               INT
                    )
                    ''')

#-----------------------------------------------------------------------------------------------#
# Function      : clear_customers_table                                                         #
#                                                                                               #
# Description   : Clear customers table                                                         #
#-----------------------------------------------------------------------------------------------#
def clear_customers_table(cursor):
    cursor.execute("TRUNCATE TABLE customers")

#-----------------------------------------------------------------------------------------------#
# Function      : insert_customer                                                               #
#                                                                                               #
# Description   : Insert values into the customer table                                         #
#-----------------------------------------------------------------------------------------------#
def insert_customer(cursor, customer):
    cursor.execute('''
                    INSERT INTO customers (customer_id, customer_name, customer_email, customer_phone_nb, ticket_id)
                    VALUES (\'''' + str(customer.id) + "\', \'" + customer.name + "', '" + customer.email + "', '" + customer.phone_nb + "', '" + str(customer.ticket.id) + '''\')
                    ON DUPLICATE KEY UPDATE customer_id = customer_id
                    '''
                    )

#-----------------------------------------------------------------------------------------------#
# Function      : delete_customer                                                               #
#                                                                                               #
# Description   : Delete a customer                                                             #
#-----------------------------------------------------------------------------------------------#
def delete_customer(cursor, customer):
    cursor.execute('''
                    DELETE FROM customers
                    WHERE customer_id = ''' + str(customer.id)
                    )

#################################################################################################
#                                         TICKETS TABLE                                         #
#################################################################################################

#-----------------------------------------------------------------------------------------------#
# Function      : count_tickets                                                                 #
#                                                                                               #
# Description   : Return the number of tickets in the table                                     #
#-----------------------------------------------------------------------------------------------#
def count_tickets(cursor):
    cursor.execute("SELECT COUNT(*) FROM tickets")
    return cursor.fetchone()[0]

#-----------------------------------------------------------------------------------------------#
# Function      : create_tickets_table                                                          #
#                                                                                               #
# Description   : Create tickets table                                                          #
#-----------------------------------------------------------------------------------------------#
def create_tickets_table(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tickets (
                        ticket_id             INT PRIMARY KEY,
                        ticket_total_cost     INT
                    )
                    ''')

#-----------------------------------------------------------------------------------------------#
# Function      : clear_tickets_table                                                           #
#                                                                                               #
# Description   : Clear tickets table                                                           #
#-----------------------------------------------------------------------------------------------#
def clear_tickets_table(cursor):
    cursor.execute("TRUNCATE TABLE tickets")

#-----------------------------------------------------------------------------------------------#
# Function      : insert_ticket                                                                 #
#                                                                                               #
# Description   : Insert values into the tickets table                                          #
#-----------------------------------------------------------------------------------------------#
def insert_ticket(cursor, ticket):
    cursor.execute('''
                    INSERT INTO tickets (ticket_id, ticket_total_cost)
                    VALUES (\'''' + str(ticket.id) + "\', \'" + str(ticket.total_cost) + '''\')
                    ON DUPLICATE KEY UPDATE ticket_id = ticket_id
                    '''
                    )

#-----------------------------------------------------------------------------------------------#
# Function      : delete_ticket                                                                 #
#                                                                                               #
# Description   : Delete a ticket                                                               #
#-----------------------------------------------------------------------------------------------#
def delete_ticket(cursor, ticket):
    cursor.execute('''
                    DELETE FROM tickets
                    WHERE ticket_id = ''' + str(tickets.id)
                    )

#################################################################################################
#                                          STOCK TABLE                                          #
#################################################################################################

#-----------------------------------------------------------------------------------------------#
# Function      : count_stock                                                                   #
#                                                                                               #
# Description   : Return the number of items in stock                                           #
#-----------------------------------------------------------------------------------------------#
def count_in_stock(cursor):
    cursor.execute("SELECT COUNT(*) FROM stock")
    return cursor.fetchone()[0]

#-----------------------------------------------------------------------------------------------#
# Function      : create_stock_table                                                            #
#                                                                                               #
# Description   : Create stock table                                                            #
#-----------------------------------------------------------------------------------------------#
def create_stock_table(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS stock (
                        item_id               INT PRIMARY KEY,
                        item_name             NVARCHAR(100),
                        item_category         NVARCHAR(100),
                        item_cost             INT,
                        item_nb               INT
                    )
                    ''')

#-----------------------------------------------------------------------------------------------#
# Function      : clear_stock_table                                                             #
#                                                                                               #
# Description   : Clear stock table                                                             #
#-----------------------------------------------------------------------------------------------#
def clear_stock_table(cursor):
    cursor.execute("TRUNCATE TABLE stock")

#-----------------------------------------------------------------------------------------------#
# Function      : insert_item_in_stock                                                          #
#                                                                                               #
# Description   : Insert values into the items table                                            #
#-----------------------------------------------------------------------------------------------#
def insert_item_in_stock(cursor, item, nb):
    cursor.execute('''
                    INSERT INTO stock (item_id, item_name, item_category, item_cost, item_nb)
                    VALUES (\'''' + str(item.id) + "\', \'" + item.name + "\', \'" + item.category.name + "\', \'" + str(item.cost) + "\', \'" + str(nb) + '''\')
                    ON DUPLICATE KEY UPDATE item_nb = item_nb + ''' + str(nb)
                    )

#-----------------------------------------------------------------------------------------------#
# Function      : delete_item_in_stock                                                          #
#                                                                                               #
# Description   : Delete an item in the stock                                                   #
#-----------------------------------------------------------------------------------------------#
def delete_item_in_stock(cursor, item, nb):
    # Get the number of item in stock
    cursor.execute('''
                    SELECT item_nb from stock
                    WHERE item_id = ''' + str(item.id)
                    )
    
    nb_in_stock = cursor.fetchone()[0] - nb

    # Delete the item in stock
    if(nb_in_stock <= 0):
        cursor.execute('''
                        DELETE FROM stock
                        WHERE item_id = ''' + str(item.id)
                        )
    # Update the number of items in stock
    else:
        cursor.execute('''
                    INSERT INTO stock (item_id, item_nb)
                    VALUES (\'''' + str(item.id) + "\', \'" + str(nb) + '''\')
                    ON DUPLICATE KEY UPDATE item_nb = ''' + str(nb_in_stock)
                    )

#################################################################################################
#                                         ORDERS TABLE                                          #
#################################################################################################

#-----------------------------------------------------------------------------------------------#
# Function      : count_orders                                                                  #
#                                                                                               #
# Description   : Return the number of items in the table                                       #
#-----------------------------------------------------------------------------------------------#
def count_orders(cursor):
    cursor.execute("SELECT COUNT(*) FROM orders")
    return cursor.fetchone()[0]

#-----------------------------------------------------------------------------------------------#
# Function      : create_orders_table                                                           #
#                                                                                               #
# Description   : Create orders table                                                           #
#-----------------------------------------------------------------------------------------------#
def create_orders_table(cursor):
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS orders (
                        order_id              INT PRIMARY KEY,
                        order_item            NVARCHAR(100),
                        order_quantity        INT
                    )
                    ''')

#-----------------------------------------------------------------------------------------------#
# Function      : clear_orders_table                                                            #
#                                                                                               #
# Description   : Clear orders table                                                            #
#-----------------------------------------------------------------------------------------------#
def clear_orders_table(cursor):
    cursor.execute("TRUNCATE TABLE orders")

#-----------------------------------------------------------------------------------------------#
# Function      : insert_order                                                                  #
#                                                                                               #
# Description   : Insert values into the orders table                                           #
#-----------------------------------------------------------------------------------------------#
def insert_order(cursor, order):
    cursor.execute('''
                    INSERT INTO orders (order_id, order_item, order_quantity)
                    VALUES (\'''' + str(order.id) + "\', \'" + order.item.name + "\', \'" + str(order.quantity) + '''\')
                    ON DUPLICATE KEY UPDATE order_quantity = order_quantity +  ''' + str(order.quantity)
                    )

#-----------------------------------------------------------------------------------------------#
# Function      : delete_order                                                                  #
#                                                                                               #
# Description   : Delete an order                                                               #
#-----------------------------------------------------------------------------------------------#
def delete_order(cursor, order):
    cursor.execute('''
                    DELETE FROM orders
                    WHERE order_id = ''' + str(order.id)
                    )