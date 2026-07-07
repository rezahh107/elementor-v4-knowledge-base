#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, urllib.request

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repository',required=True); ap.add_argument('--output',required=True); args=ap.parse_args()
    token=os.environ.get('GITHUB_TOKEN','')
    req=urllib.request.Request(f"https://api.github.com/repos/{args.repository}/pulls?state=open")
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Accept','application/vnd.github+json')
    with urllib.request.urlopen(req) as r:
        prs=json.load(r)
    data={'pull_requests':[{'number':p.get('number'),'state':p.get('state'),'draft':p.get('draft'),'head_sha':p.get('head',{}).get('sha'),'head_ref':p.get('head',{}).get('ref')} for p in prs], 'workflow_runs':[]}
    with open(args.output,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=2)
if __name__ == '__main__':
    main()
