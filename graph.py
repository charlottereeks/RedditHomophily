import matplotlib.pyplot as plt

from networkx import Graph, draw_networkx_nodes, draw_networkx_edges, \
    draw_networkx_labels, spring_layout

from similarity import group_similarity


def author_graph(authorSubs):

    authors = list(authorSubs.keys())

    G = Graph()

    n = len(authors)
    for i in range(n):
        for j in range(i+1, n):

            auth1 = authors[i]
            auth2 = authors[j]
            subs1 = authorSubs[auth1]
            subs2 = authorSubs[auth2]

            sim = group_similarity(subs1, subs2)
            G.add_edge(auth1, auth2, weight=sim)

    return G


def plot_graph(G):

    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        pos = spring_layout(G)  # positions for all nodes

        draw_networkx_nodes(G, pos, node_size=700)

        for (u,v,d) in G.edges(data=True):
            draw_networkx_edges(G, pos, edgelist=[(u,v)], alpha=d['weight'],
                                width=3)

        draw_networkx_labels(G, pos)

        plt.axis('off')
        plt.show()
