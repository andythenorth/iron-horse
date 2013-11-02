

class PassengerCar(Wagon):
    """
    Passenger Carriage.
    """
    def __init__(self, **kwargs):
        id = self.get_id('passenger_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(10000, **kwargs)
        super(PassengerCar, self).__init__(id, speedy=True, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['pax']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'PASS'
        self.default_cargo_capacities = self.capacities_pax

