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
        print(f"part of speech: {card['part_of_speech']}")
        input()
        print(f"term: {card['term']}")
        if card.get("gender") is not None:
            print(f"gender: {card['gender']}")
        print(f"unit: {card['unit']}")


if __name__ == "__main__":
    main()
