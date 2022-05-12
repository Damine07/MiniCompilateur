from TokenType import  *
class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText  # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind  # The TokenType that this token is classified as.

    @staticmethod
    def checkIfKeyword(tokenText):
            for kind in TokenType:
                # Relies on all keyword enum values being 1XX.
                if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                    return kind
            return None