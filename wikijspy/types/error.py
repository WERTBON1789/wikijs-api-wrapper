

class InvalidOutputError(Exception):
    def __init__(self, output: str, caller: str):
        self.output = output
        super().__init__(f"The given output parameter \"{output}\" is invalid for {caller}!")
