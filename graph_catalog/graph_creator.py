from constants import ROOT_PATH
from conversion.from_inc_mat import (
    IncMat2AdjList,
    IncMat2AdjMat,
    IncMat2EdgeList,
    IncMat2Graph,
)
from pyvis.network import Network


def main():
    graph = [[]]
    net = Network(directed=True, font_color="black")
    net.add_node("0")
    net.toggle_physics(True)
    net.show_buttons(filter_=["physics"])
    while True:
        with open(str(ROOT_PATH / "data" / "graph.html"), "w") as f:
            f.write(net.generate_html("graph.html", notebook=False))
        inp = input("Cmd: ")

        cmd = inp.strip().split()

        match cmd:
            case ["quit"]:
                break
            case ["print"]:
                print(graph)
            case ["printas", repr]:
                funcs = {
                    "adjlist": IncMat2AdjList,
                    "edgelist": IncMat2EdgeList,
                    "adjmat": IncMat2AdjMat,
                    "graph": IncMat2Graph,
                }
                repr = repr.lower()
                if repr in funcs.keys():
                    print(funcs[repr](graph))
                else:
                    print("unsupported repr")
            case ["addv", num]:
                num = int(num)
                num_of_E = len(graph[0])
                for __ in range(num):
                    graph.append([0] * num_of_E)
                    num_of_V = len(graph)
                    net.add_node(str(num_of_V - 1), label=str(num_of_V - 1))
            case ["adde", first_vertex, second_vertex, *args]:
                directed = False
                if len(args) != 0 and args[0] == "d":
                    directed = True
                first_vertex = int(first_vertex)
                second_vertex = int(second_vertex)
                num_of_V = len(graph)
                num_of_E = len(graph[0])
                for row in range(num_of_V):
                    graph[row].append(0)
                graph[first_vertex][-1] = 1
                graph[second_vertex][-1] = -1 if directed else 1
                arrow = "to" if directed else None
                net.add_edge(str(first_vertex), str(second_vertex), arrows=arrow)


if __name__ == "__main__":
    main()
