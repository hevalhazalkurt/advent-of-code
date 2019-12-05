# Advent of Code 2019
# Day 2 : 1202 Program Alarm


# Part 1

memory = open('input.txt', 'r').read().split(",")
opcodes = [int(code) for code in memory]

opcodes[1] = 12
opcodes[2] = 2

for pos in range(0,len(opcodes),4):
    if opcodes[pos] == 99:
        break
    elif opcodes[pos] == 1:
        first, second, result = opcodes[pos+1:pos+4]
        opcodes[result] = opcodes[first] + opcodes[second]
    elif opcodes[pos] == 2:
        first, second, result = opcodes[pos+1:pos+4]
        opcodes[result] = opcodes[first] * opcodes[second]

print(opcodes[0])



# Part 2

def one(codelist, noun, verb):
    codelist = list(codelist)
    codelist[1] = noun
    codelist[2] = verb
    i = 0
    while i < len(codelist):
        pos = codelist[i]
        if codelist[i+1] > len(codelist) or codelist[i+2] > len(codelist) or codelist[i+3] > len(codelist):
            return 0
        if pos == 99:
            break
        elif pos == 1:
            codelist[codelist[i+3]] = codelist[codelist[i+1]] + codelist[codelist[i+2]]
        elif pos == 2:
            codelist[codelist[i+3]] = codelist[codelist[i+1]] * codelist[codelist[i+2]]
        i += 4

    return codelist[0]

def two(codelist):
    for noun in range(0,100):
        for verb in range(0,100):
            if one(codelist, noun, verb) == 19690720:
                return (100 * noun + verb)

memory = open('input.txt', 'r').read().split(",")
opcodes = [int(code) for code in memory]


print(two(opcodes))
