class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger -= 3
        self.happiness += 1
        print(f'{self.name} is eating...')
        self._check_limits()

    def play(self):
        self.energy -= 2
        self.happiness += 2
        self.hunger += 1
        print(f'{self.name} is playing...')
        self._check_limits()

    def sleep(self):
        self.energy += 5
        print(f'{self.name} is sleeping...')
        self._check_limits()

    def train(self, trick):
        self.tricks.append(trick)
        print(f'{self.name} learned {trick}!')

    def _check_limits(self):
        self.hunger = max(0, min(self.hunger, 10))
        self.energy = max(0, min(self.energy, 10))
        self.happiness = max(0, min(self.happiness, 10))

    def get_status(self):
        print(f'{self.name}"s current status:')
        print(f'Hunger: {self.hunger}')
        print(f'Energy: {self.energy}')
        print(f'Happiness: {self.happiness}')
        print(f'Tricks: {self.tricks}')
