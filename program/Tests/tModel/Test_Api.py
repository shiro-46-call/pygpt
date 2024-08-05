# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch, MagicMock
from Model.Api import Api

__author__ = 's.y'
__version__ = '1.0'
__date__ = '2024/07/13 (Created: 2024/7/12)'


class TestApi(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    @patch('os.getenv')
    def test_init(self, mock_getenv):
        mock_getenv.return_value = 'API_KEY'
        api = Api()
        mock_getenv.assert_called_with('OPENAI_API_KEY')
        self.assertEqual(api.api_key, 'dummy_api_key')

    @patch('Api.OpenAI')
    def test_request(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value.to_dict.return_value = {'response': 'success'}

        response = self.api.request('program_text', 'error_text')
        self.assertIsNotNone(response)
        self.assertEqual(response, {'response': 'success'})

    @patch('Api.OpenAI')
    def test_request_failure(self, mock_openai):
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception('error')

        response = self.api.request('program_text', 'error_text')
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
