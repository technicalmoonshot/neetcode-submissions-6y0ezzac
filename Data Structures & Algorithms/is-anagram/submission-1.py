class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # counter_s = {}

        # counter_t = {}

        # for char in s:
        #     counter_s[char] = 1 +  counter_s.get(char,0)
        # for char in t:
        #     counter_t[char] = 1 +  counter_t.get(char,0)

        # if counter_s == counter_t:
        #     return True 
        # else:
        #     return False


        if len(s)!= len(t):
            return False
        
        counter_s, counter_t = {},{}

        for char in s:
            counter_s[char] = 1 + counter_s.get(char,0)
        for char in t:
            counter_t[char] = 1 + counter_t.get(char,0)

        if counter_s == counter_t:
            return True
        else:
            return False



      


        