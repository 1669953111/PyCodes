def main():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%dx%d=%d\t" % (j,i,i*j), end='')  # won't end
        print("")
    return None

if __name__ == "__main__":
    main()