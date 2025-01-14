from time import sleep, strftime, gmtime
from util.twitter import authenticate, check_mentions

def main():
    api = authenticate()
    print(f"[SYS] {strftime("%H:%M:%S", gmtime())} - Authenticated")
    while True:
        print(f"[SYS] {strftime("%H:%M:%S", gmtime())} - Checking mentions...")
        check_mentions(api)
        sleep(1)

if __name__ == "__main__":
    main()