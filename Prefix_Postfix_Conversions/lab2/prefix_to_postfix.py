# Using list we create a method to convert prefix expressions to postfix to expressions
class PrefixToPostfix:
    def __init__(self):
        # Easier to use set to look for in list for boolean check later
        self.operators = set(['+', '-', '*', '/', '$'])

    def is_operator(self, char) -> bool:
        """
        :param char: a single char
        :return: returns a boolean if this is an operator
        """
        return char in self.operators

    def convert(self, prefix_expr) -> list:
        """"
        :param prefix_expr: a prefix expression to be converted with helper function below
        :return:
        """
        # Remove any whitespace
        prefix_expr = prefix_expr.strip()

        # track the current position of stack
        self.current_pos = 0
        return self._convert_recursive(prefix_expr)


    def _convert_recursive(self, prefix_expr) -> list:
        """
        :param prefix_expr: the string value of the prefix expression
        :return: a stack of resulting postfix expressions using recursion
        """
        if self.current_pos >= len(prefix_expr):
            # Return nothing because this list is empty as base case
            return ""

        # Get the current character
        current_char = prefix_expr[self.current_pos]
        self.current_pos += 1

        # If the current character is an operator
        if current_char == ' ':
            print("Invalid character detected, check expression.")

        if self.is_operator(current_char):
            # Process left operand
            left_operand = self._convert_recursive(prefix_expr)

            # Process right operand
            right_operand = self._convert_recursive(prefix_expr)

            # Return operands followed by operator (postfix notation)
            return left_operand + right_operand + current_char
        else:
            # If the current character is an operand, return it as is
            return current_char