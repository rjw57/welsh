#!/usr/bin/env python3
import random
import yaml


def main():
    with open("./words.yaml") as f:
        words = yaml.safe_load(f)

    while True:
        card = random.choice(words)
        print("-" * 50)
        print(f"definition: {card['definition']}")
        input()
        print(f"term: {card['term']}")
        print(f"type: {card['type']}, unit: {card['unit']}")


if __name__ == "__main__":
    main()
