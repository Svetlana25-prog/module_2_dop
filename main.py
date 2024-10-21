def gene_p(n):
    res = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            p_s = i + j
            if n % p_s == 0:
                res += str(i) + str(j)
    return res


for i in range(3, 21):
    print(f'{i} - {gene_p(i)}')

