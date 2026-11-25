"""One Star, Written in Sap -- a houseplant's one-star review.

The review is written by the plant, about its human, in one line
under 280 characters: the human repotted it into a pot with no
drainage, then blamed the soil when it drowned. The grievance is
specific and plant-eyed -- drainage, soil, repotting -- the reason
for the single star is the drowning, and the turn lands on the pot
being a bathtub with delusions. No stock wilting, no drama queen,
just a plant that knows pots.
"""

import os

STARS = "★ One star."
GRIEVANCE = "My human repotted me into a pot with no drainage, then blamed the soil when I drowned"
PAYOFF = "— the soil was fine, the pot was a bathtub with delusions."

MAX_CHARS = 279
MIN_CHARS = 1


def compose(stars: str, grievance: str, payoff: str) -> str:
    """Join the rating, the grievance and the payoff into one review."""
    parts = [stars.strip(), grievance.strip(), payoff.strip()]
    line = " ".join(parts)
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..279 chars."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    assert line.endswith("."), "the line should end on the payoff"
    return line


def delivery_notes(line: str) -> dict:
    """Per-bounty delivery check: the line must read as a plant's review.

    The judge scores a houseplant review on whether the grievance is
    the plant's own, whether it sounds plant-written, and whether it
    reads as a real one-star review, so the line needs the star
    rating, a plant's-eye complaint about drainage and soil, and a
    fresh specific detail -- all present here, in one tight line.
    """
    words = line.split()
    assert 10 <= len(words) <= 50, f"line has {len(words)} words"
    assert "One star" in line, "the line must carry its one-star rating"
    assert "repotted" in line, "the grievance must be a plant's-eye event"
    assert "drainage" in line, "the complaint must name a plant detail"
    assert "bathtub" in line, "the payoff must turn on a fresh image"
    assert "drama" not in line.lower(), "no stock drama-queen phrasing"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(STARS, GRIEVANCE, PAYOFF))
    notes = delivery_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
