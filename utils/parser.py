from typing import Literal


class Parser:
    """Parser"""

    token: list[list[str]]
    parse_output: list[dict[str, str]] = []

    def __init__(self, token: list[list[str]]) -> None:
        """Initialization"""
        self.token = token

    def parse(self) -> list[dict[str, str]]:
        """Parses the token"""
        line_num = 0
        print(self.token)
        for line in self.token:
            # !Variable declaration
            if line[0] == "DECLARATION::new":
                if not line[-1] == "BREAK":
                    raise SyntaxError(f"Line {line_num+1}: No line break found")
                if not line[2] == "ASSIGNMENT":
                    raise SyntaxError(f"Line {line_num+1}: Did you mean to add ==")
                self.parse_output.append({})
                parse_item = self.parse_output[line_num]
                parse_item["type"] = "declaration"
                parse_item["variable_name"] = line[1].split("::")[-1]
                parse_item["variable_type"] = self.get_type(line)
                parse_item["variable_value"] = line[-2].split("::")[-1].replace("'", "")
            line_num += 1

        return self.parse_output

    @staticmethod
    def get_type(
        line_token: list[str],
    ) -> Literal["string"] | Literal["integer"] | Literal["none"]:
        """Gets type of assignment"""
        if line_token[1].split("::")[0] == "STR":
            return "string"
        if line_token[1].split("::")[0] == "INT":
            return "integer"
        return "none"
