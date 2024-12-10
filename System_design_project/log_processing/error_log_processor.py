from log_processor import LogProcessor

class ErrorLogProcessor(LogProcessor):
    
    def __init__(self, next_log_processor: LogProcessor):
        super().__init__(next_log_processor)

    def log(self, log_level, message):
        print(f"Log level : {log_level}")
        if log_level == self.ERROR:
            print(f"ERROR : {message}")
        else:
            super().log(log_level, message)

    
