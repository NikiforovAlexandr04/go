import unittest
from field import Field


class Tests(unittest.TestCase):
    def test_press_key(self):
        self.field = Field(0)
        self.field.board_size = 9
        self.field.current_state = self.field.field_game()
        self.field.press_key(173, 201, True)
        self.field.press_key(170, 173, True)
        self.field.press_key(203, 110, True)
        self.field.press_key(112, 264, False)
        self.field.press_key(231, 236, False)
        self.field.press_key(112, 82, False)
        self.assertEqual(self.field.current_state[5][4].color, "w")
        self.assertEqual(self.field.current_state[4][4].color, "w")
        self.assertEqual(self.field.current_state[2][5].color, "w")
        self.assertEqual(self.field.current_state[7][2].color, "b")
        self.assertEqual(self.field.current_state[6][6].color, "b")
        self.assertEqual(self.field.current_state[1][2].color, "b")

    def test_capture_black(self):
        self.field = Field(0)
        self.field.board_size = 9
        self.field.current_state = self.field.field_game()
        self.field.press_key(171, 179, True)
        self.field.press_key(198, 199, True)
        self.field.press_key(171, 232, True)
        self.field.press_key(145, 202, True)
        self.field.press_key(169, 201, False)
        self.field.capture()
        self.assertEqual(self.field.white_points, 5)

    def test_capture_white(self):
        self.field = Field(0)
        self.field.board_size = 9
        self.field.current_state = self.field.field_game()
        self.field.press_key(293, 56, True)
        self.field.press_key(231, 49, False)
        self.field.press_key(264, 48, True)
        self.field.press_key(266, 83, False)
        self.field.press_key(289, 85, True)
        self.field.press_key(290, 113, False)
        self.field.press_key(113, 178, True)
        self.field.capture()
        self.assertEqual(self.field.black_points, 6)

    def test_capture_field_first(self):
        self.field = Field(0)
        self.field.board_size = 13
        self.field.current_state = self.field.field_game()
        self.field.press_key(386, 54, True)
        self.field.press_key(412, 82, True)
        self.field.press_key(165, 200, False)
        self.field.capture()
        self.field.total_count()
        self.assertEqual(self.field.white_points, 3)

    def test_capture_field_second(self):
        self.field = Field(0)
        self.field.board_size = 13
        self.field.current_state = self.field.field_game()
        self.field.press_key(411, 203, False)
        self.field.press_key(382, 204, False)
        self.field.press_key(376, 224, False)
        self.field.press_key(382, 255, False)
        self.field.press_key(412, 251, False)
        self.field.press_key(165, 200, True)
        self.field.capture()
        self.field.total_count()
        self.assertEqual(self.field.black_points, 6)

    def test_capture_field_third(self):
        self.field = Field(0)
        self.field.board_size = 13
        self.field.current_state = self.field.field_game()
        self.field.press_key(232, 231, True)
        self.field.press_key(204, 260, True)
        self.field.press_key(235, 290, True)
        self.field.press_key(260, 298, True)
        self.field.press_key(295, 261, True)
        self.field.press_key(290, 231, True)
        self.field.press_key(261, 199, True)
        self.field.press_key(140, 141, False)
        self.field.capture()
        self.field.total_count()
        self.assertEqual(self.field.white_points, 10)

    def test_total_counts(self):
        self.field = Field(0)
        self.field.board_size = 13
        self.field.current_state = self.field.field_game()
        self.field.press_key(230, 137, True)
        self.field.press_key(170, 170, False)
        self.field.press_key(232, 203, True)
        self.field.press_key(175, 225, False)
        self.field.press_key(261, 177, True)
        self.field.press_key(148, 264, False)
        self.field.press_key(292, 144, True)
        self.field.press_key(140, 141, False)
        self.field.press_key(295, 112, True)
        self.field.capture()
        self.field.total_count()
        self.assertEqual(self.field.black_points, 4)
        self.assertEqual(self.field.white_points, 5)

    def test_total_count_capture(self):
        self.field = Field(0)
        self.field.board_size = 13
        self.field.current_state = self.field.field_game()
        self.field.press_key(200, 201, True)
        self.field.press_key(201, 238, False)
        self.field.press_key(408, 52, True)
        self.field.press_key(378, 42, False)
        self.field.press_key(237, 226, True)
        self.field.press_key(384, 84, False)
        self.field.press_key(202, 262, True)
        self.field.press_key(415, 114, False)
        self.field.press_key(169, 229, True)
        self.field.press_key(260, 81, False)
        self.field.press_key(408, 84, True)
        self.field.capture()
        self.field.total_count()
        self.assertEqual(self.field.white_points, 7)
        self.assertEqual(self.field.black_points, 7)


if __name__ == '__main__':
    unittest.main()