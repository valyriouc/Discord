import homie
import sys

def parse_args():
    config = {
        "debug": False
    }
    args = sys.argv[1:]
    for arg in args:
        if arg == "-d":
            print("Running in debug mode")
            config["debug"] = True
    return config 

if __name__ == "__main__":
    config = parse_args()
    if (config["debug"]):
        homie.run_testing_bot()
    else:
        homie.run_discord_bot()