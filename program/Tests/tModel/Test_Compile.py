# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from Model.Compile import Compile

__author__ = 's.y'
__version__ = '1.0'
__date__ = '2024/07/12 (Created: 2024/7/12)'


class TestCompile(unittest.TestCase):
    def setUp(self):
        self.compile = Compile()

    @patch('subprocess.run')
    def test_execution(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stderr=None)
        compile_flag, error_text = self.compile.execution('compile_test.py')

        self.assertFalse(compile_flag)
        self.assertIsNone(error_text)
        mock_run.assert_called_once_with(['python3', 'compile_test.py'], text=True, capture_output=True)

    @patch('subprocess.run')
    def test_execution_failure(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stderr='error')
        compile_flag, error_text = self.compile.execution('compile_test.py')

        self.assertTrue(compile_flag)
        self.assertEqual(error_text, 'error')
        mock_run.assert_called_once_with(['python3', 'compile_test.py'], text=True, capture_output=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
