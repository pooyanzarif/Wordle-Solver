import random

# ----------------------------------------------------------------------------------------------------------------------
# Load Dictionary
words = [line.rstrip() for line in open('wordlist.txt', encoding="utf8")]


# ----------------------------------------------------------------------------------------------------------------------
# Omit words in dictionary in which the is not proper character
def refine_dataset(position, c, word_result):
    global words
    i = 0
    if word_result == '2':  # the letter is in the word and in the correct spot
        while i < len(words):
            if words[i][position] != c:
                del words[i]
            else:
                i += 1

    elif word_result == '1':  # the letter is in the word but in the wrong spot
        while i < len(words):
            if (not (c in words[i])) or (c == words[i]):
                del words[i]
            else:
                i += 1
    elif word_result == 0:  # the letter is not in the word in any spot
        while i < len(words):
            if c in words[i]:
                del words[i]
            else:
                i += 1
    elif word_result == 3:  # the letter is in wrong spot but the vount of this letter is more than one
        while i < len(words):
            if c == words[i]:
                del words[i]
            else:
                i += 1
    else:
        assert "Invalid word_Result"
    if len(words) == 0:
        print("There is no word found!")
        exit(0)


# ----------------------------------------------------------------------------------------------------------------------
# analyze the word_result  character by character and call refine_dataset function to omit wrong words
def analyze(word, word_result):
    for i in range(5):
        if word_result[i] == "0":
            s = 0
            for j in range(5):
                if word[i] == word[j]:
                    s += int(word_result[j])
            if s == 0:  # there is no character in the word
                refine_dataset(i, word[i], 0)
            else:
                refine_dataset(i, word[i], 3)

        refine_dataset(i, word[i], word_result[i])


# ----------------------------------------------------------------------------------------------------------------------
#  Validate the input word_result
def validate_result(word_result):
    if word_result in ['c', 'x']:
        return True

    if len(word_result) != 5:
        return False

    for c in word_result:
        if not (c in ['0', '1', '2']):
            return False
    return True


# ----------------------------------------------------------------------------------------------------------------------
# Display the menu
def display_menu():
    cl_green = "\033[92m"
    cl_red = "\033[91m"
    cl_yellow = "\033[93m"
    cl_default = "\033[39m"

    sentences = [
        "Welcome to Vaajoor solver",
        "Instruction",
        "If the letter is in the word and in the correct spot, type 2",
        "If the letter is in the word but in the wrong spot, type 1",
        "If the letter is not in the word in any spot, type 0",
        "For example: $gH$rE$yL$rL$rO$d ->  20100",
        "To change suggestion press $rc$d",
        "To exit press $rx$d",
    ]

    max_len = max([len(s) for s in sentences])
    print("+", max_len * "-", "+")
    for s in sentences:
        # Since I used Ascii color code in string length of string has change. So We should calculate the difference
        no_color = 5 * s.count("$")
        s = s.replace("$d", cl_default).replace("$g", cl_green).replace("$y", cl_yellow).replace("$r", cl_red)
        print("|", s.center(max_len + no_color), "|")
    print("+", max_len * "-", "+")


# ----------------------------------------------------------------------------------------------------------------------
# Main Program

display_menu()
suggest_word = random.choice(words)
result = "00000"
no = 0
while result != "22222":
    print("Suggestion:", suggest_word)
    result = input("Result: ")
    while not validate_result(result):
        print("Result is not valid! Try again. (c for change suggestion an x for exit)")
        result = input("Result: ")
    if result == "x":
        break
    if result == "c":
        suggest_word = random.choice(words)
        continue

    no += 1
    analyze(suggest_word, result)
    suggest_word = random.choice(words)

print(10 * "-")
print("Number of iteration: ", no)
print("Goodbye.")
