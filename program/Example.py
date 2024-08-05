# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
from Model.Api import Api
from Model.Compile import Compile
from Model.Model import Model
from View.View import View
from Logger import Logger
import time

"""
ターミナル上で使用可能な'pygpt'コマンド

"""

__author__ = 's.y'
__version__ = '4.0'
__date__ = '2024/06/27 (Created: 2024/5/20)'


class Example:
    """
    'pygpt'のExampleクラスです。
    コンストラクタを持ちます。
    Model,Viewクラスに実行の指示を送信します。
    """
    def __init__(self, model: Model, view: View, logger: Logger, program: str):
        """
        Exampleの初期化
        """
        self.program = program
        self.model = model
        self.view = view
        self.logger = logger
        self.result = None
        self.error_text = None

    def model_controller(self):
        """
        Modelクラスに実行の指示を送信する
        """
        start_time = time.time()
        self.error_text, self.result = self.model.controller(self.program)
        execution_time = time.time() - start_time
        if not self.result:
            self.logger.log_execution(self.program, execution_time, self.error_text)
            return
        self.view_controller(self.error_text, self.result)
        self.logger.log_execution(self.program, execution_time, self.error_text)

    def view_controller(self, error_text, result):
        """
        Viewクラスに実行の指示を送信する
        """
        self.view.show_result(error_text, result)


def valid_file(parser, arg):
    """
    ファイルの拡張子が.pyかどうかを確認する
    """
    if not os.path.exists(arg):
        parser.error(f"ファイル{arg}が存在しません。")
    elif not arg.lower().endswith(('py')):
        parser.error(f"ファイル{arg}はPythonファイルではありません。")
    return arg


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="pygpt <任意のファイル>")
    parser.add_argument("file", type=lambda x: valid_file(parser, x),
                        help="Pythonファイルを指定してください。")
    args = parser.parse_args()

    an_api = Api()
    a_compile = Compile()
    model = Model(a_compile, an_api)
    view = View()
    logger = Logger()
    example = Example(model, view, logger, args.file)
    example.model_controller()
