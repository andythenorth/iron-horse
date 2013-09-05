import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'santorini_freighter',
            numeric_id = 230,
            title = 'Santorini [Freighter]',
            capacity_cargo_holds = 960,
            replacement_id = '-none',
            buy_cost = 85,
            fixed_run_cost_factor = 7.0,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1953,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            vehicle_life = 35,
            gross_tonnage = 960,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=1974,
                       spritesheet_suffix=0)

ship.add_model_variant(intro_date=1953,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
