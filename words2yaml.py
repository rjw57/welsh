#!/usr/bin/env python3
from typing import Optional
import re
import enum
import yaml


class PartOfSpeech(enum.StrEnum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    OTHER = "other"


class Gender(enum.StrEnum):
    MASCULINE = "masculine"
    FEMININE = "feminine"


def lines():
    with open("./words.txt") as f:
        for ln in f:
            yield ln.strip()


def main():
    uned = 1
    part_of_speech = PartOfSpeech.NOUN
    gender: Optional[Gender] = None
    term, defn = "", ""
    words = []
    for line_idx, line in enumerate(lines()):
        if line == "":
            continue

        if line == "EG":
            part_of_speech = PartOfSpeech.NOUN
            gender = Gender.MASCULINE
            continue
        elif line == "EB":
            part_of_speech = PartOfSpeech.NOUN
            gender = Gender.FEMININE
            continue
        elif line == "B":
            part_of_speech = PartOfSpeech.VERB
            gender = None
            continue
        elif line == "AN":
            part_of_speech = PartOfSpeech.ADJECTIVE
            gender = None
            continue
        elif line == "AR":
            part_of_speech = PartOfSpeech.OTHER
            gender = None
            continue
        elif m := re.match(r"^U(?P<uned>[0-9]+)$", line):
            uned = int(m.groupdict()["uned"])
            continue
        elif "_" in line:
            term, defn = line.split("_")
        elif line.count(" ") != 1:
            print(f"{line_idx+1}: bad space count: {line!r}")
            continue
        else:
            term, defn = line.split()

        term = term.strip()
        defn = defn.strip()

        words.append(
            {
                "term": term,
                "definition": defn,
                "unit": uned,
                "part_of_speech": part_of_speech.value,
                "gender": gender if gender is None else gender.value,
            }
        )

    words.sort(key=lambda d: d["term"])

    with open("words.yaml", "w") as f:
        yaml.safe_dump(words, f)

    print(f"Wrote {len(words)} words")


if __name__ == "__main__":
    main()
