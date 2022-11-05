class InvalidDataException(Exception):
    
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return self.message
############################################
class NoSudokuSolutionException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return self.message
############################################
class InvalidDimensionsException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return self.message
################################################
class SolvedSudokuException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

    def __str__(self):
        return self.message