class Parser:
    """Parser"""

    token = []

    def __init__(self, token: list[list[str]]) -> None:
        """Initialization"""
        self.token = token

    def parse(self):
        """Parses the token"""
        for line in self.token:
            print(line)
