
import chess.pgn

def extract_lines_from_pgn(pgn_file):
    with open(pgn_file, "r", encoding="utf-8") as f:
        game = chess.pgn.read_game(f)  # Read the first game from PGN

    lines = []

    def traverse(node, move_list, board):
        """ Recursively traverse the PGN tree and collect variations. """
        if node.move:
            move_list.append(board.san(node.move))  # Convert move to SAN
            board.push(node.move)  # Play move on board

        if not node.variations:  # If no more variations, store the move sequence
            lines.append(", ".join(move_list))
            return

        for var in node.variations:
            traverse(var, move_list[:], board.copy())  # Recurse for each variation

    traverse(game, [], chess.Board())
    return "\n".join(lines)


# Example usage
#pgn_file = "/workspaces/python-dev-container-template/src/sample.pgn"
pgn_file = "/workspaces/pgn-flattener/pgn/semislav-rep1.pgn"

output = extract_lines_from_pgn(pgn_file)
print(output)
