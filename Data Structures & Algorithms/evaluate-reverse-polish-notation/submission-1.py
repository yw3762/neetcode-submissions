class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # def to_number(s: str):
        #     if(s[0] == '-'):
        #         if s[1:].isnumeric():
        #             return -1 * int(s[1:])
        #     else:
        #         if s.isnumeric():
        #             return int(s)
        #     return None
        
        st = []
        for token in tokens:
            if token == "+":
                num2 = st.pop()
                num1= st.pop()
                st.append(num1 + num2)
            elif token == '-':
                num2 = st.pop()
                num1= st.pop()
                st.append(num1 - num2)
            elif token == '*':
                num2 = st.pop()
                num1= st.pop()
                st.append(num1 * num2)
            elif token == "/":
                num2 = st.pop()
                num1= st.pop()
                st.append(int(num1/num2))
            else:
                st.append(int(token))

        return st[0]

                
