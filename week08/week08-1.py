#題目給你數字 n 請回答 return True 還是 return False
#如果它是 2的很多次方 True ex. 1,2,4,8,16,32,64,128,......
#不是的話False ex. n % 2 餘數不是0就失敗了
#BUT 6不是 所以要把 n 慢慢變小。遇到負的、遇到0也會失敗
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:     
        if n<=0: # 遇到負的、遇到0也會失敗
            return False
        while n>1:
            if n % 2 != 0: # 餘數不是0,就失敗了
                return False
            else:
                n = n // 2 # 要變小

        return True