#!/usr/bin/env python
# -*- coding: utf-8 -*-

from openai import OpenAI
import os
from dotenv import load_dotenv

__author__ = 's.y'
__version__ = '2.0'
__date__ = '2024/06/06 (Created: 2024/5/20)'


class Api:
    """
    'pygpt'のAPIクラスです。
    OpenAIのGPT-4（仮）を使用して、テキスト、ファイルを送信し、応答を受け取ります。
    """
    def __init__(self):
        """
        APIの初期化
        """
        load_dotenv()  # .envファイルから環境変数を読み込む
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key)

        # GitHubに載せる場合に表示する
        # if not self.api_key:
        #     raise ValueError('APIキーが設定されていません.')

    def request(self, program_text, error_text):
        """
        OpenAIのGPT-4（仮）を使用して、テキスト、ファイルを送信し、応答を受け取ります。
        """
        try:
            prompt_text = (f"以下のプログラムコードにエラーが見つかりました:\n{program_text}\n"
                           f"エラーメッセージ:\n{error_text}\n"
                           "このエラーの原因と修正提案を教えてください。")

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "次の情報をもとにエラー修正のアドバイスを提供してください。"},
                    {"role": "user", "content": prompt_text}
                ],
                # max_tokens=150
            )
            return response.to_dict()

        except Exception as e:
            print(f"Failed to retrieve response from OpenAI: {e}")
            return None
