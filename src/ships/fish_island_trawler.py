import global_constants
from ship import Ship, Trawler

ship = Trawler(id = 'fish_island_trawler',
            numeric_id = 130,
            title = 'Fish Island [Trawler]',
            capacity_pax = 18,
            capacity_deck_cargo = 20,
            capacity_mail = 30,
            capacity_fish_holds = 36,
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 17.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 40,
            loading_speed = 15,
            intro_date = 1870,
            buy_menu_bb_xy = [669, 21],
            str_type_info = 'TRAWLER',
            vehicle_life = 40,
            gross_tonnage = 40,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
