def get_largest(pack: str) -> tuple[int, int]:
    if len(pack) == 1:
        return (int(pack), 0)
    l = 0
    p = 0
    for pos, char in enumerate(pack):
        curr = int(char)
        if curr > l:
            l = int(char)
            p = pos
    print(f"Pack: {pack} | Largest: {l} at position {p}")
    return (l, p)

def process_pack(pack: str, bb = None) -> int:
    pack_joltage = 0
    largest, position = get_largest(pack)
    if bb is not None:
        pack_joltage = int(str(largest)+str(bb))
        return pack_joltage
    if position < len(pack) - 1:
        largest_in_tail, _ = get_largest(pack[(position+1):])
        pack_joltage = int(str(largest) + str(largest_in_tail))
        print(f"Pack: {pack} | Joltage: {pack_joltage}")
    else:
        pack_joltage=process_pack(pack[:len(pack)-1], largest)

    return pack_joltage

def main():
    raw = []
    with open("input", "r") as f:
        raw = f.read().splitlines()

    result = 0
    for pack in raw:
        result += process_pack(pack)

    print(f"Total joltage: {result}")
        
if __name__ == "__main__":
    main()
