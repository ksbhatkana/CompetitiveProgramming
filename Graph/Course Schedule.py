from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()  # Tracks nodes currently in the recursion stack

        def dfs(course):
            if course in visited:  # Cycle detected
                return False
            if not graph[course]:  # No prerequisites, course can be completed
                return True
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)  # Backtrack
            graph[course] = []  # Mark course as completed
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
