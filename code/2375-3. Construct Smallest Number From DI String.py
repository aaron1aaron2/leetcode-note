# The same concept as recursion is implemented by stack | code by editorial
# The print in the code is just to help understand the status of the stack
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        num_stack = []

        # Iterate through the pattern
        for index in range(len(pattern) + 1):
            print("-"*10, f'iter{index}', "-"*10)
            # Push the next number onto the stack
            num_stack.append(index + 1)
            print('stack:', num_stack)

            # If 'I' is encountered or we reach the end, pop all stack elements
            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    result.append(str(num_stack.pop()))
                    print('result:', result)


        return "".join(result)
