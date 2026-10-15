MAZE = [
    '###################',
    '#........#.......#',
    '#.###.#.#.#.###.#.#',
    '#...#.#.#.#...#.#.#',
    '###.#...#...#.#.#.#',
    '#...###.###.#...#.#',
    '#.###.....#.#.###.#',
    '#...#.#.#.#...#...#',
    '###.#.#.#.###.#.#.#',
    '#...#...#...#.#...#',
    '#.#####.###.#.###.#',
    '#.............#...#',
    '###################',
]
rev = [row[::-1] for row in MAZE]
with open('maze_rows.txt', 'w', encoding='utf-8') as f:
    f.write('ORIGINAL\n')
    for row in MAZE:
        f.write(row + '\n')
    f.write('REVERSED\n')
    for row in rev:
        f.write(row + '\n')
print('wrote maze_rows.txt')
