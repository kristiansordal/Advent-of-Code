class Range:
    def __init__(self, map_):
        self.ranges = list(
            filter(lambda x: x != (), [tuple(map(int, r.split())) for r in map_[1:]])
        )

    def p1(self, seed):
        for dest, source, span in self.ranges:
            if seed >= source and seed < source + span:
                return dest + (seed - source)
        return seed

    def p2(self, r):
        inside_ranges = []
        for dest, source, span in self.ranges:
            source_end = source + span
            new_ranges = []

            while r:
                (start, end) = r.pop()

                before = (start, min(end, source))
                inside = (max(start, source), min(end, source_end))
                after = (max(start, source_end), end)

                if before[1] > before[0]:
                    new_ranges.append(before)
                if inside[1] > inside[0]:
                    inside_ranges.append(
                        (inside[0] - source + dest, inside[1] - source + dest)
                    )
                if after[1] > after[0]:
                    new_ranges.append(after)

            r = new_ranges
        return inside_ranges + r


def main():
    data = list(map(lambda x: x.split("\n"), open("input/5.in").read().split("\n\n")))
    seeds = list(map(int, data[0][0].split()[1:]))
    ranges = [Range(x) for x in data[1:]]
    location1 = 2**32

    for seed in seeds:
        for r in ranges:
            seed = r.p1(seed)
        location1 = min(location1, seed)

    pairs = list(zip(seeds[::2], seeds[1::2]))
    location2 = []

    for start, span in pairs:
        rang = [(start, start + span)]

        for r in ranges:
            rang = r.p2(rang)
        location2.append(min(rang)[0])

    print(f"P1: {location1}, P2: {min(location2)}")


if __name__ == "__main__":
    main()
