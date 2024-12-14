#!/usr/bin/env python3
import re
import enum
import yaml


class WordType(enum.StrEnum):
    MASC_NOUN = "masc. noun / enw gwrywaidd"
    FEM_NOUN = "fem. noun / enw benywaidd"
    VERB = "verb / berf"
    ADJECTIVE = "ansoddair / adjective"
    OTHER = "other / arall"


def lines():
    with open("./words.txt") as f:
        for ln in f:
            yield ln.strip()


def main():
    uned = 1
    word_type = WordType.MASC_NOUN
    term, defn = "", ""
    words = []
    for line_idx, line in enumerate(lines()):
        if line == "":
            continue

        if line == "EG":
            word_type = WordType.MASC_NOUN
            continue
        elif line == "EB":
            word_type = WordType.FEM_NOUN
            continue
        elif line == "B":
            word_type = WordType.VERB
            continue
        elif line == "AN":
            word_type = WordType.ADJECTIVE
            continue
        elif line == "AR":
            word_type = WordType.OTHER
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
                "type": word_type.value,
            }
        )

    words.sort(key=lambda d: d["term"])

    with open("words.yaml", "w") as f:
        yaml.safe_dump(words, f)

    print(f"Wrote {len(words)} words")


if __name__ == "__main__":
    main()
