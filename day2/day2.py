ram = []

def runopcode(op, args):
    if op == 99:
        return True
    if op == 1:
        ram[args[2]] = ram[args[0]] + ram[args[1]]
        return False
    if op == 2:
        ram[args[2]] = ram[args[0]] * ram[args[1]]
        return False
    print(f'No opcode found! {op}')
    return True


with open('input.txt', 'r') as fp:
    line = fp.readline()
    ram = [int(x) for x in line.split(',')]
    orig_ram = ram.copy()
    breakme = False
    for ram1 in range(0, 100):
        for ram2 in range(0, 100):
            print(f'trying {ram1} {ram2}')
            ram = orig_ram.copy()
            ram[1] = ram1
            ram[2] = ram2

            halt = False
            pc = 0
            while not halt:
              halt = runopcode(ram[pc], ram[pc+1:])
              pc += 4
            if ram[0] == 19690720:
                print(f'found! {ram1} {ram2}')
                output = 100 * ram1 + ram2
                print(f'output {output}')
                breakme = True
                break
        if breakme:
            break
