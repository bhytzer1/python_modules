#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    valid_scores = []

    i = 1
    for arg in sys.argv[1:]:
        try:
            nbr = int(arg)
            valid_scores.append(nbr)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        i += 1
    if len(valid_scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py \
        <score1> <score2> ...\n")
    else:
        print(f"Scores processed: {valid_scores}")
        print(f"Total players: {len(valid_scores)}")
        print(f"Total score: {sum(valid_scores)}")
        print(f"Average score: {sum(valid_scores) / len(valid_scores)}")
        print(f"High score: {max(valid_scores)}")
        print(f"Low score: {min(valid_scores)}")
        print(f"Score range: {max(valid_scores) - min(valid_scores)}\n")
