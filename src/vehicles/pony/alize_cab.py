from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="TGVCabEngineConsist",
        base_id="alize_cab",
        base_numeric_id=17100,
        name="Alizé",
        subrole="very_high_speed",
        subrole_child_branch_num=-1,
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

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=76,
        # no pax capacity on Helm Wind cabs
        capacity=0,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_3",
    )

    model_def.define_description(
        """Whispers in the wind. Graceful as she slices air. Swift, pure, and untamed."""
    )
    model_def.define_foamer_facts(
        """TGV Sud-Est, with TGV 001-style distributed traction"""
    )

    result.append(model_def)

    return result
