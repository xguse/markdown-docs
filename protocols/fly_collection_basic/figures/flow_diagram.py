import pydot as pd

cwd = "/home/gus/Dropbox/repos/git/markdown-docs/protocols/fly_collection_basic/figures/"

graph = pd.Dot(graph_type='digraph')


# define nodes
class StationNode(pd.Node):
    """
    Sets common attribs for station type nodes.
    """
    my_style = dict(style="filled", fillcolor="red", shape='rect')

    def __init__(self, name='', obj_dict=None, **attrs):
        self.my_style.update(attrs)
        super(StationNode, self).__init__(name=name, obj_dict=obj_dict, **self.my_style)


class ProductNode(pd.Node):
    """
    Sets common attribs for station type nodes.
    """
    my_style = dict(style="filled", fillcolor="green", shape='rect')

    def __init__(self, name='', obj_dict=None, **attrs):
        self.my_style.update(attrs)
        super(ProductNode, self).__init__(name=name, obj_dict=obj_dict, **self.my_style)


# Stations
trap_extraction = StationNode(name="Trap Extraction")
labeling = StationNode(name="Labeling")
dissection = StationNode(name="Dissection")
infection_detection = StationNode("Infection detection")
packaging = StationNode("Packaging")

# Products
trap_cages = ProductNode("Trap cages")
field_record = ProductNode("Field record sheet data")
slide_fly = ProductNode("Numbered slide + fly")
tenerals = ProductNode("Tenerals M+F")
dead_males = ProductNode("Dead Males")
dead_females = ProductNode("Dead Females")
tube_labels = ProductNode("Tube Labels")
slide_fly_tissues = ProductNode("Numbered slide + fly + tissues")
slide_fly_tissues_status = ProductNode("Numbered slide + fly + tissues")
infection_status = ProductNode("Infection status")
empty_tubes = ProductNode("Empty tubes")
packaged_tissues = ProductNode("Packaged tissues")


# Add Nodes to graph
graph.add_node(trap_extraction)
graph.add_node(labeling)
graph.add_node(dissection)
graph.add_node(infection_detection)
graph.add_node(packaging)
graph.add_node(trap_cages)
graph.add_node(field_record)
graph.add_node(slide_fly)
graph.add_node(tenerals)
graph.add_node(dead_males)
graph.add_node(dead_females)
graph.add_node(tube_labels)
graph.add_node(slide_fly_tissues)
graph.add_node(slide_fly_tissues_status)
graph.add_node(infection_status)
graph.add_node(empty_tubes)
graph.add_node(packaged_tissues)








# edges
graph.add_edge(pd.Edge(trap_cages, trap_extraction))
graph.add_edge(pd.Edge(trap_extraction, field_record))
graph.add_edge(pd.Edge(trap_extraction, slide_fly))
graph.add_edge(pd.Edge(trap_extraction, tenerals))
graph.add_edge(pd.Edge(trap_extraction, dead_males))
graph.add_edge(pd.Edge(trap_extraction, dead_females))

graph.add_edge(pd.Edge(field_record, labeling))
graph.add_edge(pd.Edge(slide_fly, dissection))
graph.add_edge(pd.Edge(tenerals, packaging, label="at the end"))
graph.add_edge(pd.Edge(dead_males, packaging, label="at the end"))
graph.add_edge(pd.Edge(dead_females, packaging, label="at the end"))

graph.add_edge(pd.Edge(labeling, tube_labels))

graph.add_edge(pd.Edge(tube_labels, packaging))


graph.add_edge(pd.Edge(dissection, slide_fly_tissues))

graph.add_edge(pd.Edge(slide_fly_tissues, infection_detection))

graph.add_edge(pd.Edge(infection_detection, slide_fly_tissues_status))
graph.add_edge(pd.Edge(infection_detection, infection_status))

graph.add_edge(pd.Edge(infection_status, packaging))
graph.add_edge(pd.Edge(empty_tubes, packaging))
graph.add_edge(pd.Edge(slide_fly_tissues_status, packaging))

graph.add_edge(pd.Edge(packaging, packaged_tissues))

# and we are done
graph.write_png(cwd + 'example2_graph.png')
