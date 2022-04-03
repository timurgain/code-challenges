"""N. Клумбы."""


def read_input():
    gardeners = int(input())
    flowerbeds = 0
    garden = []
    while flowerbeds < gardeners:
        garden.append(list(map(int, list(input().strip().split()))))
        flowerbeds += 1
    return garden


def order_flowerbeds(garden: list) -> list:

    if len(garden) == 1:
        return garden

    left = order_flowerbeds(garden[0: len(garden)//2])
    right = order_flowerbeds(garden[len(garden)//2: len(garden)])
    flowerbeds = []

    if len(left) == len(right):
        merged = False
        start = left[0][0]

        # без пересечений
        if left[0][1] < right[0][0]:
            end = left[0][1]
        # c пересечением
        elif left[0][1] >= right[0][0] and left[0][1] >= right[0][1]:
            end = left[0][1]
            merged = True
        else:
            end = right[0][1]
            merged = True
        flowerbeds.append([start, end])

        if not merged:
            return left + right
        return flowerbeds

    if len(left) > len(right):
        one_one = order_flowerbeds(garden=[left[0], right[0]])
        if len(one_one) == 2:
            two_one = order_flowerbeds(garden=[left[1], right[0]])
            if len(two_one) == 2:
                flowerbeds = garden
            else:
                flowerbeds = [left[0]] + two_one
        else:
            flowerbeds = one_one + [left[1]]

    if len(left) < len(right):
        one_one = order_flowerbeds(garden=[left[0], right[0]])
        if len(one_one) == 2:
            two_one = order_flowerbeds(garden=[left[0], right[1]])
            if len(two_one) == 2:
                flowerbeds = garden
            else:
                flowerbeds = two_one + [right[0]]
        else:
            flowerbeds = one_one + [right[1]]

    if len(flowerbeds) % 2 == 0:
        flowerbeds = order_flowerbeds(flowerbeds)

    return flowerbeds


def output(flowerbeds):
    # for i in range(len(flowerbeds)-1, -1, -1):
    for i in range(0, len(flowerbeds)):
        print(flowerbeds[i][0], flowerbeds[i][1])


# def sort_by_list_start(obj: list) -> int:
#     return obj[0]


if __name__ == '__main__':
    garden = read_input()
    # garden = sorted(garden, key=sort_by_list_start)
    garden = sorted(garden)
    flowerbeds = order_flowerbeds(garden)
    output(flowerbeds)
