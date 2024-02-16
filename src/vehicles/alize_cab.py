from train import TGVCabEngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = TGVCabEngineConsist(
        roster_id=roster_id,
        id="alize_cab",
        base_numeric_id=14820,
        name="Alizé",
        role="very_high_speed",
        role_child_branch_num=-1,
        power_by_power_source={
            "AC": 1900,
        },
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "TGV_LA_POSTE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_ORANGE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit,
        weight=76,
        # no pax capacity on Helm Wind cabs
        capacity=0,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_3",
    )

    consist.description = """"""
    consist.foamer_facts = """TGV Sud-Est, with TGV 001-style distributed traction"""

    return consist
