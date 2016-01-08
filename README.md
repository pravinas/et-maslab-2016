ET's MASLAB 2016 Code Repository
================================

Software Gameplan:

The high-level logic runs a state machine with the following modules, each of which may timeout:

- FIND: Search for the blocks.
- PICKUP: Pickup the block via conveyor belt.
- DROPOFF: Drop off the stack that has been built.

The following data should interrupt the standard routines:

- The collection motors stall (i.e., a block is stuck in the collection mechanism.)
  - In this case, "spit" out the stuck block.

### The FIND Module:

- If you do not see a block:
  - Turn until you see a block.
- Otherwise:
  - Move towards the largest block seen, attempting to center the block under the camera.
- Exit when bump sensor under conveyor belt peg is hit.

Possible Failure modes:

- No block can be seen by the camera within a full rotation of the robot.
- The block leaves the field of view before an interrupt is processed.

### The PICKUP Module:

TODO

### The DROPOFF Module:

TODO