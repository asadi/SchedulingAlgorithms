# Ebrahim Asadi
# email: ceo@hdfsoft.com

##############################################################################
#                              CLASS: RESOURCE TYPE
##############################################################################
class ResourceType:
    def __init__(self, rs_type_name, rs_type_code, execution_delay, max_resource_count):
        self.Name = rs_type_name
        self.Code = rs_type_code
        self.Execution_Delay = execution_delay
        self.Max_Resource_Count = max_resource_count


##############################################################################
#                          DEFINE RESOURCE TYPES
##############################################################################
NOP = ResourceType("NOP", 0, 0, 1)  # resource_code=0, exec_delay=0, max_resource_count = 1
Multiplier = ResourceType("Multiplier", 1, 2, 3)  # resource_code=1, exec_delay=2, max_resource_count = 3
ALU = ResourceType("ALU", 2, 1, 1)  # resource_code=2, exec_delay=1, max_resource_count = 1

ResourceTypes = [NOP, Multiplier, ALU]

##############################################################################
