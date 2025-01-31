element_list = [("A", "fraise"), ("B", "pomme"), ("C", "glacon"), ("A", "glacon"), ("A", "banane"), ("G", "grenade")]

letter_input = "A"
score_letter = 0
fail = False
for i in range(0, len(element_list)):
    if letter_input == element_list[i][0]:
        if element_list[i][1] == "grenade":
            print("game over")
            fail = True
        elif element_list[i][1] == "glacon":
            print("gele temps")
            score_letter += 1
        else :
            score_letter += 1

element_list = [e for e in element_list if e[0] != letter_input]

if fail: 
    score_letter = 0

if score_letter > 2:
    score_letter -= 1

print(score_letter)
print(element_list)