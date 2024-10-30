
#the 'float and int' is just for documentation on what to expect from input

def get_percent(score:float, total_score:float = 100):
    score_in_percent = (score/total_score) * 100
    return score_in_percent

get_percent(20)