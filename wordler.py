with open("words.js", "w+") as file:
    words = file.readlines()[0].split()[3:-1]
    words[0] = words[0][1:]
    words[-1] = words[-1][:-9]

    words = [word for word in words if len({*word}) <= 7]

    file.write(f'const allwords = "{" ".join(words)}".split(" ");\nconst numwords = allwords.length;')
