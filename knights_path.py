
board = [[0 for j in range(0,8)] for i in range(0,8)]

# from and to are tuples
def find_path(frm, to):
    queue = []
    queue.append([frm])
    while queue:
        path = queue.pop(0)
        cur_pos = path[-1]
        board[cur_pos[0]][cur_pos[1]] = 1;
        if cur_pos[0] == to[0] and cur_pos[1] == to[1]:
            return path
        valid_moves = get_valid_moves(cur_pos)
        for position in valid_moves:
            new_path = list(path)
            new_path.append(position)
            queue.append(new_path)

def get_valid_moves(position):
    moves = [(-2,-1), (-2,1), (2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
    valid_moves = []
    for move in moves:
        potential_move = tuple(map(sum, zip(move, position)))
        if potential_move[0] > 0 and potential_move[0] < 8 and potential_move[1] > 0 and potential_move[1] and board[potential_move[0]][potential_move[1]] == 0:
            valid_moves.append(potential_move)
    return valid_moves

print(find_path((0,0), (2,5)))
