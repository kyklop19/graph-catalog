from constants import ROOT_PATH
from conversion.from_inc_mat import (
    IncMat2AdjList,
    IncMat2AdjMat,
    IncMat2EdgeList,
    IncMat2Graph,
)
from pyvis.network import Network
from regex_spm import fullmatch_in


class CommandExecutor:

    def __init__(self):
        self.reset()

    def reset(self):
        self.graph = [[]]
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

    def add_edge(self, first_vertex, second_vertex, directed):
        num_of_V = len(self.graph)
        num_of_E = len(self.graph[0])

        for row in range(num_of_V):
            self.graph[row].append(0)

        self.graph[first_vertex][-1] = 1
        self.graph[second_vertex][-1] = -1 if directed else 1

        arrow = "to" if directed else None
        self.net.add_edge(
            str(first_vertex), str(second_vertex), arrows=arrow, label=str(num_of_E)
        )

        self.update_html()

    def execute_command(self, cmd):
        quit = False
        match fullmatch_in(cmd):
            case r"quit":
                quit = True
            case r"reset":
                self.reset()
            case r"print ?(\w+)?" as m:
                self.print(m[1])
            case r"addv (\d+)" as m:
                self.add_vertices(int(m[1]))
            case r"(\d+) (\d+) ?(\w)?" as m:
                first_vertex = int(m[1])
                second_vertex = int(m[2])
                directed = True if m[3] == "d" else False

                self.add_edge(first_vertex, second_vertex, directed)

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
