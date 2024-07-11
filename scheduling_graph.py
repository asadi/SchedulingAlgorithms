# Ebrahim Asadi
# email: asadi.email@gmail.com

from operation import *


##############################################################################
#                           CLASS: SCHEDULING GRAPH
##############################################################################
class SchedulingGraph:
    def __init__(self):
        self.__nodes: list = []
        self.__edges: list = []

    ##############################################################################
    # ADD NODES TO GRAPH
    ##############################################################################
    def add_node(self, node_name: str, node_type: ResourceType):
        self.__nodes.append(Operation(node_name, node_type))
        print('node', node_name, 'added successfully')
        return

    ##############################################################################
    # FIND A NODE BY ITS NAME
    ##############################################################################
    def find_node(self, node_name):
        for node in self.__nodes:
            if node.node_name == node_name:
                return node
        return None

    ##############################################################################
    # ADD A NEW EDGE TO GRAPH FROM "source_node_name" TO "destination_node_name"
    ##############################################################################
    def add_edge(self, source_node_name: str, destination_node_name: str):
        source_node = self.find_node(source_node_name)
        destination_node = self.find_node(destination_node_name)
        self.__edges.append((source_node, destination_node))
        print('edge', source_node.node_name, '--->', destination_node.node_name, 'added successfully')
        return

    ##############################################################################
    # FIND SUCCESSORS OF A GIVEN NODE
    ##############################################################################
    def successors(self, node: Operation):
        result = []
        for edge in self.__edges:
            if edge[0] == node:
                result.append(edge[1])
        return result

    ##############################################################################
    # FIND PREDECESSORS OF A GIVEN NODE
    ##############################################################################
    def predecessors(self, node: Operation):
        result = []
        for edge in self.__edges:
            if edge[1] == node:
                result.append(edge[0])
        return result

    ##############################################################################
    # CHECK IF ALL PREDECESSORS OF A NODE ARE SCHEDULED
    ##############################################################################
    def __all_predecessors_of_node_are_scheduled(self, node: Operation):
        result = True
        predecessors = self.predecessors(node)
        if not predecessors:
            return False

        for p in predecessors:
            if not p.is_scheduled:
                result = False
        return result

    ##############################################################################
    # CHECK IF ALL SUCCESSORS OF A NODE ARE SCHEDULED
    ##############################################################################
    def __all_successors_of_node_are_scheduled(self, node: Operation):
        result = True
        successors = self.successors(node)
        if not successors:
            return False

        for s in successors:
            if not s.is_scheduled:
                result = False
        return result

    ##############################################################################
    # CALCULATE PRIORITY OF NODES BASED ON THE DISTANCE TOWARD THE SINK NODE
    ##############################################################################
    def __calc_priorities(self):
        ##############################################################################
        # INTERNAL FUNCTION USED FOR CALCULATING THE PRIORITY OF NODES
        ##############################################################################
        def recursive_calc_priorities(op: Operation, successor_priority: int):
            if op.node_name == 'v0':
                return
            else:
                op.priority = op.priority + successor_priority + 1

            predecessors = self.predecessors(op)
            for p in predecessors:
                recursive_calc_priorities(p, op.priority)

            return
        ##############################################################################
        vn = self.find_node('vn')
        recursive_calc_priorities(vn, -1)

        print('')
        print('Operations Priorities:')
        for node in self.__nodes:
            print(node.node_name, 'priority=', node.priority)

        return

    ##############################################################################
    # RESET SCHEDULING STATUS OF ALL NODES
    ##############################################################################
    def __reset_scheduling_status(self):
        for node in self.__nodes:
            node.is_scheduled = False
            node.ASAP_Start_Time = 0
            node.ALAP_Start_Time = 0
            node.List_Scheduling_Start_Time = 0
        return

    ##############################################################################
    # PRINT PREDECESSORS OF A NODE
    ##############################################################################
    def print_predecessors(self, node_name: str):
        node = self.find_node(node_name)
        predecessors = self.predecessors(node)
        print("predecessors of", node.node_name, ":")
        for p in predecessors:
            print("  ", p.node_name)
        return

    ##############################################################################
    # PRINT SUCCESSORS OF A NODE
    ##############################################################################
    def print_successors(self, node_name: str):
        node = self.find_node(node_name)
        successors = self.successors(node)
        print("successors of", node.node_name, ":")
        for s in successors:
            print("  ", s.node_name)
        return

    ##############################################################################
    # FIND MAXIMUM OF ASAP START TIMES OF THE PREDECESSORS OF A NODE
    ##############################################################################
    def __max_asap_start_time_of_predecessors(self, node):
        result = 0
        predecessors = self.predecessors(node)
        for p in predecessors:
            new_time = p.ASAP_Start_Time + p.resource_type.Execution_Delay
            if new_time > result:
                result = new_time
        return result

    ##############################################################################
    # ASAP SCHEDULING
    ##############################################################################
    def ASAP(self):
        self.__reset_scheduling_status()

        v0 = self.find_node('v0')
        v0.ASAP_Start_Time = 1
        v0.is_scheduled = True

        vn = self.find_node('vn')

        while True:
            if vn.is_scheduled:
                break

            for node in self.__nodes:
                if node.is_scheduled or not self.__all_predecessors_of_node_are_scheduled(node):
                    continue
                node.ASAP_Start_Time = self.__max_asap_start_time_of_predecessors(node)
                node.is_scheduled = True

        print('ASAP Scheduling:')
        for n in self.__nodes:
            print(n.node_name, ': ', n.ASAP_Start_Time)
        return

    ##############################################################################
    # ALAP SCHEDULING
    ##############################################################################
    def ALAP(self, landabar: int):
        self.__reset_scheduling_status()

        vn = self.find_node('vn')
        vn.ALAP_Start_Time = landabar + 1
        vn.is_scheduled = True

        v0 = self.find_node('v0')

        while True:
            if v0.is_scheduled:
                break

            for node in self.__nodes:
                if node.is_scheduled or not self.__all_successors_of_node_are_scheduled(node):
                    continue
                node.ALAP_Start_Time = self.__min_alap_start_time_of_successors(node)
                node.is_scheduled = True

        print('ALAP Scheduling:')
        for n in self.__nodes:
            print(n.node_name, ': ', n.ALAP_Start_Time)
        return

    ##############################################################################
    # FIND MINIMUM OF ALAP START TIMES OF THE SUCCESSORS OF A NODE
    ##############################################################################
    def __min_alap_start_time_of_successors(self, node):
        result = float('inf')  # float('inf') means infinity in python
        successors = self.successors(node)
        for s in successors:
            new_time = s.ALAP_Start_Time - s.resource_type.Execution_Delay
            if new_time < result:
                result = new_time

        return result

    ##############################################################################
    # FIND UNFINISHED OPERATIONS OF TYPE "resource_type" AT TIME STEP "time_step"
    ##############################################################################
    def unfinished_operations_at_level(self, time_step, resource_type):
        result = []
        scheduled_operations = []
        for node in self.__nodes:
            if node.is_scheduled and node.resource_type.Code == resource_type:
                scheduled_operations.append(node)

        for node in scheduled_operations:
            if node.resource_type.Execution_Delay + node.List_Scheduling_Start_Time > time_step:
                result.append(node)
        return result

    ##############################################################################
    # FIND CANDIDATE OPERATIONS OF TYPE "resource_type" AT TIME STEP "time_step"
    # THEN SORT THEM BASED ON "priority" PROPERTY
    ##############################################################################
    def candidate_operations_of_type_k_sorted_by_priority(self, time_step, resource_type):
        ##############################################################################
        # INTERNAL FUNCTION USED FOR SORTING OPERATIONS BASES ON "priority" PROPERTY
        ##############################################################################
        def sort_on_priority(e):
            return e.priority
        ##############################################################################
        result = []
        for node in self.__nodes:
            if node.resource_type.Code == resource_type and not node.is_scheduled:
                node_is_a_candidate = True
                predecessors = self.predecessors(node)
                for p in predecessors:
                    if not p.is_scheduled or p.resource_type.Execution_Delay + p.List_Scheduling_Start_Time > time_step:
                        node_is_a_candidate = False

                if node_is_a_candidate:
                    result.append(node)
        result.sort(reverse=True, key=sort_on_priority)
        return result

    ##############################################################################
    # LIST SCHEDULING
    ##############################################################################
    def list_scheduling(self):
        self.__reset_scheduling_status()
        self.__calc_priorities()

        vn = self.find_node('vn')
        time_step = 1

        while True:
            for k in range(0, len(ResourceTypes)):
                unfinished_operations = self.unfinished_operations_at_level(time_step, k)
                available_resources_of_type_k = ResourceTypes[k].Max_Resource_Count - len(unfinished_operations)
                candidate_operations_sorted_by_priority = \
                    self.candidate_operations_of_type_k_sorted_by_priority(time_step, k)
                sk = []
                if len(candidate_operations_sorted_by_priority) <= available_resources_of_type_k:
                    sk = candidate_operations_sorted_by_priority
                else:
                    for i in range(0, available_resources_of_type_k):
                        sk.append(candidate_operations_sorted_by_priority[i])

                # Schedule the sk operations
                print("-----------------")
                print("time step: " + str(time_step))
                print("operation:  " + ResourceTypes[k].Name)
                operation_list = "{ "
                for s in sk:
                    operation_list = operation_list + s.node_name + ", "
                    s.List_Scheduling_Start_Time = time_step
                    s.is_scheduled = True
                operation_list = operation_list + "}"
                print(operation_list)

            time_step = time_step + 1

            if vn.is_scheduled:
                break

        return

##############################################################################


