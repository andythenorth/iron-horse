import global_constants
from train import Train, PacketBoat

vehicle = PacketBoat(id = 'capo_sandalo_vehicle_ferry',
            numeric_id = 80,
            title = 'Capo Sandalo [Ferry]',
            capacity_pax = 20,
            capacity_cargo_holds = 20,
            capacity_mail = 20,
            replacement_id = '-none',
            buy_cost = 63,
            fixed_run_cost_factor = 16.0,
            fuel_run_cost_factor = 1.0,
            speed = 23.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-67, -25], [-59, -29], [-15, -26], [-14, -45], [-67, -26], [-59, -29], [-15, -25]],
            buy_menu_width = 117,
            loading_speed = 30,
            intro_date = 1959,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 45,
            gross_tonnage = 1150,
            graphics_status = 'Done',)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
