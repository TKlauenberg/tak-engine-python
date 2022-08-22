from .grammar import grammar


class Tag:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value

    def get_key(self):
        return str.lower(self.name)

    @staticmethod
    def parse(tagString: str):
        parts = grammar['tagGrouped'].match(tagString)
        if not parts:
            return (False, "Tag could not be parsed")
        (name, value) = parts.group(2, 5)
        return (True, Tag(name, value))
