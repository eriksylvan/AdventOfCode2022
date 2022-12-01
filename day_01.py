# https://adventofcode.com/2022/day/1

inputFile = 'input/01_input'
   
def file2intListDict(file):
    '''Reads file return dictionary with key ind Value int list
    Parameters:
    file: the input file
    Returns:
    list: output as dictionary
    '''
    elfDict = {}
    with open(file) as input:
        elf=1
        elfDict[elf]=[]
        for line in input:
            line = line.strip()
            if line != '':
                elfDict[elf].append(int(line))
            else:
                elf += 1
                elfDict[elf]=[]
                
    return elfDict

def max_calories(e):
    max = 0
    for elf, food in e.items():
        s = sum(food)
        if s > max:
            max = s
    return max
        

def max_3_calories(e):
    cal_list = []
    for elf, food in e.items():
        cal_list.append(sum(food))
    cal_list.sort(reverse=True)
    max3 = sum(cal_list[0:3]) 
    return max3

def day01PartOne():
    input = file2intListDict(inputFile)
    output = max_calories(input)

    print(
        f'# Solution Day 01, Part one:\n# Answer: {output} \n\n')


def day01PartTwo():
    input = file2intListDict(inputFile)
    output =  output = max_3_calories(input)

    

    print(
        f'# Solution Day 01, Part two:\n# Answer: {output} \n\n')
    pass


if __name__ == "__main__":
    day01PartOne()
    day01PartTwo()


# Solution Day 01, Part one:
# Answer: 72478


# Solution Day 01, Part two:
# Answer: 210367


# Run from terminal:
# $ python day_01.py
