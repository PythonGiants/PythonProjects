answer1 = [item[0] for item in ["Elie", "Tim", "Matt"]]
print(answer1)

answer2 = [value for value in [1,2,3,4,5,6] if value % 2 == 0]
print(answer2)

answer3 = [value for value in [1,2,3,4] if value in [3,4,5,6]]
print(answer3)

answer4 = [item[::-1].lower() for item in ["Elie", "Tim", "Matt"]]
print(answer4)

answer5 = [value for value in range(1,101) if value % 12 == 0]
print(answer5)

answer6 = [letter for letter in "amazing" if letter not in "aeiou"]
print(answer6)

answer7A = [[value for value in range(3)] for item in range(3)]
print(answer7A)

answer7B = [[val for val in range(10)] for res in range(10)]
print(answer7B)
