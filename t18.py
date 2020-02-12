#!python3


import sys
from attr import attrs, attrib
from collections import defaultdict, Counter


@attrs
class Lumber_collector:
    field = attrib(default=defaultdict(lambda: '.'))

    def print_field(self):
        # print(self.field.items())

        prev_x = 0
        row = ''
        for x, y in self.field:
            if x != prev_x:
                prev_x = x
                print(row)
                row = ''
            row += self.field[x, y]
        print(row, '\n')

        return 0

    def load_field(self, inp):

        inp = open(sys.argv[1]).read().split('\n')
        data = list(map(str, inp))

        # first load the input to a grid

        for i in (range(len(data))):
            for j in (range(len(data[i]))):
                self.field[i, j] = data[i][j]

        return 1

    def print_result(self):

        trees = len([square for square in self.field
                    if self.field[square] in ['|']])
        lumbers = len([square for square in self.field
                      if self.field[square] in ['#']])

        print('trees', trees, 'lumbers', lumbers, 'total', trees*lumbers)

    def run_round(self):

        field_c = dict(self.field)

        for x, y in field_c:
            # open acre

            tree_count = 0
            lumber_count = 0

            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if a == b == 0:
                        continue
                    if field_c.get((x+a, y+b), '') == '|':
                        tree_count += 1

                    if field_c.get((x+a, y+b), '') == '#':
                        lumber_count += 1

            if field_c[x, y] == '.' and tree_count >= 3:
                self.field[x, y] = '|'

            if field_c[x, y] == '|' and lumber_count >= 3:
                self.field[x, y] = '#'

            if field_c[x, y] == '#':
                if lumber_count < 1 or tree_count < 1:
                    self.field[x, y] = '.'

        return 1

    def main(self):

        assert len(sys.argv) == 2

        self.load_field(sys.argv[1])

        results = dict()
        seen_again = None
        first_repeated = None
        loop = []

        for i in range(1, 1_000_000_000):
            # if i%1000 == 0:
            # print('Round', i)
            self.run_round()

            if i == 10:
                print("Round 1 :")
                self.print_result()

            if seen_again and tuple(self.field.items()) == tuple(first_repeated):
                print('Seen again at ', i)

                self.print_field()
                index = (1_000_000_000 - seen_again) % len(loop)
                print('index', index)
                print('Result 2 :', loop[index])
                break

            if results.get(tuple(self.field.items()), None):
                if not seen_again:
                    print("Found at i", i)
                    seen_again = i
                    first_repeated = tuple(self.field.items())
            else:
                results[tuple(self.field.items())] = i

            if seen_again:
                c = Counter(self.field.values())
                r = c['#'] * c["|"]
                loop.append(r)


if __name__ == '__main__':
    lc = Lumber_collector()
    lc.main()
