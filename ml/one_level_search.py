

def one_level_search(board, value_function):
    start_state = board.copy()
    que = []

    for possible_put in start_state.user_possible_puts(start_state.user2):
        new_state = start_state.copy()
        new_state.user_put_block_on_point(new_state.user2, possible_put[0], possible_put[1])
        que.append((new_state, possible_put))

    que = sorted(que, key=lambda state: value_function(state[0]), reverse=True)

    return que[0][1]
