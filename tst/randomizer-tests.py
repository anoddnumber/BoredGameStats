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

if __name__ == "__main__":
    unittest.main()

