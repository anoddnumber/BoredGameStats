import unittest
from utilities.file_accessor import read_player_scores_from_file


class TestFileAccessor(unittest.TestCase):

    READ_TEST_FILES_DIRECTORY = './file_accessor_test_files/read_test_files/'

    def test_read_player_scores_from_file_normal_1(self):
        scores = read_player_scores_from_file(self.READ_TEST_FILES_DIRECTORY + 'test_read_normal_1.txt')
        self.assertEqual(scores, [[1]])
        print("Passed test_read_player_scores_from_file_normal_1")

    def test_read_player_scores_from_file_normal_2(self):
        scores = read_player_scores_from_file(self.READ_TEST_FILES_DIRECTORY + '/test_read_normal_2.txt')
        self.assertEqual(scores, [[1], [2]])
        print("Passed test_read_player_scores_from_file_normal_2")

    def test_read_player_scores_from_file_normal_3(self):
        scores = read_player_scores_from_file(self.READ_TEST_FILES_DIRECTORY + '/test_read_normal_3.txt')
        self.assertEqual(scores, [[1, 2], [3, 4]])
        print("Passed test_read_player_scores_from_file_normal_3")

    def test_read_player_scores_from_file_normal_4(self):
        scores = read_player_scores_from_file(self.READ_TEST_FILES_DIRECTORY + '/test_read_normal_4.txt')
        self.assertEqual(scores, [[9, 8, 7], [20, 30, 40], [-1, -2, -3]])
        print("Passed test_read_player_scores_from_file_normal_4")

    def test_read_player_scores_from_file_extra_spaces_1(self):
        scores = read_player_scores_from_file(self.READ_TEST_FILES_DIRECTORY + '/test_read_extra_spaces_1.txt')
        self.assertEqual(scores, [[10, 2, 3], [3, 4, 56]])
        print("Passed test_read_player_scores_from_file_extra_spaces_1")

if __name__ == "__main__":
    unittest.main()
