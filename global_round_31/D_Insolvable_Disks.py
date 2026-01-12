import sys

# Set recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    iterator = iter(data)

    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    out = []

    for _ in range(num_test_cases):
        try:
            n = int(next(iterator))
            a = []
            for _ in range(n):
                a.append(int(next(iterator)))
        except StopIteration:
            break

        if n < 2:
            out.append("0")
            continue

        # Calculate gaps between points
        # gap[i] is the distance between point i and i+1
        gaps = []
        for i in range(n - 1):
            gaps.append(a[i+1] - a[i])

        total_tangent_pairs = 0

        # Current valid range for the 'left' radius of the current connection
        # We model the constraint: min_r < r_left < max_r
        # Initially, for a new chain starting at a gap D, r_left can be (0, D)
        min_r = 0
        max_r = float('inf')

        # We track the length of the current valid chain of edges
        current_chain_len = 0

        # Iterate through every gap to see if we can extend the chain
        for val in gaps:
            # If we are starting a new chain (current_chain_len == 0)
            if current_chain_len == 0:
                # The radius must be positive and less than the gap size
                min_r = 0
                max_r = val
                current_chain_len = 1
            else:
                # We are extending a chain.
                # Previous constraint was: min_r < r_prev < max_r
                # New equation: r_prev + r_curr = val  =>  r_curr = val - r_prev
                # So new bounds are:
                # val - max_r < r_curr < val - min_r

                new_min = val - max_r
                new_max = val - min_r

                # Intersect with the physical constraint that radius > 0
                # r_curr must be between (0, val) as well

                final_min = max(0, new_min)
                final_max = min(val, new_max)

                if final_min < final_max:
                    # Valid extension found
                    min_r = final_min
                    max_r = final_max
                    current_chain_len += 1
                else:
                    # Impossible to extend chain.
                    # Add the accumulated edges to total
                    total_tangent_pairs += current_chain_len

                    # Start a new chain completely ignoring the previous connection
                    # This gap becomes the first link of a new chain
                    min_r = 0
                    max_r = val
                    current_chain_len = 1

        # Add the last chain processed
        total_tangent_pairs += current_chain_len

        out.append(str(total_tangent_pairs))

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()