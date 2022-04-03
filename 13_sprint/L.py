"""L. Два велосипеда."""


def read_input() -> tuple:
    days = int(input())
    sorted_amount = list(map(int, input().rstrip().split()))
    bike_price = int(input())

    return bike_price, days, sorted_amount


def when_can_buy(
    bike_price,
    sorted_amount,
    left_id,
    right_id,
    bikes,
):
    # empty space
    if right_id <= left_id:
        return -1

    mid_id = sum((left_id, right_id)) // 2

    # narrowed down the search to the first day and sum is enough
    if (left_id == mid_id
       and sorted_amount[mid_id] // bike_price >= bikes):
        day = mid_id + 1
        return day

    # whole sum today, yesterday was not enough
    if (sorted_amount[mid_id] // bike_price >= bikes
       and sorted_amount[mid_id-1] // bike_price < bikes):
        day = mid_id + 1
        return day

    # whole sum today, yesterday was also enough
    if (sorted_amount[mid_id] // bike_price >= bikes
       and sorted_amount[mid_id-1] // bike_price >= bikes):
        day = when_can_buy(
            bike_price=bike_price,
            sorted_amount=sorted_amount,
            left_id=0,
            right_id=mid_id,
            bikes=bikes,
        )

    # not enough sum yet today, look right
    if sorted_amount[mid_id] // bike_price < bikes:
        day = when_can_buy(
            bike_price=bike_price,
            sorted_amount=sorted_amount,
            left_id=mid_id + 1,
            right_id=right_id,
            bikes=bikes,
        )
    return day


if __name__ == '__main__':
    bike_price, days, sorted_amount = read_input()
    day_for_one_bike = when_can_buy(
        bike_price=bike_price,
        sorted_amount=sorted_amount,
        left_id=0,
        right_id=days,
        bikes=1,
    )
    day_for_two_bike = when_can_buy(
        bike_price=bike_price,
        sorted_amount=sorted_amount,
        left_id=0,
        right_id=days,
        bikes=2,
    )
    print(day_for_one_bike, day_for_two_bike)
