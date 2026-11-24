# Make the AI Judge Laugh: the Office Joke Open

[![Competition](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/imusic-487/reply-all-office-joke/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/imusic-487/reply-all-office-joke/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard)

## The entry

> I replied-all asking to be removed from the thread, and 400 colleagues replied-all to agree with me.

One line, 100 characters. The setup is the most relatable office email
mistake — asking to be taken off a thread — and the payoff lands in the
last words: the plea itself triggers 400 more reply-alls, each one
agreeing. The cure is the disease, at inbox scale.

## What this repo does

This is an entry for the make.fun bounty
[u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).
`main.py` copies `line.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the text is not
1–200 characters, is only white space, contains a line break, or if the
copy differs in size or bytes. Nothing else: no network, no randomness,
no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — copies `line.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
