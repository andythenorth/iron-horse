print "running"

import dispatcher
import time
from multiprocessing import Process, active_children
import codecs
from subprocess import call

# Have nmlc generate the deps file from the .nml file. Will fail if the .nml file is missing (but .nml should have been built by a script and/or makefile).
# N.B. we have to provide nmlc with the correct path to the lang files etc, relative to where it's called from.
call(["nmlc", "-M", "--lang-dir=../../lang", "../../bandit.nml"])

dep_file = codecs.open('../../bandit.dep')
trailer_filenames = set()

for line in dep_file:
    if "pixel_generator/output/" in line:
        filename = line.split("pixel_generator/output/")[1]
        filename = filename.strip()
        trailer_filenames.add(filename)

# I tried auto-detecting required cargos from vehicle filenames.
# That's's possible, but it's probably easier and low-cost to simply generate from a manual list for now.
cargo_filenames = [
    'cargo_coils-grey_metal-2_8.png',
    'cargo_coils-grey_metal-3_8.png',
    'cargo_coils-grey_metal-4_8.png',
    'cargo_coils-grey_metal-5_8.png',
    'cargo_coils-grey_metal-6_8.png',
    'cargo_coils-grey_metal-7_8.png',
    'cargo_coils-grey_metal-8_8.png',
    'cargo_coils-white-2_8.png',
    'cargo_coils-white-3_8.png',
    'cargo_coils-white-4_8.png',
    'cargo_coils-white-5_8.png',
    'cargo_coils-white-6_8.png',
    'cargo_coils-white-7_8.png',
    'cargo_coils-white-8_8.png',
    'cargo_coils-copper_metal-2_8.png',
    'cargo_coils-copper_metal-3_8.png',
    'cargo_coils-copper_metal-4_8.png',
    'cargo_coils-copper_metal-5_8.png',
    'cargo_coils-copper_metal-6_8.png',
    'cargo_coils-copper_metal-7_8.png',
    'cargo_coils-copper_metal-8_8.png',
    'cargo_tarps-default-2_8.png',
    'cargo_tarps-default-3_8.png',
    'cargo_tarps-default-4_8.png',
    'cargo_tarps-default-5_8.png',
    'cargo_tarps-default-6_8.png',
    'cargo_tarps-default-7_8.png',
    'cargo_tarps-default-8_8.png',
    'cargo_tarps-cc1-2_8.png',
    'cargo_tarps-cc1-3_8.png',
    'cargo_tarps-cc1-4_8.png',
    'cargo_tarps-cc1-5_8.png',
    'cargo_tarps-cc1-6_8.png',
    'cargo_tarps-cc1-7_8.png',
    'cargo_tarps-cc1-8_8.png',
    'cargo_tarps-cc2-2_8.png',
    'cargo_tarps-cc2-3_8.png',
    'cargo_tarps-cc2-4_8.png',
    'cargo_tarps-cc2-5_8.png',
    'cargo_tarps-cc2-6_8.png',
    'cargo_tarps-cc2-7_8.png',
    'cargo_tarps-cc2-8_8.png',
    'cargo_tarps-pinkish-2_8.png',
    'cargo_tarps-pinkish-3_8.png',
    'cargo_tarps-pinkish-4_8.png',
    'cargo_tarps-pinkish-5_8.png',
    'cargo_tarps-pinkish-6_8.png',
    'cargo_tarps-pinkish-7_8.png',
    'cargo_tarps-pinkish-8_8.png',
    'cargo_tarps-greenish-2_8.png',
    'cargo_tarps-greenish-3_8.png',
    'cargo_tarps-greenish-4_8.png',
    'cargo_tarps-greenish-5_8.png',
    'cargo_tarps-greenish-6_8.png',
    'cargo_tarps-greenish-7_8.png',
    'cargo_tarps-greenish-8_8.png',
]

# generate body filenames as dependencies from trailer filenames
body_filenames = []
for i in trailer_filenames:
    body_filenames.append('body_' + i.split('body_')[1])

def make_sprites(filenames):
    # check for __main__ because fork bombs are bad
    if __name__ == '__main__':
        for filename in filenames:
            Process(target=dispatcher.dispatch, args=(filename,)).start()

    # dirty way to wait until all processes are complete before moving on
    while True:
        time.sleep(0.027) # 0.027 because it's a reference to TTD ticks :P (blame Rubidium)
        if len(active_children()) == 0:
            break

make_sprites(cargo_filenames)
make_sprites(body_filenames)
make_sprites(trailer_filenames)

print "done"
