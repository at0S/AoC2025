def main():
    input = ""
    with open("input", "r") as file:
        input = file.read().strip()

    input = list(input.split("\n"))
    original = 50
    result = 0
    current = 0

    for r in input:
        print(f"At position: {original}, current result: {result}")
        print(f"Processing instruction: {r}")
        tick = r[1:]
        right, left = factor(tick)
        direction = r[0]
        print(f"Moving {direction} by {int(right)} ticks")
        if direction == "L":
            current = original - int(right)
        if direction == "R":
            current = original + int(right)

        print(f"Current unfiltered position: {current}")
        
        if len(left) > 0:
            result = result + int(left)
            print(f"Factoring in {int(left)} for extra zero crossings")

        if current == 0:
            original = 0
            continue

        if current < 0:
            current = current + 100
            result = result + 1
        if current > 99:
            current = current - 100
            result = result + 1

        right, left = None, None
        original = current
        
    print(f"Result: {result}")


def factor(tail, head = ""):
    if len(tail) <= 2:
        return tail, head
    else:
        head = head + tail[0]
        return factor (tail[1:], head)

def changed_sign(before, after):
    if (before * after) < 0:
        return True
    return False

if __name__ == "__main__":
    main()
