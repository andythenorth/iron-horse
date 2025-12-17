from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineExpressRailcar",
        model_id="stratos",
        base_numeric_id=390,
        name="Stratos",
        subrole="express_pax_railcar",  # this will cause it to get the express label, but eh, probably fine
        subrole_child_branch_num=-2,
        base_track_type="NG",
        power_by_power_source={
            "DIESEL": 1200,  # corsica AMG 800 is 590hp per engine https://fr.wikipedia.org/wiki/AMG_800
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        tilt_bonus=True,  # for lolz
        livery_group_name="gen_4_reversed_ng_pax_liveries",  # override default liveries from gestalt
        formation_ruleset="railcars_4_unit_sets",  # special case
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselExpressRailcarPaxUnit",
        weight=50,
        capacity=24,
        chassis="railcar_ng_32px",
        tail_light="railcar_32px_6",
        suppress_roof_sprite=True,
        repeat=2,
    )

    model_def.define_description("""Every journey becomes a panorama.""")
    model_def.define_foamer_facts("""Corsican AMG 800""")

    result.append(model_def)

    return result
