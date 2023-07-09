#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import TableManager
import Item
from enum import Enum

#################################################################################################
#                                           CLASS STOCK                                         #
#################################################################################################

class Stock:

    #-------------------------------------------------------------------------------------------#
    # Function      : __init__                                                                  #
    #                                                                                           #
    # Description   : Initialize an instance of Stock                                           #
    #-------------------------------------------------------------------------------------------#
    def __init__(self):
        self.items = []
        self.nb = []
    
    #--------------------------------------------------------------------------------------------#
    # Function      : load_stock                                                                 #
    #                                                                                            #
    # Description   : Load the items from a table into the items and stocks table                #
    #--------------------------------------------------------------------------------------------#
    def load_stock(self, cursor, stock):
        for i in range(len(stock)):
            TableManager.insert_item_in_stock(cursor, stock[i][0], stock[i][1])
    
    #-------------------------------------------------------------------------------------------#
    # Function      : get_stock_from_table                                                      #
    #                                                                                           #
    # Description   : Load the stock from the stocks table                                      #
    #-------------------------------------------------------------------------------------------#
    def get_stock_from_table(self, cursor):
        # Get all rows from the table of stocks
        cursor.execute("SELECT * FROM stock")
        stock_info = cursor.fetchall()
        # Fill the stock tables with this information
        for info in stock_info:
            self.items.append(Item.Item(info[0], info[1], Item.get_category(info[2]), info[3]))
            self.nb.append(info[4])
    
    #-------------------------------------------------------------------------------------------#
    # Function      : get_items_index_from_category                                             #
    #                                                                                           #
    # Description   : Return the index list of items with the corresponding category            #
    #-------------------------------------------------------------------------------------------#
    def get_items_index_from_category(self, cursor, category):
        items_index = []
        for i in range (len(self.items)):
            if(self.items[i].category == category and self.nb[i] > 0):
                items_index.append(i)
                print(self.items[i].name)
        
        return items_index
        
# An array of [items, nb] that can be used to load a stock
stock_test = [
    # VIANDE
    [Item.Item(0, "poulet", Item.Category.VIANDE, 5), 7],
    [Item.Item(1, "beuf", Item.Category.VIANDE, 7), 8],
    [Item.Item(2, "dinde", Item.Category.VIANDE, 6), 4],
    [Item.Item(3, "porc", Item.Category.VIANDE, 6), 9],
    [Item.Item(4, "saucisse", Item.Category.VIANDE, 5), 6],

    # LEGUME
    [Item.Item(5, "potate", Item.Category.LEGUME, 4), 12],
    [Item.Item(6, "tomate", Item.Category.LEGUME, 3), 13],
    [Item.Item(7, "salad", Item.Category.LEGUME, 4), 10],
    [Item.Item(8, "carotte", Item.Category.LEGUME, 4), 12],
    [Item.Item(9, "champignon", Item.Category.LEGUME, 3), 4], 

    # FRUIT
    [Item.Item(10, "pomme", Item.Category.FRUIT, 2), 16],
    [Item.Item(11, "banane", Item.Category.FRUIT, 5), 23],
    [Item.Item(12, "orange", Item.Category.FRUIT, 4), 13],
    [Item.Item(13, "peche", Item.Category.FRUIT, 7), 17],
    [Item.Item(14, "mangue", Item.Category.FRUIT, 2), 14], 

    # POISSON
    [Item.Item(15, "thon", Item.Category.POISSON, 16), 6],
    [Item.Item(16, "saumon", Item.Category.POISSON, 13), 7],
    [Item.Item(17, "morue", Item.Category.POISSON, 4), 6],
    [Item.Item(18, "eglefin", Item.Category.POISSON, 14), 8],
    [Item.Item(19, "sardine", Item.Category.POISSON, 12), 9], 

    # ELECTRONIQUE
    [Item.Item(20, "lampe", Item.Category.ELECTRONIQUE, 20), 5],
    [Item.Item(21, "clavier", Item.Category.ELECTRONIQUE, 59), 4],
    [Item.Item(22, "casque", Item.Category.ELECTRONIQUE, 70), 6],
    [Item.Item(23, "imprimante", Item.Category.ELECTRONIQUE, 60), 7],
    [Item.Item(24, "ordinateur", Item.Category.ELECTRONIQUE, 500), 5],
]