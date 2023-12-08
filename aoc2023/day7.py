from collections import Counter

card_vals = dict(zip("AKQJT98765432", range(14, 1, -1)))
old_card_vals = dict(zip("AKQT98765432J", range(14, 1, -1)))


class Hand:
    def __init__(self, cards, bid):
        self.freqs = Counter(cards)
        self.old_freqs = Counter(cards)
        self.cards = cards
        self.old_cards = ""
        self.bid = bid
        self.vals = [card_vals[x] for x in cards]
        self.old_vals = []
        self.hand = self.get_hand()
        self.old_hand = self.hand

    def transform_jokers(self):
        j_count = self.freqs["J"]
        self.old_cards = self.cards
        self.old_vals = [old_card_vals[x] for x in self.old_cards]

        if j_count == 0:
            return

        if j_count == 5:
            self.cards = "AAAAA"
            return

        m = max((v, k) for k, v in self.freqs.items() if k != "J")
        self.cards = self.old_cards.replace("J", m[1])
        self.vals = [card_vals[x] for x in self.cards]
        self.freqs = Counter(self.old_cards)
        self.old_hand = self.get_hand()
        self.freqs = Counter(self.cards)
        self.hand = self.get_hand()

    def get_hand(self):
        for k, v in self.freqs.items():
            if v == 5:
                return 6
            if v == 4:
                return 5
            if v == 3:
                for k1, v1 in self.freqs.items():
                    if v1 == 2:
                        return 4
                return 3
            if v == 2:
                for k1, v1 in self.freqs.items():
                    if v1 == 2 and k1 != k:
                        return 2
                    if v1 == 3:
                        return 4
                return 1
        return 0

    def __lt__(self, other):
        if self.old_cards == "":
            if self.hand != other.hand:
                return self.hand < other.hand

            for i in range(5):
                if self.vals[i] < other.vals[i]:
                    return True
                if self.vals[i] > other.vals[i]:
                    return False

        else:
            if self.hand == other.hand:
                for i in range(5):
                    if self.old_vals[i] < other.old_vals[i]:
                        return True
                    if self.old_vals[i] > other.old_vals[i]:
                        return False
            else:
                if self.hand != other.hand:
                    return self.hand < other.hand

                for i in range(5):
                    if self.vals[i] < other.vals[i]:
                        return True
                    if self.vals[i] > other.vals[i]:
                        return False


def main():
    D = open("input/7.in").read().splitlines()
    hands = sorted([Hand(x.split()[0], x.split()[1]) for x in D])
    p1 = sum((i + 1) * int(h.bid) for i, h in enumerate(hands))

    for h in hands:
        h.transform_jokers()

    p2 = sum((i + 1) * int(h.bid) for i, h in enumerate(sorted(hands)))
    print(f"P1: {p1}, P2: {p2}")


if __name__ == "__main__":
    main()
