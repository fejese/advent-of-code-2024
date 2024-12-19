#!/usr/bin/env python3

from collections import defaultdict
from typing import DefaultDict, List

# INPUT_FILE_NAME: str = "test-input-b"
INPUT_FILE_NAME: str = "input"


class Machine:
    @staticmethod
    def from_file(input_file_name: str) -> "Machine":
        with open(input_file_name, "r") as input_file:
            reg_a = int(input_file.readline().strip().split(" ")[-1])
            reg_b = int(input_file.readline().strip().split(" ")[-1])
            reg_c = int(input_file.readline().strip().split(" ")[-1])
            input_file.readline()
            program = [
                int(instr)
                for instr in input_file.readline().strip().split(" ")[1].split(",")
            ]
        return Machine(reg_a, reg_b, reg_c, program)

    def __init__(self, reg_a: int, reg_b: int, reg_c: int, program: List[int]) -> None:
        self.reg_a = self._reg_a = reg_a
        self.reg_b = self._reg_b = reg_b
        self.reg_c = self._reg_c = reg_c
        self.program = program
        self.ins_ptr: int = 0
        self.outputs: List[int] = []
        # self.report()

    def reset(self, reg_a: int) -> "Machine":
        self.reg_a = reg_a
        self.reg_b = self._reg_b
        self.reg_c = self._reg_c
        self.ins_ptr = 0
        self.outputs = []
        return self

    def report(self) -> None:
        print(f"{self.reg_a=}")
        print(f"{self.reg_b=}")
        print(f"{self.reg_c=}")
        print(f"{self.program=}")
        print(f"{self.ins_ptr=}")
        print(f"{self.outputs=}")
        print()

    def get_op(self) -> int:
        return self.program[self.ins_ptr + 1]

    def get_combo_op(self) -> int:
        combo_op = self.get_op()
        if 0 <= combo_op <= 3:
            return combo_op
        elif combo_op == 4:
            return self.reg_a
        elif combo_op == 5:
            return self.reg_b
        elif combo_op == 6:
            return self.reg_c
        else:
            raise ValueError(f"Invalid combo_op: {combo_op}")

    def run(self) -> None:
        while self.ins_ptr < len(self.program):
            instr = self.program[self.ins_ptr]
            # print(f"{ins_ptr=}, {instr=}")
            if instr == 0:  # adv
                op = self.get_combo_op()
                self.reg_a = self.reg_a // (2**op)
                self.ins_ptr += 2
            elif instr == 1:  # bxl
                op = self.get_op()
                self.reg_b = self.reg_b ^ op
                self.ins_ptr += 2
            elif instr == 2:  # bst
                op = self.get_combo_op()
                self.reg_b = op % 8
                self.ins_ptr += 2
            elif instr == 3:  # jnz
                if self.reg_a == 0:
                    self.ins_ptr += 2
                else:
                    op = self.get_op()
                    self.ins_ptr = op
            elif instr == 4:  # bxc
                self.reg_b = self.reg_b ^ self.reg_c
                self.ins_ptr += 2
            elif instr == 5:  # out
                op = self.get_combo_op()
                self.outputs.append(op % 8)
                self.ins_ptr += 2
            elif instr == 6:  # bdv
                op = self.get_combo_op()
                self.reg_b = self.reg_a // (2**op)
                self.ins_ptr += 2
            elif instr == 7:  # cdv
                op = self.get_combo_op()
                self.reg_c = self.reg_a // (2**op)
                self.ins_ptr += 2

            # self.report()

    @property
    def output_str(self) -> str:
        return ",".join(str(n) for n in self.outputs)


machine = Machine.from_file(INPUT_FILE_NAME)
solutions_by_matching_suffix_length = defaultdict(set)
solutions_by_matching_suffix_length[0] = {0}

for suffix_match_len in range(1, len(machine.program) + 1):
    for prev in solutions_by_matching_suffix_length[suffix_match_len - 1]:
        for delta in range(8):
            reg_a_override = (prev << 3) + delta
            # print(f"{reg_a_override=} {machine.outputs=}")
            machine.reset(reg_a_override)
            machine.run()
            if len(machine.outputs) == suffix_match_len and machine.outputs == machine.program[-suffix_match_len:]:
                solutions_by_matching_suffix_length[suffix_match_len].add(reg_a_override)

print(min(solutions_by_matching_suffix_length[len(machine.program)]))
