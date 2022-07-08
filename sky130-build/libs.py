import siliconcompiler

def lib_setup(chip):
    libname = 'sky130sram'
    lib = siliconcompiler.Chip(libname)

    stackup = '5M1LI' # TODO: this should this be extracted from something
    version = 'v0_0_2'

    lib.set('package', 'version', version)

    lib.set('asic', 'pdk', 'skywater130')
    lib.set('asic', 'stackup', stackup)

    lib.add('model', 'timing', 'nldm', 'typical', 'ram/sky130_sram_4kbyte_1rw_64x512_8_TT_1p8V_25C.lib')
    lib.add('model', 'layout', 'lef', stackup, 'ram/sky130_sram_4kbyte_1rw_64x512_8.lef')
    lib.add('model', 'layout', 'gds', stackup, 'ram/sky130_sram_4kbyte_1rw_64x512_8.gds')

    chip.import_library(lib)
