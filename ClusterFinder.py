def get_length(vector):
    return (vector[0] ** 2 + vector[0] ** 2) ** 0.5


def dist(a_vec, b_vec):
    return get_length([b_vec[0] - a_vec[0], b_vec[1] - a_vec[1]])


def find_closest_dot(a_vec, all_dots):
    min_num = float('inf')
    index = -1
    if len(all_dots) <= 1:
        return [id, min_num]
    for dot_vec in range(len(all_dots)):
        distance = dist(a_vec, all_dots[dot_vec])
        if distance < min_num and a_vec != all_dots[dot_vec]:
            min_num = distance
            index = dot_vec
    return [index, min_num]


def find_closest_cluster(a_vec, cls):
    if len(cls) == 0:
        return [-1, float('inf')]
    min_num = float('inf')
    index = -1
    for cl in range(len(cls)):
        closest = find_closest_dot(a_vec, cls[cl])
        if closest[1] < min_num:
            index = cl
            min_num = closest[1]
    return [index, min_num]


initialDots = [
    [17, 17],
    [16, 16],
    [2, 2],
    [1, 1],
    [0.5, 1],
    [-10, -10],
    [-9, -8],
    [-11.5, -9],
    [-9, -9]
]

clusterMergingBias = float(input("\nEnter cluster merging distance bias (type '-1' to set fixed number of clusters): "))
if clusterMergingBias < 0:
    numberOfClusters = int(input("Enter number of clusters: "))
else:
    numberOfClusters = 1

clusters = []
dots = initialDots.copy()

while len(dots) > 1:
    dot = dots[0]
    closest_dot = find_closest_dot(dot, dots)
    cluster = find_closest_cluster(dot, clusters)
    if cluster[1] < closest_dot[1]:
        clusters[cluster[0]].append(dot)
        dots.remove(dot)
    else:
        clusters.append([dots[int(closest_dot[0])], dot])
        dots.pop(int(closest_dot[0]))
        dots.remove(dot)

if len(dots) == 1 and len(clusters) > 0:
    clusters[find_closest_cluster(dots[0], clusters)[0]].append(dots[0])
    dots.clear()

while (len(clusters) > numberOfClusters or clusterMergingBias >= 0 ) and len(clusters) > 1:
    minimalCl = float('inf')
    idA = -1
    idB = -1
    for a in range(len(clusters)):
        for b in range(len(clusters)):
            if a != b:
                for dot in clusters[a]:
                    closestDot = find_closest_dot(dot, clusters[b])
                    if closestDot[1] < minimalCl:
                        minimalCl = closestDot[1]
                        idA = a
                        idB = b
    if minimalCl > clusterMergingBias >= 0:
        break
    if idA != -1:
        dotsA = clusters[idA].copy()
        for dot in dotsA:
            clusters[idB].append(dot)
        clusters.pop(idA)

for i in range(len(clusters)):
    print(f"\nCluster number {i + 1}:")
    for dot in clusters[i]:
        print("\t", dot[0], dot[1])
