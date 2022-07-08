import os

def add_sources(chip):
        chip.add('option', 'define', 'SYNTHESIS')
        chip.add('option', 'idir', '../core/include')
        chip.add('input', 'verilog', '../core/include/cv32a60x_config_pkg.sv')
        chip.add('input', 'verilog', '../core/include/riscv_pkg.sv')
        chip.add('input', 'verilog', '../core/include/ariane_pkg.sv')
        chip.add('input', 'verilog', '../core/include/ariane_axi_pkg.sv')
        chip.add('input', 'verilog', '../core/include/axi_intf.sv')
        chip.add('input', 'verilog', '../core/include/cvxif_pkg.sv')
        chip.add('input', 'verilog', '../corev_apu/axi/src/axi_pkg.sv')
        chip.add('input', 'verilog', '../core/include/instr_tracer_pkg.sv')
        chip.add('input', 'verilog', '../core/include/std_cache_pkg.sv')
        chip.add('input', 'verilog', '../core/include/wt_cache_pkg.sv')

        chip.add('input', 'verilog', '../corev_apu/riscv-dbg/src/dm_pkg.sv')
        chip.add('option', 'idir', '../corev_apu/riscv-dbg/src/')
        chip.add('input', 'verilog', '../core/fpu/src/fpnew_pkg.sv')
        chip.add('option', 'idir', '../common/submodules/common_cells/include/')
        chip.add('input', 'verilog', 'tech_cells_generic/tc_sram.sv')

        folders = ['core/frontend/',
                   'common/local/util/',
                   'core/mmu_sv39/',
                   'core/mmu_sv32/',
                   'core/pmp/src/',
                   'core/cache_subsystem/',
                   'common/submodules/common_cells/src/',
                  ]

        for folder in folders:
            chip.add('option', 'idir', '../' + folder)
            for file in os.listdir('../' + folder):
                filename, file_extension = os.path.splitext(file)
                if file_extension == '.sv':
                    chip.add('input', 'verilog', '../' + folder + file)

        chip.add('input', 'verilog', 'ram/sky130_sram_4kbyte_1rw_64x512_8.bb.v')

        for file in os.listdir('../core/'):
             filename, file_extension = os.path.splitext(file)
             if file_extension == '.sv':
                 chip.add('input', 'verilog', '../core/' + file)
