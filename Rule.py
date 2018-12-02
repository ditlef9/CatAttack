
def isLegalDogMove(current_pos, wanted_pos):
    x = current_pos[0]
    y = current_pos[1]
    x_new = wanted_pos[0]
    y_new = wanted_pos[1]

    one_forward_backward = (x + 1 == x_new or x - 1 == x_new) and y == y_new
    one_left_right = (y + 1 == y_new or y - 1 == y_new) and x == x_new
    return one_forward_backward or one_left_right
