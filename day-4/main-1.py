def check_field(matrix, row, col):
    roll_counter = 0
    if matrix[row][col] == ".":
        return False
    if matrix[row][col] == "@":
        if row !=0:
            if matrix[row-1][col] == "@":
                roll_counter += 1
        if row != len(matrix)-1:
            if matrix[row+1][col] == "@":
                roll_counter += 1
        if col !=0:
            if matrix[row][col-1] == "@":
                roll_counter += 1
        if col != len(matrix[0])-1:
            if matrix[row][col+1] == "@":
                roll_counter += 1

        if col !=0 and row !=0:
            if matrix[row-1][col-1] == "@":
                roll_counter += 1

        if col != len(matrix[0])-1 and row !=0:
            if matrix[row-1][col+1] == "@":
                roll_counter += 1

        if col !=0 and row != len(matrix)-1:
            if matrix[row+1][col-1] == "@":
                roll_counter += 1

        if col != len(matrix[0])-1 and row != len(matrix)-1:
            if matrix[row+1][col+1] == "@":
                roll_counter += 1

    if roll_counter < 4:
        return True
    return False

def main():
    raw=""
    with open("input", "r") as f:
        raw = f.read()

    lines = raw.strip().split("\n")

    print(lines)

    matrix = []

    for line, data in enumerate(lines):
        matrix.append([])
        for char in data:
            matrix[line].append(char)

    accessable_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"Checking: [{i}][{j}]: {check_field(matrix, i, j)}")
            if check_field(matrix, i, j) == True:
                accessable_count += 1
    print(accessable_count)

if __name__ == "__main__":
    main()
