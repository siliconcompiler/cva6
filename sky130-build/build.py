#!/usr/bin/env python3

import argparse
import copy
import siliconcompiler
import os

from sources import add_sources
from libs import lib_setup

def setup_options(chip):
        chip.set('option', 'define', 'VERILATOR')
        chip.set('option', 'loglevel', 'INFO')
        chip.set('option', 'relax', True)
        chip.set('option', 'jobname', 'job0')

        chip.add('option', 'define', 'WT_DCACHE')
        
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        chip.add('option', 'define', f'MEM_ROOT={cur_dir}')

def configure_chip(remote=False):
        chip = siliconcompiler.Chip('cva6')

        setup_options(chip)

        chip.set('option', 'frontend', 'systemverilog')
        chip.set('option', 'cmdfile', 'design.f')
        chip.load_target('skywater130_demo')

        chip.set('tool', 'openroad', 'var', 'place', '0', 'place_density', ['0.15'])
        chip.set('tool', 'openroad', 'var', 'route', '0', 'grt_allow_congestion', ['true'])

        chip.set('asic', 'macrolib', ['sky130sram'])
        lib_setup(chip)

        for step in ('extspice', 'drc'):
                chip.set('tool', 'magic', 'var', step, '0', 'exclude', ['sky130sram'])
        chip.set('tool', 'netgen', 'var', 'lvs', '0', 'exclude', ['sky130sram'])

        add_sources(chip)

        chip.clock('we_din\[5\]', period=20)
 
        return chip

def build_chip(verify=True, remote=False):
        chip = configure_chip(remote)
        stackup = chip.get('asic', 'stackup')

        chip.set('asic', 'diearea', [(0, 0), (5000, 5000)])
        chip.set('asic', 'corearea', [(10, 10), (4990, 4990)]) 


        chip.set('model', 'layout', 'lef', stackup, 'cva6.lef')

        run_build(chip)

        if verify:
                run_signoff(chip, 'dfm', 'export')

        # set up pointers to final outputs for integration
        gds = chip.find_result('gds', step='export')
        netlist = chip.find_result('vg', step='dfm')

        chip.set('model', 'layout', 'gds', stackup, gds)
        chip.set('output', 'netlist', netlist)
        chip.write_manifest('cva6.pkg.json')

        return chip

def run_signoff(chip, netlist_step, layout_step):
    gds_path = chip.find_result('gds', step=layout_step)
    netlist_path = chip.find_result('vg', step=netlist_step)

    jobname = chip.get('option', 'jobname')
    chip.set('option', 'jobname', f'{jobname}_signoff')
    chip.set('option', 'flow', 'signoffflow')

    chip.set('input', 'gds', gds_path)
    chip.set('input', 'netlist', netlist_path)

    run_build(chip)

def run_build(chip):
        chip.run()
        chip.summary()

def main():
        build_chip()

if __name__ == '__main__':
        main(
)
