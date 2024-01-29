class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        cs={")":"(","}":"{","]":"["}
        for c in s:
            if c in cs:
                if a and a[-1]==cs[c]:
                    a.pop()
                else:
                    return False  
            else:
                a.append(c)
            
        # print(a)
        if not a:
            return True
        else:
            return False

############## other way #################


class Solution:
    def isValid(self, s: str) -> bool:
        my_string=s
        brackets = ['()', '{}', '[]']
        while any(x in my_string for x in brackets):
            for br in brackets:
                my_string = my_string.replace(br, '')
        return not my_string

