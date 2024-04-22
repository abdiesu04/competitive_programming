# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5',
                     '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}
        prev_slot = {'0': '9', '1': '0', '2': '1', '3': '2', '4': '3',
                     '5': '4', '6': '5', '7': '6', '8': '7', '9': '8'}

        visited = set(deadends)
        pending = deque()

        turns = 0

        if "0000" in visited:
            return -1

        pending.append("0000")
        visited.add("0000")

        while pending:
            for _ in range(len(pending)):
                current = pending.popleft()

                if current == target:
                    return turns

                for wheel in range(4):
                    new_combination = list(current)
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination = "".join(new_combination)
                    if new_combination not in visited:
                        pending.append(new_combination)
                        visited.add(new_combination)

                    new_combination = list(current)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination = "".join(new_combination)
                    if new_combination not in visited:
                        pending.append(new_combination)
                        visited.add(new_combination)

            turns += 1

        return -1