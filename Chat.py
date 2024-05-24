import json
import re
import random_responses


def load_json(file):
    with open(file,'r') as bot_responses:
        print(f"{file}file is loaded")
        return json.load(bot_responses)


responses_data=load_json("ChatBot.json")

def get_response(input_string):
    split_message=re.split(r'\s+|[,;?!.-]\s*',input_string.lower())
    score_list=[]
    for response in responses_data:
        response_score=0
        required_score=0
        required_words=response["required_words"]

        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score+=1

    
        if required_score==len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score+=1
        

        score_list.append(response_score)
        
    best_response=max(score_list)
    response_index=score_list.index(best_response)

    if input_string=="":
        return "please enter something"
    if best_response!=0:
        return responses_data[response_index]["bot_response"]
    
    if "date" in input_string.lower():
        return random_responses.Date()
    
    return random_responses.random_string()


while True:
    user_input=input("you:")
    print("Bot:", get_response(user_input))
