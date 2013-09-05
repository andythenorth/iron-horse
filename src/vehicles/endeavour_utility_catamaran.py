import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'endeavour_utility_catamaran',
            numeric_id = 120,
            title = 'Endeavour [Rig Supply Fast Catamaran]',
            capacity_pax = 65,
            capacity_cargo_holds = 70,
            capacity_mail = 70,
            replacement_id = '-none',
            buy_cost = 7,
            fixed_run_cost_factor = 3.0,
            fuel_run_cost_factor = 1.0,
            speed = 45.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 49,
            loading_speed = 15,
            intro_date = 1998,
            buy_menu_bb_xy = [664, 21],
            str_type_info = 'RIG_SUPPLY_FAST_CATAMARAN',
            vehicle_life = 25,
            gross_tonnage = 70,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
