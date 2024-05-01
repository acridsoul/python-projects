filepath = "pico.txt"
output_filepath = "output.txt"
i = 0
max_chars = 30

with open(filepath, "r") as f, open(output_filepath, "w") as out_f:
    for line in f:
        i += 1
        words = line.strip().split()
        output_line = ""
        for word in words:
            if len(output_line) + len(word) > max_chars:
                out_f.write(output_line.strip() + '\n')
                output_line = ""
            output_line += word + ' '
        out_f.write(output_line.strip() + '\n')
        if i % 4 == 0:
            out_f.write('\n')