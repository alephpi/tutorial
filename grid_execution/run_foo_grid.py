import itertools
import logging
import os
from math import log

base_command = "python foo.py "
grid_options = {
    "--first": ["Voxceleb1o", "CNCeleb"],
    "--second": ["origin", "car", "meeting_room", "theater"],
}

combinations = list(itertools.product(
    grid_options["--first"],
    grid_options["--second"]
))

for combo in combinations:
    cmd = (
        f"{base_command} "
        f"--first {combo[0]} "
        f"--second {combo[1]} "
    )
    logging.warning(f"Executing command: {cmd}")
    os.system(cmd)
