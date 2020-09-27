from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='toaster',
                            base_numeric_id=4800,
                            name='Toaster',
                            role='heavy_freight',
                            role_child_branch_num=-2, # Joker eh
                            power=4450, # 850hp steps Revolution -> Endeavor -> Toaster
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            gen=6,
                            fixed_run_cost_points=220, # unrealism: run cost nerf for being so high-powered
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=128, # weight reduced from 140 to nerf run cost down :P
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """I've heard these might catch fire, but we're getting them cheap."""
    consist.foamer_facts = """GE Class 70 <i>Powerhaul</i>."""

    return consist
