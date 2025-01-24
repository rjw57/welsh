#!/usr/bin/env python3
import csv
import yaml


def describe(word):
    if word["part_of_speech"] == "noun":
        return f"{word['definition']}, {word['gender']} noun"
    return f"{word['definition']}, {word['part_of_speech']}"


def main():
    with open("./words.yaml") as f:
        words = yaml.safe_load(f)

    with open("words-simple.tsv", "w") as f:
        writer = csv.writer(f, delimiter="\t")
        for word in words:
            if word["unit"] < 7:
                continue
            writer.writerow(
                [
                    f"{word['term']} ({word['part_of_speech']})",
                    describe(word),
                ]
            )


if __name__ == "__main__":
    main()
