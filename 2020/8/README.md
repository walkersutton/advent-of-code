# AOC 2020 - Day 8

[instructions](https://adventofcode.com/2020/day/8)

### Part 1

> * acc increases or decreases a single global value called the accumulator by the value given in the argument.
> * jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction.
> * nop does nothing. The instruction immediately below it is executed next.
> 
> This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.
> 
> Immediately before any instruction is executed a second time, what value is in the accumulator?

### Part 2

> Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
>
> Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
