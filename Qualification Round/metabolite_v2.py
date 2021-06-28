import sys

def main():
    file = open("metabolite_input_5.txt") # edit file name accordingly
    lines = file.read().splitlines()
    t = int(lines[0]) # number of tests
    linecount = 1
    output = open('metabolite_out_5.txt', 'w') # edit file name accordingly
    for i in range(t):
        num_list = lines[i+linecount].split(' ')
        m = int(num_list[0]) # number of metabolites
        k = int(num_list[1]) # number of adducts
        n = int(num_list[2]) # number of signals
        mj = [float(y) for y in lines[i+linecount+1].split()]
        ak = [float(y) for y in lines[i+linecount+2].split()]
        si = [float(y) for y in lines[i+linecount+3].split()]
        for a in range(n):
            mj_sort = sorted(mj)
            ak_sort = sorted(ak)
            res = findSmallestDifference(mj_sort, ak_sort, m, k, si[a])
            index = [mj.index(res[0])+1, ak.index(res[1])+1]
            output.write(" ".join([str(ind) for ind in index]))
            output.write('\n')
            print(i, a)
        linecount += 3
    file.close()
    output.close()

def findSmallestDifference(mj, ak, m , k, si):
    # mj = list for masses of metabolites (note that they have to be sorted in increasing order)
    # ak = list for masses of adducts (note that they have to be sorted in increasing order)
    # si = signal
    # return the pair of values of metabolite and adduct with sum is closest to the signal si.

    diff = sys.maxsize # initialize difference as maximum value
    left = 0 
    right = k-1

    while(left < m and right >= 0):
        if abs(si - (mj[left] + ak[right])) < diff and mj[left] + ak[right] > 0:
            res_l = left
            res_r = right
            diff = abs(mj[left] + ak[right] - si)

        if mj[left] + ak[right] > si:
            right = right - 1
        else:
            left = left + 1

    return(mj[res_l], ak[res_r])

if __name__  == "__main__":
    main()
