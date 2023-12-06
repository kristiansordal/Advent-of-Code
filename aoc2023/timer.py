import subprocess
import time
import sys

files = [f"day{i}.py" for i in range(1, int(sys.argv[1]) + 1)]
green_color_code = "\033[92m"
reset_color_code = "\033[0m"
red_color_code = "\033[91m"

start_time = time.time()
times = []

for file in files:
    sub_time = time.time()
    subprocess.run(["python3", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sub_end = time.time()
    times.append(sub_end - sub_time)

end_time = time.time()
total_time = end_time - start_time

# ╔╗╚╝║═
b1 = "╔════════════════════════╗"
b2 = "╚════════════════════════╝"


print(b1)
s1 = f"║ {green_color_code}Total :{reset_color_code} {red_color_code}{round(total_time,4)}{reset_color_code} seconds ║"
l1 = len(s1)
if len(s1) < 44:
    s1 = s1[:-9]
    s1 += " " * ((44 - 9) - len(s1))
    s1 += "seconds ║"
for i, t in enumerate(times):
    if i <= 9:
        s = f"║ {green_color_code}Day {i + 1} :{reset_color_code} {red_color_code}{round(t,4)}{reset_color_code} seconds ║"
        if len(s) < len(s1):
            s = s[:-9]
            s += " " * ((len(s1) - 9) - len(s))
            s += "seconds ║"
        print(s)
    else:
        s = f"║ {green_color_code}Day {i + 1}:{reset_color_code} {red_color_code}{round(t,4)}{reset_color_code} seconds ║"
        if len(s) < len(s1):
            s = s[:-9]
            s += " " * ((len(s1) - 9) - len(s))
            s += "seconds ║"
        print(s)
print(s1)
print(b2)
