# соответствует оператору ≤

class Moon:
    r = 1737.10

    def __le__(self, other):
        print('moon le')
        return self.r <= other.r


class Earth:
    r = 6371.0

    def __le__(self, other):
        print('earth le')
        return self.r <= other.r


my_moon = Moon()
my_earth = Earth()

is_le = (my_moon <= my_earth)  # moon le
is_le  # True
is_le = (my_earth <= my_moon)  # earth le
is_le  # False

is_le = (my_moon <= my_moon)  # moon le
is_le  # True
