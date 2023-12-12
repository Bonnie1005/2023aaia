#LeetCode 1688. Count of matches in Tournament
#因為是淘汰賽，n隊的話，只要n-1場，就得到肝進了
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1 