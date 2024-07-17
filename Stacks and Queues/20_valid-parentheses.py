class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {")":"(", "]":"[", "}":"{"}
        for ele in s:
            if ele in d:
                f_ele = st.pop() if st else None
                if d[ele] != f_ele:
                    return False
            else:
                st.append(ele)
            
        return not st
        
