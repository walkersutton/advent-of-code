# AOC 2020 - Day 5

[instructions](https://adventofcode.com/2020/day/5)

### Part 1

> The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
>
> The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
>
> What is the highest seat ID on a boarding pass?

### Part 2

> It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
>
> Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
>
> What is the ID of your seat?
