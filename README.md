# C07 · Memory Provenance

> **机制簇**：记忆巩固/溯源 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
让 AI 的记忆能说清「这句话从哪来的」；没来源就承认不知道，而不是瞎编。

**L1 · 机制本质**
每条记忆带 provenance（源 URL/文件/行号）与置信度；巩固时去重合并但保留来源链；无源则 abstain。

**L2 · 怎么用上**
provenance-ledger 记账；consolidator 合并去重；cite-or-abstain 做对外出口闸。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c07-memory-provenance.git && cd eim-c07-memory-provenance
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p24-tool-use-memory-ledger/impl.py        # 看 demo 输出
python components/p24-tool-use-memory-ledger/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P24` | tool-use-memory-ledger | 每条记忆带(source, confidence, ts)；cite(query) 返回带溯源的命中。 | `components/p24-tool-use-memory-ledger/` |
| `P25` | drift-aware-consolidator | 按 token Jaccard 相似度合并近重复，保留置信度高者。 | `components/p25-drift-aware-consolidator/` |
| `P26` | cite-or-abstain-memory | 检索命中且有 source 才回答，否则 ABSTAIN。 | `components/p26-cite-or-abstain-memory/` |
| `P27` | episodic-replay-compressor | 按事件类型去重后按时间拼接，截断到 max_len。 | `components/p27-episodic-replay-compressor/` |

## 该用 / 不该用 / 常见误用

**该用**
知识库问答、法务/医疗/财务等要求可追溯的场景；长期记忆库维护。

**不该用**
纯创意生成（无源可溯）；一次性临时上下文。

**常见误用（这条最重要）**
有 URL 就当作已核验。URL 会 404、内容会变——必须回源比对正文。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C07 · Memory Provenance © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
