#! /usr/bin/python3
# This will shutdown the computer remotely
import subprocess

# This is the time it will take the computer to shutdown
time = 0


def shutdown():
	subprocess.call(["shutdown", "/s", "/t", time])

