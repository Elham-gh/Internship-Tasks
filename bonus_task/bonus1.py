import numpy as np

def main(proj=['a', 'b', 'c', 'd', 'e', 'f'], deps=[('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]):
    proj = proj[::-1]
    A = np.zeros((len(proj), len(proj)))
    for i, j in deps:
        A[proj.index(i), proj.index(j)] = 1
    assert np.all((A + A.T) <= 1), 'Error: There is a loop in the matrix'
    remaining_list = proj.copy()
    output_order = list()
    sys.exit("Error: Values greater than 1 found.") if np.any(A > 1) else None
    while remaining_list:
        for j in remaining_list:
            j = proj.index(j)
            if A[j, :].sum() == 0:
                output_order.append(proj[j])
                remaining_list.remove(proj[j])
                A[:, j] = [0] * A.shape[0]
    print(output_order[::-1])


if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    main(projects, dependencies)