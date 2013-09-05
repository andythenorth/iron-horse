import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'fastnet_paddle_steamer',
            numeric_id = 40,
            title = 'Fastnet [Paddle Steamer]',
            capacity_pax = 720,
            capacity_cargo_holds = 250,
            capacity_mail = 320,
            replacement_id = 'capo_sandalo_vehicle_ferry',
            buy_cost = 79,
            fixed_run_cost_factor = 19.0,
            fuel_run_cost_factor = 1.0,
            speed = 23.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -54], [-63, -24], [-50, -29], [-10, -28], [-14, -55], [-58, -27], [-50, -29], [-8, -24]],
            buy_menu_width = 138,
            loading_speed = 12,
            intro_date = 1918,
            buy_menu_bb_xy = [620, 26],
            str_type_info = 'PADDLE_STEAMER',
            vehicle_life = 40,
            gross_tonnage = 800,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
