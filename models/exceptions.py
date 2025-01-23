class TooManyStudentsError(Exception):
    def __init__(self, message="Група не може містити більше 10 студентів"):
        self.message = message
        super().__init__(self.message)
