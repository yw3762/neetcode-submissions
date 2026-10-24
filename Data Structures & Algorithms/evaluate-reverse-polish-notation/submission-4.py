class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for op in tokens:
            if op == '+':
                st.append(st.pop(-1) + st.pop(-1))
            elif op == '-':
                st.append(-st.pop(-1) + st.pop(-1))
            elif op == '*':
                st.append(st.pop(-1) * st.pop(-1))
            elif op == '/':
                num2 = st.pop(-1)
                num1 = st.pop(-1)
                st.append(int(num1 / num2))
            else:
                st.append(int(op))
        return st[0]