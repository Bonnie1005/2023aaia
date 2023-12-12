#每日挑戰提2023-12-01 把字串 .join() 起來， 看他們是否相同
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1)
        b = ''.join(word2)

        if a==b: return True #兩字相同，就成功
        else: return False #反之則失敗