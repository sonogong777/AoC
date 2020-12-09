#!/usr/bin/python3
import argparse
import subprocess

SESSION = <SECRET>
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day', type=int)
parser.add_argument('--year', type=int, default=2020)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
        args.year, args.day, SESSION)
output = subprocess.check_output(cmd, shell=True)
print(output.decode('utf-8'), end='')


