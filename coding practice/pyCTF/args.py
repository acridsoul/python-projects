import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

number_iterations = sys.argv[1]

f = open("args.txt", "w")

for i in range(int(number_iterations)):
    if i < 5:
        f.write("the number is less than 5 \n")
    else:
        f.write("the number is greater than or equal to 5 \n")
    f.write(str(i) + "\n")

f.close()
print("Done writing to file")
