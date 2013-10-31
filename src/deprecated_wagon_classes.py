

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


class MailCar(Wagon):
    """
    Mail Carriage.
    """
    def __init__(self, **kwargs):
        id = self.get_id('mail_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(11000, **kwargs)
        super(MailCar, self).__init__(id, speedy=True, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['mail', 'express_freight']
        self.label_refits_allowed = [] # no specific labels needed
        self.label_refits_disallowed = []
        self.autorefit = True
        self.capacities_freight = [int(0.5 * capacity) for capacity in self.capacities_mail]
        self.default_cargo_capacities = self.capacities_mail
        self.default_cargo = 'MAIL'


class CabooseCar(Wagon):
    """
    Caboose (Brake Van).
    """
    def __init__(self, **kwargs):
        id = self.get_id('caboose_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(20000, **kwargs)
        super(CabooseCar, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.default_cargo_capacities = [0]
        self.loading_speed = 0
        self.speed = 0


class HopperCar(Wagon):
    """
    Hopper Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('hopper_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(13000, **kwargs)
        super(HopperCar, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['hopper_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'COAL'
        self.default_cargo_capacities = self.capacities_freight


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


class TankCar(Wagon):
    """
    Tank Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('tank_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(15000, **kwargs)
        super(TankCar, self).__init__(id, **kwargs)
        self.template = 'tank_car.pynml'
        self.class_refit_groups = ['liquids']
        self.num_cargo_rows = 3
        # mappings are to rows in the spritesheet, 0-based (0 is also default)
        # also get the allowed label refits from the graphics mapping - use row 0 if there's no specific graphics for the label 
        self.cargo_graphics_mappings = {'FMSP': 1, 'MILK': 2, 'RFPR': 1}
        self.label_refits_allowed = self.cargo_graphics_mappings.keys() 
        self.label_refits_disallowed = []
        self.default_cargo = 'OIL_'
        self.default_cargo_capacities = self.capacities_freight


class LivestockCar(Wagon):
    """
    Livestock Car (Gondola).
    """
    def __init__(self, **kwargs):
        id = self.get_id('livestock_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(16000, **kwargs)
        super(LivestockCar, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = []
        self.label_refits_allowed = ['LVST'] # no specific labels needed
        self.label_refits_disallowed = []
        self.default_cargo = 'LVST'
        self.default_cargo_capacities = self.capacities_freight


class ReeferCar(Wagon):
    """
    Reefer (Refrigerated) Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('reefer_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(18000, **kwargs)
        super(ReeferCar, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['refrigerated_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'FOOD'
        self.default_cargo_capacities = self.capacities_freight


class FlatCar(Wagon):
    """
    Flat Car.
    """
    def __init__(self, **kwargs):
        id = self.get_id('flat_car', **kwargs)
        kwargs['numeric_id'] = self.get_numeric_id(19000, **kwargs)
        super(FlatCar, self).__init__(id, **kwargs)
        self.template = 'train.pynml'
        self.class_refit_groups = ['flatcar_freight']
        self.label_refits_allowed = []
        self.label_refits_disallowed = []
        self.autorefit = True
        self.default_cargo = 'GOOD'
        self.default_cargo_capacities = self.capacities_freight
