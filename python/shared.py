def check_win(board):
    """
    returns:
    0 - not win or tie
    1,2 - player 1 or 2 win
    -1 - tie
    """

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

    # check if board full
    open_squares = 0
    for square in board:
        if square == 0:
            open_squares += 1
    if open_squares == 0:
        return -1

    # return not win or tie
    return 0


def draw_tree(root, max_depth=999, show_no_visit_nodes=False):
    # draw the tree in dfs
    node_stack = [(root, 0, 1)]  # format for entries is (node, depth, parent visits)
    while len(node_stack) > 0:  # run until stack is empty
        # get top node
        (top_node, depth, parent_visits) = node_stack.pop()

        if show_no_visit_nodes or top_node.num_visits > 0 or (top_node.is_win != 0 and parent_visits > 0):
            # draw node if less than max_depth, starts with player that made the move then has the id
            if depth < max_depth:
                if depth != 0:
                    print("    " * (depth - 1) + "----", end='')

                if top_node.player_to_act == 1:
                    parent_player_to_act = 2
                else:
                    parent_player_to_act = 1

                if top_node.is_win != 0:
                    print(f"{ parent_player_to_act } { top_node.id }: finished { top_node.is_win }")
                else:
                    # format is win loss tie / visits
                    print(f"{ parent_player_to_act } { top_node.id }: { top_node.simulation_outcomes[2] } { top_node.simulation_outcomes[1] } { top_node.simulation_outcomes[-1] } / { top_node.num_visits }")

        # add children to stack
        for child in top_node.children:  
            node_stack.append((child, depth + 1, top_node.num_visits))

    print()  # add a newline
