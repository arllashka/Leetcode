class Solution:
    # O(n)
    def plusOne(self, di: List[int]) -> List[int]:
        num=0
        ans=[]
        for i in di:
            num=num*10+i
        num+=1
        for j in str(num):
            ans.append(int(j))
        return ans