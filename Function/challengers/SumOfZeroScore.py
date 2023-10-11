Scores = [200,456,300,100,234,678]

def check_end_zero(number):
    strNumber = str(number)
    if strNumber[len(strNumber)-1] == '0':
        return True
    else:
        return False

def sum_zero_score(scores):
    sum = 0
    for score in scores:
        if check_end_zero(score):
            sum+= score
    return sum

print(sum_zero_score(Scores))
