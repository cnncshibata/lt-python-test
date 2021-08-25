def add_3(x: int) -> int:
    return x + 3

def div_int(x: int, y: int) -> int:
    return x // y

def grade(score: int) -> str:
    if score < 0:
        raise Exception()
    elif score < 40:
        return 'C'
    elif score < 60:
        return 'B'
    elif score < 80:
        return 'A'
    elif score <= 100:
        return 'S'
    else:
        raise Exception()
