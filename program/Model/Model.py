#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Model.Compile import Compile
from Model.Api import Api

__author__ = 's.y'
__version__ = '3.0'
__date__ = '2024/06/27 (Created: 2024/5/20)'


class Model:
    """
    'pygpt'のモデルクラスです。
    Compile、Api、Viewクラスに各処理の指示を送信します。
    """
    def __init__(self, compile: Compile, api: Api):
        """
        Modelの初期化
        """
        self.compile = compile
        self.api = api
        self.program_text = None  # プログラムのテキスト
        self.compile_flag = False  # コンパイル結果のフラグ
        self.error_text = None  # コンパイルエラー文
        self.result = None  # APIの結果

    def controller(self, program):
        """
        各クラスに処理の実行の指示を送信する
        """
        try:
            self.compile_flag, self.error_text = self.compile.execution(program, self.compile_flag)
            if not self.compile_flag:
                self.result = ()
                return self.error_text, tuple(self.result)

            self.program_text = self.convert_text(program)
            self.result = self.api.request(self.program_text, self.error_text)
            return self.error_text, self.result

        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    def convert_text(self, program):
        """
        Pythonファイルのテキストを抽出する
        """
        try:
            with open(program, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            raise Exception(f"Error reading the file: {e}")
