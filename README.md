ET's MASLAB 2016 Code Repository
================================
	
Software Gameplan:

The high-level logic runs a state machine with the following modules, each of which may timeout:

- FOLLOW: Search for the blocks.
- CHECK: See what color an obtained block is.
- PICKUP: Pickup the block via conveyor belt.
- DROPOFF: Drop off the stack that has been built.

The following data should interrupt the standard routines:

- The collection motors stall (i.e., a block is stuck in the collection mechanism.)
  - In this case, "spit" out the stuck block.

### The FOLLOW Module:

- Move in some direction for some amount of time.
- Jerk pseudorandomly and repeat.
- Intake motors are always running.
- Exit when block limit switch is activated.

Possible Failure modes:

- No longer actually looks for a block. We might never obtain a block. This is unlikely, and frankly a design choice.

### The CHECK module:

- Checks that we have the right color block, and if not, spits it out.

### The PICKUP Module:

This module launches when a block is sensed using the color sensor, interrupting the FIND process. 

- Initially, store the current encoder value and tell the motors to move the conveyor belt up.
- Until the belt reaches the max encoder limit (+ the base value), continue to move upwards.
- Stop the belt for a brief amount of time.
- Move the belt downwards until either the encoder value is less than the base encoder value, or the conveyor belt limit switch is triggered.

After these have all been completed in that order, either the FIND module or DROPOFF module is triggered, depending on how many blocks are in the stack.

### The DROPOFF Module:

This module opens the back door and drives forward after the PICKUP module has been completed 4 times.