import json
points = 0
current_answer = ""


def show_question(question):
    global points
    global current_answer
    current_answer = ""
    while current_answer != 'a' and current_answer != "b" and current_answer != "c" and current_answer != "d":
        print()
        print(question["question"])
        print('a:', question["a"])
        print('b:', question["b"])
        print('c:', question["c"])
        print('d:', question["d"])
        print()
        current_answer = input("Select answer: ")
        print()
        if current_answer == question["correct_answer"]:
            points += 1
            print("Answer correct!")
        else:
            print("Wrong answer :(")


with open("questions.json") as json_file:
    questions = json.load(json_file)
    for i in range(0, len(questions)):
        show_question(questions[i])
print("Quiz completed")
print("Your score is:", points, "points")
