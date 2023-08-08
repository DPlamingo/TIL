import sys
sys.stdin = open('input1210.txt')

for tc in range(1, 11):
    T = int(input())
    ladder = []
    for _ in range(100):
        row_data = list(map(int, input().split()))
        ladder.append(row_data)

    dest_col = 0
    start_col = 0  # Store the initial column index

    # Find the destination column (where value is 2) at the bottom row (row index T-1)
    for col in range(100):
        if ladder[T-1][col] == 2:
            dest_col = col
            break

    start_col = dest_col  # Store the initial column index before moving upwards

    # Start from the bottom and move upwards
    row = T - 1
    while row >= 0:
        # Move left if possible
        if dest_col > 0 and ladder[row][dest_col - 1] == 1:
            while dest_col > 0 and ladder[row][dest_col - 1] == 1:
                dest_col -= 1
        # Move right if possible
        elif dest_col < 99 and ladder[row][dest_col + 1] == 1:
            while dest_col < 99 and ladder[row][dest_col + 1] == 1:
                dest_col += 1

        row -= 1

    print(f'#{tc} {start_col}')  # Print the initial column index
