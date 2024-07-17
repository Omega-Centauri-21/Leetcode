class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        
        for ele in s:
            if ele ==")":
                if st and st[-1] == "(":
                    st.pop()

                else:
                    st.append(ele)
            else:
                st.append(ele)
        return len(st)
