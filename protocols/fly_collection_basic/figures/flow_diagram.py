import pydot as pd

cwd = "/home/gus/Dropbox/repos/git/markdown-docs/protocols/fly_collection_basic/figures/"

collection_protocol = pd.Dot(graph_type='digraph', clusterrank='true', pad='.2')


after_live_flies = pd.Cluster('after_lives', style='filled',
                              fillcolor="#B2E9A2", fontsize='11', fontname="DroidSans-Bold.ttf bold",
                              labelloc='b')


# define nodes
class StationNode(pd.Node):
    """
    Sets common attribs for station type nodes.
    """
    my_style = dict(style="filled, bold", fillcolor="grey", shape='box', fontsize='18')

    def __init__(self, name='', obj_dict=None, **attrs):
        self.my_style.update(attrs)
        super(StationNode, self).__init__(name=name, obj_dict=obj_dict, **self.my_style)


class ProductNode(pd.Node):
    """
    Sets common attribs for station type nodes.
    """
    my_style = dict(fillcolor="white", shape='box', fontname="DroidSans-Bold.ttf", fontsize='13', style='rounded, filled')

    def __init__(self, name='', obj_dict=None, **attrs):
        self.my_style.update(attrs)
        super(ProductNode, self).__init__(name=name, obj_dict=obj_dict, **self.my_style)


# Stations
trap_extraction = StationNode(name="Trap Extraction")
labeling = StationNode(name="Labeling")
dissection = StationNode(name="Dissection")
infection_detection = StationNode("Infection detection")
packaging = StationNode("Packaging")
sealing = StationNode("Tube sealing")

# Products
trap_cages = ProductNode("Trap cages")
field_record = ProductNode("Field record data")
slide_fly = ProductNode("Numbered slide + fly")
tenerals = ProductNode("Tenerals M+F")
dead_males = ProductNode("Dead Males")
dead_females = ProductNode("Dead Females")
tube_labels = ProductNode("Tube Labels")
slide_fly_tissues = ProductNode("Numbered slide + fly + tissues")
infection_status = ProductNode("Infection status")
empty_tubes = ProductNode("Empty tubes")
packaged_tissues = ProductNode("Packaged tissues")
sealed_tubes = ProductNode("Sealed tubes")


# Add Nodes to collection_protocol
# trap_label = pd.Subgraph('', rank='same')
# trap_label.add_node(trap_extraction)
# trap_label.add_node(labeling)
# collection_protocol.add_subgraph(trap_label)

collection_protocol.add_node(trap_extraction)
collection_protocol.add_node(labeling)
collection_protocol.add_node(trap_extraction)
collection_protocol.add_node(labeling)
collection_protocol.add_node(dissection)
collection_protocol.add_node(infection_detection)
collection_protocol.add_node(packaging)
collection_protocol.add_node(trap_cages)
collection_protocol.add_node(field_record)
collection_protocol.add_node(slide_fly)
collection_protocol.add_node(tube_labels)
collection_protocol.add_node(slide_fly_tissues)
collection_protocol.add_node(infection_status)
collection_protocol.add_node(empty_tubes)
collection_protocol.add_node(packaged_tissues)
collection_protocol.add_node(sealing)
collection_protocol.add_node(sealed_tubes)


after_live_flies.add_node(tenerals)
after_live_flies.add_node(dead_males)
after_live_flies.add_node(dead_females)
collection_protocol.add_subgraph(after_live_flies)




# edges
collection_protocol.add_edge(pd.Edge(trap_cages, trap_extraction))
collection_protocol.add_edge(pd.Edge(trap_extraction, field_record))
collection_protocol.add_edge(pd.Edge(trap_extraction, slide_fly, penwidth="3"))
collection_protocol.add_edge(pd.Edge(trap_extraction, tenerals))
collection_protocol.add_edge(pd.Edge(trap_extraction, dead_males))
collection_protocol.add_edge(pd.Edge(trap_extraction, dead_females))

collection_protocol.add_edge(pd.Edge(field_record, labeling))
collection_protocol.add_edge(pd.Edge(slide_fly, dissection, penwidth="3"))
collection_protocol.add_edge(pd.Edge(tenerals, packaging))
collection_protocol.add_edge(pd.Edge(dead_males, packaging))
collection_protocol.add_edge(pd.Edge(dead_females, packaging))

collection_protocol.add_edge(pd.Edge(labeling, tube_labels))

collection_protocol.add_edge(pd.Edge(tube_labels, packaging))


collection_protocol.add_edge(pd.Edge(dissection, slide_fly_tissues, penwidth="3"))

collection_protocol.add_edge(pd.Edge(slide_fly_tissues, infection_detection, penwidth="3"))

collection_protocol.add_edge(pd.Edge(infection_detection, slide_fly_tissues, penwidth="3"))
collection_protocol.add_edge(pd.Edge(infection_detection, infection_status))

collection_protocol.add_edge(pd.Edge(infection_status, packaging))
collection_protocol.add_edge(pd.Edge(infection_status, labeling))
collection_protocol.add_edge(pd.Edge(empty_tubes, packaging))
collection_protocol.add_edge(pd.Edge(slide_fly_tissues, packaging, penwidth="3"))

collection_protocol.add_edge(pd.Edge(packaging, packaged_tissues, penwidth="3"))

collection_protocol.add_edge(pd.Edge(packaged_tissues, sealing, penwidth="3"))

collection_protocol.add_edge(pd.Edge(sealing, sealed_tubes, penwidth="3"))

# and we are done
collection_protocol.write_png(cwd + 'fly_processing_flow.png')
