'''for filename in ['miles', 'tyler', 'tim', 'alferdo']:
    file = open(filename + '.txt', 'r')
    times = []

    for line in file.readlines():
        if "CPU" in line:
            time = line.strip().split(": ")[1]
            times.append(float(time))

    file.close()

    print(filename + ": ", times)
    print("\n")'''
