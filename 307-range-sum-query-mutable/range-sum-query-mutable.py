class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.tree = [0] * (4 * self.n) 
        self.build(0, 0, self.n - 1)

    def getChildren(self, node):
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        return left_child, right_child

    def build(self, node, nLeft, nRight):
        if nLeft == nRight:
            self.tree[node] = self.arr[nLeft]
            return

        nMid = (nLeft + nRight) // 2
        left_child, right_child = self.getChildren(node)

        self.build(left_child, nLeft, nMid)
        self.build(right_child, nMid + 1, nRight)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]  

    def update(self, node, nLeft, nRight, index, value):
        if nLeft == nRight:
            self.arr[index] = value
            self.tree[node] = value
            return

        nMid = (nLeft + nRight) // 2
        left_child, right_child = self.getChildren(node)

        if index <= nMid:
            self.update(left_child, nLeft, nMid, index, value)
        else:
            self.update(right_child, nMid + 1, nRight, index, value)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, node, nLeft, nRight, qLeft, qRight):
        if qLeft > nRight or qRight < nLeft:
            return 0  

        if qLeft <= nLeft and nRight <= qRight:
            return self.tree[node]

        nMid = (nLeft + nRight) // 2
        left_child, right_child = self.getChildren(node)

        left_sum = self.query(left_child, nLeft, nMid, qLeft, min(nMid, qRight))
        right_sum = self.query(right_child, nMid + 1, nRight, max(nMid + 1, qLeft), qRight)

        return left_sum + right_sum

class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(0, 0, len(self.tree.arr) - 1, index, val)  
    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(0, 0, len(self.tree.arr) - 1, left, right)  
