
'''https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python'''


def rps(p1, p2):
    match p1+p2:
        case "scissorspaper":
            return "Player 1 won!"
        case "paperscissors":
            return "Player 2 won!"
        case "scissorsrock" :
            return "Player 2 won!"
        case "rockpaper" :
            return "Player 2 won!"
        case "paperrock" :
            return "Player 1 won!"
        case "rockscissors" :
            return "Player 1 won!"
        case "rockrock":
            return "Draw!"
        case "paperpaper":
            return "Draw!"
        case "scissorsscissors":
            return "Draw!"