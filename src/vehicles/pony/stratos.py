from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineExpressRailcar",
        model_type_id="stratos",
        base_numeric_id=390,
        name="Stratos",
        subrole="express_pax_railcar",  # quite a specific role, may or may not scale to other rosters
        subrole_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1200,  # corsica AMG 800 is 590hp per engine https://fr.wikipedia.org/wiki/AMG_800
        },
        gen=4,
        tilt_bonus=True,  # for lolz
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        formation_ruleset="railcars_4_unit_sets",  # special case
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselExpressRailcarPaxUnit",
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
