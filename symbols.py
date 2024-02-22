#Parent class for symbols
class Symbol:
    def __init__(self, name):
        self.name = name

# ------------------------------------------------
#Inherit from Symbol, while passing in subsymbol name
class Blue_ray(Symbol):
    def __init__(self):
        super().__init__('Blue_ray')

class Orange_ray(Symbol):
    def __init__(self):
        super().__init__('Orange_ray')

class Star(Symbol):
    def __init__(self):
        super().__init__('Star')

class Melon(Symbol):
    def __init__(self):
        super().__init__('Melon')

class Plum(Symbol):
    def __init__(self):
        super().__init__('Plum')

class Grape(Symbol):
    def __init__(self):
        super().__init__('Grape')

class Pear(Symbol):
    def __init__(self):
        super().__init__('Pear')

class Orange(Symbol):
    def __init__(self):
        super().__init__('Orange')

class Cherry(Symbol):
    def __init__(self):
        super().__init__('Cherry')

class Strawberry(Symbol):
    def __init__(self):
        super().__init__('Strawberry')

# ----------------------

class Heads(Symbol):
    def __init__(self):
        super().__init__('Heads')

class Tails(Symbol):
    def __init__(self):
        super().__init__('Tails')

class Half(Symbol):
    def __init__(self):
        super().__init__('Half')

class Neither(Symbol):
    def __init__(self):
        super().__init__('Neither')
