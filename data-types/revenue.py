# Dictionary of lists storing monthly revenue for branches
revenue = {
    "Delhi": [50000, 62000, 58000, 61000],
    "Mumbai": [70000, 68000, 72000, 69000],
    "Noida": [45000, 47000, 49000, 51000]
}
# Find total revenue of each branch
totals = {}
for branch in revenue:
    totals[branch] = sum(revenue[branch])

# Find branch with highest total revenue
highest_branch = max(totals, key=totals.get)

# Display result
print("Total Revenue:", totals)
print("Branch with Highest Revenue:", highest_branch)
print("Highest Total Revenue:", totals[highest_branch])