# P26 · cite-or-abstain-memory

> 机制簇：**记忆巩固/溯源** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
没有出处就别硬答，直接说'不知道'，比为编一个更可信。

**L1 · 机制本质**
检索命中且有 source 才回答，否则 ABSTAIN。

**L2 · 怎么用上**
answer(ledger, q) → (text, source) 或 ('ABSTAIN', None)。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P26] ('x is 1', 'math') ('ABSTAIN', None)
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 长期 agent、需要 cite-or-abstain（有据才答）、多来源冲突需仲裁。 |
| **不该用** | 单轮问答、无历史依赖的纯生成。 |
| **常见误用** | 伪造 provenance：比没有溯源更危险，因为它让人误以为可审计。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P24` tool-use-memory-ledger · `P25` drift-aware-consolidator · `P27` episodic-replay-compressor
- 本仓是 **P26 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P26-cite-or-abstain-memory/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P26 · cite-or-abstain-memory © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
