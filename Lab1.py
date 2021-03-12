data = [41, 295, 842, 1365, 66, 1093, 102, 5340,
        343, 1539, 333, 933, 854, 1630, 1434, 279,
        1029, 574, 787, 2701, 1644, 853, 456, 846,
        490, 328, 2360, 384, 1202, 1061, 342, 246,
        445, 715, 736, 295, 345, 772, 41, 1510, 315,
        889, 409, 809, 66, 64, 752, 746, 45, 1774,
        469, 1508, 212, 581, 1136, 266, 186, 720,
        295, 4668, 139, 586, 254, 2023, 1502, 292,
        946, 1779, 152, 291, 7, 979, 646, 58, 2115,
        957, 897, 5961, 392, 832, 2091, 2, 265, 187,
        823, 1464, 449, 258, 533, 36, 525, 1571,
        707, 1160, 1576, 25, 609, 486, 48, 230]

gamma = 0.95
work_time = 5695
intensive = 1670


def count_intervals(sd, inter, i):
    c = 0
    amount = 0
    while sd[c] < inter[i]:
        if i != 0:
            if sd[c] > inter[i-1]:
                amount += 1
        if i == 0:
            amount += 1
        c += 1
    return amount


def find_worktime(f, inter, w_t):
    c = 0
    p = 0
    while w_t > inter[c]:
        p += f[c]*inter[0]
        c += 1
    if c != len(f)-1:
        p += f[c+1]*(w_t-inter[c-1])
    return p


def find_last(inter, w_t):
    c = 0
    while w_t > inter[c]:
        c += 1
    return c


time_cp = sum(data)/len(data)
print('Tcp =', time_cp)
sorted_data = sorted(data)
print('sorted data =',sorted_data)
intervals = []
h = sorted_data[-1]/10
for i in range(10):
    intervals.append((sorted_data[-1]/10)*(i+1))
print('intervals = ',intervals)
f = []
for i in range(len(intervals)):
    f.append(count_intervals(sorted_data, intervals, i)/(len(sorted_data)*intervals[0]))
print('f =', f)
chance_of_work = [1]
for i in range(len(intervals)):
    chance_of_work.append(h*f[i])
print('chance of work =', chance_of_work)
d = []
for i in range(len(chance_of_work)-1):
    if chance_of_work[i+1] != chance_of_work[i]:
        d.append((chance_of_work[i+1]-gamma)/(chance_of_work[i+1]-chance_of_work[i]))
print('d =',d)
t_y = []
for i in range(len(d)):
    t_y.append(intervals[i]-intervals[i]*d[i])
print('t_y =', t_y[0])
last = find_last(intervals, intensive)
print('P =', 1 - find_worktime(f, intervals, work_time))
print('Lambda('+str(intensive)+') = '+str(f[last]/(1-find_worktime(f, intervals, intensive))))
