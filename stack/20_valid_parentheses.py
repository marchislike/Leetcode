class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']':'['}

        for brkt in s:
            if brkt in bracket_map.values(): # 열린 괄호(value)
                stack.append(brkt)

            elif brkt in bracket_map: #닫힌 괄호(key)
            # stack이 비어있거나
            #해당 닫힌 괄호를 key로 삼아 조회했을 때 기존 스택에 매칭되는 value(=열린괄호)가 없다면
                if not stack or stack.pop() != bracket_map[brkt]: 
                    return False
        
        return not stack #모든 괄호가 정상적으로 닫히면 스택이 비워지므로
        # not stack이 맞으면 True, 아니면 False