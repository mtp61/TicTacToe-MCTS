def check_win(board):
    """
    returns:
    0 - not win or tie
    1,2 - player 1 or 2 win
    -1 - tie
    """

    # check if board full
    open_squares = 0
    for square in board:
        if square == 0:
            open_squares += 1
    if open_squares == 0:
        return -1

    # check for win
    # check rows
    for i in range(3):
        row_sum = 0
        num_filled = 0
        for j in range(3):
            row_sum += board[3 * i + j]
            if board[3 * i + j] != 0:
                num_filled += 1
        if num_filled == 3:
            if row_sum == 3:
                return 1
            elif row_sum == 6:
                return 2

    # check cols
    for i in range(3):
        col_sum = 0
        num_filled = 0
        for j in range(3):
            col_sum += board[i + 3 * j]
            if board[i + 3 * j] != 0:
                num_filled += 1
        if num_filled == 3:
            if col_sum == 3:
                return 1
            elif col_sum == 6:
                return 2

    # check diagonals
    diag_sum = board[0] + board[4] + board[8]
    if board[0] != 0 and board[4] != 0 and board[8] != 0:
        if diag_sum == 3:
            return 1
        elif diag_sum == 6:
            return 2
    if board[2] != 0 and board[4] != 0 and board[6] != 0:
        diag_sum = board[2] + board[4] + board[6]
        if diag_sum == 3:
            return 1
        elif diag_sum == 6:
            return 2

    # return not win or tie
    return 0
