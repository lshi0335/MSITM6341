def find_median(X):
    count = len(X)
    X_sorted = sorted(X)
    if count%2 == 0:
        mth = int(count/2)
        median = (X_sorted[mth-1]+X_sorted[mth])/2
    else:
        mth = int((count+1)/2)
        median = X_sorted[mth-1]
        # Alternatively:
        # mth = count//2
        # median = X_sorted[mth]
    return median

A = [1,3,5,19,21,14,6]

print('Input List: ' + str(A))
print('Sorted List: ' + str(sorted(A)))
print('Median: ' + str(find_median(A)))

B = [1,3,5,19,21,14,6,123]

print('Input List: ' + str(B))
print('Sorted List: ' + str(sorted(B)))
print('Median: ' + str(find_median(B)))


