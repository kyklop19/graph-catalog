from collections import deque
from enum import Enum, auto
from pathlib import Path
from sys import path

path.insert(0, str(Path(__file__).resolve().parents[1]))

from pyvis.network import Network
from regex_spm import fullmatch_in

from graph_catalog.catalog import SaveOpts, save
from graph_catalog.constants import ROOT_PATH
from graph_catalog.conversion.from_inc_mat import (
    IncMat2AdjList,
    IncMat2AdjMat,
    IncMat2EdgeList,
    IncMat2Graph,
)


class EdgeType:
    UNDIRECTED = auto()
    DIRECTED_TO = auto()
    DIRECTED_FROM = auto()


class CommandExecutor:

    def __init__(self):
        self.call_stack = deque()
        self.reset()

    def reset(self):
        self.graph = [[]]
        self.edge_weights = []
        self.default_weight_name = "length"
        self.default_arrow = None
        self.ARROW_MAP = {"to": "to", "from": "from", "u": None}

        self.net = Network(directed=True, font_color="black")
        self.net.add_node("0")
        self.net.toggle_physics(True)
        self.net.show_buttons(filter_=["physics"])
        self.update_html()

    def print(self, repr):
        funcs = {
            "": lambda x: x,
            "incmat": lambda x: x,
            "adjlist": IncMat2AdjList,
            "edgelist": IncMat2EdgeList,
            "adjmat": IncMat2AdjMat,
            "graph": IncMat2Graph,
        }
        if repr is None:
            repr = ""
        repr = repr.lower()
        if repr in funcs.keys():
            print(funcs[repr](self.graph))
        else:
            print("unsupported repr")

    def add_vertices(self, amount):
        num_of_E = len(self.graph[0])
        for __ in range(amount):
            self.graph.append([0] * num_of_E)
            num_of_V = len(self.graph)
            self.net.add_node(str(num_of_V - 1), label=str(num_of_V - 1))

        self.update_html()

    def add_edge(self, first_vertex, second_vertex, arrow):
        num_of_V = len(self.graph)
        num_of_E = len(self.graph[0])

        for row in range(num_of_V):
            self.graph[row].append(0)

        self.graph[first_vertex][-1] = 1

        if arrow is None:
            arrow = self.default_arrow
        else:
            arrow = self.ARROW_MAP[arrow]

        directed = False
        if arrow is not None:
            directed = True

        if self.graph[second_vertex][-1] != 0:
            second_vertex_value = 2
        elif directed:
            second_vertex_value = -1
        else:
            second_vertex_value = 1
        self.graph[second_vertex][-1] = second_vertex_value

        self.edge_weights.append({})

        self.net.add_edge(
            str(first_vertex),
            str(second_vertex),
            arrows=arrow,
            label=str(num_of_E),
        )

        self.update_html()

    def add_edge_weight(self, edge, value):
        self.edge_weights[edge][self.default_weight_name] = value
        self.net.get_edges()[edge][
            "label"
        ] += f"\n| {self.default_weight_name}: {value}"
        self.update_html()

    def join_vertex(self, nbr):
        num_of_V = len(self.graph)

        for row in range(num_of_V):
            self.graph[row].append(0)

        num_of_E = len(self.graph[0])
        self.graph.append([0] * num_of_E)

        self.graph[nbr][-1] = 1
        self.graph[-1][-1] = 1

        self.net.add_node(str(num_of_V))

        self.net.add_edge(str(nbr), str(num_of_V), arrows=None, label=str(num_of_E - 1))

        self.update_html()

    def execute_command(self, cmd):
        self.call_stack.append(cmd)
        quit = False
        match fullmatch_in(cmd):
            case r"quit":
                quit = True
            case r"reset":
                self.call_stack = deque()
                self.reset()
            case r"print ?(\w+)?" as m:
                self.print(m[1])
            case r"addv (\d+)" as m:
                self.add_vertices(int(m[1]))
            case r"(\d+) (\d+) ?(\w)?" as m:
                first_vertex = int(m[1])
                second_vertex = int(m[2])

                self.add_edge(first_vertex, second_vertex, m[3])
            case r"(\d+)" as m:
                self.join_vertex(int(m[1]))
            case r"sete (\w+)" as m:
                self.default_arrow = self.ARROW_MAP[m[1]]
            case r"setw (\w+)" as m:
                self.default_weight_name = m[1]
            case r"w (\d+) (\d+)" as m:
                self.add_edge_weight(int(m[1]), int(m[2]))
            case r"save ([\w_]+)(?: -([co]))? (.+)" as m:
                match m[2]:
                    case "o":
                        opts = SaveOpts.OVERWRITE_GRAPH
                    case "c":
                        opts = SaveOpts.CREATE_NEW_FILE
                    case __:
                        opts = None
                save(m[3], m[1], self.graph, opts=opts)
            case r"back":
                reset_calls = self.call_stack
                self.call_stack = deque()
                self.reset()
                for __ in range(2):
                    reset_calls.pop()
                while len(reset_calls) != 0:
                    cmd = reset_calls.popleft()
                    self.execute_command(cmd)
            case r"history":
                for cmd in self.call_stack:
                    print(cmd)
            case __:
                print("unsupported cmd")
        return quit

    def update_html(self):
        with open(str(ROOT_PATH / "data" / "graph.html"), "w") as f:
            f.write(self.net.generate_html("graph.html", notebook=False))


def main():

    executor = CommandExecutor()

    quit = False

    while not quit:
        inp = input("Cmd: ")
        cmd = inp.strip()
        quit = executor.execute_command(cmd)


if __name__ == "__main__":
    main()
