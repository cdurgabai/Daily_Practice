def hanoi(n, source, auxiliary, target, moves):
    if n == 1:
        moves.append(f"Move 1 from {source} to {target}")
        return
    hanoi(n - 1, source, target, auxiliary, moves)
    moves.append(f"Move {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, source, target, moves)

def tower_of_hanoi():
    T = int(input())
    test_cases = [int(input()) for _ in range(T)]

    for n in test_cases:
        moves = []
        hanoi(n, 'A', 'B', 'C', moves)
        print(len(moves))
        for move in moves:
            print(move)

# Run the function
tower_of_hanoi()
c
