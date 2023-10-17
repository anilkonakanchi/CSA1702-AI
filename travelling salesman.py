import itertools

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += distances[order[i]][order[i + 1]]
    total_distance += distances[order[-1]][order[0]]
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    if num_cities <= 2:
        return list(range(num_cities))

    cities = list(range(num_cities))
    shortest_path = None
    shortest_distance = float('inf')

    for perm in itertools.permutations(cities[1:]):
        order = [cities[0]] + list(perm)
        distance = calculate_total_distance(order, distances)

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = order

    return shortest_path, shortest_distance

if __name__ == '__main__':
    distances = [
        [0, 29, 20, 21],
        [29, 0, 15, 18],
        [20, 15, 0, 17],
        [21, 18, 17, 0]
    ]

    shortest_path, shortest_distance = traveling_salesman_bruteforce(distances)

    print(f"Shortest Path: {shortest_path}")
    print(f"Shortest Distance: {shortest_distance}")
