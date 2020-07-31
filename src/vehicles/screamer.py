from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='screamer',
                            base_numeric_id=450,
                            name='Screamer',
                            role='heavy_express',
                            role_child_branch_num=-3,
                            power=5500,
                            random_reverse=True,
                            gen=5,
                            pantograph_type='z-shaped-double',
                            intro_date_offset=2, # introduce later than gen epoch by design
                            cc_livery_keys=['FREIGHTLINER'],
                            default_livery_extra_docs_examples=[('COLOUR_WHITE', 'COLOUR_BLUE'), ('COLOUR_BLUE', 'COLOUR_WHITE'), ('COLOUR_PINK', 'COLOUR_DARK_BLUE')],
                            sprites_complete=False)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=85,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
