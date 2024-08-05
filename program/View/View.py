#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Fore, Style

init()

__author__ = 's.y'
__version__ = '3.0'
__date__ = '2024/06/14 (Created: 2024/5/20)'


class View:
    """
    'pygpt'のビュークラスです。
    ターミナル上での表示の部分の処理を担当します。
    """
    def show_result(self, error_text, result):
        """
        ChatGPT APIから返ってきたJSONファイルを解析し、ユーザーに見やすい形式でターミナルに表示するメソッド
        """
        print(f"{Fore.CYAN}エラーメッセージ:{Style.RESET_ALL}\n{error_text}")
        if "error" in result:
            print(f"{Fore.RED}エラー: {result['error']}{Style.RESET_ALL}")
        else:
            try:
                choices = result.get('choices', [])
                if choices:
                    message = choices[0]['message']['content']
                    # メッセージ内の不要な文字列や改行を整形
                    formatted_message = self.format_message(message)
                    print(f"{Fore.GREEN}解析結果:{Style.RESET_ALL}\n{formatted_message}")
                else:
                    print(f"{Fore.YELLOW}警告: 選択肢が見つかりません{Style.RESET_ALL}")
            except KeyError as e:
                print(f"{Fore.RED}エラー:応答データから必要な情報を見つけられませんでした ({e}).{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}予期せぬエラーが発生しました: {e}{Style.RESET_ALL}")

    def format_message(self, message):
        """
        不要な文字列を除去し、改行を適切に処理するメソッド
        """
        message = message.replace("ChatCompletionMessage(content=", "")
        message = message.replace("'", "")
        message = message.strip(")")
        message = message.replace("\\n", "\n")
        return message
