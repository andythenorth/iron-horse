import global_constants
from ship import Ship, Tanker

ship = Tanker(id = 'yokohama_tanker',
            numeric_id = 280,
            title = 'Yokohama [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 1220,
            replacement_id = '-none',
            buy_cost = 99,
            fixed_run_cost_factor = 8.0,
            fuel_run_cost_factor = 1.0,
            speed = 22.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 40,
            intro_date = 1973,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTAL_TANKER',
            vehicle_life = 45,
            gross_tonnage = 1290,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
