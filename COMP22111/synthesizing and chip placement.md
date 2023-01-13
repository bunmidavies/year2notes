[[COMP22111]]

Synthesization involves changing a ==functional== design into a ==physical== design

There are a number of constraints on the synthesizer as well as place/route tools:
- Clock period (performance)
- Floorplan/pinout
- Area/density (cost)
- Power

*The ==floorplan== of an IC is a schematic representation of tentattive placement of its major functional blocks*

While floorplanning, there are a number of geometrical constraints:
- bonding pads (for off chip connections) placement
- chip area should be a minimum to fit these bonding pads, and to limit data paths
- prepurchased IP blocks have predefined area blocks

there are a number of different tools that are involved in the layout process:
- ==extractor== - interprets layout polygons as components (i.e. identifies transistors, follows wires to find their interconnection)
- ==layout editor== - used for 'polygon pushing' i.e. ==drawing== the features for the floorplan
- ==equivalence checker== - used to check that the synthesized netlist matches the RTL design in semantics

note that ==floorplanning== is similar to layout editing, but is used to figure out where the major blocks in the circuit should be placed, but not all of them

### chip placement

- chip placement is one of the most time consuming stages of the chip design process, as power, performance and area are minimized, while constraints on density and ==routing== congestion are adhered