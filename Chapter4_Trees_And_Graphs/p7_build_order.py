from Graph import Graph

def build_graph(projects, dependencies):
    project_graph = Graph(directed=True)
    for project in projects:
        project_graph.addVertex(project)
    for dep_edge in dependencies:
        project_graph.addEdge(dep_edge[0], dep_edge[1])
    return project_graph

def dep_set(graph):
    dep_proj = set()
    for sublist in graph.V.values():
        dep_proj.update(sublist)
    return dep_proj

def build_order(projects, dependencies):
    my_graph = build_graph(projects, dependencies)
    project_build_order = []
    # dep_proj = set([proj for outgoing in my_graph.V.values() for proj in outgoing])

    dep_proj = dep_set(my_graph)
    ind_proj = set(projects) - dep_proj
    while ind_proj:
        project_build_order.extend(ind_proj)
        for proj in ind_proj:
            my_graph.V[proj] = []
        dep_proj = dep_set(my_graph)
        print dep_proj

    return project_build_order

projects = ['a','b','c','d','e','f']
dependencies = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]
print build_order(projects, dependencies)

# def build_order(projects, dependencies):
#     build_order = []
#     dep_copy = dependencies
#     dep_proj = set([x[1] for x in dependencies])
#
#     while dep_copy:
#         ind_proj = set(projects) - dep_proj
#         build_order.extend(ind_proj)
#
#         for ind in ind_proj:
#             for i, dep in enumerate(dep_copy):
#                 if ind == dep[0]:
#                     del dep_copy[i]
#
#     return ind_proj
#
# print build_order(['a','b','c','d','e','f'], [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']])