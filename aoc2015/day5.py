with open("input/5.in") as f:
    data = f.read().splitlines()
    illegal = ["ab", "cd", "pq", "xy"]
    n = 0
    for l in data:
        vowels = "aeiou"
        nice = False
        for i in range(0, len(l), 2):
            s = l[i : i + 2]
            if s in illegal:
                break

            if l[i] in vowels:
                vowels = vowels.replace(l[i], "")
            if l[i + 1] in vowels:
                vowels = vowels.replace(l[i + 1], "")

            if l[i] == l[i + 1]:
                nice = True
        n += 1 if nice and len(vowels) < 3 else 0
    print(n)
