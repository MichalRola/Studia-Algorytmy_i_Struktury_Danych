import time


def naive_method(path, pattern):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()
    string = ' '.join(text).lower()
    m = 0           # Indeks w tekscie
    i = 0           # Indeks we wzorcu
    temp_idx = 0    # Indeks przed znalezieniem takiego samego znaku
    counter = 0
    compare = 0
    find_idx = []
    if len(pattern) == 0:
        return 0
    while temp_idx < len(string):
        compare += 1
        if i == len(pattern):
            find_idx.append(m - len(pattern))
            counter += 1
            i = 0
            temp_idx += 1
            m = temp_idx
            continue
        if string[m] != pattern[i]:
            temp_idx += 1
            m = temp_idx
            i = 0
            continue
        m += 1
        i += 1
    return counter, compare, find_idx


def hash_method(word, d=256, q=101):
    hw = 0
    for i in range(len(word)):
        hw = (hw*d + ord(word[i])) % q
    return hw


def rk_method(path, pattern):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()
    string = ' '.join(text).lower()
    counter = 0
    compare = 0
    string_length = len(string)
    pattern_length = len(pattern)

    h_w = hash_method(pattern)
    for m in range(string_length - pattern_length + 1):
        h_s = hash_method(string[m:m+pattern_length])
        compare += 1
        if h_s == h_w:
            if string[m:m+pattern_length] == pattern:
                counter += 1
    return counter, compare

def kmp_method(path, pattern):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()
    string = ' '.join(text).lower()
    m = 0       # Indeks w tekscie
    i = 0       # Indeks we wzorcu
    P = []
    nP = 0
    compare = 0
    T = kmp_table(pattern)
    while m < len(string):
        compare += 1
        if pattern[i] != string[m]:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
        else:
            m += 1
            i += 1
            if i == len(pattern):
                P.append(m-i)
                nP += 1
                i = T[i]
    return P, nP, compare

def kmp_table(pattern):
    pos = 1
    cnd = 0
    T_temp = []
    T_temp.append(-1)
    while pos < len(pattern):
        if pattern[pos] == pattern[cnd]:
            T_temp[pos] = T_temp[cnd]
        else:
            T_temp.append(cnd)
            while cnd >= 0 and pattern[pos] != pattern[cnd]:
                cnd = T_temp[cnd]
        pos += 1
        cnd += 1
    T_temp.append(cnd)
    return T_temp


t_start = time.perf_counter()
count, compared, find_index = naive_method('lotr.txt', 'time.')
t_stop = time.perf_counter()
print(str(count) + "; " + str(compared))

t_start = time.perf_counter()
count, compared = rk_method('lotr.txt', 'time.')
t_stop = time.perf_counter()
print(str(count) + "; " + str(compared))

t_start = time.perf_counter()
nP, P, compared = kmp_method('lotr.txt', 'time.')
t_stop = time.perf_counter()
print(str(P) + "; " + str(compared))
