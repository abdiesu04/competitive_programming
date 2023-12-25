class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [x for x in range(1,n+1)]
        j = 0
        while len(friends) > 1:
            j = (j+k-1) % len(friends)
            friends.remove(friends[j])
        return friends[0]        