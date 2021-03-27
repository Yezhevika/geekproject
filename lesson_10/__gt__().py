# соответствует оператору >

class Moon:
    r = 1737.10

    def __gt__(self, other):
        print('moon gt')
        return self.r > other.r


class Earth:
    r = 6371.0

    def __gt__(self, other):
        print('earth gt')
        return self.r > other.r


my_moon = Moon()
my_earth = Earth()

is_gt = (my_moon > my_earth)  # moon gt
is_gt  # False
is_gt = (my_earth > my_moon)  # earth gt
is_gt  # True

is_gt = (my_earth > my_earth)  # earth gt
is_gt  # False
