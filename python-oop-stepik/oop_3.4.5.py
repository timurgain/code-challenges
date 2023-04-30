class NewList:
    def __init__(self, data: list = None):
        self.data = data.copy() if data and type(data) == list else []

    # @staticmethod
    # def lists_substraction(source: list, subtrahend: list):
    #     del_index = []
    #     for sub in subtrahend:      
    #         for i in range(len(source)):
    #             if source[i] == sub and (type(source[i])) == type(sub):
    #                 if i in del_index:
    #                     continue
    #                 del_index.append(i)
    #                 break
    #     source = source.copy()
    #     for ind in sorted(del_index, reverse=True):
    #         source.pop(ind)
    #     return source

    @staticmethod
    def lists_substraction(source: list, subtrahend: list):
        if len(subtrahend) == 0:
            return source
        subtr = subtrahend.copy()
        return [x for x in source if not NewList.__is_elem(x, subtr)]

    @staticmethod
    def __is_elem(x, subtr):
        res = any(map(lambda s: type(x) == type(s) and x == s, subtr))
        if res:
            subtr.remove(x)
        return res

    def __sub__(self, subtrahend: list):
        other = subtrahend if type(subtrahend) == list else subtrahend.data
        return NewList(self.lists_substraction(self.data, other))

    def __rsub__(self, subtrahend: list):
        other = subtrahend if type(subtrahend) == list else subtrahend.data
        return NewList(self.lists_substraction(other, self.data))

    def __isub__(self, subtrahend: list):
        return self.__sub__(subtrahend)

    def get_list(self):
        return self.data


if __name__ == '__main__':
    lst = NewList()
    lst1 = NewList([0, 1, -3.4, "abc", True])
    lst2 = NewList([1, 0, True])
    assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
    res1 = lst1 - lst2
    res2 = lst1 - [0, True]
    res3 = [1, 2, 3, 4.5] - lst2
    lst1 -= lst2
    assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
    assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
    assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
    assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
    lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
    lst_2 = NewList([10, True, False, True, 1, 7.87])
    res = lst_1 - lst_2
    assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"
