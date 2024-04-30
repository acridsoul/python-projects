filepath = "pico.txt"
output = "test2.txt"

i = 0
n = 10

with open(filepath, "r") as f, open(output, "w") as out_f:
    for line in f:
        i += 1
        out_f.write(line.strip()[:n] + "\n")
        if i % 4 == 0:
            out_f.write("\n")

