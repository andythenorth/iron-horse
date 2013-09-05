import global_constants
from ship import Ship, Hydrofoil

ship = Hydrofoil(id = 'matsushima_hydrofoil',
            numeric_id = 70,
            title = 'Matsushima [Hydrofoil]',
            capacity_pax = 240,
            capacity_cargo_holds = 0,
            capacity_mail = 60,
            replacement_id = '-none',
            buy_cost = 44,
            fixed_run_cost_factor = 6.0,
            fuel_run_cost_factor = 3.5,
            speed = 56.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -54], [-57, -26], [-35, -29], [-19, -32], [-14, -54], [-58, -32], [-42, -29], [-1, -26]],
            buy_menu_width = 67,
            loading_speed = 18,
            intro_date = 1978,
            buy_menu_bb_xy = [624, 28],
            str_type_info = 'HYDROFOIL_FAST_FERRY',
            vehicle_life = 45,
            gross_tonnage = 120,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
