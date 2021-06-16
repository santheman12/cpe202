# Name:         San Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Winter 2021

import random
from typing import List, Tuple


class PuzzleState:  # do not modify

    def __init__(self, tiles: Tuple[int, ...], path: str) -> None:
        self.tiles = tiles
        self.width = int(len(tiles) ** 0.5)
        self.path = path

    def __eq__(self, other: "PuzzleState") -> bool:
        return self.tiles == other.tiles and self.path == other.path

    def __repr__(self) -> str:
        return self.path


def make_adjacent(state: PuzzleState) -> List[PuzzleState]:
    """
    Return a list of PuzzleState objects that represent valid, non-opposing
    moves from the given PuzzleState. A move is considered valid if it moves a
    tile adjacent to the blank tile into the blank tile. A move is considered
    non-opposing if it does not undo the previous move.

    >>> state = PuzzleState((3, 2, 1, 0), "")
    >>> make_adjacent(state)
    [PuzzleState((3, 0, 1, 2), "J"), PuzzleState((3, 2, 0, 1), "L")]
    """

    #result = []

    for i in range(len(state.tiles)):
        if state.tiles[i] == 0:
            zero = i

    # middle

    if zero % state.width == 1 and state.width != 2:
        result = middle(state, zero)

    # r_col

    if zero % state.width == (state.width-1):
        result = r_col(state, zero)

    if zero % state.width == 0:
        result = l_col(state, zero)

    #print(result[0].tiles)
    #print(result[1].tiles)
    #print(result)

    return result


def l_col(state: PuzzleState, zero: int) -> List[PuzzleState]:
    temp_state = state
    result_list = []

    for i in range(len(state.tiles)):
        if state.tiles[i] == 0:
            zero = i

    if len(state.path) > 0:
        move = state.path[-1]
    else:
        move = ''

    if move != 'L':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero + 1] = \
            temp_list[zero + 1], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list),
                                       temp_state.path + 'H'))
        temp_state = state

    if zero - temp_state.width >= 0 and move != 'K':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero - temp_state.width] = \
            temp_list[zero - temp_state.width], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'J'))
        temp_state = state

    if len(temp_state.tiles) > zero + temp_state.width and move != 'J':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero + temp_state.width] = \
            temp_list[zero + temp_state.width], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'K'))
        temp_state = state

    return result_list


def r_col(state: PuzzleState, zero: int) -> List[PuzzleState]:
    temp_state = state
    result_list = []

    for i in range(len(state.tiles)):
        if state.tiles[i] == 0:
            zero = i

    if len(state.path) > 0:
        move = state.path[-1]
    else:
        move = ''

    if zero - temp_state.width >= 0 and move != 'K':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero - temp_state.width] = \
            temp_list[zero - temp_state.width], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'J'))
        temp_state = state

    if len(temp_state.tiles) > zero + temp_state.width and move != 'J':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero + temp_state.width] = \
            temp_list[zero + temp_state.width], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'K'))
        temp_state = state

    if move != 'H':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero - 1] = \
            temp_list[zero - 1], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'L'))
        temp_state = state

    return result_list


def middle(state: PuzzleState, zero: int) -> List[PuzzleState]:
    temp_state = state
    result_list = []

    if len(state.path) > 0:
        move = state.path[-1]
    else:
        move = ''

    if move != 'L':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero + 1] = \
            temp_list[zero + 1], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'H'))
        temp_state = state

    if zero - temp_state.width >= 0 and move != 'K':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero - temp_state.width] = \
            temp_list[zero - temp_state.width], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'J'))
        temp_state = state

    if len(temp_state.tiles) > zero + temp_state.width and move != 'J':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero + temp_state.width] = \
            temp_list[zero + temp_state.width], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'K'))
        temp_state = state

    if move != 'H':
        temp_list = list(temp_state.tiles)
        temp_list[zero], temp_list[zero - 1] = \
            temp_list[zero - 1], temp_list[zero]
        result_list.append(PuzzleState(tuple(temp_list), temp_state.path + 'L'))
        temp_state = state

    print(result_list)
    for i in result_list:
        print(i.tiles)
    return result_list


def is_solvable(tiles: Tuple[int, ...]) -> bool:
    """
    Return a Boolean indicating whether the given tuple represents a solvable
    puzzle. Use the Merge Sort algorithm (possibly in a helper function) to
    efficiently count the number of inversions.

    >>> is_solvable((3, 2, 1, 0))
    True
    >>> is_solvable((0, 2, 1, 3))
    False
    """

    if len(tiles) < 4:
        return False

    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, (len(tiles))):
            if tiles[j] != 0:
                if tiles[i] > tiles[j]:
                    inversions += 1

    width = len(tiles) ** 0.5

    print(inversions)

    if width % 2 != 0:
        return inversions % 2 == 0
    else:
        if (tiles.index(0) // width) % 2 == 0:
            print('hi')
            return inversions % 2 == 0

        else:
            return inversions % 2 != 0


def solve_puzzle(tiles: Tuple[int, ...]) -> str:
    """
    Return a string (containing characters "H", "J", "K", "L") representing the
    optimal number of moves to solve the given puzzle using Uniform Cost Search.
    A state is considered a solution if its tiles are sorted.

    >>> solve_puzzle((3, 2, 1, 0))
    "JLKHJL"
    """
    path = ''
    queue = []
    while count_inversions(tiles, len(tiles)) != 0:
        temp_puzzle = make_adjacent(PuzzleState(tiles, path))
        for i in temp_puzzle:
            queue.append(i)
        temp_first = queue.pop(0)
        tiles = temp_first.tiles
        path = temp_first.path
        #print(count_inversions(tiles, len(tiles)))

    #while count != 0:
        #print('hi')
        #count =

    #print('hi')
    #print(path)
    print(path)
    return path


def count_inversions(tiles: Tuple[int, ...], size: int) -> int:
    inv_count = 0
    for i in range(size):
        for j in range(i+1, size):
            if tiles[i] > tiles[j] and j > i:
                inv_count += 1

    print(inv_count)
    return inv_count


def main() -> None:
    random.seed(int(input("Random Seed: ")))
    tiles = list(range(int(input("Puzzle Width: ")) ** 2))  # use 2 or 3
    random.shuffle(tiles)
    print("Tiles:", "[", " ".join(str(t) for t in tiles), "]")
    if not is_solvable(tuple(tiles)):
        print("Unsolvable")
    else:
        print("Solution:", solve_puzzle(tuple(tiles)))


if __name__ == "__main__":
    main()
