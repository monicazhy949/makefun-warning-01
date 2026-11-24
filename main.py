"""One-line safety warning label for humans, for make.fun."""
import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "WARNING: Contains one human. Runs on caffeine and spite. "
    "Do not shake, do not wake before coffee, do not expect logic."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
