# !/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

__author__ = 's.y'
__version__ = '1.0'
__date__ = '2024/06/03 (Created: 2024/5/20)'


class Compile:
    """
    'pygpt'のコンパイルクラスです。
    プログラムがエラーを出すかを確認します。
    """

    def __init__(self):
        """
        Compileの初期化
        """
        self.error_text = None
        self.output_text = None

    def execution(self, program, compile_flag=False):
        """入力されたプログラムを実行し、エラーが起きるか確認する"""
        result = subprocess.run(['python3', program],
                                         text=True, capture_output=True)

        if result.returncode != 0:
            compile_flag = True
            self.error_text = result.stderr
            return compile_flag, self.error_text
        else:
            compile_flag = False
            self.output_text = result.stdout
            return compile_flag, self.output_text
