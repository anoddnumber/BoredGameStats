import unittest

import utilities.randomizer as randomizer


class TestRandomizer(unittest.TestCase):

    def test_roll_dice_default(self):
        for i in range(1000):
            rand_nums = randomizer.roll_dice()
            self.assertEqual(len(rand_nums), 1, 'Number of dice rolled is incorrect')
            self.assertEqual(type(rand_nums[0]), int, "Dice number is not an integer")
            self.assertTrue(0 < rand_nums[0] <= 6, "Dice number out of range")
        print("Passed test_roll_dice_default")

    def test_roll_multiple_dice(self):
        for i in range(100):
            rand_nums = randomizer.roll_dice(i)
            self.assertEqual(len(rand_nums), i, 'Number of dice rolled is incorrect')

            for rand_num in rand_nums:
                self.assertEqual(type(rand_num), int, "Dice number is not an integer")
                self.assertGreaterEqual(rand_num, 1, "Dice number too low")
                self.assertLessEqual(rand_num, 6, "Dice number too high")
        print("Passed test_roll_multiple_dice")

    def test_roll_many_sides(self):
        for num_sides in range(1, 100):
            for i in range(100):
                rand_nums = randomizer.roll_dice(1, num_sides)
                self.assertEqual(len(rand_nums), 1, 'Number of dice rolled is incorrect')
                self.assertEqual(type(rand_nums[0]), int, "Dice number is not an integer")
                self.assertGreaterEqual(rand_nums[0], 1, "Dice number too low")
                self.assertLessEqual(rand_nums[0], num_sides, "Dice number too high")
        print("Passed test_roll_many_sides")

    def test_roll_multiple_dice_and_many_sides(self):

        for num_dice in range(1, 100):
            for num_sides in range(1, 10):
                for i in range(10):
                    rand_nums = randomizer.roll_dice(num_dice, num_sides)
                    self.assertEqual(len(rand_nums), num_dice, 'Number of dice rolled is incorrect')
                    for rand_num in rand_nums:
                        self.assertEqual(type(rand_num), int, "Dice number is not an integer")
                        self.assertTrue(0 < rand_num <= num_sides, "Dice number out of range")
        print("Passed test_roll_multiple_dice_and_many_sides")

    def test_bad_dice_roll_input(self):
        rand_nums = randomizer.roll_dice(0)
        self.assertEqual(rand_nums, [], 'Expected an empty list')
        rand_nums = randomizer.roll_dice(-1)
        self.assertEqual(rand_nums, [], 'Expected an empty list')
        rand_nums = randomizer.roll_dice(1, 0)
        self.assertEqual(rand_nums, [], 'Expected an empty list')
        rand_nums = randomizer.roll_dice(1, -1)
        self.assertEqual(rand_nums, [], 'Expected an empty list')
        print("Passed test_bad_dice_roll_input")

    def test_randomize_teams_happy(self):
        # default_number_of_teams = 2

        for num_teams in range(1, 100):
            for num_players in range(num_teams, 100):
                # print("num_teams: " + str(num_teams))
                # print("num_players: " + str(num_players))
                teams = randomizer.randomize_teams(num_players, num_teams)
                # print("teams: " + str(teams))
                self.assertEqual(len(teams), num_teams)

                expected_team_len = int(num_players / num_teams)
                expected_num_teams_with_additional_player = num_players % num_teams
                expected_num_team_without_additional_player = num_teams - expected_num_teams_with_additional_player

                actual_num_teams_with_additional_player = 0
                actual_num_team_without_additional_player = 0
                for team in teams:
                    actual_team_len = len(team)
                    if actual_team_len != expected_team_len and actual_team_len != expected_team_len + 1:
                        self.fail("expected team length to be " + str(expected_team_len) + " or "
                                  + str(expected_team_len + 1) + ", instead the team length was " + str(actual_team_len))

                    if actual_team_len == expected_team_len + 1:
                        actual_num_teams_with_additional_player += 1
                    elif actual_team_len == expected_team_len:
                        actual_num_team_without_additional_player += 1

                self.assertEqual(expected_num_teams_with_additional_player, actual_num_teams_with_additional_player)
                self.assertEqual(expected_num_team_without_additional_player, actual_num_team_without_additional_player)


if __name__ == "__main__":
    unittest.main()
