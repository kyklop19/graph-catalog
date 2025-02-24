from pyvis.network import Network


def main():
    graph = [[]]
    net = Network(font_color="black")
    net.add_node("0", label="0")
    net.toggle_physics(True)
    net.show_buttons(filter_=["physics"])
    while True:
        net.show("graph.html", notebook=False)
        inp = input("Cmd: ")

        cmd, *args = inp.strip().split()

        match cmd:
            case "quit":
                break
            case "print":
                print(graph)
            case "addv":
                num_of_V = len(graph)
                num_of_E = len(graph[0])
                graph.append([0] * num_of_E)
                net.add_node(str(num_of_V - 1), label=str(num_of_V - 1))


if __name__ == "__main__":
    main()
