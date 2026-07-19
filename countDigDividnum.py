class Solution(object):
    def countDigits(self, num):
    
       temp=num
       ans=0
       while temp>0:
        digit=temp%10
        if digit!=0 and num%digit==0:
            ans+=1
        temp//=10
       return ans 