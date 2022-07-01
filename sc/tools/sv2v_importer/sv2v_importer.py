def setup(chip):
    ''' Per tool function that returns a dynamic options string based on
    the dictionary settings.
    '''
    tool = 'sv2v_importer'
    step = chip.get('arg','step')
    index = chip.get('arg','index')

    chip.set('tool', tool, 'exe', 'sv2v')
    chip.set('tool', tool, 'vswitch', '--numeric-version')
    chip.set('tool', tool, 'version', '>=0.0.9', clobber=False)
    chip.set('tool', tool, 'threads', step, index,  4, clobber=False)

    topmodule = chip.get('design')

    options = []
    options.append("--write=outputs/" + topmodule + ".v")
    for value in chip.get('option', 'define'):
        options.append('-D' + value)

    chip.set('tool', tool, 'option', step, index, options)

    chip.set('tool', tool, 'output', step, index, f'{topmodule}.v')

def runtime_options(chip):
    cmdlist = []
    for value in chip.find_files('option', 'idir'):
        cmdlist.append('-I' + value)

    for value in chip.find_files('input', 'verilog'):
        cmdlist.append(value)

    return cmdlist

def parse_version(stdout):
    # 0.0.7-130-g1aa30ea
    return '-'.join(stdout.split('-')[:-1])
