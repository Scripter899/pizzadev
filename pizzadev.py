import sys
import os
import time
import random

amt = 0

class pz_wait():
  def __init__(self):
    self.sleep_time = 1
  def wait(self, sleep_time):
    time.sleep(sleep_time)
