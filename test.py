# Description: Test script to get debian packages by date and generate a graph
# Ignore this file

import networkx as nx
from pyvis.network import Network
from utils.headerparser_helper import parser

G = nx.Graph()
g = Network()
with open('Packagelist_DUMP/test','r') as rf:
    header = ""
    node = dict()
    for line in rf:
        if line == "\n":
            a  =  parser.parse_string(header).normalized_dict()
            print(a)
            #     stripped_i = i[1].replace("\n","").replace(" ", "")
            #     if ',' in i[1]:
            #         node[i[0]] = stripped_i.split(",")
            #     else:
            #         node[i[0]] = stripped_i
            # # G.add_node(node["Package"] + "|" +node["Version"], **node)
            # if "Depends" not in node:
            #     node["Depends"] = []
            # # G.add_node(node["Package"], Depends = node["Depends"])
            header = ""
            node = dict()
        else:
            header += line
            
# print(G.nodes)

# for i in list(G.nodes(data="Depends", default=[])):
#     print(i[1])
#     if isinstance(i[1], list):
#         for j in i[1]:
#             G.add_edge(i[0], j.replace(" ", "").split('(')[0])
#     else:
#         G.add_edge(i[0], j.replace(" ", "").split('(')[0])

# g.from_nx(G)
# # g.show_buttons(filter_=['physics'])
# g.show("test.html")