def update_light(current: str) -> str:
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]

    # light = ['green', 'yellow', 'red', 'green']
    # return light[light.index(current) + 1]


if __name__ == '__main__':
    print(update_light('red'))

    assert update_light('green') == 'yellow'
    assert update_light('yellow') == 'red'
    assert update_light('red') == 'green'
