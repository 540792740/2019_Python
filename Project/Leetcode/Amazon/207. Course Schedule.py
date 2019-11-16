import collections

def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for i, j in prerequisites:
        graph[j].append(i)
    visited = [0] * numCourses

    def dfs( i):
        # visited == 1, is going to take the course
        # visited == 2, finished courses
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not dfs(j):
                return False
        visited[i] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


# 15%
def canFinish2(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # Init Grapg to save all pre courses need
    graph = collections.defaultdict(list)
    pre_need = collections.defaultdict(int)
    for i, j in prerequisites:
        graph[j].append(i)
        pre_need[i] += 1
    # Traverse all Node
    for i in range(numCourses):
        course_avaliable = False
        for j in range(numCourses):
            if pre_need[j] == 0:
                course_avaliable = True
                break
        # If there is a course still need pre_course, return False
        if not course_avaliable: return False

        # Visited node value -1
        pre_need[j] = -1

        # -1 for all courses which need course[j]
        for node in graph[j]:
            pre_need[node] -= 1
    return True

print(canFinish(2, [[1,0],[0,1]]))