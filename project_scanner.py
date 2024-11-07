import re

class Token:
    def __init__(self, type, value):
        self.type = type  # Type of the token (e.g., KEYWORD, IDENTIFIER, etc.)
        self.value = value  # The actual string value of the token

    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}')"


class Lexer:
    # Define all token types and their corresponding regex patterns
    TOKEN_PATTERNS = [
        ("KEYWORD", r'\b(if|else|int|return|for|while|do|break|continue)\b'),
        ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
        ("NUMBER", r'\b\d+(\.\d+)?\b'),
        ("OPERATOR", r'[+\-*/=]'),
        ("COMPARISON", r'[<>]=?|==|!='),
        ("SYMBOL", r'[{}();,]'),
        ("STRING_LITERAL", r'\".*?\"'),
        ("WHITESPACE", r'\s+'),
        ("COMMENT", r'//.*?$|/\*.*?\*/')
    ]

    def __init__(self, code):
        self.code = code  # The code to be analyzed
        self.tokens = []  # List to hold generated tokens
        self.pos = 0      # Current position in the code string
        self.token_regex = [(label, re.compile(pattern)) for label, pattern in self.TOKEN_PATTERNS]

    def tokenize(self):
        # Main loop to scan the code
        while self.pos < len(self.code):
            match = None
            for label, regex in self.token_regex:
                match = regex.match(self.code, self.pos)
                if match:
                    text = match.group(0)
                    if label != "WHITESPACE" and label != "COMMENT":  # Skip whitespace and comments
                        token = Token(label, text)
                        self.tokens.append(token)
                    self.pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f"Unknown token at position {self.pos}: {self.code[self.pos]}")
        
        return self.tokens  # Return the list of tokens

# Take C code input from the user

print("Enter your C code below. Type 'END' on a new line to finish:")

lines = []
while True:
    line = input()  # Take each line as input
    if line.strip() == "END":  # Check if the user typed the specific end character
        break
    lines.append(line)  # Add the line to the list

# Join the lines to form the full code string
c_code = "\n".join(lines)

# Create a Lexer object and tokenize the code
lexer = Lexer(c_code)
tokens = lexer.tokenize()

# Print each token
for token in tokens:
    print(token)
