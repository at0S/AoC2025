def get_largest(slice: str) -> tuple[int, int]:
    if len(slice) == 0:
        print("Empty slice | Largest: 0 at position 0")
        return (0, 0)
    if len(slice) == 1:
        print(f"slice {slice}| Largest: {int(slice)} at position 0")
        return (int(slice), 0)
    l = 0
    p = 0
    for pos, char in enumerate(slice):
        curr = int(char)
        if curr > l:
            l = int(char)
            p = pos
    print(f"slice: {slice} | Largest: {l} at position {p}")
    return (l, p)

def process_pack(pack: str) -> int:
    current_pack = pack
    pack_joltage = 0
    str_repr = ""
    iters = 12 
    while iters > 0:
        largest, position = get_largest(current_pack[0:len(current_pack)-iters+1])
        str_repr += str(largest)
        iters -= 1
        current_pack = current_pack[position+1:]
        print(f"Current pack: {current_pack}")
    pack_joltage = int(str_repr)
    print(f"Processed pack: {pack} to joltage: {pack_joltage}")
    return pack_joltage

def main():
    # day 2 considerations:
    # - for the first day, the boundary was that the larget digit should not be the last.
    # - for the second day, the largest digit cant be at  (last - eleven)
    # - we don't check input, does not matter
    # - we need to find the larget element in [0:pack_length-12]
    # - we need to register the largets elements position. We will cut the pack [postion+1:]
    # - we then will do the same to the tail - find the largest element, it should not be the la
    with open("input", "r") as f:
        raw = f.read().splitlines()

    result = 0
    for pack in raw:
        result += process_pack(pack)

    print(f"Total joltage: {result}")
        
if __name__ == "__main__":
    main()
