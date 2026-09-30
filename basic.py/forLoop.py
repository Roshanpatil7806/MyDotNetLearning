list=[12,35,67,45]
print("List:", list)
nonvoters=[]
voters=[]
for i in list:
    if i<18:
        nonvoters.append(i)
    else:
        voters.append(i)
print("Non-voters:", nonvoters)
print("Voters:", voters)