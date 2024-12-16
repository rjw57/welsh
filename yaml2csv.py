#!/usr/bin/env python3
import csv
import yaml


def main():
    with open("./words.yaml") as f:
        words = yaml.safe_load(f)

    all_units = {w["unit"] for w in words}

    with open(f"words.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Term", "Definition", "Part of Speech", "Gender", "Unit"])
        for word in words:
            writer.writerow(
                [
                    word["term"],
                    word["definition"],
                    word["part_of_speech"],
                    word.get("gender"),
                    word["unit"],
                ]
            )

    for unit in all_units:
        with open(f"unit-{unit}.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["Term", "Definition", "Part of Speech", "Gender", "Whence"])
            for word in words:
                if word["unit"] != unit:
                    continue
                writer.writerow(
                    [
                        word["term"],
                        word["definition"],
                        word["part_of_speech"],
                        word.get("gender"),
                        f"Unit {word['unit']}",
                    ]
                )


if __name__ == "__main__":
    main()
