# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/solutions/python?filter=me&sort=best_practice&invalids=false
def rps(player1: str, player2: str) -> str:
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    if player2 == player1:
        return "Draw!"
    return "Player 1 won!" if beats[player1] == player2 else "Player 2 won!"


if __name__ == '__main__':
    print(rps(*input('введите результат через пробел:\n').split()))
    print(rps('scissors', 'rock'))
    print(rps('paper', 'rock'))
    print(rps('rock', 'scissors'))
    print(rps('rock', 'rock'))
