#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from tools.wp_decision import load,plan
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--repo-state",required=True,type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=plan(load(a.repo_state));t=json.dumps(r,sort_keys=True,indent=2)+"\n";a.output and a.output.write_text(t,encoding="utf-8");print(t,end="")
