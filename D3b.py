import re

test = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

def search_chars():
    # with open(file) as game:
    game = test.split('\n')
    num_list = []
    sym_list = []
    for line in game:
        num_list.append([n for n in re.finditer(r'\d{2,3}', line)])
        sym_list.append([a.start() for a in re.finditer(r'\*', line)])
    return num_list, sym_list

def buffer(list: list) -> list:
    list.insert(0, [])
    list.insert(len(list), [])
    return list

def expand_line(list: list, index: int) -> list:
    line = list[line]
    return line

def check_neighbours(target: list, line: int) -> list:
    part_neighbour = []
    for row in range(line , line + 3):
        for num in target[row]:
            part_neighbour.append(num)
    return part_neighbour

def is_neighbour(target: int, check: list) -> list | bool:
    count = 0
    nums = []
    for e in check:
        for indexes in range(e.start(), e.end())
        if e.start() - 1 == target or e.end() + 1 == target:
            count += 1
            nums.append(int(e.group(0)))
    if count == 2:
        # print(nums)
        return nums
    else:
        return False

def gear_ratio(nums: list) -> int:
    ratio = nums[0] * nums[1]
    return ratio
    
def main():
    ttl = 0
    num_list, sym_list = search_chars()
    print(f'This is num list: \n {num_list}\n This is sym list: {sym_list}')
    num_list = buffer(num_list)
    print(f' This is num list: {num_list}')
    for e, _ in enumerate(sym_list):
        print(f'\nCHECKING LINE {e}\n')
        for gear in _:
            if gear:
                nums = check_neighbours(num_list, e)
                print(f'This is neighbour line nums {nums}\n')
                valid = is_neighbour(gear, nums)
                print(valid)
    #             if valid:
    #                 print(valid)
    #                 ttl += gear_ratio(valid)
    print(ttl)

main()