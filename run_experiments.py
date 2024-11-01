from extend_mahim import * 
import subprocess

def add_key(key, global_key):
    for k in global_key:  # Iterate over each label in global_key (k1, k2, ..., mid-leaf)
        for rank in global_key[k]:  # Iterate over each rank (r0, r1, ...) for the label
            global_key[k][rank] += key[k][rank]  # Add the value from key to global_key

def reset_key(): 
    return {"k1": {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "mid": 0, "sd": 0}, 
        "k2":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "mid": 0, "sd": 0}, 
        "k3":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "mid": 0, "sd": 0}, 
        "k4":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "mid": 0, "sd": 0}, 
        "k5":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "mid": 0, "sd": 0}, 
        "mid-leaf":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0, "mid": 0, "sd": 0}} # global key

# turns key into % 
def fix(key): 
    for k in key:  # Iterate over each label in global_key (k1, k2, ..., mid-leaf)
        for rank in key[k]:  # Iterate over each rank (r0, r1, ...) for the label
            if rank in ["mid", "sd"]:
                key[k][rank] = (key[k][rank] / NUMBER_OF_EXPERIMENTS)
            else:
                key[k][rank] = (key[k][rank] / NUMBER_OF_EXPERIMENTS) * 100
    return key 

def display_map(key):
    key = fix(key)
    for k, ranks in key.items():
        print(k)
        for rank, count in ranks.items():
            print(f"  {rank}: {count}")

def process_output(result_text, key):
    # Regular expression pattern to capture rank and label (k1, k2, ..., mid-leaf)
    #pattern = r"^ *(\d+),\s+(k\d|mid-leaf),"

    # Find all matches in the result text
    #matches = re.findall(pattern, result_text, re.MULTILINE)
    pattern = r"^ *(\d+),\s+(k\d|mid-leaf),\s+([0-9.]+),\s+([0-9.]+)"
    matches = re.findall(pattern, result_text, re.MULTILINE)

    for rank, label, mid_value, sd_value in matches:
    # Populate the global key dictionary
        if label in key:
            # Format rank as "r{rank}" to match the structure in key
            rank_key = f"r{rank}"
            if rank_key in key[label]:
                key[label][rank_key] += 1  # Increment the count for each specific rank
                key[label]["mid"] += float(mid_value)
                key[label]["sd"] += float(sd_value)


NUMBER_OF_EXPERIMENTS = 30

def runCode():
    key = reset_key()
    noise = [0, 0.2, 0.25, 0.3, 0.35, 0.4] # hardcoded for now, TODO: change
    for n in noise: 
        print(f"noise: {n}")
        for repeat in range(NUMBER_OF_EXPERIMENTS):
            command = ["python3.13", "-B", "extend_mahim.py", "data/optimize/config/SS-A.csv", str(n)]
            #command = ["python3.13", "-B", "extend_mahim.py", "data/optimize/misc/auto93.csv", str(n)]
            # Run the command with arguments
            result = subprocess.run(command, capture_output=True, text=True)
            process_output(result.stdout, key)
        display_map(key)
        # add_key(key, global_key) # throwaway: we don't care about global key
        key = reset_key()
    return 0

if __name__ == "__main__":
    runCode()
    print("\n\nglobal key: \n")
    # display_map(global_key)





"""
throwaway 
global_key = {"k1": {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}, 
        "k2":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}, 
        "k3":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}, 
        "k4":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}, 
        "k5":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}, 
        "mid-leaf":  {"r0": 0, "r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}} # global key

"""