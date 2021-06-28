def main():
    file = open("testA_input.txt")
    lines = file.read().splitlines()
    output = open('testA_out.txt', 'w')
    for i in range(1,int(lines[0])+1):
        a = int(lines[i][0])
        b = int(lines[i][2])
        output.write(str(a+b))
        output.write('\n')
    output.close()
    file.close()

if __name__ == "__main__":
    main()
