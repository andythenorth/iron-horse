import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'maspalomas_freighter',
            numeric_id = 240,
            title = 'Maspalomas [Freighter]',
            capacity_cargo_holds = 1140,
            replacement_id = '-none',
            buy_cost = 90,
            fixed_run_cost_factor = 6.0,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1985,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            vehicle_life = 35,
            gross_tonnage = 1140,
            graphics_status = 'Work in Progress - andythenorth',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
