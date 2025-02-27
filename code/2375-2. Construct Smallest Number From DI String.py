# Regulated Brute Force via Recursion | solution of editorial
# The print in the code is just to help understand the state of recursion 
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.result = []

        # Start building the sequence by calling the helper function
        self.build_sequence(0, 0, pattern)
        # Reverse the final result
        return "".join(self.result[::-1])

    # Recursively build the sequence
    def build_sequence(
        self, current_index: int, current_count: int, pattern: str
    ) -> int:
        if current_index != len(pattern):
            if pattern[current_index] == "I":
                # If 'I', increment the count and move to the next index
                print('I', current_index, '|', current_count)
                self.build_sequence(current_index + 1, current_index + 1, pattern)
            else:
                # If 'D', keep the count and move to the next index
                print('D', current_index, '|', current_count)
                current_count = self.build_sequence(
                    current_index + 1, current_count, pattern
                )
        
        print(current_index, '|', current_count, 'D')
        self.result.append(str(current_count + 1))
        print('append', current_count + 1)

        # Return the next count for the sequence
        return current_count + 1

