from numpy import amax, array, empty
from rpy2 import robjects
from scipy.spatial.distance import cosine


FNAME = 'subredsimdata.rdata'
robjects.r['load'](FNAME)

matrix = robjects.r['subsimmat']
rowNames = [n for n in matrix.names[0]]
colNames = [n for n in matrix.names[1]]

subInds = {k: v for v, k in enumerate(rowNames)}
vecs = array(matrix)


def sub_similarity(sub1, sub2):

    try:
        ind1 = subInds[sub1]
        ind2 = subInds[sub2]
        return 1 - cosine(vecs[ind1], vecs[ind2])
    except:
        print('subs not found')


def group_similarity(subs1, subs2):

    # take only subs contained in our dataset
    subs1 = [sub for sub in subs1 if sub in rowNames]
    subs2 = [sub for sub in subs2 if sub in rowNames]

    m = len(subs1)
    n = len(subs2)
    similarities = empty([m, n])

    # compute pairwise similarities between subs1 and subs2
    for i in range(m):
        for j in range(n):
            similarities[i, j] = sub_similarity(subs1[i], subs2[j])

    maxs1 = [amax(similarities[i]) for i in range(m)]
    maxs2 = [amax(similarities[:,j]) for j in range(n)]
    return sum(maxs1 + maxs2) / (m + n)
