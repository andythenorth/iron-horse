from train import ConsistFactory

# skeiron does not have pax capacity, so it can be used for pure mail consists


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="TGVCabEngineConsist",
        roster_id=roster_id,
        id="skeiron_cab",
        base_numeric_id=25120,
        name="Skeiron",
        subrole="very_high_speed",
        subrole_child_branch_num=2,
        pantograph_type="z-shaped-single",
        power_by_power_source={
            "AC": 3200,  # more than Brenner, but Brenner has pax capacity
        },
        gen=6,
        intro_year_offset=-14,  # introduce earlier than gen epoch by design, similar to Brenner
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "WHITE_STRIPE"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit",
        weight=54,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_3",
    )

    consist_factory.description = (
        """Myth in motion, swift. Continents woven in speed. Elegance entwined."""
    )
    consist_factory.foamer_facts = """Alstom Class 373 <i>Eurostar</i>"""

    return consist_factory
