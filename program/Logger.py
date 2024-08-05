import logging
import os

__author__ = 's.y'
__version__ = '2.0'
__date__ = '2024/07/11 (Created: 2024/6/27)'


class Logger:
    """
    pygptのロガークラスです。
    ログファイルの作成・管理、エラーの記録を担当します。
    """
    def __init__(self):
        self.logger = self.setup_logger()

    def setup_logger(self, name='application_logger', level=logging.INFO):
        log_file = os.path.join(os.getcwd(), 'pygpt.csv')
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

    def log_execution(self, file_path, execution_time, error=None):
        if error:
            self.logger.error(f'"{file_path}",{execution_time},"{error.replace('"', '""')}"')
        else:
            self.logger.info(f'"{file_path}",{execution_time}')
