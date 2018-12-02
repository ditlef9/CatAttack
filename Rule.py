def is_legal_move_dog(current_pos, wanted_pos):
    x = current_pos[0]
    y = current_pos[1]
    x_new = wanted_pos[0]
    y_new = wanted_pos[1]

    one_forward_backward = (x + 1 == x_new or x - 1 == x_new) and y == y_new
    one_left_right = (y + 1 == y_new or y - 1 == y_new) and x == x_new
    return one_forward_backward or one_left_right


def is_legal_move_monkey(current_pos, wanted_pos):
    x = current_pos[0]
    y = current_pos[1]
    x_new = wanted_pos[0]
    y_new = wanted_pos[1]

    one_forward_left = x + 1 == x_new and y + 1 == y_new
    one_forward_right = x + 1 == x_new and y - 1 == y_new
    one_backward_left = x - 1 == x_new and y + 1 == y_new
    one_backward_right = x - 1 == x_new and y - 1 == y_new
    return one_forward_left or one_forward_right or one_backward_left or one_backward_right


def is_legal_move_lion(current_pos, wanted_pos):
    return is_legal_move_dog(current_pos, wanted_pos) or is_legal_move_monkey(current_pos, wanted_pos)


