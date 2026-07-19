class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        sum=0
        prod=1

        while temp>0:
            digit=temp%10
            sum+=digit
            prod*=digit
            temp=temp//10

            diff=prod-sum
        return diff 