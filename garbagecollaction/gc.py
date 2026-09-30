import sys          
import gc
"""
##2 object references are created for policy_1 and policy_2.
policy = {
    "policy_id": "POL1001",
    "customer": "Ravi",
    "coverage": 1000000
}
policy_2 = policy
 

policy["status"] ="active"

print(policy)
print(policy_2)

del policy_2


print(sys.getrefcount(policy))  
"""



"""
# in class, we can create a class to represent a policy and create two references to the same object
# . When we modify the object through one reference, the changes will be reflected in the other reference as well. Here's an example:
class policy:
    def __init__(self, policy_id, customer, coverage):
        self.policy_id = policy_id
        self.customer = customer
        self.coverage = coverage

policy_1 = policy("POL1001", "Ravi", 1000000)
policy_2 = policy_1
print(policy_1.__dict__)
print(policy_2.__dict__)
"""
import gc


class Customer:
    pass


class InsurancePolicy:
    pass


customer = Customer()
policy = InsurancePolicy()

customer.policy = policy
policy.customer = customer

print("Objects created")

del customer
del policy

print("References deleted")

collected = gc.collect()

print("Garbage collected:", collected)