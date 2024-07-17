class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        insertions = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            else:  # s[i] == ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1  # Move to the next character
                else:
                    insertions += 1  # We need one more ')'
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    insertions += 1  # We need an extra '('
            i += 1
        # For any remaining '(' in the stack, we need to add '))' for each '('
        insertions += len(stack) * 2
        return insertions


