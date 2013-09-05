import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'marstein_freighter',
            numeric_id = 200,
            title = 'Marstein [Freighter]',
            capacity_cargo_holds = 240,
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 20,
            intro_date = 2008,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'COASTER',
            vehicle_life = 40,
            gross_tonnage = 270,
            graphics_status = 'Unstarted',)

ship.add_model_variant(intro_date=0, 
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)