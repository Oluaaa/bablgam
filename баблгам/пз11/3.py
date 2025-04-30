class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self.current_line = ""
        self.lines = []

    def add(self, words):
        for word in words.split():
            if len(self.current_line) + len(word) + (1 if self.current_line else 0) > self.length:
                self.lines.append(self.current_line)
                self.current_line = word
            else:
                if self.current_line:
                    self.current_line += " "
                self.current_line += word

    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)
        for line in self.lines:
            print(line)
        self.lines.clear()
        self.current_line = ""


class RightParagraph:
    def __init__(self, length):
        self.length = length
        self.current_line = ""
        self.lines = []

    def add(self, words):
        for word in words.split():
            if len(self.current_line) + len(word) + (1 if self.current_line else 0) > self.length:
                self.lines.append(self.current_line)
                self.current_line = word
            else:
                if self.current_line:
                    self.current_line += " "
                self.current_line += word

    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)
        for line in self.lines:
            print(line.rjust(self.length))
        self.lines.clear()
        self.current_line = ""


leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()

leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()
