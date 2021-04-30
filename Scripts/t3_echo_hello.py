#!/usr/bin/env python3
import pandas as pd
import numpy as np
import argparse
import time


def main(input, out_dir):
    print(f"input: {input}, output: {out_dir}")

    qq = np.random.random(10)
    df1 = pd.DataFrame({"row1": [input for i in range(10)], "value": qq})

    df1.to_csv(f"{out_dir}/trial_df.csv")
    time.sleep(5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', metavar='N', type=str, default="xxx",
                        help='an integer for the accumulator')
    parser.add_argument('out_dir', type=str, default="placeA",
                        help='sum the integers (default: find the max)')
    args = parser.parse_known_args()

    main(input=args[0].input, out_dir=args[0].out_dir)