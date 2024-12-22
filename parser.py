class TopDownParser:
    def __init__(self):
        self.grammar = {}  # Grammar rules
        self.start_symbol = None  # Starting symbol
    
    def input_grammar(self):
        """
        Allows the user to input grammar rules.
        """
        self.grammar = {}
        print("Enter grammar rules in the format: NonTerminal -> production1 | production2 ...")
        print("Type 'done' when you are finished.")
        
        while True:
            rule = input("Enter a rule: ").strip()
            if rule.lower() == 'done':
                break
            if '->' not in rule:
                print("Invalid format. Please try again.")
                continue
            
            # Parse the rule into non-terminal and productions
            non_terminal, productions = map(str.strip, rule.split('->', 1))
            productions = [prod.strip() for prod in productions.split('|')]
            self.grammar[non_terminal] = productions
        
        self.start_symbol = input("Enter the start symbol: ").strip()
        print("\nGrammar rules entered:")
        for nt, prods in self.grammar.items():
            print(f"{nt} -> {' | '.join(prods)}")
    
    def is_simple(self):
        """
        Checks if the grammar is simple (Simple Grammar).
        """
        for non_terminal, productions in self.grammar.items():
            for production in productions:
                # A production is simple if it contains only one symbol (Terminal or Non-Terminal)
                if len(production.split()) > 1:
                    return False
        return True
    
    def parse(self, sequence):
        """
        Parses a given sequence to check if it is accepted by the grammar.
        """
        def recursive_parse(current_symbol, remaining_sequence):
            # If no current symbol is left
            if not current_symbol:
                return not remaining_sequence  # Sequence should also be empty
            
            # If the sequence is empty
            if not remaining_sequence:
                return False
            
            # If the current symbol is a Terminal
            if current_symbol not in self.grammar:
                return remaining_sequence[0] == current_symbol and recursive_parse("", remaining_sequence[1:])
            
            # Try each production for the current Non-Terminal
            for production in self.grammar[current_symbol]:
                if recursive_parse(production, remaining_sequence):
                    return True
            return False

        return recursive_parse(self.start_symbol, sequence.split())
    
    def run(self):
        """
        Infinite loop for user interaction.
        """
        while True:
            print("\nChoose an option:")
            print("1. Enter new grammar rules")
            print("2. Check if the grammar is simple")
            print("3. Test a sequence")
            print("4. Exit the program")
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                self.input_grammar()
            elif choice == '2':
                if self.is_simple():
                    print("The grammar is simple (Simple Grammar).")
                else:
                    print("The grammar is not simple.")
            elif choice == '3':
                sequence = input("Enter the sequence: ").strip()
                if self.parse(sequence):
                    print("The sequence is Accepted.")
                else:
                    print("The sequence is Rejected.")
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
parser = TopDownParser()
parser.run()
