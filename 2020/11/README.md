# AOC 2020 - Day 11

[instructions](https://adventofcode.com/2020/day/11)

### Part 1

> The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#).
> 
> * If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
> * If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
> * Otherwise, the seat's state does not change.
> 
> Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

### Part 2

> Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions.
>
> It now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.
>
> Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
