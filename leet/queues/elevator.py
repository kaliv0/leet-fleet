# In a small building people are queued up in front of the elevator.
# Every person weighs a certain amount of kilograms and needs a lift to a specific floor within the building.
# Calculate how many courses we would need to transfer all the people to their desired floors while keeping within the elevator restrictions
# for weight and max people allowed inside and without breaking queue order.
# Moving from one floor to another counts as a course. Going back to ground floor is one course as well.
from collections import deque


def elevator_task(people, floors, max_ppl, max_kg):
    courses = 0
    elevator = deque()
    index = 0

    while index < len(people):
        # enter elevator
        total_weight = 0
        while index < len(people) and len(elevator) < max_ppl and people[index] + total_weight <= max_kg:
            elevator.appendleft((people[index], floors[index]))
            total_weight += people[index]
            index += 1

        # exit elevator
        prev_floor = 0
        while elevator:
            curr_weight, floor = elevator.pop()
            if prev_floor != floor:
                courses += 1
            prev_floor = floor

        # go back to ground floor
        courses += 1
    return courses


if __name__ == "__main__":
    assert elevator_task([100, 160, 150, 30, 70, 200], [2, 4, 2, 6, 5, 3], 2, 250) == 11
    assert elevator_task([70, 80, 100], [2, 3, 5], 2, 150) == 5
    assert elevator_task( [100, 70, 80], [3, 2, 2], 2, 150) == 4
    assert elevator_task([10, 20, 100, 20, 200, 30, 70], [2, 3, 4, 5, 6, 7, 8], 2, 200) == 11