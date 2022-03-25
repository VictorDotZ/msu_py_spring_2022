import unittest

import TicTacGame


class TestIsValidInput(unittest.TestCase):
    def test_is_valid_input(self):
        self.assertTrue(TicTacGame.is_valid_input("1 1"))
        self.assertTrue(TicTacGame.is_valid_input("2 3"))
        self.assertFalse(TicTacGame.is_valid_input(" 1 1"))
        self.assertFalse(TicTacGame.is_valid_input("1 1 "))
        self.assertFalse(TicTacGame.is_valid_input(" 1 1 "))
        self.assertFalse(TicTacGame.is_valid_input("1  1"))
        self.assertFalse(TicTacGame.is_valid_input("4 1"))
        self.assertFalse(TicTacGame.is_valid_input("1 4"))
        self.assertFalse(TicTacGame.is_valid_input(""))
        self.assertFalse(TicTacGame.is_valid_input("1"))
        self.assertFalse(TicTacGame.is_valid_input("1 "))
        self.assertFalse(TicTacGame.is_valid_input(" 1"))
        self.assertFalse(TicTacGame.is_valid_input(" 1 "))
        self.assertFalse(TicTacGame.is_valid_input("4"))
        self.assertFalse(TicTacGame.is_valid_input("-1"))
        self.assertFalse(TicTacGame.is_valid_input("-1 -1"))
        self.assertFalse(TicTacGame.is_valid_input("11 1"))
        self.assertFalse(TicTacGame.is_valid_input("1 11"))


class TestToArrayLikeCoordinates(unittest.TestCase):
    def test_to_arraylike_coordinates(self):
        self.assertEqual(TicTacGame.to_arraylike_coordinates("1 1"), 0)
        self.assertEqual(TicTacGame.to_arraylike_coordinates("2 2"), 4)
        self.assertEqual(TicTacGame.to_arraylike_coordinates("3 3"), 8)
        self.assertEqual(TicTacGame.to_arraylike_coordinates("1 3"), 2)
        self.assertEqual(TicTacGame.to_arraylike_coordinates("3 1"), 6)
        self.assertEqual(TicTacGame.to_arraylike_coordinates("1 2"), 1)
        self.assertEqual(TicTacGame.to_arraylike_coordinates("2 1"), 3)


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame.TicTacGame()

    def test_is_someone_won(self):
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertFalse(self.game.is_someone_won())
        self.game.state = [1, -1, 1, -1, 1, -1, -1, 1, -1]
        self.assertFalse(self.game.is_someone_won())

        self.game.state = [1, 1, 1, -1, 0, -1, -1, 0, 0]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [-1, 0, -1, 1, 1, 1, -1, 0, 0]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [1, 0, 1, 1, 0, 0, -1, -1, -1]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [1, 0, 1, -1, 1, 0, -1, -1, 1]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [1, 0, -1, 1, -1, 1, -1, 1, -1]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [1, 0, 1, 1, 0, -1, 1, -1, -1]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [1, -1, 1, 1, -1, 0, 1, -1, -1]
        self.assertTrue(self.game.is_someone_won())
        self.game.state = [1, 0, -1, 1, 1, -1, -1, 1, -1]
        self.assertTrue(self.game.is_someone_won())

    def test_is_game_continue(self):
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.game.is_game_continue())
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.game.is_game_continue())
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertTrue(self.game.is_game_continue())
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.assertTrue(self.game.is_game_continue())

        self.game.state = [1, -1, 1, -1, 1, -1, -1, 1, -1]
        self.assertFalse(self.game.is_game_continue())
        self.game.state = [1, 0, -1, 1, 1, -1, -1, 1, -1]
        self.assertFalse(self.game.is_game_continue())
        self.game.state = [1, 0, 1, 1, 0, 0, -1, -1, -1]
        self.assertFalse(self.game.is_game_continue())
        self.game.state = [-1, 0, -1, 1, 1, 1, -1, 0, 0]
        self.assertFalse(self.game.is_game_continue())
        self.game.state = [1, -1, 1, 1, -1, 1, -1, 1, -1]
        self.assertFalse(self.game.is_game_continue())
        self.game.state = [1, -1, 1, -1, 1, -1, 1, 1, -1]
        self.assertFalse(self.game.is_game_continue())

    def test_is_turn_possible(self):
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.game.is_turn_possible(5))
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.game.is_turn_possible(0))
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertTrue(self.game.is_turn_possible(8))

        self.game.state = [1, -1, 1, 1, -1, 1, -1, 1, -1]
        self.assertFalse(self.game.is_turn_possible(1))
        self.game.state = [1, -1, 1, -1, 1, -1, 1, 1, -1]
        self.assertFalse(self.game.is_turn_possible(7))

        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertTrue(self.game.is_turn_possible(2))
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.assertTrue(self.game.is_turn_possible(7))
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertTrue(self.game.is_turn_possible(5))
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.assertTrue(self.game.is_turn_possible(6))

        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertFalse(self.game.is_turn_possible(1))
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.assertFalse(self.game.is_turn_possible(3))
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertFalse(self.game.is_turn_possible(6))
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.assertFalse(self.game.is_turn_possible(8))

    def test_current_player(self):
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.game.current_player(), 1)
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertEqual(self.game.current_player(), -1)
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.assertEqual(self.game.current_player(), -1)
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.assertEqual(self.game.current_player(), -1)
        self.game.state = [1, -1, 1, -1, 0, 1, 0, 0, -1]
        self.assertEqual(self.game.current_player(), 1)

    def test_make_turn(self):
        self.game.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.game.make_turn(4)
        self.assertEqual(self.game.state[4], 1)
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.game.make_turn(2)
        self.assertEqual(self.game.state[2], -1)
        self.game.state = [0, -1, 1, 1, 0, 1, 0, 0, -1]
        self.game.make_turn(0)
        self.assertEqual(self.game.state[0], -1)
        self.game.state = [1, -1, 0, -1, 1, 0, 1, 1, -1]
        self.game.make_turn(5)
        self.assertEqual(self.game.state[5], -1)
        self.game.state = [1, -1, 1, -1, 0, 1, 0, 0, -1]
        self.game.make_turn(7)
        self.assertEqual(self.game.state[7], 1)


if __name__ == "__main__":
    unittest.main()

