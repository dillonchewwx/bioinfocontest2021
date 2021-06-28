def main():
    file = open("testB_input.txt")
    lines = file.read().splitlines()
    numSeq = int(lines[0])
    output = open('testB_out.txt', 'w')
    for i in range(1, numSeq+1):
        s = lines[2*i-1]
        t = lines[2*i]
        output.write(motifFinder(s,t))
        output.write('\n')
    output.close()
    file.close()
    
def motifFinder(s,t):
    location = ""
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            location += str(i+1) + " "
    return location

if __name__  == "__main__":
    main()
