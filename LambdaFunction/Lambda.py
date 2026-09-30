policies = [
    {"policy_id": "POL1001", "customer": "Ravi", "coverage": 1000},
    {"policy_id": "POL1002", "customer": "Amit", "coverage": 500},
]
discounted_policies=list(
    map(
        lambda p:{
            **p,
            "coverage": p["coverage"] * 0.90
    
        },
        policies
    )
)
print(discounted_policies)

print("\nfiltering policies with coverage greater than 700\n")

high_coverage = list(
    filter(
        lambda policy: policy["coverage"] > 700,
        policies
    )
)

print(high_coverage)

print("\nSorting policies by coverage\n")
sorted_policies = sorted(
    policies,
    key=lambda policy: policy["coverage"]
)

print(sorted_policies)