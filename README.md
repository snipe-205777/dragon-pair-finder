# Dragon Pair Finder

This script will take a dragon ID and the desired colour of hatchling and provide a list of compatible partners from a CSV of dragon information.

## How to use
1. Run the command `git clone https://github.com/snipe-205777/dragon-pair-finder.git` in the place where you want to store this.
1. Input the information of all dragons you might want to use as parents in the `dragons.csv` file. You can delete the examples already in there but keep the header row.
1. Optional but recommended: Create a virtual environment with the command `python3 -m venv .venv`. Activate it with the command `source .venv/bin/activate`. You will need to reactivate the virtual environment every time you open a new terminal.
1. Install the requirements with the command `pip3 install -r requirements.txt`. This only needs to be done the first time.
1. Run the command `python3 matches.py`.
1. When prompted, enter the ID of the dragon to find partners for and the desired colours. The given ID must be of a dragon in `dragons.csv`.
1. The script will print out the information of all compatible partners to the terminal.