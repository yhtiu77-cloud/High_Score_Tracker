import json

hight_scorelist = list()



try:
    with open("highscore.json","r") as f:
        hightscore_info = json.load(f)
        hight_scorelist = hightscore_info
except:
    print("A hight score has not been created yet")
    answer = input("Do you wish to create one? ").lower()
    if answer == "yes":
        with open("highscore.json", "w") as f:
            json.dump(hight_scorelist, f)


while True:
    user_choice = input("1-to add new score, 2-to change an existing one, 3- to quit")
    if user_choice == "1":
        name = input("What is the name of the person?")
        score = int(input("what is the score of the person?"))
        new_dict = {"name" : name, "score" : score}
        hight_scorelist.append(new_dict)
    elif user_choice == "2":
        player_choice = input("Whose player do you want to change the score?")
        for i in hight_scorelist:
            if player_choice == i["name"]:
                new_score = int(input("what do you want his new score to be?"))
                i["score"] = new_score
    elif user_choice == "3":
        with open("highscore.json", "w") as f:
            json.dump(hight_scorelist, f)
        break

print(hight_scorelist)



   
