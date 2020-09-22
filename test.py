def fizzbuzz(i, s, m):
    global k
    if m % i == 0:
        k = True
        print(s)


if __name__ == "__main__":
    with open('input.txt', encoding='utf8') as f:
        k = False
        lines = f.read().strip().split('\n')
        m = int(lines[-1])
        lines = lines[:-1]
        lines.sort()
        for line in lines[:-1]:
            i = int(line.split(':')[0])
            s = line.split(':')[1]
            fizzbuzz(i, s, m)
        if not k:
            print(m)
