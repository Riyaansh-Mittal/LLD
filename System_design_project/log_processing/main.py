from log_processor import LogProcessor
from debug_log_processor import DebugLogProcessor
from info_log_processor import InfoLogProcessor
from error_log_processor import ErrorLogProcessor

if __name__ == "__main__":

    log_object: LogProcessor = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))

    log_object.log(LogProcessor.ERROR, "Exception happens")
    log_object.log(LogProcessor.DEBUG, "Need to dubug this")
    log_object.log(LogProcessor.INFO, "Just for info")



