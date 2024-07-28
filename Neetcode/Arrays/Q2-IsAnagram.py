'''
This is the Brute force implementation and is not efficient

Time: O(n^3)
Space: O(n^2)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_letters = {}
        t_letters = {}

        for s_letter in s:
            if s_letter not in s_letters:
                s_letters[s_letter] = 1
            else:
                s_letters[s_letter] += 1

        for t_letter in t:
            if t_letter not in t_letters:
                t_letters[t_letter] = 1
            else:
                t_letters[t_letter] += 1

        for key in s:
            if(key not in t_letters):
                return False
            
            elif(s_letters[key] != t_letters[key]):
                return False
            
        return True
    

"""
Here is the more efficient method:

1. check if str same len, if not return false
2. create two dicts countS and Count2
3. fill these dicts 
"""
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool;
        # check if the the len is the same, if not cant have same letters

        if len(s) != len(t):
            return False
        
        #create dicts to hold letters
        countS, countT = {}, {}

        # loop and fill dicts
        for i in range(len(s)):
            # this line adds one to ith key in dict or
            # if it does not exist the get function returns a zero and the entry is added to dict
            countS[s[i]] = 1 + countS.get(s[i,0])

            countT[t[i]] = 1 + countT.get(s[i],0)

            return countS == countT
        



        
        
