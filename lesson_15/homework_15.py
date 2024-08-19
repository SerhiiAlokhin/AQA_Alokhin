class Paralelogram(object):
    def __init__(self, side_a, side_b, angle_a, angle_b):
        self.side_a = side_a
        self.side_b = side_b
        self.angle_a = angle_a
        self.angle_b = angle_b


    def __setattr__(self, key, value):
        if key in ['side_a', 'side_b']:
            if value <= 0:
                raise ValueError(f"{key} must be greater than 0.")
        if key in ['angle_a', 'angle_b']:
            if not (0 < value < 180):
                raise ValueError(f"{key} must be between 0 and 180 degrees.")
        super().__setattr__(key, value)

    def angels_check(self):
        if self.angle_a + self.angle_b != 180:
            raise ValueError(f'Incorrect angles. Angle A + Angle B should be 180')


try:
    p1 = Paralelogram( 0.3, 10, 120, 60)
    p1.angels_check()
except ValueError as er:
    print(f"Error: {er}")








