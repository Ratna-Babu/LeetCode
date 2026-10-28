class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        for a, b in prerequisites:
            is_prerequisite[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True
        return [is_prerequisite[u][v] for u, v in queries]