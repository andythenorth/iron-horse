import global_constants
from train import Train, CoveredHopperCar

vehicle = CoveredHopperCar(title = 'Covered Hopper [Car]',
                        vehicle_set = 'nagn',
                        wagon_generation = 2,
                        capacity_freight = 20,
                        replacement_id = '-none',
                        buy_cost = 22,
                        fixed_run_cost_factor = 3.5,
                        fuel_run_cost_factor = 1.0,
                        weight = 100,
                        vehicle_length = 6,
                        buy_menu_width = 32,
                        loading_speed = 20,
                        intro_date = 1900,
                        str_type_info = 'COASTER',
                        vehicle_life = 40,
                        graphics_status = '')

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
