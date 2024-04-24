# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class DSU:
    def __init__(self, sz):
        self.representative = list(range(sz))
        self.size = [1] * sz

    def findRepresentative(self, x):
        if x == self.representative[x]:
            return x
        self.representative[x] = self.findRepresentative(self.representative[x])
        return self.representative[x]

    def unionBySize(self, a, b):
        representativeA = self.findRepresentative(a)
        representativeB = self.findRepresentative(b)

        if representativeA == representativeB:
            return

        if self.size[representativeA] >= self.size[representativeB]:
            self.size[representativeA] += self.size[representativeB]
            self.representative[representativeB] = representativeA
        else:
            self.size[representativeB] += self.size[representativeA]
            self.representative[representativeA] = representativeB
class Solution:

    def accountsMerge(self, accountList):
        n = len(accountList)
        dsu = DSU(n)

        emailGroup = defaultdict(int)

        for i in range(len(accountList)):
            accountName = accountList[i][0]
            j = len(accountList[i])
            for k in range(1, j):
                email = accountList[i][k]
                if email in emailGroup:
                    dsu.unionBySize(i, emailGroup[email])
                else:
                    emailGroup[email] = i

        mergedAccounts = defaultdict(list)
        for email, group in emailGroup.items():
            mergedAccounts[dsu.findRepresentative(group)].append(email)
        print(mergedAccounts)

        result = []
        for group, emails in mergedAccounts.items():
            accountName = accountList[group][0]
            mergedAccount = [accountName] + sorted(emails)
            result.append(mergedAccount)

        return result