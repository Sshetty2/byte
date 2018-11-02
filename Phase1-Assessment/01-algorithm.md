## Implement an algorithm

* Write an algorithm without using ```sort``` or ```sorted```
that shifts all of the zeros in a list to the end. Do not create
a new list, manipulate the values in-place.

So for instance:

```
1, 0, 7, 2, 0, 3, 9, 0, 4
```

will be rearranged as:

```
1, 7, 2, 3, 9, 4, 0, 0, 0
```

* Again, your algorithm should not create a new list, but rather rearrange the one it is given.

```
def sortzeros(vector):
    # implement this
    pass

vec = [1, 0, 7, 2, 0, 3, 9, 0, 4]
sortzeros(vec)

assert vec == [1, 7, 2, 3, 9, 4, 0, 0, 0]
```
