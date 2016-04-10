

def one_level_search(board, user, value_function, return_list=False):
    que = []

    for possible_put in board.user_possible_puts(user):
        new_state = board.copy()
        new_state.user_put_block_on_point(user, possible_put[0], possible_put[1])
        que.append([new_state, possible_put])

    que = sorted(que, key=lambda state: value_function(state[0], user), reverse=True)

    if return_list:
        return que
    else:
        return que[0][1]
