from annoy import AnnoyIndex
import random

f = 40
t = AnnoyIndex(f, 'euclidean')  # Length of item vector that will be indexed
for i in range(1000):
    v = [random.gauss(0, 1) for z in range(f)]
    t.add_item(i, v)

t.build(10) # 10 trees
#t.save('test.ann')

# ...

#u = AnnoyIndex(f, 'angular')
#u.load('test.ann') # super fast, will just mmap the file
closest = t.get_nns_by_item(32, 2)
print(closest[1]) # will find the 1000 nearest neighbors
print(t.get_item_vector(closest[1]))
