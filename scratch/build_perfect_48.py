# -*- coding: utf-8 -*-
"""
Builder for 100% Dedicated DsaLab Models for all 48 diagrams in Wiki
"""
import sys, io, json, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# We load build_all_visualizers.py and adjust the conditions and add missing models
with open('scratch/build_all_visualizers.py', 'r', encoding='utf-8') as f:
    orig = f.read()

# Let's inspect the structure of get_engine_code
startToken = "def get_engine_code():\n    return r'''"
endToken = "\n'''\n"
s_idx = orig.find(startToken) + len(startToken)
e_idx = orig.find(endToken, s_idx)
engine_code = orig[s_idx:e_idx]

print(f"Original engine code lines: {len(engine_code.splitlines())}")
