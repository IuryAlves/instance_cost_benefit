#!/usr/bin/env python
# coding: utf-8

import unittest
from os.path import join
from main import main


class TestCase(unittest.TestCase):

    def test_calculate_cost_benefit_from_empty_file(self):
        paths = (
            join('test_files', 'empty.txt'),
        )

        result = main(paths)

        self.assertEqual(result, [])

    def test_calculate_instance_cost_benefit(self):
        paths = (
            join('test_files', 'first-exercise-input-1.txt'),
            join('test_files', 'first-exercise-input-2.txt')
        )

        result = main(paths)

        self.assertEqual(
            result,
            ['r4.2xlarge', 'r4.large',
             'c4.xlarge', 'c4.2xlarge',
             'c4.8xlarge', 'c4.4xlarge',
             'm4.xlarge']
        )

    def test_calculate_instances_cost_benefit_with_duplicated_files(self):
        paths = (
            join('test_files', 'first-exercise-input-1.txt'),
            join('test_files', 'first-exercise-input-2.txt'),
            join('test_files', 'first-exercise-input-2.txt'),
            join('test_files', 'first-exercise-input-1.txt')

        )

        result = main(paths)

        self.assertEqual(
            result,
            ['r4.2xlarge', 'r4.large',
             'c4.xlarge', 'c4.2xlarge',
             'c4.8xlarge', 'c4.4xlarge',
             'm4.xlarge']
        )

    def test_calculate_cost_benefit_from_file_without_cost_info(self):

        paths = (
            join('test_files', 'first-exercise-input-1.txt'),
        )

        result = main(paths)

        self.assertEqual(result, [])

    def test_calculate_cost_benefit_lowercase(self):

        paths = (
            join('test_files', 'first-exercise-input-1-lowercase.txt'),
            join('test_files', 'first-exercise-input-2-lowercase.txt')
        )

        result = main(paths)

        self.assertEqual(
            result,
            ['r4.2xlarge', 'r4.large',
             'c4.xlarge', 'c4.2xlarge',
             'c4.8xlarge', 'c4.4xlarge',
             'm4.xlarge']
        )


if __name__ == '__main__':
    unittest.main()
