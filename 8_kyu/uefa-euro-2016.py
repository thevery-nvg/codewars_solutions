
'''https://www.codewars.com/kata/57613fb1033d766171000d60/train/python'''


def uefa_euro_2016(teams, scores):
    if scores[0]!=scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[scores.index(max(scores))]} won!"
    else:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."