# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)

        tasks.sort(key=lambda task: task[0])

        result, min_heap = [], []
        task_index, current_time = 0, tasks[0][0]
        
        while min_heap or task_index < len(tasks):
            while task_index < len(tasks) and current_time >= tasks[task_index][0]:
                heappush(min_heap, (tasks[task_index][1], tasks[task_index][2]))
                task_index += 1

            if not min_heap:
                current_time = tasks[task_index][0]
            else:
                processing_time, index = heappop(min_heap)
                current_time += processing_time
                result.append(index)

        return result