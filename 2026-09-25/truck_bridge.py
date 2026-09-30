a = int(input("max weight of a"))
b = int(input("max weight of b"))
c = int(input("max weight of c"))
d = int(input("max weight of d"))
e = int(input("max weight of e"))

route_1_limit = min(a, b, c)
route_2_limit = min (d, e)
optimal_weight = max(route_1_limit, route_2_limit)

print(f"maximum weight delivered: {optimal_weight} lbs")
if route_1_limit > route_2_limit:
    print("Route 1 is more ideal.")
elif route_2_limit > route_1_limit:
    print("Route 2 is more ideal.")
else:
    print("both are ideal")