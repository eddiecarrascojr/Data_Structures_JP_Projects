# Postfix expression to Prefix expression class
class PostfixToPrefix:
    def __init__(self):
        # Easier to use set to look for in list for boolean check later
        self.operators = set(['+', '-', '*', '/', '$'])

    def is_operator(self, char) -> bool:
        """
        :param char: a single char
        :return: returns a boolean if this is an operator
        """
        return char in self.operators

    def convert(self, postfix_expr):
        """
        :param postfix_expr: a postfix expression
        :return: a prefix expression
        """
        # Remove any whitespace
        postfix_expr = postfix_expr.strip()

        if not postfix_expr:
            return ""

        # Use list as stack for processing
        stack = []

        # Process the expression from left to right (recursively)
        result = self._convert_recursive(postfix_expr, 0, stack)

        # The final result should be the only item left in the stack
        if len(stack) == 1:
            return stack[0]
        else:
            raise ValueError("Invalid postfix expression check the stack {}".format(stack))

    def _convert_recursive(self, postfix_expr, current_pos, stack):
        """
        :param postfix_expr: input of a postfix expression
        :param current_pos: current location of the stack postfix expression in stack for recursive use
        :param stack: a stack of postfix expressions used for the recursive call
        :return:
        """
        # Base case: if we've processed the entire expression
        if current_pos >= len(postfix_expr):
            return current_pos

        # Get the current character
        current_char = postfix_expr[current_pos]

        # If the current character is an operand, push it to the stack
        if not self.is_operator(current_char):
            stack.append(current_char)
        else:
            # If fewer than 2 operands are available, the expression is invalid
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression: not enough operands")

            # Pop the two operands (in reverse order as this is postfix)
            top_value = stack.pop() # First value of stack
            bottom_value = stack.pop() # second value of stack

            # Create the new prefix value
            prefix_expr = current_char + top_value + bottom_value

            # return the value in stack
            stack.append(prefix_expr)

        # Recursively process the next character
        return self._convert_recursive(postfix_expr, current_pos + 1, stack)

