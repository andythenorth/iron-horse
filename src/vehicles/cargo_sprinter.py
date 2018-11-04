from train import EngineConsist, CargoSprinter

# cargo_sprinter is full of special cases, lots of yak-shaving to get it done
consist = EngineConsist(id='cargo_sprinter',
                        base_numeric_id=100,
                        name='Cargo Sprinter',
                        power=1000,
                        # cargo sprinter is hard to balance stats for, it needs to be fast, cheap, powerful
                        # after experiments, it's now balanced suited to express intermodal, reaching top speed quickly
                        # it's not intended for very marginal routes to compete with RVs
                        # top speed is limited to 100mph for realism, and to match other freights, but this might be worth reconsidering
                        # it's also balanced to add capacity by adding more cargo sprinter units,
                        # rather than adding capacity by adding trailing wagons
                        # it doesn't make a good loco for unpowered consists, although one or two trailing wagons should be ok per unit
                        intro_date=1999)  # explicit intro date by design

consist.add_unit(type=CargoSprinter,
                 weight=46,
                 vehicle_length=7,
                 capacity=36,  # matched to 1.5x standard Road Hog and Squid containers
                 repeat=2)
