import math
LIGHT_SPEED = 1.

class Particle:
    """Class describing a particle"""

    def __init__(self, name, mass, charge, momentum=0.):
        """Arguments:
        - name of the particles
        - mass (in MeV/c^2)
        - charge (in e)
        - momentum [optional] in MeV/c
        """
        self.name = name
        self._mass = mass
        self._charge = charge
        self.momentum = momentum

    def print_info(self):
        """Print particle info in a nice, formatted way"""
        message = 'Particle {}:'
        message += 'mass = {} MeV/c^2, charge = {} e, momentum = {} MeV/c'
        print(message.format(self.name, self.mass, self.charge, self.momentum))

    @property
    def mass(self):
        return self._mass
    @property
    def charge(self):
        return self._charge

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, value):
        if value < 0:
            print('Cannot set the momentum  to a vlue inferior to 0')
            print('The momentum will be set to 0')
            self._momentum = 0.
        else:
            self._momentum = value

    @property
    def energy(self):
        return math.sqrt((self.momentum * LIGHT_SPEED)**2 + \
                         (self.mass * LIGHT_SPEED**2)**2)

    @energy.setter
    def energy(self, value):
        if (value < self.mass):
            print('Cannot set the energy to a value inferior to its mass')
        else:
            self.momentum = math.sqrt(value**2 - (self.mass * LIGHT_SPEED**2)**2)/LIGHT_SPEED**2

    @property
    def beta(self):
        if not (self.energy >0.):
            return 0.
        else:
            return self.momentum * LIGHT_SPEED/self.energy

    @beta.setter
    def beta(self, value):
        if (value <0.) or (value >1.):
            print('Beta must be in the [0., 1.] range')
            return
        if (not (value < 1.)) and (self.mass >0.):
            print('Only massless particles can travel at Beta=1.!')
            return
        self.momentum = LIGHT_SPEED * value * self.mass / math.sqrt(1 - value**2)


    @property
    def gamma(self):
        if not (self.energy >0.):
            return 0.
        else:
            return self.energy/(self.mass * LIGHT_SPEED**2)

    @gamma.setter
    def gamma(self, value):
        if (value <0.):
            print('Gamma cannot be inferior to 0.')
            return
        if (not (value < (math.inf))) and (self.mass >0.):
            print('Only massless particles can travel at Gamma=inf!')
            return
        self.momentum = LIGHT_SPEED * value * self.mass * math.sqrt(1 - 1/(value**2))


class Proton(Particle):
    """Class describing proton"""

    NAME = 'Proton'
    MASS = 938. #MeV/c^2
    CHARGE = +1 #e
    
    def __init__(self, momentum=0.):
        """Derived class constructor"""
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


class Alpha(Particle):
    """Class describing alpha"""

    NAME = 'Alpha'
    MASS = 3727.3 #MeV/c^2
    CHARGE = +2 #e
    
    def __init__(self, momentum=0.):
        """Derived class constructor"""
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)

class Electron(Particle):
    """Class describing electron"""

    NAME = 'Electron'
    MASS = 0.511 #MeV/c^2
    CHARGE = -1 #e
    
    def __init__(self, momentum=0.):
        """Derived class constructor"""
        super().__init__(self.NAME, self.MASS, self.CHARGE, momentum)


if __name__=='__main__':
    alpha = Alpha(20.)
    alpha.print_info()
    alpha.beta = 0.8
    alpha.print_info()
    alpha.gamma = math.inf
    alpha.print_info()
    
