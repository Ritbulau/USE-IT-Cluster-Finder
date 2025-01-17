from vector import *
class Cluster:
    def __init__(self, a, b):

        self.dotsIn = [a, b]

def findClosestDot(a: Vector2, dots):
    minimal = 99999999
    id = -1
    if len(dots) <= 1:
        return [id, minimal]
    for dot in range(len(dots)):
        distance = dist(a, dots[dot])
        if distance < minimal and a != dots[dot]:
            minimal = distance
            id = dot
    return [id, minimal]


def findClosestCluster(a: Vector2, clusters):
    if len(clusters) == 0:
        return [-1, 99999999]
    minimal = 99999999
    id = -1
    for cluster in range(len(clusters)):
        closest = findClosestDot(a, clusters[cluster].dotsIn)
        if closest[1] < minimal:
            id = cluster
            minimal = closest[1]
    return [id, minimal]








initialDots = [
    Vector2(17, 17),
    Vector2(16, 16),
    Vector2(2, 2),
    Vector2(1, 1),
    Vector2(0.5, 1),
    Vector2(-10, -10),
    Vector2(-9, -8),
    Vector2(-11.5, -9),
    Vector2(-9, -9)
]
numberOfClusters = 3

clusters = []
dots = initialDots.copy()

while len(dots) > 1:
    dot = dots[0]
    closestDot = findClosestDot(dot, dots)
    cluster = findClosestCluster(dot, clusters)
    if cluster[1] < closestDot[1]:
        print(f"Added to cluster (dot: {dot.x, dot.y}), {len(dots) - 1} dots left")
        clusters[cluster[0]].dotsIn.append(dot)
        dots.remove(dot)

    else:
        print( f"created cluster (dots: {dots[closestDot[0]].x, dots[closestDot[0]].y} and {dot.x, dot.y}), {len(dots) - 2} dots left")
        clusters.append(Cluster(dots[closestDot[0]], dot))
        dots.pop(closestDot[0])
        dots.remove(dot)

if len(dots) == 1 and len(clusters) > 0:
    clusters[findClosestCluster(dots[0], clusters)[0]].dotsIn.append(dots[0])
    print(f"Added to cluster (dot: {dots[0].x, dots[0].y})")
    dots.clear()

print("\n\n")


while len(clusters) > numberOfClusters:

    idA = -1
    idB = -1

    minimalCl = 999999

    for a in range(len(clusters)):
        for b in range(len(clusters)):
            if a != b:
                minimal = 999999
                for dot in clusters[a].dotsIn:
                    closestDot = findClosestDot(dot, clusters[b].dotsIn)
                    if closestDot[1] < minimal:
                        minimal = closestDot[1]
                if minimal < minimalCl:
                    idA = a
                    idB = b

    if idA != -1:
        dotsA = clusters[idA].dotsIn.copy()
        for dot in dotsA:
            clusters[idB].dotsIn.append(dot)
        clusters.pop(idA)


for cluster in clusters:
    for dot in cluster.dotsIn:
        print(dot.x, dot.y)
    print("\n")

# НЫНЕШНЯЯ ПРОБЛЕМА - КЛАСТЕРЫ СОЕДИНЯЮТСЯ НЕ ИЗХОДЯ ИЗ НАИМЕНЬШЕЙ ДАЛЬНОСТИ