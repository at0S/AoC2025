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

    matrix = []

    for line, data in enumerate(lines):
        matrix.append([])
        for char in data:
            matrix[line].append(char)

    total_count = 0
    run = True

    while run:
        accessable_count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if check_field(matrix, i, j) == True:
                    matrix[i][j] = "."
                    accessable_count += 1
        if accessable_count == 0:
            run = False
        total_count += accessable_count


    print(total_count)

if __name__ == "__main__":
    main()
