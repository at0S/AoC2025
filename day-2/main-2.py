import re

def main():
    raw=""
    with open("input", "r") as file:
        raw = file.read()

    ranges = []
    result = 0
    dodgy_re = re.compile(r"(.+)(\1+)")
    ranges = raw.split(",")

    for r in ranges:
        l_bound, r_bound = r.split("-")

        l = int(l_bound.strip())
        r = int(r_bound.strip()) 

        for value in range(l, r + 1):
            str_repr = str(value)
            if dodgy_re.fullmatch(str_repr):
                print(f"found dodgy number: {str_repr}")
                result += value
       #     len_str = len(str_repr)
       #     l_slice = str_repr[0:len_str//2]
       #     r_slice = str_repr[-1 * len_str//2:]
       #     if len_str >= 2:
       #         if l_slice == r_slice:
       #             print(f"found dodgy number: {str_repr}")
       #             result += value
       
       # Continue to extra id verification logic




    print(f"Result: {result}")

if __name__ == "__main__":
    main()
