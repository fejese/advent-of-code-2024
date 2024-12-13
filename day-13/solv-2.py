#!/usr/bin/env python3

from dataclasses import dataclass


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


@dataclass
class C:
    x: int
    y: int


@dataclass
class Machine:
    a: C
    b: C
    p: C


def parse_machine(machine: str) -> Machine:
    astr, bstr, pstr = machine.strip().splitlines()
    a = C(*[int(x.split("+")[1].strip()) for x in astr.split(":")[1].split(",")])
    b = C(*[int(x.split("+")[1].strip()) for x in bstr.split(":")[1].split(",")])
    p = C(
        *[10000000000000 + int(x.split("=")[1]) for x in pstr.split(":")[1].split(",")]
    )
    return Machine(a=a, b=b, p=p)


def solve(m: Machine) -> int:
    cost_a = 3
    cost_b = 1

    if m.p.x % m.b.x == 0:
        count_b = m.p.x / m.b.x
        if count_b * m.b.y == m.p.y:
            return int(count_b * cost_b)

    count_b = int((m.p.x * m.a.y - m.p.y * m.a.x) / (m.b.x * m.a.y - m.b.y * m.a.x))
    count_a = int((m.p.x - count_b * m.b.x) / m.a.x)
    if (count_b * m.b.y + count_a * m.a.y) != m.p.y:
        # print("-")
        return 0
    if (count_b * m.b.x + count_a * m.a.x) != m.p.x:
        # print("-")
        return 0

    result = count_a * cost_a + count_b * cost_b
    # print(result)
    return result


with open(INPUT_FILE_NAME, "r") as input_file:
    result = sum(
        solve(parse_machine(machine)) for machine in input_file.read().split("\n\n")
    )

print("final:", result)
