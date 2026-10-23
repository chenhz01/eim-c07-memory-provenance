# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P24 tool-use-memory-ledger — 记忆巩固/溯源

L0: 记住'哪个工具怎么用过'，并且记得它是从哪儿知道的，防止瞎编。
L1: 每条记忆带(source, confidence, ts)；cite(query) 返回带溯源的命中。
L2: L=MemoryLedger(); L.add(...); L.cite('deploy')。
"""

class MemoryLedger:
    def __init__(self): self.items = []
    def add(self, claim, source, confidence=1.0):
        self.items.append(dict(claim=claim, source=source, confidence=confidence))
    def cite(self, query):
        return [i for i in self.items if query.lower() in i["claim"].lower()]

def demo():
    L = MemoryLedger(); L.add("deploy uses git push", "doc:x", 0.9)
    print("[P24]", L.cite("deploy"))


if __name__ == "__main__":
    demo()
