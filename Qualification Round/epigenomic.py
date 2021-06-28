def main():
    file = open("epigenomic_input_2.txt") # change this file name accordingly
    lines = file.read().splitlines()
    t = int(lines[0]) # number of tests
    linecount = 1
    output = open('epigenomic_out_2.txt', 'w') # change this file name accordingly
    for i in range(t):
        num_list = lines[i+linecount].split(' ')
        n = int(num_list[0]) # number of sequences
        l = int(num_list[1]) # length of sequences
        mat = [list(x) for x in lines[i+linecount+1:i+linecount+n+1]]
        state_dict = {}
        state_list = []
        s = 0 # number of states
        for j in range(l):
            state = "".join([row[j] for row in mat])
            if state in state_dict:
                state_list.append(state_dict[state])
            else: 
                state_dict[state] = s+1
                state_list.append(state_dict[state])
                s += 1
        output.write(str(s))
        output.write('\n')
        output.write(" ".join([str(item) for item in state_list]))
        output.write('\n')
        linecount += n
    output.close()
    file.close()

if __name__  == "__main__":
    main()