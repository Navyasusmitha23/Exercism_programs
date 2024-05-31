# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

# Calculate the bake time remaining.
def bake_time_remaining(actual_minutes):
    """Calculate the bake time remaining.
    
    Parameters:
    actual_minutes (int): The actual minutes the lasagna has been in the oven.

    Returns:
    int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - actual_minutes

# Calculate the preparation time in minutes.
def preparation_time_in_minutes(no_of_layers):
    """
    Calculate the preparation time in minutes.

    Parameters:
    no_of_layers (int): The number of layers in the lasagna.

    Returns:
    int: The preparation time in minutes based on the number of layers.
    """
    preparation_time = 2  # Assuming 2 minutes per layer for preparation
    return no_of_layers * preparation_time

# Calculate the elapsed time in minutes.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed time in minutes.

    Parameters:
    number_of_layers (int): The number of layers in the lasagna.
    elapsed_bake_time (int): The baking time already elapsed.

    Returns:
    int: The remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
