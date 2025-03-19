from collections import Counter

def calculate_distance_score(filename):
    with open(filename, 'r') as f:
        left, right = zip(*[map(int, line.split()) for line in f])
    
    # Part 1
    total_distance = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))
    
    # Part 2
    right_counts = Counter(right)
    similarity_score = sum(num * right_counts[num] for num in left)
    
    return total_distance, similarity_score

distance, score = calculate_distance_score('number-pairs.txt')
print(f"Total distance: {distance}")
print(f"Similarity score: {score}")