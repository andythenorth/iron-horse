from train import TGVCabEngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = TGVCabEngineConsist(
        roster_id=roster_id,
        id="hokuhokusei_cab",
        base_numeric_id=9620,
        name="Hokuhokusei",
        role="very_high_speed",
        role_child_branch_num=-4, # note branch number offset, this is solely to make the tech tree group the cabs and middle cars for main branch
        dual_headed=True,
        power_by_power_source={
            "AC": 3000,
        },
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        #note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit,
        weight=52,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_2",
    )

    consist.description = """."""
    consist.foamer_facts = """ """

    return consist
