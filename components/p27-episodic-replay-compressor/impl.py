# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P27 episodic-replay-compressor — 记忆巩固/溯源

L0: 把一长串经历压成几句能回放的摘要，省地方还能重演。
L1: 按事件类型去重后按时间拼接，截断到 max_len。
L2: compress(events, max_len) → 摘要字符串。
"""

def compress(events, max_len=120):
    seen, out = set(), []
    for e in events:
        if e not in seen:
            seen.add(e); out.append(e)
    s = " -> ".join(out)
    return s[:max_len]

def demo():
    print("[P27]", compress(["start","read","read","write","end"]))


if __name__ == "__main__":
    demo()
