import fileinput


def simulate(n):
    cycle_length = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        cycle_length += 1
    return cycle_length + 1 # since we terminate before n=1
    

if __name__ == '__main__':
    for line in fileinput.input():
        i, j = map(int, line.split())
        cycle_lengths = [simulate(n) for n in range(i, j + 1)]
        max_cycle = max(cycle_lengths)
        print('{i} {j} {max_cycle}'.format(i=i, j=j, max_cycle=max_cycle))
