# one-star-five-stars-for-the-food

[![make.fun · u-po-pu-one-star-five-stars-for-the-food-f9166ee7](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/museweilejing923/one-star-five-stars-for-the-food/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/museweilejing923/one-star-five-stars-for-the-food/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

The entry:

> One star for the traffic, the queues and the weather — five stars for the dumplings, which I would cross a galaxy to eat again.

127 characters, limit 200.

The review holds two verdicts in a single sentence, and the gap between them is the joke. Earth gets one star for everything it can control — traffic, queues, weather — and then the dumplings arrive and undo the entire complaint in one clause: a dish worth crossing a galaxy to eat again makes the one star look like a clerical error. Even the aliens file the review twice, once for the planet and once for the kitchen. In a head-to-head vote the sharpest sentence wins, and this one is a complete review, a punchline, and a travel plan in a single breath. The em dash does the heavy lifting: everything before it is the complaint, everything after it is the surrender, and the sentence never needs a second breath to finish the thought.

## Run

```sh
python3 main.py
```

## How it works

`main.py` keeps the entry as a single constant, walks it through a table of named rule functions, and only then writes it to `/output/entry.txt`. Each rule returns either `None` (the sentence passes) or a short reason (it fails); the first failure is printed to stderr and stops the run with exit code 1, so a rejected sentence never produces an output file. The script is fully deterministic — no network, no randomness, no clock — so repeated runs produce byte-identical output. In table order the checks are: the sentence is not blank; it fits the 200-character limit; it has no ragged spacing; it contains letters; it has no control characters; it is exactly one sentence, with a single full stop at the end; and it names the dumplings.
