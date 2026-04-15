def time(rate, people, walls):
    old_people = rate["people"]
    old_walls = rate["walls"]
    old_minutes = rate["minutes"]

    new_time = (old_minutes * walls * old_people) / (old_walls * people)

    return int(new_time)


rate = {"people": 10, "walls": 10, "minutes": 22}

print(time(rate, 14, 14))
