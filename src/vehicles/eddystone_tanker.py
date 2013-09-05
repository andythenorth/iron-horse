import global_constants
from ship import Ship, Tanker

ship = Tanker(id = 'eddystone_tanker',
            numeric_id = 260,
            title = 'Eddystone [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 330,
            replacement_id = '-none',
            buy_cost = 12,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 40,
            intro_date = 1920,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'SMALL_TANKER_COASTAL_INLAND',
            vehicle_life = 35,
            gross_tonnage = 350,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
