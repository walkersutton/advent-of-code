# AOC 2020 - Day 3

[instructions](https://adventofcode.com/2020/day/3)

> You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
>
> These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
>
> The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

```
..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
```

### Part 1

> Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

### Part 2

> Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
> 
> * Right 1, down 1.
> * Right 3, down 1. (This is the slope you already checked.)
> * Right 5, down 1.
> * Right 7, down 1.
> * Right 1, down 2.
> 
> What do you get if you multiply together the number of trees encountered on each of the listed slopes?
