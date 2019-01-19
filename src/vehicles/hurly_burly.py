from train import EngineConsist, ElectricEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='hurly_burly',
                            base_numeric_id=390,
                            name='Hurly Burly',
                            role='heavy_express_2',
                            power=1800,
                            tractive_effort_coefficient=0.25,
                            random_reverse=True,
                            gen=2,
                            pantograph_type='diamond-double',
                            intro_date_offset=5)  # introduce later than gen epoch by design

    consist.add_unit(type=ElectricEngineUnit,
                     weight=90,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
