import math
import random

import matplotlib.pyplot as plt
import numpy as np

show_animation = True


class RTree(object):
    # Class to represent the explicit tree created
    # while sampling through the state space

    def _init_(self, start=None, lowerLimit=None, upperLimit=None,
                 resolution=1.0):

        if upperLimit is None:
            upperLimit = [10, 10]
        if lowerLimit is None:
            lowerLimit = [0, 0]
        if start is None:
            start = [0, 0]
        self.vertices = dict()
        self.edges = []
        self.start = start
        self.lowerLimit = lowerLimit
        self.upperLimit = upperLimit
        self.dimension = len(lowerLimit)
        self.num_cells = [0] * self.dimension
        self.resolution = resolution
        # compute the number of grid cells based on the limits and
        # resolution given
        for idx in range(self.dimension):
            self.num_cells[idx] = np.ceil(
                (upperLimit[idx] - lowerLimit[idx]) / resolution)

        vertex_id = self.real_world_to_node_id(start)
        self.vertices[vertex_id] = []

    @staticmethod
    def get_root_id():
        # return the id of the root of the tree
        return 0

    def add_vertex(self, vertex):
        # add a vertex to the tree
        vertex_id = self.real_world_to_node_id(vertex)
        self.vertices[vertex_id] = []
        return vertex_id

    def add_edge(self, v, x):
        # create an edge between v and x vertices
        if (v, x) not in self.edges:
            self.edges.append((v, x))
        # since the tree is undirected
        self.vertices[v].append(x)
        self.vertices[x].append(v)

    def real_coords_to_grid_coord(self, real_coord):
        # convert real world coordinates to grid space
        # depends on the resolution of the grid
        # the output is the same as real world coords if the resolution
        # is set to 1
        coord = [0] * self.dimension
        for i in range(len(coord)):
            start = self.lowerLimit[i]  # start of the grid space
            coord[i] = int(np.around((real_coord[i] - start) / self.resolution))
        return coord

    def grid_coordinate_to_node_id(self, coord):
        # This function maps a grid coordinate to a unique
        # node id
        nodeId = 0
        for i in range(len(coord) - 1, -1, -1):
            product = 1
            for j in range(0, i):
                product = product * self.num_cells[j]
            nodeId = nodeId + coord[i] * product
        return nodeId

    def real_world_to_node_id(self, real_coord):
        # first convert the given coordinates to grid space and then
        # convert the grid space coordinates to a unique node id
        return self.grid_coordinate_to_node_id(
            self.real_coords_to_grid_coord(real_coord))

    def grid_coord_to_real_world_coord(self, coord):
        # This function maps a grid coordinate in discrete space
        # to a configuration in the full configuration space
        config = [0] * self.dimension
        for i in range(0, len(coord)):
            # start of the real world / configuration space
            start = self.lowerLimit[i]
            # step from the coordinate in the grid
            grid_step = self.resolution * coord[i]
            config[i] = start + grid_step
        return config

    def node_id_to_grid_coord(self, node_id):
        # This function maps a node id to the associated
        # grid coordinate
        coord = [0] * len(self.lowerLimit)
        for i in range(len(coord) - 1, -1, -1):
            # Get the product of the grid space maximums
            prod = 1
            for j in range(0, i):
                prod = prod * self.num_cells[j]
            coord[i] = np.floor(node_id / prod)
            node_id = node_id - (coord[i] * prod)
        return coord

    def node_id_to_real_world_coord(self, nid):
        # This function maps a node in discrete space to a configuration
        # in the full configuration space
        return self.grid_coord_to_real_world_coord(
            self.node_id_to_grid_coord(nid))


class BITStar(object):

    def _init_(self, start, goal,
                 obstacleList, randArea, eta=2.0,
                 maxIter=80):
        self.start = start
        self.goal = goal

        self.min_rand = randArea[0]
        self.max_rand = randArea[1]
        self.max_iIter = maxIter
        self.obstacleList = obstacleList
        self.startId = None
        self.goalId = None

        self.vertex_queue = []
        self.edge_queue = []
        self.samples = dict()
        self.g_scores = dict()
        self.f_scores = dict()
        self.nodes = dict()
        self.r = float('inf')
        self.eta = eta  # tunable parameter
        self.unit_ball_measure = 1
        self.old_vertices = []

        # initialize tree
        lowerLimit = [randArea[0], randArea[0]]
        upperLimit = [randArea[1], randArea[1]]
        self.tree = RTree(start=start, lowerLimit=lowerLimit,
                          upperLimit=upperLimit, resolution=0.01)

    def setup_planning(self):
        self.startId = self.tree.real_world_to_node_id(self.start)
        self.goalId = self.tree.real_world_to_node_id(self.goal)

        # add goal to the samples
        self.samples[self.goalId] = self.goal
        self.g_scores[self.goalId] = float('inf')
        self.f_scores[self.goalId] = 0

        # add the start id to the tree
        self.tree.add_vertex(self.start)
        self.g_scores[self.startId] = 0
        self.f_scores[self.startId] = self.compute_heuristic_cost(
            self.startId, self.goalId)

        # max length we expect to find in our 'informed' sample space, starts as infinite
        cBest = self.g_scores[self.goalId]

        # Computing the sampling space
        cMin = math.hypot(self.start[0] - self.goal[0],
                          self.start[1] - self.goal[1]) / 1.5
        xCenter = np.array([[(self.start[0] + self.goal[0]) / 2.0],
                            [(self.start[1] + self.goal[1]) / 2.0], [0]])
        a1 = np.array([[(self.goal[0] - self.start[0]) / cMin],
                       [(self.goal[1] - self.start[1]) / cMin], [0]])
        eTheta = math.atan2(a1[1], a1[0])
        # first column of identity matrix transposed
        id1_t = np.array([1.0, 0.0, 0.0]).reshape(1, 3)
        M = np.dot(a1, id1_t)
        U, S, Vh = np.linalg.svd(M, True, True)
        C = np.dot(np.dot(U, np.diag(
            [1.0, 1.0, np.linalg.det(U) * np.linalg.det(np.transpose(Vh))])),
                   Vh)

        self.samples.update(self.informed_sample(
            200, cBest, cMin, xCenter, C))

        return eTheta, cMin, xCenter, C, cBest

    def setup_sample(self, iterations, foundGoal, cMin, xCenter, C, cBest):

        if len(self.vertex_queue) == 0 and len(self.edge_queue) == 0:
            print("Batch: ", iterations)
            # Using informed rrt star way of computing the samples
            self.r = 2.0
            if iterations != 0:
                if foundGoal:
                    # a better way to do this would be to make number of samples
                    # a function of cMin
                    m = 200
                    self.samples = dict()
                    self.samples[self.goalId] = self.goal
                else:
                    m = 100
                cBest = self.g_scores[self.goalId]
                self.samples.update(self.informed_sample(
                    m, cBest, cMin, xCenter, C))

            # make the old vertices the new vertices
            self.old_vertices += self.tree.vertices.keys()
            # add the vertices to the vertex queue
            for nid in self.tree.vertices.keys():
                if nid not in self.vertex_queue:
                    self.vertex_queue.append(nid)
        return cBest

    def plan(self, animation=True):

        eTheta, cMin, xCenter, C, cBest = self.setup_planning()
        iterations = 0

        foundGoal = False
        # run until done
        while iterations < self.max_iIter:
            cBest = self.setup_sample(iterations,
                                      foundGoal, cMin, xCenter, C, cBest)
            # expand the best vertices until an edge is better than the vertex
            # this is done because the vertex cost represents the lower bound
            # on the edge cost
            while self.best_vertex_queue_value() <= \
                    self.best_edge_queue_value():
                self.expand_vertex(self.best_in_vertex_queue())

            # add the best edge to the tree
            bestEdge = self.best_in_edge_queue()
            self.edge_queue.remove(bestEdge)

            # Check if this can improve the current solution
            estimatedCostOfVertex = self.g_scores[bestEdge[
                0]] + self.compute_distance_cost(
                bestEdge[0], bestEdge[1]) + self.compute_heuristic_cost(
