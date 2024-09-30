class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        for p in "!?',;.":
            paragraph = paragraph.replace(p, " ")
    
        paragraph = paragraph.lower().split() 
        paragraph = [word for word in paragraph if word not in banned]
        
        return Counter(paragraph).most_common(1)[0][0]
