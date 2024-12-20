FREE_SPACE = '.'


def compress_disk_space_part1():
    with open('part1-input.txt', 'r') as input_file:
        disk_map = input_file.read().strip()

    # Generate disk space representation
    disk_space = []
    for index, block in enumerate(disk_map):
        if index % 2 == 0:  # File block
            file_id = index // 2
            for _ in range(int(block)):
                disk_space.append(str(file_id))
        else:  # Free space
            for _ in range(int(block)):
                disk_space.append(FREE_SPACE)

    # Compress the disk space
    left, right = 0, len(disk_space) - 1
    while left < right:
        while left < len(disk_space) and disk_space[left] != FREE_SPACE:
            left += 1
        while right >= 0 and disk_space[right] == FREE_SPACE:
            right -= 1
        if left > right:
            break
        # Swap file block with free space
        disk_space[left], disk_space[right] = disk_space[right], disk_space[left]
        left += 1
        right -= 1

    # Calculate filesystem checksum
    filesystem_checksum = 0
    for index, block in enumerate(disk_space):
        if block != FREE_SPACE:
            filesystem_checksum += int(block) * index
    return filesystem_checksum


def compress_disk_space_part2():
    with open('part2-input.txt', 'r') as input_file:
        disk_map = input_file.read().strip()

    # Parse the disk map into blocks
    disk_space = []
    free_spaces = []  # (start_index, length)
    file_blocks = []  # (file_id, start_index, length)

    start = 0
    for index, block in enumerate(disk_map):
        if index % 2 == 0:  # File block
            file_id = index // 2
            for _ in range(int(block)):
                disk_space.append(str(file_id))
            if int(block) > 0:
                file_blocks.append((file_id, start, int(block)))
        else:  # Free space
            for _ in range(int(block)):
                disk_space.append(FREE_SPACE)
            if int(block) > 0:
                free_spaces.append((start, int(block)))
        start += int(block)

    # Sort files by descending file ID
    file_blocks.sort(reverse=True, key=lambda x: x[0])
    # Sort free spaces by starting index to ensure we use the leftmost free space
    free_spaces.sort()

    # Compact files
    for file_id, file_start, file_length in file_blocks:
        for free_space_index, (free_space_start, free_space_length) in enumerate(free_spaces):
            if free_space_length >= file_length and free_space_start < file_start:
                # Move file to the free space
                for i in range(file_length):
                    disk_space[free_space_start + i] = disk_space[file_start + i]
                    disk_space[file_start + i] = FREE_SPACE

                # Update free space list
                free_spaces[free_space_index] = (free_space_start + file_length, free_space_length - file_length)
                if free_space_length - file_length == 0:
                    free_spaces.pop(free_space_index)
                free_spaces.append((file_start, file_length)) # we add file_start and file_length, because, free spaces
                break

    # Calculate checksum
    checksum = 0
    for index, block in enumerate(disk_space):
        if block != FREE_SPACE:
            checksum += int(block) * index

    return checksum


if __name__ == '__main__':
    print(compress_disk_space_part2())
