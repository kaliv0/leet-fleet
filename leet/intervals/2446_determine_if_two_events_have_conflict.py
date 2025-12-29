# 2446. Determine if Two Events Have Conflict
def have_conflict(event1: list[str], event2: list[str]) -> bool:
    # translate events to int -> actually we can skip this step
    event1 = [_translate(i) for i in event1]
    event2 = [_translate(i) for i in event2]

    # check if events overlap -> NB: we need both conditions
    return event1[0] <= event2[1] and event1[1] >= event2[0]


def _translate(event: str) -> int:
    hours, minutes = event.split(":")
    return int(hours) * 60 + int(minutes)


if __name__ == "__main__":
    for first, second, result in (
            (["01:15", "02:00"], ["02:00", "03:00"], True),
            (["01:00", "02:00"], ["01:20", "03:00"], True),
            (["10:00", "11:00"], ["14:00", "15:00"], False),
            (["14:13", "22:08"], ["02:40", "08:08"], False),
    ):
        assert (actual := have_conflict(first, second)) == result, actual
