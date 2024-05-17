#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import TableManager
import Ticket
import Item
import Stock

#################################################################################################
#                                           CLASS ORDER                                         #
#################################################################################################

class Order:

    #-------------------------------------------------------------------------------------------#
    # Function      : __init__                                                                  #
    #                                                                                           #
    # Description   : Initialize an instance of Order                                           #
    #-------------------------------------------------------------------------------------------#
    def __init__(self, _id, _item, _quantity):
        self.id = _id
        self.item = _item
        self.quantity = _quantity

#-------------------------------------------------------------------------------------------#
# Function      : make_order                                                                #
#                                                                                           #
# Description   : Add a command to the table commands                                       #
#                 Add the order to the customer's ticket                                    #
#                 Add the cost to the total_cost of the customer's ticket                   #
#                 Delete the items from the stock                                           #
#-------------------------------------------------------------------------------------------#
def make_order(cursor, customer, stock, index, quantity):
    # Checks if the customer has already ordered this item
    _id = -1
    for i in range(len(customer.ticket.orders)):
        if(customer.ticket.orders[i].item.name == stock.items[index].name):
            _id = customer.ticket.orders[i].id
            _order = Order(_id, stock.items[index], quantity)
            customer.ticket.orders[i].quantity += quantity

    if(_id == -1):
        _id = TableManager.count_orders(cursor)
        _order = Order(_id, stock.items[index], quantity)
        customer.ticket.orders.append(_order)

    TableManager.delete_item_in_stock(cursor, stock.items[index], quantity)
    stock.nb[index] -= quantity
    TableManager.insert_order(cursor, _order)
    customer.ticket.total_cost += stock.items[index].cost * quantity