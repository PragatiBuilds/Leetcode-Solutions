class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        ans = []
        for i in range(len(order)):
            if order[i] in friends_set:
                ans.append(order[i])
            
        return ans
        