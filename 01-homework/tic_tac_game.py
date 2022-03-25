import re


def is_valid_input(field):
    return re.search(r"^[123]\s[123]$", field) is not None


def to_arraylike_coordinates(field):
    row, col = [int(x) - 1 for x in field.split(" ")]
    return row * 3 + col


class TicTacGame:
    def __init__(self) -> None:
        self.state = [0 for _ in range(9)]
        self.states = {1: "X ", 0: "- ", -1: "O "}

    def redraw_board(self):
        print("\033[H\033[J", end="")
        print(
            "  1 2 3\n"
            + "\n".join(
                [
                    f"{i+1} "
                    + "".join(
                        list(map(lambda x: self.states[x], self.state))[
                            i * 3 : i * 3 + 3
                        ]
                    )
                    for i in range(3)
                ]
            ),
        )

    def is_someone_won(self):
        return (
            max(
                [
                    abs(sum(x))
                    for x in [self.state[i * 3 : i * 3 + 3] for i in range(3)]
                    + [self.state[i::3] for i in range(3)]
                    + [self.state[0::4], self.state[2:8:2]]
                ]
            )
            == 3
        )

    def is_game_continue(self):
        if self.is_someone_won():
            return False
        return sum(list(map(abs, self.state))) < 9

    def current_player(self):
        return 1 if sum(self.state) == 0 else -1

    def is_turn_possible(self, field_loc):
        return self.state[field_loc] == 0

    def make_turn(self, field_loc):
        self.state[field_loc] = self.current_player()

    def start_game(self):
        while self.is_game_continue():
            self.redraw_board()

            print(f"Player's {self.states[self.current_player()]} turn")
            print("enter field as row and column separated by space: ", end="")

            while True:
                field = input()
                if not is_valid_input(field):
                    print("incorrect input format. Please, enter field again: ", end="")
                elif not self.is_turn_possible(to_arraylike_coordinates(field)):
                    print("field not free. Please, enter field again: ", end="")
                else:
                    break

            self.make_turn(to_arraylike_coordinates(field))

        self.redraw_board()
        if self.is_someone_won():
            print(f"Player {self.states[-1 * self.current_player()]}won!")
        else:
            print("Draw!")


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
