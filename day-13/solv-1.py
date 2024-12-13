#!/usr/bin/env python3

from dataclasses import dataclass


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


@dataclass
class Machine:
    a: complex
    b: complex
    p: complex


def parse_machine(machine: str) -> Machine:
    astr, bstr, pstr = machine.strip().splitlines()
    a = complex(*[int(x.split("+")[1].strip()) for x in astr.split(":")[1].split(",")])
    b = complex(*[int(x.split("+")[1].strip()) for x in bstr.split(":")[1].split(",")])
    p = complex(*[int(x.split("=")[1]) for x in pstr.split(":")[1].split(",")])
    return Machine(a=a, b=b, p=p)


def solve(m: Machine) -> int:
    cost_a = 3
    cost_b = 1

    for count_b in range(int(m.p.real // m.b.real), -1, -1):
        if (remainder := (m.p.real - m.b.real * count_b)) % m.a.real != 0:
            continue

        count_a = remainder / m.a.real
        if (count_b * m.b.imag + count_a * m.a.imag) != m.p.imag:
            continue

        return int(count_a * cost_a + count_b * cost_b)

    return 0


with open(INPUT_FILE_NAME, "r") as input_file:
    result = sum(
        solve(parse_machine(machine)) for machine in input_file.read().split("\n\n")
    )

print(result)
