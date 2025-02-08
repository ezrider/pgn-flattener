import chess.pgn

def extract_lines_from_pgn(pgn_file):
    lines = []
    
    with open(pgn_file, "r", encoding="utf-8") as f:
        while True:
            game = chess.pgn.read_game(f)  # Read one game at a time
            if game is None:  # Stop when no more games are found
                break

            game_lines = []  # Store variations for the current game
            
            def traverse(node, move_list, board):
                """ Recursively traverse the PGN tree and collect variations. """
                if node.move:
                    move_list.append(board.san(node.move))  # Convert move to SAN
                    board.push(node.move)  # Play move on board

                if not node.variations:  # If no more variations, store the move sequence
                    game_lines.append(", ".join(move_list))
                    return

                for var in node.variations:
                    traverse(var, move_list[:], board.copy())  # Recurse for each variation

            traverse(game, [], chess.Board())
            lines.append("\n".join(game_lines))  # Separate games with a newline

    return "\n\n".join(lines)  # Separate different games clearly

# Example usage
pgn_file = "your_file.pgn"
output = extract_lines_from_pgn(pgn_file)
print(output)

