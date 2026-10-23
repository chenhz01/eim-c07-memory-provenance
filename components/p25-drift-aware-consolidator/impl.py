# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P25 drift-aware-consolidator — 记忆巩固/溯源

L0: 记忆会过时、重复。这个工具合并重复的、丢掉过时的。
L1: 按 token Jaccard 相似度合并近重复，保留置信度高者。
L2: consolidate(items, thr) → 合并后列表。
"""

def _j(a, b):
    A, B = set(a.lower().split()), set(b.lower().split())
    return len(A & B) / max(1, len(A | B))
def consolidate(items, thr=0.6):
    out = []
    for it in items:
        for o in out:
            if _j(it["claim"], o["claim"]) >= thr:
                if it.get("confidence",0) > o.get("confidence",0): o.update(it)
                break
        else: out.append(dict(it))
    return out

def demo():
    print("[P25]", len(consolidate([
        dict(claim="git push deploy", confidence=.9),
        dict(claim="git push deploy", confidence=.5),
        dict(claim="run tests", confidence=.8)])))


if __name__ == "__main__":
    demo()
