class Solution(object):
    def Armstrong(x):
        if x<0:
            return False
        
        num=n
        result=0
        nod=len(str(n))

        while num>0:
            ld=num%10
            result=result+(ld**nod)
            num=num//10

        return n==result    