class Logger:
    def __init__(self, filename: str = "myLog.txt"):
        self.filename = filename

    def __write_log(self, message: str, level: str):
        with open(self.filename, 'a') as log_file:
            message: str = f"{level} - {message}\n"
            log_file.write(message)

    def info(self, message: str):
        level: str = 'INFO'
        self.__write_log(message, level)

    def error(self, message: str):
        level: str = 'ERROR'
        self.__write_log(message, level)

    def debug(self, message: str):
        level: str = 'DEBUG'
        self.__write_log(message, level)


if __name__ == '__main__':
    logger = Logger()
    logger.info('Info message')
    logger.error("This is an error message...")