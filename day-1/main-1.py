def main():
    input = ""
    with open("input", "r") as file:
        input = file.read().strip()

    input = list(input.split("\n"))
    current = 50
    result = 0
    chunk = -1

    for r in input:
        if len(r) > 2:
            chunk = -2
        direction = r[0]
        tick = r[1:]
        if isinstance(int(r[1:]), int):
            if direction == 'R':
                current = current + int(tick[chunk:])
            if direction == 'L':
                current = current - int(tick[chunk:])
        if current > 99:
            current = current - 100
        if current < 0:
            current = current + 100
        
        if current == 0:
            result = result + 1  

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
