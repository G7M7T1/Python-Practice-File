from collections import defaultdict


def default_factory():
    return "This is not defined"


d = defaultdict(default_factory)
d["a"] = 1
d["b"] = 2

print(d["a"], d["b"], d["c"])

# or ----------------------------------

Harry = defaultdict(lambda: "Wrong key!!")
print(Harry["3"])
