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
- Exit when PICKUP module initiates.

Possible Failure modes:

- No block can be seen by the camera within a full rotation of the robot.
- The block leaves the field of view before an interrupt is processed.

### The PICKUP Module:

This module launches when a block is sensed using the color sensor, interrupting the FIND process. 

- Initially, store the current encoder value and tell the motors to move the conveyor belt up.
- Until the belt reaches the max encoder limit (+ the base value), continue to move upwards.
- Stop the belt for a brief amount of time.
- Move the belt downwards until either the encoder value is less than the base encoder value, or the conveyor belt limit switch is triggered.

After these have all been completed in that order, either the FIND module or DROPOFF module is triggered, depending on how many blocks are in the stack.

### The DROPOFF Module:

This module opens the back door and drives forward after the PICKUP module has been completed 4 times.