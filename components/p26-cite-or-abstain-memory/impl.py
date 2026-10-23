# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P26 cite-or-abstain-memory — 记忆巩固/溯源

L0: 没有出处就别硬答，直接说'不知道'，比为编一个更可信。
L1: 检索命中且有 source 才回答，否则 ABSTAIN。
L2: answer(ledger, q) → (text, source) 或 ('ABSTAIN', None)。
"""

def answer(ledger, q):
    hits = [i for i in ledger.items if q.lower() in i["claim"].lower() and i.get("source")]
    if not hits: return ("ABSTAIN", None)
    best = max(hits, key=lambda i: i.get("confidence", 0))
    return (best["claim"], best["source"])

def demo():
    class L: items=[dict(claim="x is 1", source="math", confidence=.9)]
    print("[P26]", answer(L(), "x"), answer(L(), "y"))


if __name__ == "__main__":
    demo()
