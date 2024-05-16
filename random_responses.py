import random
import datetime

def random_string():
    random_list=[
        "Hey try to elaborate properly",
        "It seems to be incomplete input",
        "Uhh! I'm sorry I couldn't understand it properly",
        "please try to rephrase that",
        "I can't understand"
    ]
    list_count=len(random_list)
    random_item=random.randrange(list_count)
    return random_list[random_item]

def Date():
    return str(datetime.date.today())+" "+"is today's date in yyyy-mm-dd format"

