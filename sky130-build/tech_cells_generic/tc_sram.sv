// Copyright (c) 2020 ETH Zurich and University of Bologna.
// Copyright and related rights are licensed under the Solderpad Hardware
// License, Version 0.51 (the "License"); you may not use this file except in
// compliance with the License.  You may obtain a copy of the License at
// http://solderpad.org/licenses/SHL-0.51. Unless required by applicable law
// or agreed to in writing, software, hardware and materials distributed under
// this License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
// CONDITIONS OF ANY KIND, either express or implied. See the License for the
// specific language governing permissions and limitations under the License.

// Author: Wolfgang Roenninger <wroennin@ethz.ch>

// Description: Functional module of a generic SRAM
//
// Parameters:
// - NumWords:    Number of words in the macro. Address width can be calculated with:
//                `AddrWidth = (NumWords > 32'd1) ? $clog2(NumWords) : 32'd1`
//                The module issues a warning if there is a request on an address which is
//                not in range.
// - DataWidth:   Width of the ports `wdata_i` and `rdata_o`.
// - ByteWidth:   Width of a byte, the byte enable signal `be_i` can be calculated with the
//                ceiling division `ceil(DataWidth, ByteWidth)`.
// - NumPorts:    Number of read and write ports. Each is a full port. Ports with a higher
//                index read and write after the ones with lower indices.
// - Latency:     Read latency, the read data is available this many cycles after a request.
// - SimInit:     Macro simulation initialization. Values are:
//                "zeros":  Each bit gets initialized with 1'b0.
//                "ones":   Each bit gets initialized with 1'b1.
//                "random": Each bit gets random initialized with 1'b0 or 1'b1.
//                "none":   Each bit gets initialized with 1'bx. (default)
// - PrintSimCfg: Prints at the beginning of the simulation a `Hello` message with
//                the instantiated parameters and signal widths.
//
// Ports:
// - `clk_i`:   Clock
// - `rst_ni`:  Asynchronous reset, active low
// - `req_i`:   Request, active high
// - `we_i`:    Write request, active high
// - `addr_i`:  Request address
// - `wdata_i`: Write data, has to be valid on request
// - `be_i`:    Byte enable, active high
// - `rdata_o`: Read data, valid `Latency` cycles after a request with `we_i` low.
//
// Behaviour:
// - Address collision:  When Ports are making a write access onto the same address,
//                       the write operation will start at the port with the lowest address
//                       index, each port will overwrite the changes made by the previous ports
//                       according how the respective `be_i` signal is set.
// - Read data on write: This implementation will not produce a read data output on the signal
//                       `rdata_o` when `req_i` and `we_i` are asserted. The output data is stable
//                       on write requests.

module tc_sram #(
  parameter int unsigned NumWords     = 32'd1024, // Number of Words in data array
  parameter int unsigned DataWidth    = 32'd128,  // Data signal width
  parameter int unsigned ByteWidth    = 32'd8,    // Width of a data byte
  parameter int unsigned NumPorts     = 32'd2,    // Number of read and write ports
  parameter int unsigned Latency      = 32'd1,    // Latency when the read data is available
  parameter              SimInit      = "none",   // Simulation initialization
  parameter bit          PrintSimCfg  = 1'b0,     // Print configuration
  // DEPENDENT PARAMETERS, DO NOT OVERWRITE!
  parameter int unsigned AddrWidth = (NumWords > 32'd1) ? $clog2(NumWords) : 32'd1,
  parameter int unsigned BeWidth   = (DataWidth + ByteWidth - 32'd1) / ByteWidth, // ceil_div
  parameter type         addr_t    = logic [AddrWidth-1:0],
  parameter type         data_t    = logic [DataWidth-1:0],
  parameter type         be_t      = logic [BeWidth-1:0]
) (
  input  logic                 clk_i,      // Clock
  input  logic                 rst_ni,     // Asynchronous reset active low
  // input ports
  input  logic  [NumPorts-1:0] req_i,      // request
  input  logic  [NumPorts-1:0] we_i,       // write enable
  input  addr_t [NumPorts-1:0] addr_i,     // request address
  input  data_t [NumPorts-1:0] wdata_i,    // write data
  input  be_t   [NumPorts-1:0] be_i,       // write byte enable
  // output ports
  output data_t [NumPorts-1:0] rdata_o     // read data
);

wire clk0 = clk_i;
wire csb0 = !req_i;// ACTIVE LOW
wire web0 = !we_i; // ACTIVE LOW
wire wmask0 [7:0] = be_i? 8'b1000000 : 8'b11111111;
wire spare_wen0 = 1'b0;
wire addr0 = addr_i;
wire din0 = wdata_i;
wire dout0 = rdata_o;

  sky130_sram_4kbyte_1rw_64x512_8 #(
  ) i_sky130_sram_4kbyte_1rw_64x512_8 (
      .clk0        ( clk_i      ),
      .csb0        ( req_i      ),
      .web0        ( we_i       ),
      .wmask0      ( wmask0     ),
      .spare_wen0  ( spare_wen0 ),
      .addr0       ( addr0      ),
      .din0        ( din0       ),
      .dout0       ( dout0      )
    );

endmodule
