class Stack(list):
    def put(self, item: any) -> None:  # inserts an element at the last
        self.append(item)

    def get(self) -> any:  # removes an element from the last
        return self.pop()

    def empty(self) -> bool:  # check if the stack is empty
        return not len(self)
