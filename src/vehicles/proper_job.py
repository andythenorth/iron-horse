from train import EngineConsist, SteamEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='proper_job',
                            base_numeric_id=1300,
                            name='2-6-2 Proper Job',
                            role='branch_express',
                            power=800,
                            tractive_effort_coefficient=0.2,
                            random_reverse=True,
                            gen=3)

    consist.add_unit(type=SteamEngineUnit,
                     weight=57,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
