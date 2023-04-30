class StackObj:
    def __init__(self, data: str = None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    next = property()

    @next.getter
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, (StackObj, type(None))):
            self.__next = value


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, obj):
        last_obj = self.top
        if last_obj is None:
            self.top = obj
        else:
            while last_obj.next:
                last_obj = last_obj.next
            last_obj.next = obj

    def pop(self):
        if self.top is None:
            return
        last_obj = self.top
        prev_obj = self.top
        while last_obj.next:
            prev_obj = last_obj
            last_obj = last_obj.next
        prev_obj.next = None
        if last_obj == prev_obj:
            self.top = None
        return last_obj

    def get_data(self):
        vertex = self.top
        obj_list = []
        while vertex:
            obj_list.append(vertex.data)
            vertex = vertex.next
        return obj_list



if __name__ == '__main__':
    # st = Stack()
    # st.push(StackObj("obj1"))
    # st.push(StackObj("obj2"))
    # st.push(StackObj("obj3"))
    # st.pop()
    # res = st.get_data()
    # print(res)

    s = Stack()
    top = StackObj("obj_1")
    s.push(top)
    s.push(StackObj("obj_2"))
    s.push(StackObj("obj_3"))
    s.pop()
    res = s.get_data()
    assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"

    h = s.top
    while h:
        res = h.data
        h = h.next
    s = Stack()
    top = StackObj("obj_1")
    s.push(top)
    s.pop()
    assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

