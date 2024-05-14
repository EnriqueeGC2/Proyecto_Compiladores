class Symbol:
    def __init__(self, value, type=None, scope=None, visibility=None, role=None, line=None, column=None, size=None):
        self.value = value
        self.type = type
        self.scope = scope
        self.visibility = visibility
        self.role = role
        self.line = line
        self.column = column
        self.size = size

def __str__(self):
    return f'{self.name} {self.type} {self.scope} {self.visibility} {self.role} {self.line} {self.column} {self.size}'
