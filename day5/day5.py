from collections import namedtuple

Instruction = namedtuple('Instruction', ['op', 'argc', 'outa', 'name', 'func'])


class IntcodeVM(object):
    def __init__(self, ram, debug):
        self.ram = ram
        self.ip = 0
        self.debug = debug
        self.opcodes = { 1: Instruction(op=1, argc=3, outa=[2], name='ADD', func=self.add),
                    2: Instruction(op=2, argc=3, outa=[2], name='MULT', func=self.mult),
                    3: Instruction(op=3, argc=1, outa=[0], name='IN', func=self.inpt),
                    4: Instruction(op=4, argc=1, outa=[], name='OUT', func=self.outpt),
                    5: Instruction(op=5, argc=2, outa=[], name='J_IF_TRUE', func=self.jump_true),
                    6: Instruction(op=6, argc=2, outa=[], name='J_IF_FALSE', func=self.jump_false),
                    7: Instruction(op=7, argc=3, outa=[2], name='LESS_THAN', func=self.less_than),
                    8: Instruction(op=8, argc=3, outa=[2], name='EQUALS', func=self.equals),
                    99: Instruction(op=99, argc=0, outa=[], name='HALT', func=self.halt)}
    def run(self):
        halt = False
        while not halt:
          if self.debug:
              print(f'ip = {self.ip}')
          halt = self.run_instr()
        print("Halted!")
    def parse_opcode(self, op):
        all = '{:05d}'.format(op)
        opcode = int(all[3:])
        modes = [int(all[2:3]), int(all[1:2]), int(all[0:1])]
        return (opcode, modes)
    def run_instr(self):
        op, modes = self.parse_opcode(self.ram[self.ip])
        assert op in self.opcodes.keys()
        instr = self.opcodes[op]
        args = []
        orig_ip = self.ip
        for x in range(instr.argc):
            arg = self.ram[self.ip+x+1]
            val = arg if modes[x] or x in instr.outa else self.ram[arg]
            args.append(val)
        if self.debug:
            print(f'op {instr.op}: {instr.name} {args}')
        instr.func(args)
        if self.ip == orig_ip:
            self.ip += instr.argc+1
        if self.ip < 0:
            return True
        return False

    def add(self, args):
        self.ram[args[2]] = args[0] + args[1]

    def mult(self, args):
        self.ram[args[2]] = args[0] * args[1]

        return None
    def inpt(self, args):
        self.ram[args[0]] = int(input("Input:"))

    def outpt(self, args):
        print(F'Output: {args[0]}')

    def jump_true(self, args):
        if args[0] != 0:
            self.ip = args[1]

    def jump_false(self, args):
        if args[0] == 0:
            self.ip = args[1]

    def less_than(self, args):
        if args[0] < args[1]:
            self.ram[args[2]] = 1
        else:
            self.ram[args[2]] = 0

    def equals(self, args):
        if args[0] == args[1]:
            self.ram[args[2]] = 1
        else:
            self.ram[args[2]] = 0

    def halt(self, args):
        self.ip = -1


with open('input.txt', 'r') as fp:
    line = fp.readline()
    ram = [int(x) for x in line.split(',')]
    vm = IntcodeVM(ram, debug=True)
    vm.run()
