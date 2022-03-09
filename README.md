# Scheduling Algorithms
(The following text is copied from chapter 5 of the book <em>SYNTHESIS AND OPTIMIZATION OF DIGITAL CIRCUITS, writen by Giovanni De Micheli</em>)
Scheduling is a very important problem in architectural synthesis. Whereas a sequencing graph prescribes only dependencies among the operations, the scheduling-of a sequencing graph determines the precise start time of each task. The start times must satisfy the original dependencies of the sequencing graph, which limit the amount of parallelism of the operations, because any pair of operations related by a sequency dependency (or by a chain of dependencies) may not execute concurrently.
Scheduling determines the concurrency of the resulting implementation, and therefore'it affects its pelformance. By the same token, the maximum number of concurrent operations of any given type at any step of the schedule is a lower bound on the number of required hardware resources of that type. Therefore the choice of a schedule affects also the area of the implementation.
The number of resources (of any given type) may he bounded from above to satisfy some design requirement. For example, a circuit with a prescribed size may have at most one floating point multiplierldivider. When resource constraints are imposed, the number of operations of a given type whose execution can overlap in time is limited by the number of resources of that type. A spectrum of solutions may be obtained by scheduling a sequencing graph with different resource constraints.
Tight hounds on the number of resources correlate to serialized implementations. As a limiting case, a scheduled sequencing graph may he such that all operations are executed in a linear sequence. This is indeed the case when only one resource is available to implement all operations.
Aredatency trade-off points can be derived as solutions to constrained scheduling problems for desired values of the cycle-time. The area evaluation is just a weighted sum of the resource usage for resource-dominatedcircuits. When considering other circuits, an additional component must be taken into account, corresponding to steering logic, registers, wiring and control area.

This work is based on the algorithms introduced in book <em>SYNTHESIS AND OPTIMIZATION OF DIGITAL CIRCUITS, writen by Giovanni De Micheli</em>

<h2>Unconstrained Scheduling: The ASAP Scheduling Algorithm</h2>
The unconstrained minimum-latency scheduling problem can be solved in polynomial time by topologically sorting the vertices of the sequencing graph. This approach is called in jargon as soon as possible (ASAP) scheduling, because the start time for each operation is the least one allowed by the dependencies.

<h2>Latency-Constrained Scheduling: The ALAP Scheduling Algorithm</h2>
The ASAP scheduling algorithm yields the minimum values of the start times. A complementary algorithm, the as late as possible (ALAP) scheduling Algorithm, provides the
corresponding maximum values.

<h2>Heuristic Scheduling Algorithms: List Scheduling</h2>
Practical problems in hardware scheduling are modeled by generic sequencing graphs, with (possibly) multiple-cycle operations with different types. With this model, the minimum-latency resource-constrained scheduling problem and the minimum-resourcelatency-constrained problem are known to be intractable. Therefore, heuristic algorithms have been researched and used. We consider a family of algorithms called list scheduling algorithms. The list scheduling algorithms are classified according to the selection step. A priority list of the operations is used in choosing among the operations, based on some heuristic urgency measure.
A common priority list is to label the vertices with weights of their longest path to the sink and to rank them in decreasing order. The most urgent operations
are scheduled first. Note that when the operations have unit delay and when there is only one resource type, the algorithm is the same as Hu's and it yields an optimum solution for tree-structured sequencing graphs.
Scheduling under resource and relative timing constraints can be handled by list scheduling .In particular, minimum timing constraints can be dealt with by
delaying the selection of operations in the candidate set. The priority list is modified to reflect the proximity of an unscheduled operation to a deadline related to a maximum timing constraint. Schedules constructed by the algorithms satisfy the required constraints by construction. Needless to say, the heuristic nature of list scheduling may prevent finding a solution that may exist.
