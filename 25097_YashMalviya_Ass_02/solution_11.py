# Part D: Challenge Complexity (2 Exercises)
# Exercise 11: Group Anagrams
def Group_Anagrams():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    dump = []
    see = [False] * len(words)

    for i in range(len(words)):
        if see[i]:
            continue
        temp = [words[i]]
        see[i] = True
        for j in range(i + i, len(words)):
            if not see[j] and sorted(words[i]) == sorted(words[j]):
                temp.append(words[j])
                see[j] = True
        dump.append(temp)
    print(dump)


Group_Anagrams()
