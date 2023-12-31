#################################################################################################
#                                  IMPORT LIBRAIRIES / MODULES                                  #
#################################################################################################

import TableManager

#################################################################################################
#                                          CLASS TICKET                                         #
#################################################################################################

class Ticket:

    #-------------------------------------------------------------------------------------------#
    # Function      : __init__                                                                  #
    #                                                                                           #
    # Description   : Initialize an instance of Ticket                                          #
    #-------------------------------------------------------------------------------------------#
    def __init__(self, _id):
        self.id = _id
        self.orders = []
        self.total_cost = 0

        # (Useless but gives clarity to the class)
        self.tva = 0.0

    #-------------------------------------------------------------------------------------------#
    # Function      : get_final_cost                                                            #
    #                                                                                           #
    # Description   : Return the final cost of the ticket                                       #
    #-------------------------------------------------------------------------------------------#
    def get_final_cost(self):
        return self.total_cost * (1 + self.tva)