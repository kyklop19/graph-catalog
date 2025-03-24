class Heap:

    def __init__(self, item_list: list[tuple[int, int]] = []):
        self.item_list = item_list

        self.id_indexes = {}
        for i, item in enumerate(self.item_list):
            self.id_indexes[item[1]] = i

        self.heapify()

    def __len__(self):
        return len(self.item_list)

    def heapify(self):
        for i in range(len(self) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, index):
        if index < 0:
            index = len(self) + index

        highest_priority = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self) and self.item_list[left] < self.item_list[highest_priority]:
            highest_priority = left
        if (
            right < len(self)
            and self.item_list[right] < self.item_list[highest_priority]
        ):
            highest_priority = right
        if highest_priority != index:
            self.item_list[index], self.item_list[highest_priority] = (
                self.item_list[highest_priority],
                self.item_list[index],
            )
            self.id_indexes[self.item_list[index][1]] = index
            self.id_indexes[self.item_list[highest_priority][1]] = highest_priority

            self.heapify_down(highest_priority)

    def heapify_up(self, index):
        if index < 0:
            index = len(self) + index

        lowest_priority = index
        parent = (index - 1) // 2

        if parent >= 0 and self.item_list[parent] > self.item_list[lowest_priority]:
            lowest_priority = parent
        if lowest_priority != index:
            self.item_list[index], self.item_list[lowest_priority] = (
                self.item_list[lowest_priority],
                self.item_list[index],
            )
            self.id_indexes[self.item_list[index][1]] = index
            self.id_indexes[self.item_list[lowest_priority][1]] = lowest_priority
            self.heapify_up(lowest_priority)

    def change_value(self, value: int, id: int):
        index = self.id_indexes[id]
        old_value = self.item_list[index][0]
        self.item_list[index] = (value, id)
        if value < old_value:
            self.heapify_up(index)
        elif value > old_value:
            self.heapify_down(index)

    def pop(self):
        self.item_list[0], self.item_list[-1] = self.item_list[-1], self.item_list[0]
        res = self.item_list.pop()
        self.heapify_down(0)
        del self.id_indexes[res[1]]
        return res

    def push(self, item):
        self.item_list.append(item)
        self.id_indexes[item[1]] = -1
        self.heapify_up(-1)
