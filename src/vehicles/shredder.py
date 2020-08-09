from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='shredder',
                            base_numeric_id=2830,
                            name='Shredder', # Griffon and Shredder names are wrong way round, but seems to suit the shapes so eh, leave it :)
                            role='express',
                            role_child_branch_num=1,
                            power=1950,
                            random_reverse=True,
                            gen=5,
                            speed=125,
                            intro_date_offset=7,  # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=DieselEngineUnit,
                     weight=76,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.foamer_facts = """EMD JT42HW-HS (Class 67)."""

    return consist
