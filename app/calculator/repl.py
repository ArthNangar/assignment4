"""
Author: Arth Nangar
Date: 2025-09-30
REPL interface for calculator
"""

from app.calculation.calculation import CalculationFactory


class CalculatorREPL:
    def __init__(self):
        self.history = []

    def run(self):
        print("Welcome to Calculator! Type 'help' for commands.")
        while True:
            try:
                command = input(">>> ").strip().lower()
                if command == "exit":
                    print("Goodbye!")
                    break
                elif command == "help":
                    self.show_help()
                # if command == "history":  
                #     self.show_history()     # pragma: no cover
                #     continue
                if command == "history": # pragma: no cover
                    for h in self.history:  # pragma: nocover
                        print(h) if self.history else print("No history available.")  # pragma: nocover
                    continue  

                else:
                    self.handle_command(command) 
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")

    def show_help(self):
        print("Commands:")
        print(" add a b   -> Add numbers")
        print(" sub a b   -> Subtract numbers")
        print(" mul a b   -> Multiply numbers")
        print(" div a b   -> Divide numbers")
        print(" pow a b   -> a raised to power b")
        print(" mod a b   -> a modulo b")
        print(" history   -> Show history")
        print(" help      -> Show this help")
        print(" exit      -> Quit program")

    def show_history(self):
        if not self.history:
            print("No history available.")
        else:
            for h in self.history:
                print(h)

    def handle_command(self, command: str):
        parts = command.split()
        if len(parts) != 3:
            raise ValueError("Invalid format. Example: add 2 3")
        op, a, b = parts
        calc = CalculationFactory.create(a, b, op)
        result = calc.perform()
        entry = f"{op} {float(a)} {float(b)} = {result}"
        print(entry)
        self.history.append(entry)

if __name__ == "__main__":  # pragma: no cover
    repl = CalculatorREPL()
    repl.run()
