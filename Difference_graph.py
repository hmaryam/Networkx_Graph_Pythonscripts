from xlrd import open_workbook
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.operators.binary  # to find the difference graph

def excel_sheet_to_graph(file_name, sheet_number):

    book = open_workbook(file_name)
    sheet = book.sheet_by_index(sheet_number)
    graph = nx.Graph()

    header_list = sheet.row_slice(0, 1)  # (row is,col starts from)
    sidebar_list = sheet.col_slice(0, 1) # (col is,row starts from)
    edges_list = []
    nodes_list = []
     
    for row in range(1,sheet.nrows):

        values = []
        
        for col in range(1,sheet.ncols):

            header = header_list[col - 1]
            sidebar = sidebar_list[row - 1]
            cell = sheet.cell(row,col)

            if "".join(str(cell.value).split( )) != '' :
    #           print sidebar.value, ',', header.value, ',' , cell.value
                edges_list.append([sidebar.value,header.value])

    for cell in header_list:
        nodes_list.append(cell.value)
    
    graph.add_nodes_from(nodes_list)
    graph.add_edges_from(edges_list)

    pos = nx.circular_layout(graph)  # Comes after adding nodes and edges!(creating a real graph)
    
    nx.draw_networkx_nodes(graph,pos, nodelist=nodes_list, node_color="b", node_size=1500)
    nx.draw_networkx_edges(graph,pos, edgelist=edges_list, edge_color='b',width=8) 
    nx.draw_networkx_labels(graph,pos,width=8.0,alpha=0.5, font_size= 20, font_color = '#A0CBE2')  # to draw the lables!

#   plt.savefig("M.PDF",facecolor='pink')  #save graph
#   plt.show()  # creats a graph for each file
    
# To find the list of paths and the shortest path
    paths =nx.all_simple_paths(graph, source='H1', target='H3')
    paths_list = (list(paths))
    print 'All paths_file', file_name, ':' ,paths_list                # List of paths
    print 'Shortest path_file', file_name,':', min(paths_list, key=len)  # Shortest path
    print 'Number of nodes: ', len(nodes_list)
    print ' '
    #plt.show()   # We need it to show each graph separately
    return graph

def difference(graph2, graph1):

    D1 = nx.difference(graph2, graph1)
    pos = nx.circular_layout(D1)
    D2 = nx.difference(graph1, graph2)  # edges in graph1 but not in graph2
    pos = nx.circular_layout(D2)

    nx.draw_networkx_nodes(D1,pos, node_color="g", node_size=1000)
    nx.draw_networkx_edges(D1,pos, edge_color='g',width=10) 
    nx.draw_networkx_nodes(D2,pos, node_color="r", node_size=1000)
    nx.draw_networkx_edges(D2,pos, edge_color='r',width=10) 

    plt.show()
#   plt.savefig("M.PDF",facecolor='pink')  #save graph

    return difference

"""
def short_path_between( G, node1, node2, cutoff_number):
    paths =nx.all_simple_paths(G, source=node1, target=node2, cutoff=cutoff_number)  # cutoff is optional
    paths_list = (list(paths))
    print 'List of paths between',node1,'and',node2,'for', G, 'is:', paths_list   
    print 'Shortest path between',node1,'and',node2,'for' ,G,'is:', min(paths_list, key=len)   
    plt.show()
    return short_path_between
"""


graph1 = excel_sheet_to_graph('R.xlsx', 0)
graph2 = excel_sheet_to_graph('R2.xlsx', 0)
#short_path_between(graph1,'H1','H3','')

Difference = difference(graph2, graph1)
