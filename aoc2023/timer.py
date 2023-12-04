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
print("╔════════════════════════╗")

for i, t in enumerate(times):
    if i <= 9:
        s = len(
            f"║ {green_color_code}Day {i + 1} :{reset_color_code} {red_color_code}{round(t,4)}{reset_color_code} seconds ║"
        )
        print(
            f"║ {green_color_code}Day {i + 1} :{reset_color_code} {red_color_code}{round(t,4)}{reset_color_code} seconds ║"
        )
    else:
        print(
            f"║ {green_color_code}Day {i + 1}:{reset_color_code} {red_color_code}{round(t,4)}{reset_color_code} seconds ║"
        )
print(
    f"║ {green_color_code}Total :{reset_color_code} {red_color_code}{round(total_time,4)}{reset_color_code} seconds ║"
)
print("╚════════════════════════╝")
