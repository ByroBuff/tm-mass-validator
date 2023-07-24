import argparse
import os
from pygbx import Gbx, GbxType

red = '\033[91m'
green = '\033[92m'
reset = '\033[0m'

os.system("")

def check_replays(replayDir, verbose):
    replays = [f for f in os.listdir(replayDir) if f.lower().endswith('.replay.gbx')]
    print(f"Checking {len(replays)} replays from {replayDir}...")

    for replay in replays:
        g = Gbx(os.path.join(replayDir, replay))
        ghost = g.get_class_by_id(GbxType.CTN_GHOST)

        interface = False

        for event in ghost.control_entries:
            if event.time % 10 == 5 and event.event_name == '_FakeIsRaceRunning':
                interface = True

        if not interface:
            if verbose:
                print(f"{green}[+] {replay[:-11]}: Valid{reset}")
        else:
            print(f"{red}[!] {replay[:-11]}: Invalid{reset}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check replays for validity.")
    parser.add_argument("-dir", "-d", dest="replayDir", default="./replays", help="Custom directory to check replays")
    parser.add_argument("-v", dest="verbose", action="store_true", help="Shows valid replays as well")
    args = parser.parse_args()
    
    check_replays(args.replayDir, args.verbose)