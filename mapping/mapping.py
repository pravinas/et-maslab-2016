# Localization notes:
# Use the encoder to guess arc lengths. Use the gyro to check.
# I feel like training an adaboost neural net to figure out which to rely on would be pretty cool.
# Occasionally do hard resets to avoid relying too much on dead reckoning.

# Use encoder for short-term motions, and gyro for longer/faster motions.
# Theta = f(gyro_omega, dt) * alpha + theta_encoder * (1 - alpha)
# Do a bunch of math, basically. Use the complementary filter model.

# Planning: 
# We'll be given a map. Use a greedy search algorithm over the search space.
# Probably shouldn't do path planning.