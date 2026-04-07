def interview_qualify(time_list: list, total_time: int) -> str:
    if len(time_list) != 8:
        return "disqualified"
    else:
        if time_list[0] > 5 or time_list[1] > 5:
            return "disqualified"
        elif time_list[2] > 10 or time_list[3] > 10:
            return "disqualified"
        elif time_list[4] > 15 or time_list[5] > 15:
            return "disqualified"
        elif time_list[6] > 20 or time_list[7] > 20:
            return "disqualified"
        elif total_time > 120:
            return "disqualified"
        else:
            return "qualified"


print(interview_qualify([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview_qualify([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview_qualify([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview_qualify([5, 5, 10, 10, 15, 15, 20], 120))
print(interview_qualify([5, 5, 10, 10, 15, 15, 20, 20], 130))
