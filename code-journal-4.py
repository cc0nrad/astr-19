class Cat:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length      # float
        self.leg_length = leg_length      # float
        self.num_eyes = num_eyes          # int
        self.has_tail = has_tail          # bool
        self.is_furry = is_furry          # bool

    def describe(self):
        print("Cat Description:")
        print(f"  Arm length: {self.arm_length} inches")
        print(f"  Leg length: {self.leg_length} inches")
        print(f"  Number of eyes: {self.num_eyes}")
        print(f"  Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"  Is furry: {'Yes' if self.is_furry else 'No'}")


def main():
    my_cat = Cat(arm_length=6.5, leg_length=7.0, num_eyes=2, has_tail=True, is_furry=True)
    
    my_cat.describe()

if __name__ == "__main__":
    main()
