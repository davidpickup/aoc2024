from collections import defaultdict


def _parse_input(input):
    return [
        item
        for sublist in [
            ["."] * x if i % 2 == 1 else [i // 2] * x
            for i, x in enumerate(map(int, input))
        ]
        for item in sublist
    ]


def part1(input):
    """Reorder the disk so that all files are contiguous and all free space is contiguous.

    File blocks are moved from the end of the disk to the first free space block.
    """
    disk = _parse_input(input)
    i = 0
    j = len(disk) - 1
    while i < j:
        while disk[i] != "." and i < j:
            i += 1
        while disk[j] == "." and i < j:
            j -= 1
        disk[i], disk[j] = disk[j], disk[i]

    return sum(i * block for i, block in enumerate(disk) if block != ".")


def part2(input):
    """Reorder the disk so that all files are contiguous and all free space is contiguous.

    Whole files are moved from the end of the disk to the first free space block that is large enough.
    """
    disk = _parse_input(input)
    max_file = max([x for x in disk if x != "."])

    for file_index in range(max_file, 0, -1):
        file_size = disk.count(file_index)
        file_pos = disk.index(file_index)
        i = 0
        while disk[i] != file_index:
            while disk[i] != "." and disk[i] != file_index:
                i += 1
            j = i + 1
            while j < len(disk) and disk[j] == ".":
                j += 1
            if j - i >= file_size:
                disk[file_pos:file_pos + file_size] = ["."] * file_size
                disk[i:i+file_size] = [file_index] * file_size
                break
            i = j
        
    return sum(i * block for i, block in enumerate(disk) if block != ".")


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
