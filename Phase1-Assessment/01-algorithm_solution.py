"""

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
"""

def sort_zeros(arr):
    n = len(arr)
    for i in range(n):
 
        for j in range(0, n-i-1):
            if arr[j] == 0 :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



vec =  [0, 0, 0, 7, 5, 3, 9, 0, 4]
vec2 = [3, 4, 0, 7, 5, 3, 9, 0, 4]
vec3 = [1, 2, 3, 7, 5, 3, 9, 3, 4]
vec4 = [0, 0, 0, 7, 0, 0, 0, 0, 0]
vec5 = [0, 0, 0, 7, 0, 0, 0, 0, 0]

print(sort_zeros(vec))
print(sort_zeros(vec2))
print(sort_zeros(vec3))
print(sort_zeros(vec4))
print(sort_zeros(vec5))
