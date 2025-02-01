# Polymorphism
# •	11. Create a class `Logger` with a method `log(message)`. Implement method overloading to
# log different message types (`error`, `warning`, `info`).

class Logger:
    def error(self,message):
        self.message=message
        print(f"This message is: {self.message}")
    def warning(self,message):
        self.message=message
        print(f"This message is: {self.message}")
    def info(self,message):
        self.message=message
        print(f"This message is: {self.message}")
logger=Logger()
logger.error("error message")
logger.warning("warning message")
logger.info("Info message")
