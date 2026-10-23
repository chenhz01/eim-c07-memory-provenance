# P25 · drift-aware-consolidator

> 机制簇：**记忆巩固/溯源** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
记忆会过时、重复。这个工具合并重复的、丢掉过时的。

**L1 · 机制本质**
按 token Jaccard 相似度合并近重复，保留置信度高者。

**L2 · 怎么用上**
consolidate(items, thr) → 合并后列表。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P25] 2
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 长期 agent、需要 cite-or-abstain（有据才答）、多来源冲突需仲裁。 |
| **不该用** | 单轮问答、无历史依赖的纯生成。 |
| **常见误用** | 伪造 provenance：比没有溯源更危险，因为它让人误以为可审计。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P24` tool-use-memory-ledger · `P26` cite-or-abstain-memory · `P27` episodic-replay-compressor
- 本仓是 **P25 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P25-drift-aware-consolidator/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](../../LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](../../LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P25 · drift-aware-consolidator © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](../../NOTICE)。
