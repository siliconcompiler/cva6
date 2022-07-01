import siliconcompiler

def main():
    chip = siliconcompiler.Chip('fpnew_top')
    # Set up search path for custom 'sv2v_importer' tool
    chip.set('option', 'scpath', 'sc/')

    sources = [
        # TODO: add sources for rest of core

        ## fpu
        'core/fpu/src/fpnew_pkg.sv',
        'core/fpu/src/fpnew_cast_multi.sv',
        'core/fpu/src/fpnew_classifier.sv',
        'core/fpu/src/fpnew_divsqrt_multi.sv',
        'core/fpu/src/fpnew_fma.sv',
        'core/fpu/src/fpnew_fma_multi.sv',
        'core/fpu/src/fpnew_noncomp.sv',
        'core/fpu/src/fpnew_opgroup_block.sv',
        'core/fpu/src/fpnew_opgroup_fmt_slice.sv',
        'core/fpu/src/fpnew_opgroup_multifmt_slice.sv',
        'core/fpu/src/fpnew_rounding.sv',
        'core/fpu/src/fpnew_top.sv',

        ## fpu_div_sqrt_mvp
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/control_mvp.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/defs_div_sqrt_mvp.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/div_sqrt_mvp_wrapper.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/div_sqrt_top_mvp.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/iteration_div_sqrt_mvp.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/norm_div_sqrt_mvp.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/nrbd_nrsc_mvp.sv',
        'core/fpu/src/fpu_div_sqrt_mvp/hdl/preprocess_mvp.sv',

        ## Common cells
        # 'common/submodules/common_cells/src/binary_to_gray.sv',
        # 'common/submodules/common_cells/src/cb_filter_pkg.sv',
        # 'common/submodules/common_cells/src/cc_onehot.sv',
        'common/submodules/common_cells/src/cf_math_pkg.sv',
        # 'common/submodules/common_cells/src/clk_int_div.sv',
        # 'common/submodules/common_cells/src/delta_counter.sv',
        # 'common/submodules/common_cells/src/ecc_pkg.sv',
        # 'common/submodules/common_cells/src/edge_propagator_tx.sv',
        # 'common/submodules/common_cells/src/exp_backoff.sv',
        # 'common/submodules/common_cells/src/fifo_v3.sv',
        # 'common/submodules/common_cells/src/gray_to_binary.sv',
        # 'common/submodules/common_cells/src/isochronous_4phase_handshake.sv',
        # 'common/submodules/common_cells/src/isochronous_spill_register.sv',
        # 'common/submodules/common_cells/src/lfsr.sv',
        # 'common/submodules/common_cells/src/lfsr_16bit.sv',
        # 'common/submodules/common_cells/src/lfsr_8bit.sv',
        # 'common/submodules/common_cells/src/mv_filter.sv',
        # 'common/submodules/common_cells/src/onehot_to_bin.sv',
        # 'common/submodules/common_cells/src/plru_tree.sv',
        # 'common/submodules/common_cells/src/popcount.sv',
        'common/submodules/common_cells/src/rr_arb_tree.sv',
        # 'common/submodules/common_cells/src/rstgen_bypass.sv',
        # 'common/submodules/common_cells/src/serial_deglitch.sv',
        # 'common/submodules/common_cells/src/shift_reg.sv',
        # 'common/submodules/common_cells/src/spill_register_flushable.sv',
        # 'common/submodules/common_cells/src/stream_demux.sv',
        # 'common/submodules/common_cells/src/stream_filter.sv',
        # 'common/submodules/common_cells/src/stream_fork.sv',
        # 'common/submodules/common_cells/src/stream_intf.sv',
        # 'common/submodules/common_cells/src/stream_join.sv',
        # 'common/submodules/common_cells/src/stream_mux.sv',
        # 'common/submodules/common_cells/src/sync.sv',
        # 'common/submodules/common_cells/src/sync_wedge.sv',
        # 'common/submodules/common_cells/src/unread.sv',
        # 'common/submodules/common_cells/src/cdc_reset_ctrlr_pkg.sv',
        'common/submodules/common_cells/src/lzc.sv',
        # 'common/submodules/common_cells/src/cdc_2phase.sv',
        # 'common/submodules/common_cells/src/cdc_4phase.sv',
        # 'common/submodules/common_cells/src/addr_decode.sv',
        # 'common/submodules/common_cells/src/cb_filter.sv',
        # 'common/submodules/common_cells/src/cdc_fifo_2phase.sv',
        # 'common/submodules/common_cells/src/counter.sv',
        # 'common/submodules/common_cells/src/ecc_decode.sv',
        # 'common/submodules/common_cells/src/ecc_encode.sv',
        # 'common/submodules/common_cells/src/edge_detect.sv',
        # 'common/submodules/common_cells/src/max_counter.sv',
        # 'common/submodules/common_cells/src/rstgen.sv',
        # 'common/submodules/common_cells/src/spill_register.sv',
        # 'common/submodules/common_cells/src/stream_delay.sv',
        # 'common/submodules/common_cells/src/stream_fifo.sv',
        # 'common/submodules/common_cells/src/stream_fork_dynamic.sv',
        # 'common/submodules/common_cells/src/cdc_reset_ctrlr.sv',
        # 'common/submodules/common_cells/src/cdc_fifo_gray.sv',
        # 'common/submodules/common_cells/src/fall_through_register.sv',
        # 'common/submodules/common_cells/src/id_queue.sv',
        # 'common/submodules/common_cells/src/stream_to_mem.sv',
        # 'common/submodules/common_cells/src/stream_arbiter_flushable.sv',
        # 'common/submodules/common_cells/src/stream_register.sv',
        # 'common/submodules/common_cells/src/stream_xbar.sv',
        # 'common/submodules/common_cells/src/cdc_fifo_gray_clearable.sv',
        # 'common/submodules/common_cells/src/cdc_2phase_clearable.sv',
        # 'common/submodules/common_cells/src/stream_arbiter.sv',
        # 'common/submodules/common_cells/src/stream_omega_net.sv'
    ]

    chip.set('input', 'verilog', sources)

    # avoid confusing stuff in import/
    chip.set('input', 'verilog', False, field='copy')

    chip.add('option', 'idir', 'common/submodules/common_cells/include')

    chip.load_target('skywater130_demo')

    # Switch import tool to sv2v_importer (replaces surelog)
    # Note we don't set the systemverilog frontend, so there's no extra sv2v
    # convert step.
    chip.set('flowgraph', 'asicflow', 'import', '0', 'tool', 'sv2v_importer')

    chip.set('option', 'steplist', ['import', 'syn'])

    chip.run()

if __name__ == '__main__':
    main()
