# Question Link : https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))

if __name__ == '__main__':
    s = input()
    minion_game(s)
