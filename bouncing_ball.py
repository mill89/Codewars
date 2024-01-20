def bouncing_ball(h: int, bounce: float, window: float) -> int:
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    count = 1

    while h * bounce > window:
        h *= bounce
        count += 2
    return count


# def bouncingBall(h, bounce, window):
#     seen = -1
#
#     if 0 < bounce < 1:
#         while h > window > 0:
#             seen += 2
#             h *= bounce
#
#     return seen


if __name__ == '__main__':
    print(bouncing_ball(3, 0.66, 1.5))  # Output: 3
    print(bouncing_ball(3, 1, 1.5))  # Output: -1

    assert bouncing_ball(2, 0.5, 1) == 1
    assert bouncing_ball(3, 0.66, 1.5) == 3
    assert bouncing_ball(30, 0.66, 1.5) == 15
    assert bouncing_ball(30, 0.75, 1.5) == 21
