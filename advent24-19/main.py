# Check if a design is possible given a list of patterns
def is_possible(design, patterns):
    # Get the length of the design string
    n = len(design)
    # Create a list to track if we can make each prefix
    dp = [False] * (n + 1)
    dp[0] = True
    # Loop over each starting position in the design
    for i in range(n):
        # If there’s at least one way to reach position i
        if dp[i]:
            # Try each pattern from position i
            for p in patterns:
                # Get length of the current pattern
                p_len = len(p)
                # Check if pattern fits and matches the design substring
                if i + p_len <= n and design[i:i + p_len] == p:
                    dp[i + p_len] = True
    # Return if we can make the full design or not
    return dp[n]

# Read the file input and split into patterns and designs..
def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    
    # Split the first line by commas, remove extra whitespace patterns
    patterns = [p.strip() for p in lines[0].split(',')]
    # Take all lines after the blank line (index 2), skipping empty ones
    designs = [d for d in lines[2:] if d.strip()]
    return patterns, designs

# Count the number of possible designs.
def count_possible_designs(filename):
    patterns, designs = read_input(filename)
    # Count how many designs can be made (sum 1 for each design where is_possible returns True)
    count = sum(1 for design in designs if is_possible(design, patterns))
    
    print(f"Total possible designs: {count}")

# Count the number of ways a specific design can be created using the given patterns. 
# Same is is_possible function but uses accumulating integer count rather than boolean.
def design_possibilities(design, patterns):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1 
    for i in range(n):
        if dp[i] > 0:
            for p in patterns:
                p_len = len(p)
                if i + p_len <= n and design[i:i + p_len] == p:
                    dp[i + p_len] += dp[i]
    return dp[n]

# Calculate the total number of design possibilities
def calculate_all_design_possibilities(filename):
    patterns, designs = read_input(filename)
    
    # Number of possibilities using design as the dictionary key
    design_counts = {}
    total_design_possibilities = 0
    
    for design in designs:
        # Calculate how many possible ways each design can be made
        possibilities = design_possibilities(design, patterns)
        # Store the number of possibilities
        design_counts[design] = possibilities  
        # Add possibilites to the total
        total_design_possibilities += possibilities
    
    print(f"Total possibilities to create all designs: {total_design_possibilities}")

# Set filename with patterns and designs to process
filename = 'towel-designs-patterns.txt'
print(f"Processing file: {filename}")

# Part 1: Count all the possible designs.
count_possible_designs(filename)

# Part 2: Calculate all the possibilities to create the designs
calculate_all_design_possibilities(filename)