# States (variables)
states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Neighbour relationships
adjacent_states = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q' : ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Colors (domain)
color_list = ['Red', 'Green', 'Blue']
domain_map = {s: color_list[:] for s in states}

# ---------------- VALIDATION ----------------
def check_valid(state, color, assigned):
    for neighbour in adjacent_states[state]:
        if neighbour in assigned and assigned[neighbour] == color:
            return False
    return True

# ---------------- BACKTRACKING ----------------
def solve_csp(assigned):
    if len(assigned) == len(states):
        return assigned

    # pick unassigned state
    current_state = next(s for s in states if s not in assigned)

    for col in domain_map[current_state]:
        if check_valid(current_state, col, assigned):
            assigned[current_state] = col

            result = solve_csp(assigned)
            if result:
                return result

            del assigned[current_state]  # backtrack

    return None

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("CSP Problem: Map Coloring")

    answer = solve_csp({})

    print("\nSolution:")
    if answer:
        for st, col in answer.items():
            print(f"{st} -> {col}")



        # Check constraints
        valid = all(
            answer[s] != answer[n]
            for s in states
            for n in adjacent_states[s]
            if n in answer
        )

        print("\nConstraints satisfied:", valid)
    else:
        print("No solution found")