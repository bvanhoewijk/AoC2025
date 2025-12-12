# Advent of Code 2025

Repository for storing the code for [Advent of Code 2025](https://adventofcode.com/2025). Previous years: [2024](https://github.com/bvanhoewijk/AoC2024), [2023](https://github.com/bvanhoewijk/AoC2023).

Rules I impose on myself:
1. Code must not be generated via A.I.
2. When I get stuck for a prolonged amount of time, I can go to reddit for help for hints. But I am not allowed to copy-paste code.
3. Same goes for YouTube. 

Goal is to solve fun programming exercises to improve my coding skills.

---

New things learned:
- Look-ahead regex
- Merging interval ranges
- Working with polygons
- Memoized DFS
--- 

Total stars: 22/24: Everything except Day 10 Part 2! Quite happpy with the result and I learned a couple of new things!


## Day 12: ⭐
- [x] Part 1: Sum (Area of presents < Area of placement). The creator could have made this one much more complicated.
- [x] Part 2: N/A

## Day 11: ⭐⭐
- [x] Part 1: Simple DFS
- [x] Part 2: Took a hint from Reddit for this one: *Memoized DFS* where the key is "next node", dac == seen and fft == seen. 

## Day 10: ⭐
- [x] Part 1: Transform the input to boolean lists/tuples and xor. Next; try all `combinations` of `n` buttons.
- [ ] Part 2: I have no clue on how to even start with this.

## Day 09: ⭐⭐
- [x] Part 1: Part 1 was trivial
- [x] Part 2: For part 2 I first tried to do connect the path to create the polygon positions and then floodfill the outside, which was the wrong approach as it took way too long. I also tried raytracing, to find intersections, but also too slow. Finally, I ended up using `shapely.geometry` with `Polygon` and `box` objects and used `polygon.contains(rectangle)`.

## Day 08: ⭐⭐
- [x] Part 1: Reading is hard. Used itertools.combinations to get all pairs. Then I sort that list and process and merge the first 1000 combinations/nodes.
- [x] Part 2: Merge until there is only one merged node. 

## Day 07: ⭐⭐
- [x] Part 1: BFS
- [x] Part 2: BFS was not going to work. I could have tried memoization, but ended up with a "Pascals" triangle kind of approach by summing the possible paths given the previous score.

## Day 06: ⭐⭐
- [x] Part 1: Parse text file and iterate over the columns
- [x] Part 2: Solved by transposing and cutting the dataset in blocks and process those.

## Day 05: ⭐⭐
- [x] Part 1: Find item in interval range
- [x] Part 2: Merge interval ranges

## Day 04: ⭐⭐
- [x] Part 1: loop through coordinates. Trick was not to loop through the grid.
- [x] Part 2: loop through coordinates with While loop. I found this one way easier than Part 2 of yesterday.

## Day 03: ⭐⭐
- [x] Part 1: argmax
- [x] Part 2: Very difficult with argmax in a sliding window. I needed help from reddit for this one. 

## Day 02: ⭐⭐
- [x] Part 1: Slice and compare
- [x] Part 2: look-ahead regex

## Day 01: ⭐⭐
- [x] Part 1: Rotating of dials. Solved by modulo.
- [x] Part 2: Rotating of dials. Solved by modulo + integer division `//` + offset.