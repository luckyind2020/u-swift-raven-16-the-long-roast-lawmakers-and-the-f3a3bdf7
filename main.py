"""Print the one-line roast entered for the make.fun bounty
"The Long Roast: Lawmakers and the File They Cannot Convert".

The roast itself lives in entry.txt so the text stays editable
without touching the code; this script only loads and prints it.
"""

from pathlib import Path


def load_roast() -> str:
    entry_path = Path(__file__).with_name("entry.txt")
    text = entry_path.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty — nothing to roast with")
    # A single sentence has no ". " mid-text (".docx" / ".pdf" are fine:
    # their dots are not followed by a space) and no ? or ! at all.
    if ". " in text or "!" in text or "?" in text:
        raise SystemExit("the roast must stay a single sentence")
    return text


def main() -> None:
    print(load_roast())


if __name__ == "__main__":
    main()
