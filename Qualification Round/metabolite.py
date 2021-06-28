def main():
    file = open("metabolite_input_2.txt")
    lines = file.read().splitlines()
    t = int(lines[0]) # number of tests
    linecount = 1
    output = open('metabolite_out_2.txt', 'w')
    for i in range(t):
        num_list = lines[i+linecount].split(' ')
        m = int(num_list[0]) # number of metabolites
        k = int(num_list[1]) # number of adducts
        n = int(num_list[2]) # number of signals
        mj = [float(y) for y in lines[i+linecount+1].split()]
        ak = [float(y) for y in lines[i+linecount+2].split()]
        si = [float(y) for y in lines[i+linecount+3].split()]
        delta = {}
        for a in range(n):
            for b in range(m):
                for c in range(k):
                    if mj[b] + ak[c] > 0:
                        delta[b+1,c+1] = abs(si[a]-(mj[b] + ak[c]))
            combination = min(delta, key=delta.get)
            output.write(" ".join([str(item) for item in combination]))
            output.write('\n')
            print(a)
        linecount += 3
    file.close()
    output.close()

if __name__  == "__main__":
    main()