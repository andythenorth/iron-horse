import os.path

currentdir = os.curdir

import sys

sys.path.append(os.path.join("src"))  # add to the module search path

numeric_ids_to_migrate = [
    110,
    500,
    6770,
    1300,
    6750,
    900,
    6440,
    2840,
    6730,
    3250,
    5400,
    5480,
    5490,
    280,
    880,
    2170,
    4920,
    2830,
    2950,
    6400,
    4810,
    3090,
    4940,
    4970,
    3500,
    420,
    4930,
    6430,
    4290,
    7470,
    4400,
    390,
    170,
    2230,
    2180,
    5510,
    4950,
    450,
    5500,
    4860,
    3150,
    5390,
    5170,
    5180,
    3980,
    3990,
    4900,
    1330,
    1730,
    4990,
    1720,
    3340,
    5470,
    2240,
    6380,
    1000,
    780,
    160,
    3350,
    4820,
    3470,
    5070,
    5370,
    220,
    5380,
    4250,
    4800,
    1740,
    3910,
    4010,
    4880,
    3970,
    4980,
    4960,
    4000,
    3000,
    5650,
    5660,
    5670,
    1770,
    470,
    530,
    100,
    1760,
    3070,
    3080,
    2150,
    2140,
    3200,
    3210,
    2130,
    700,
    3190,
    2120,
    4220,
    3040,
    3770,
    3800,
    3830,
    3330,
    3320,
    3060,
    130,
    490,
    240,
    2030,
    430,
    1320,
    2960,
    5910,
    140,
    590,
    260,
    310,
    3900,
    3480,
    3490,
    7130,
    7140,
    7150,
    2940,
    2910,
    2050,
    4680,
    4540,
    4600,
    4610,
    5580,
    5600,
    5620,
    5590,
    5610,
    5630,
    5640,
    740,
    3300,
    2250,
    2260,
    2270,
    3120,
    3130,
    1860,
    5520,
    5530,
    5540,
    5550,
    5560,
    5570,
    3310,
    3290,
    750,
    760,
    3110,
    3100,
    1580,
    4570,
    3260,
    3280,
    3270,
    2280,
    2290,
    1830,
    1430,
    520,
    870,
    2220,
    920,
    2300,
    3160,
    970,
    1950,
    940,
    3170,
    3140,
    10,
    1050,
    1060,
    1110,
    1390,
    1410,
    1100,
    1120,
    1400,
    1420,
    1510,
    3220,
    3240,
    3230,
    5750,
    5740,
    5710,
    5770,
    5760,
    5730,
    5720,
    5780,
    5850,
    5870,
    5890,
    5860,
    5880,
    5900,
    5800,
    3920,
    3940,
    3930,
    3950,
    3880,
    3720,
    5080,
    3890,
    3730,
    3750,
    3710,
    3740,
    3760,
    5410,
    5440,
    5420,
    5450,
    5430,
    5460,
    820,
    840,
    1450,
    830,
    2440,
    2450,
    2460,
    1650,
    2470,
    1660,
    7210,
    7230,
    7250,
    7270,
    7220,
    7240,
    7260,
    7280,
    7290,
    7480,
    7500,
    7520,
    7510,
    7530,
    7540,
    7560,
    7550,
    7570,
    1780,
    560,
    570,
    550,
    2340,
    2500,
    2480,
    1670,
    1980,
    2490,
    1680,
    7300,
    7320,
    7340,
    7310,
    7330,
    7350,
    7370,
    7360,
    7380,
    7440,
    7460,
    7450,
    7400,
    7420,
    7410,
    7430,
    540,
    710,
    1440,
    510,
    980,
    1460,
    1570,
    410,
    330,
    1790,
    440,
    320,
    4620,
    4640,
    4660,
    4630,
    4650,
    4670,
    1480,
    1500,
    1550,
    1490,
    1540,
    1470,
    1800,
    1960,
    1590,
    1840,
    1870,
    1970,
    1140,
    1350,
    1560,
    1150,
    1160,
    2540,
    2520,
    1630,
    2550,
    2530,
    2510,
    1640,
    4700,
    4730,
    4710,
    4740,
    4760,
    4780,
    4720,
    4750,
    4770,
    4790,
    5230,
    5220,
    5240,
    5210,
    340,
    370,
    350,
    400,
    5280,
    5300,
    5330,
    5290,
    5310,
    5340,
    5360,
    5260,
    5320,
    5350,
    5250,
    5270,
    5000,
    5010,
    5030,
    5050,
    5020,
    5040,
    5060,
    3510,
    3530,
    3550,
    3520,
    3540,
    3560,
    5680,
    2040,
    2320,
    1380,
    1090,
    3010,
    2780,
    3020,
    6450,
    6470,
    6460,
    6480,
    2310,
    1070,
    1080,
    1610,
    2330,
    2000,
    1600,
    2020,
    2010,
    1620,
    1990,
    5700,
    4110,
    4120,
    4380,
    4390,
    4130,
    4140,
    4160,
    4150,
    4170,
    6600,
    6610,
    6630,
    6690,
    6620,
    6640,
    6650,
    6670,
    6660,
    6680,
    6720,
    3860,
    3780,
    6710,
    3870,
    3790,
    3810,
    3840,
    3820,
    3850,
    5690,
    2350,
    2370,
    6700,
    2360,
    2380,
    1810,
    2400,
    2110,
    2390,
    6490,
    6510,
    6500,
    6520,
    6530,
    6550,
    6540,
    6560,
    4180,
    4200,
    4190,
    4210,
    4230,
    4260,
    4240,
    4270,
    1200,
    630,
    640,
    2410,
    2920,
    3180,
    2430,
    960,
    2420,
    2970,
    2900,
    1250,
    2930,
    2790,
    2860,
    3360,
    3380,
    3410,
    3370,
    3390,
    3420,
    3440,
    3460,
    3400,
    3430,
    3450,
    6130,
    6140,
    6170,
    6310,
    6160,
    6150,
    6180,
    6320,
    6340,
    6300,
    6330,
    6350,
    80,
    180,
    6190,
    6280,
    6290,
    250,
    6200,
    6220,
    6240,
    6210,
    6230,
    6250,
    20,
    6270,
    6260,
    50,
    90,
    190,
    60,
    150,
    200,
    4280,
    4300,
    4310,
    4330,
    4340,
    4360,
    4350,
    4370,
    4500,
    4510,
    4520,
    4530,
    4550,
    4580,
    4560,
    4590,
    6950,
    6960,
    6970,
    7030,
    6980,
    6990,
    7010,
    7000,
    7020,
    7100,
    7080,
    7090,
    6920,
    7060,
    7050,
    7070,
    7040,
    6110,
    6040,
    6050,
    6060,
    6070,
    6090,
    6080,
    6100,
    3680,
    3620,
    3650,
    3690,
    3630,
    3660,
    3700,
    3640,
    3670,
    1230,
    1270,
    2060,
    1240,
    1340,
    2070,
    1260,
    1940,
    2700,
    1010,
    2680,
    1020,
    2720,
    2710,
    3030,
    1190,
    2990,
    1210,
    1690,
    1700,
    2100,
    1220,
    3050,
    2090,
    730,
    720,
    2560,
    7390,
    2590,
    2570,
    1820,
    3580,
    2580,
    1850,
    2640,
    2630,
    2600,
    2620,
    2610,
    2650,
    1890,
    3570,
    2660,
    1900,
    2850,
    2870,
    2080,
    2670,
    2800,
    2810,
    2690,
    2820,
    2740,
    2730,
    1710,
    2750,
    2760,
    2770,
    1910,
    1930,
    930,
    1920,
    7110,
    6930,
    7120,
    6940,
    4410,
    4420,
    4430,
    4450,
    4480,
    4460,
    4490,
    4030,
    4040,
    7930,
    7950,
    7970,
    7940,
    7960,
    7980,
    8000,
    8020,
    8010,
    8030,
    7600,
    7620,
    7640,
    7610,
    7630,
    7650,
    7670,
    7690,
    7660,
    7680,
    7700,
    8040,
    8060,
    8080,
    8050,
    8070,
    8090,
    8100,
    8120,
    8140,
    8110,
    8130,
    7820,
    7840,
    7860,
    7850,
    7870,
    7890,
    7910,
    7900,
    7920,
    8150,
    8160,
    8180,
    8170,
    8190,
    7710,
    7730,
    7750,
    7720,
    7740,
    7760,
    7780,
    7800,
    7770,
    7790,
    7810,
    1280,
    2210,
    7580,
    7590,
    990,
    4470,
    770,
    800,
    860,
    1530,
    600,
    660,
    950,
    610,
    670,
    3960,
    850,
    2160,
    910,
    580,
    1180,
    810,
    1170,
    1130,
    1370,
    5120,
    5130,
    5140,
    5950,
    5960,
    5970,
    3590,
    3600,
    3610,
    5920,
    5930,
    5940,
    4020,
    30,
    40,
    5090,
    5100,
    5110,
    650,
    2980,
    690,
    6010,
    6020,
    6030,
    5980,
    5990,
    6000,
    6570,
    6580,
    6590,
    1030,
    620,
    680,
    1310,
    1360,
    1520,
    7180,
    7190,
    7200,
    4440,
    7830,
    6910,
    7490,
    7880,
    7990,
    4100,
    1290,
]

for filename in os.listdir(os.path.join("src", "vehicles")):
    if not ".py" in filename:
        continue
    file = open(os.path.join("src", "vehicles", filename), "r")
    try:
        content = file.readlines()
        content_new = []
        for line in content:
            found = False
            for base_numeric_id in numeric_ids_to_migrate:
                if "base_numeric_id=" + str(base_numeric_id) + "," in line:
                    found = True
                    new_base_numeric_id = 9040 + base_numeric_id
                    break
            if found:
                print(
                    "migrating", filename, base_numeric_id, ">", new_base_numeric_id
                )
                modified_line = line.replace(
                    "base_numeric_id=" + str(base_numeric_id),
                    "base_numeric_id=" + str(new_base_numeric_id),
                )
                content_new.append(modified_line)
            else:
                content_new.append(line)
    except:
        raise BaseException(filename)

    file = open(os.path.join("src", "vehicles", filename), "w")
    file.write("".join(content_new))
    file.close
