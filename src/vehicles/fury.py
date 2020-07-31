from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='fury',
                            base_numeric_id=2180,
                            name='Fury',
                            role='heavy_express',
                            role_child_branch_num=2,
                            power=3600,
                            random_reverse=True,
                            gen=5,
                            replacement_consist_id='revolution', # this line ends with Fury and is merged to heavy_express 3
                            pantograph_type='z-shaped-double',
                            intro_date_offset=1,  # introduce later than gen epoch by design
                            alternative_cc_livery='RAILFREIGHT_TRIPLE_GREY',
                            default_livery_extra_docs_examples=[('COLOUR_GREEN', 'COLOUR_YELLOW'), ('COLOUR_PALE_GREEN', 'COLOUR_PALE_GREEN'), ('COLOUR_LIGHT_BLUE', 'COLOUR_WHITE')],
                            sprites_complete=False)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=82,
                     vehicle_length=8,
                     spriterow_num=0)

    return consist
