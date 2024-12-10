from abc import ABC, abstractclassmethod

class LogProcessor:
    
    INFO: int = 1
    DEBUG: int = 2
    ERROR: int = 3

    def __init__(self, logger_processor):
        self.next_log_processor = logger_processor

    def log(self, log_level: int, message: str):

        if self.next_log_processor is not None:
            self.next_log_processor.log(log_level, message)