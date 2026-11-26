#!/usr/bin/env python3
"""One Star, Five Stars for the Food — the aliens review Earth.

The aliens hand Earth one star and still admit the food was
excellent, so the sentence has to hold both verdicts at once.
Everything earthly gets docked — the traffic, the queues, the
weather — and then the dumplings undo the whole complaint: a
dish worth crossing a galaxy for makes the one star look like a
clerical error. The joke is the gap between the two ratings,
and the dumpling is the only thing on the planet that survives
the review.

This script holds one fixed sentence, checks it against the
bounty rules, and writes it to the output file. Nothing here
touches the network, rolls dice, or reads the clock, so running
it twice produces the exact same bytes twice.
"""

import sys

# The entry itself. Do not touch a single character: the wording,
# the em dash, the spacing and the final full stop are the
# submission.
ENTRY = "One star for the traffic, the queues and the weather — five stars for the dumplings, which I would cross a galaxy to eat again."

# Bounty limits for this task: one sentence, at most 200
# characters long.
CHAR_LIMIT = 200

# Where the validated sentence is written, one line plus newline.
DESTINATION = "/output/entry.txt"

# The review only counts if it names the food worth five stars.
TARGET_WORD = "dumplings"

# Characters that may never appear inside the sentence.
FORBIDDEN_WHITESPACE = ("  ", "\n", "\t", "\r")


def reject(message):
    """Print the failing rule and exit non-zero."""
    print(f"rejected: {message}", file=sys.stderr)
    raise SystemExit(1)


def _has_content(candidate):
    """An entry must say something; blank text is not a review.

    Whitespace alone does not count, and neither does a line that
    is only punctuation, so both cases are rejected here and in
    the letters rule below.
    """
    if len(candidate.strip()) == 0:
        return "entry is empty"
    return None


def _fits_limit(candidate):
    """Count every character, including spaces and punctuation.

    The bounty caps the sentence at 200 characters; anything
    longer is rejected even if every other rule would pass.
    """
    if len(candidate) > CHAR_LIMIT:
        return (
            f"entry is {len(candidate)} characters, "
            f"over the {CHAR_LIMIT} limit"
        )
    return None


def _spacing_is_clean(candidate):
    """One sentence means one line: no ragged edges or breaks.

    Leading or trailing space, a double space, a newline, a tab
    or a carriage return would all break the single-sentence
    shape, so each one is a failure.
    """
    if candidate.strip() != candidate:
        return "entry has leading or trailing space"
    for bad in FORBIDDEN_WHITESPACE:
        if bad in candidate:
            return "entry has ragged spacing"
    return None


def _contains_letters(candidate):
    """At least one letter, so pure punctuation cannot pass."""
    letters = [ch for ch in candidate if ch.isalpha()]
    if len(letters) == 0:
        return "entry has no letters"
    return None


def _no_control_chars(candidate):
    """Control characters are never part of a one-sentence review."""
    if any(ord(ch) < 32 for ch in candidate):
        return "entry has control characters"
    return None


def _is_single_sentence(candidate):
    """Exactly one sentence: one full stop, and it closes the line.

    Two full stops would mean two sentences, and a full stop
    anywhere but the end would mean the sentence stopped early.
    Both cases fail, because the bounty asks for exactly one
    sentence.
    """
    stops = candidate.count(".")
    if stops != 1:
        return f"entry has {stops} full stops, expected exactly one"
    if candidate.rstrip().endswith(".") is False:
        return "entry must end with a full stop"
    return None


def _names_the_food(candidate):
    """The review has to name the food worth five stars."""
    if TARGET_WORD not in candidate.lower():
        return "entry must name the food worth five stars"
    return None


# The full rule table, in the order the checks run. Each entry
# pairs a short rule id (used in the rejection message) with the
# function that tests it. A rule returns None when the text
# passes, or a human-readable reason when it fails. The order
# matters only for which failure is reported first: cheap shape
# checks come before the content checks, so a blank or over-long
# sentence is caught before anyone asks whether it names the
# dumplings.
RULES = [
    ("has-content", _has_content),
    ("fits-limit", _fits_limit),
    ("clean-spacing", _spacing_is_clean),
    ("contains-letters", _contains_letters),
    ("no-control-chars", _no_control_chars),
    ("single-sentence", _is_single_sentence),
    ("names-the-food", _names_the_food),
]


def run_checks(candidate):
    """Walk the rule table; the first failure stops the run.

    Every rule is tried in table order. A rule that returns a
    string has found a problem, and the run ends there with that
    rule's id and reason on stderr. A rule that returns None has
    passed, and the walk moves on to the next one.
    """
    for rule_id, rule in RULES:
        problem = rule(candidate)
        if problem is not None:
            reject(f"{rule_id}: {problem}")


def publish(candidate):
    """Write the validated sentence to the output file.

    The file holds exactly the sentence plus one trailing
    newline, encoded as UTF-8. Writing only happens after every
    rule has passed, so a rejected sentence never produces an
    output file.
    """
    with open(DESTINATION, "w", encoding="utf-8") as handle:
        handle.write(candidate + "\n")


def main():
    """Validate the fixed entry, then publish it.

    The entry is a constant, so the only way this can fail is if
    the constant itself ever stops matching the bounty rules —
    in which case the rejection message names the rule that
    caught it, and no output file is written.
    """
    run_checks(ENTRY)
    publish(ENTRY)


if __name__ == "__main__":
    main()
