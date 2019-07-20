from train import EngineConsist, SteamEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='proper_job',
                            base_numeric_id=1300,
                            name='2-6-2 Proper Job',
                            role='branch_express_1',
                            power=800,
                            gen=3,
                            replacement_consist_id='shoebox', # this line ends with Shoebox and is merged with branch_express_2
                            tractive_effort_coefficient=0.2,
                            random_reverse=True)

    consist.add_unit(type=SteamEngineUnit,
                     weight=57,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist
