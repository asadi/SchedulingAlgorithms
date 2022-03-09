# Ebrahim Asadi
# email: ceo@hdfsoft.com

from resource_type import *


##############################################################################
#                              CLASS: OPERATION
##############################################################################
class Operation:
    ##############################################################################
    # CONSTRUCTOR
    ##############################################################################
    def __init__(self, node_name: str, rs_type: ResourceType):
        self.node_name = node_name
        self.resource_type = rs_type
        self.priority = 0
        self.is_scheduled = False
        self.ALAP_Start_Time = 0
        self.ASAP_Start_Time = 0
        self.List_Scheduling_Start_Time = 0

    ##############################################################################
    # SHOWS THE CLASS OBJECT AS STRING WHILE DEBUGGING
    ##############################################################################
    def __str__(self):
        result = self.node_name + "(" + self.RS_Type_Name + ")"
        if self.is_scheduled:
            result = result + " is scheduled"
        else:
            result = result + " is not scheduled"

        result = result + ", List_Scheduling_Start_Time=" + str(self.List_Scheduling_Start_Time)
        result = result + ", Execution_Delay=" + str(self.Execution_Delay)

        return result

    ##############################################################################
    # SHOWS THE CLASS OBJECT AS STRING WHEN PRINTING THE OBJECT
    ##############################################################################
    def __repr__(self):
        return self.node_name

##############################################################################

