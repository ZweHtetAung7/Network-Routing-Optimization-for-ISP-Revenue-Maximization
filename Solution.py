from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info


    def bfs(self, start, goal):
        queue = deque([start])
        visited = set([start])
        parent = {start: None}

        while queue:
            curr = queue.popleft()

            if curr == goal:
                break

            for neighbor in self.graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = curr
                    queue.append(neighbor)

        if goal not in parent:
            return []

        path = []
        curr = goal
        while curr is not None:
            path.append(curr)
            curr = parent[curr]

        path.reverse()
        return path


    def output_paths(self):
        """
        This method must be filled in by you. You may add other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        """
        paths, bandwidths, priorities = {}, {}, {}

        for client in self.info["list_clients"]:
            paths[client] = self.bfs(self.isp, client)

        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
