def majority_vote(vote_list: list) -> str:
    length = len(vote_list)
    if length == 0:
        return None
    else:
        for i in range(length):
            count = 0
            for j in range(length):
                if vote_list[i] == vote_list[j]:
                    count += 1

            if count > (length // 2):
                return vote_list[i]
    return None


print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
