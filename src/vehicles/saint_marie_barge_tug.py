import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'saint_marie_barge_tug',
            numeric_id = 170,
            title = 'Saint Marie [Barge Tug]',
            capacity_cargo_holds = 300,
            replacement_id = 'lindau_freight_barge',
            buy_cost = 4,
            fixed_run_cost_factor = 1.0,
            fuel_run_cost_factor = 1.0,
            speed = 17.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 44,
            loading_speed = 20,
            intro_date = 1870,
            buy_menu_bb_xy = [667, 21],
            str_type_info = 'BARGE_TUG',
            vehicle_life = 55,
            gross_tonnage = 45,
            graphics_status = 'Work in Progress - Coxx',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
