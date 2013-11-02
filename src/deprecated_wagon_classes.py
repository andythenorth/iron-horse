

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


class OpenCar(Wagon):
    """
    Open Car (Gondola).
    """
    def __init__(self, **kwargs):
        id = self.get_id('open_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(14000, **kwargs)
        super(OpenCar, self).__init__(id, **kwargs)
        self.template = 'car_with_visible_cargo.pynml'
        self.class_refit_groups = ['all_freight']
        self.num_cargo_rows = 15
        # mappings are to rows in the spritesheet, 0-based (0 is also default)
        # also get the allowed label refits from the graphics mapping - use row 0 if there's no specific graphics for the label 
        self.cargo_graphics_mappings = {'AORE': 1, 'COAL': 2, 'SAND': 3, 'CORE': 4, 'LIME': 5, 
                                        'SCMT': 6, 'IORE': 7, 'GRVL': 8, 'GRAI': 10, 'WHEA': 10,
                                        'MAIZ': 10, 'FICR': 11, 'SGCN': 11, 'OLSD': 12, 'CLAY': 13,
                                        'FRUT': 14, 'FRVG': 14}
        self.label_refits_allowed = self.cargo_graphics_mappings.keys() 
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_cargo_capacities = self.capacities_freight

