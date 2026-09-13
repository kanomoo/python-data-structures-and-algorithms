# -*- coding: utf-8 -*-
"""
Generate scratch/final_engine.js with all 48 dedicated visualizers.
Zero generic fallback. 100% pedagogical precision.
"""
import sys, io, json, re

def generate():
    with open('scratch/all_diagrams.json', 'r', encoding='utf-8') as f:
        all_diagrams = json.load(f)

    # We read build_all_visualizers.py
    with open('scratch/build_all_visualizers.py', 'r', encoding='utf-8') as f:
        content = f.read()

    startToken = "def get_engine_code():\n    return r'''"
    endToken = "\n'''\n"
    s_idx = content.find(startToken) + len(startToken)
    e_idx = content.find(endToken, s_idx)
    raw_engine = content[s_idx:e_idx]

    # Let's inspect the sections in raw_engine
    print(f"Loaded raw engine: {len(raw_engine)} bytes")

if __name__ == '__main__':
    generate()
