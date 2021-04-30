#!/usr/bin/env python3
import subprocess
import argparse
import time


def main(input, out_dir):
    out_path = f"{out_dir}/output.txt"
    print(f"input: {input}, output: {out_dir}")
    subprocess.call(f"echo {input} > {out_path}", shell=True)
    time.sleep(10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', metavar='N', type=str,
                        help='an integer for the accumulator')
    parser.add_argument('out_dir', type=str,
                        help='sum the integers (default: find the max)')
    args = parser.parse_known_args()

    main(input=args[0].input, out_dir=args[0].out_dir)
    print("OK, this process is over!!")