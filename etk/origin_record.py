

class OriginRecord():
    def __init__(self, json_path: str, start_char: str, end_char:str) -> None:
        #Extractable.__init__(self)
        self.json_path = json_path
        self.start_char = start_char
        self.end_char = end_char

    @property
    def full_path(self) -> str:
        """
        Returns: The full path of a JSONPath match
        """
        return self.json_path