class Solution:
    def interpret1(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

    def interpret(self, command: str) -> str:
        result = ''
        n = len(command)
        i = 0
        while i < n:
            if command[i] == 'G':
                result += 'G'
            if command[i] == '(':
                if command[i + 1] == ')':
                    result += 'o'
                    i += 1
                else:
                    result += 'al'
                    i += 3
            i += 1
        return result


s = Solution()
print(s.interpret("G()(al)"))
print(s.interpret("G()()()()(al)"))
print(s.interpret("(al)G(al)()()G"))
