# Error Printing with Colors
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def error(text):
    msg = FAIL + text + ENDC
    print(msg)

def warning(text):
    msg = WARNING + text + ENDC
    print(msg)

def success(text):
    msg = OKGREEN + text + ENDC
    print(msg)