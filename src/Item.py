#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import TableManager
from enum import Enum

#################################################################################################
#                                           CLASS ITEM                                          #
#################################################################################################

class Item:

    #-------------------------------------------------------------------------------------------#
    # Function      : __init__                                                                  #
    #                                                                                           #
    # Description   : Initialize an instance of Item                                            #
    #-------------------------------------------------------------------------------------------#
    def __init__(self, _id, _name, _category, _cost):
        self.id = _id
        self.name = _name
        self.category = _category
        self.cost = _cost

#################################################################################################
#                                          ENUM CATEGORY                                        #
#################################################################################################

class Category(Enum):
    VIANDE        = 1
    LEGUME        = 2
    FRUIT         = 3
    POISSON       = 4
    ELECTRONIQUE  = 5

#-----------------------------------------------------------------------------------------------#
# Function      : get_category                                                                  #
#                                                                                               #
# Description   : Return the category corresponding to the category_name                        #
#-----------------------------------------------------------------------------------------------#
def get_category(category_name):
    for category in Category:
        if(category.name == category_name):
            return category

#-----------------------------------------------------------------------------------------------#
# Function      : list_categories                                                               #
#                                                                                               #
# Description   : Return the list of categories in the enum                                     #
#-----------------------------------------------------------------------------------------------#
def list_categories():
    categories = []
    for category in Category:
        categories.append(category)
    
    return categories