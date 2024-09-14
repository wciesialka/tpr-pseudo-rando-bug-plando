from . import items
from . import rungen
def main():
    pairings = rungen.generate_pairings(items.PROGRESSION_ITEMS)
    for check, item in sorted(pairings.items()):
        print(f"\033[93m{check}\033[0m: \033[92m{item}\033[0m")

if __name__ == "__main__":
    main()