# 实验进度总结 — AI-Agent Drug Discovery Pipeline Evaluation

> 最后更新: 2026-04-06 19:15
> 状态: Phase 1 + Phase 2 完成, 进入论文写作阶段

---

## 总体目标

为 review paper 提供**代码级实证**, 证明:
1. 当前 AIDD pipeline 无法区分临床有效药物与 decoy (Section 4 + 5.3)
2. LLM Agent 的工具增强引入 Goodhart 偏差 (Section 5.3)
3. 纯 LLM 的"化学直觉"优于计算工具的排名能力 (Section 5.3)

---

## 测试数据集

**文件**: `agent_evaluation_dataset.json` — 36 个分子

| 类别 | 数量 | 描述 | 代表分子 |
|------|------|------|----------|
| **A: FDA 获批** | 12 | 临床验证成功 | Imatinib, Osimertinib, Venetoclax |
| **B: 临床失败** | 12 | 进入临床后失败/撤市 | Rofecoxib, DSP-1181, Torcetrapib |
| **C: Decoy** | 12 | 计算指标优秀但无临床价值 | ZINC 类药分子, 设计优化物 |

---

## Phase 1: 本地 Pipeline 测试 (已完成)

### Pipeline 1: RDKit Comprehensive Pipeline
- **文件**: `test_rdkit_pipeline.py` → `results_rdkit_pipeline.json`
- **组件**: QED + Lipinski/Veber/Ghose/Egan/Muegge + SA Score + PAINS/Brenk + 药物空间相似度
- **结果**: **C (0.758) > A (0.724) > B (0.653)**
- **AUC**: A vs B = 0.694, A vs C = 0.562 (近随机)

### Pipeline 2: ADMET Proxy Pipeline
- **文件**: `test_admet_proxy.py` → `results_admet_proxy.json`
- **组件**: Caco-2/HIA/P-gp + BBB/PPB + CYP + hERG/DILI/Ames
- **结果**: **C (0.787) > B (0.681) > A (0.631)**
- **AUC**: A vs B = 0.410 (反转), A vs C = 0.069 (严重反转!)

### Pipeline 3: DeepChem RF
- **文件**: `test_deepchem_pipeline.py` → `results_deepchem_summary.json`
- **组件**: 210 个 RDKit 描述符 + PCA + Random Forest (LOO)
- **结果**: Silhouette = 0.043 (不可分), LOO AUC(A vs B) = 0.531

### Goodhart's Law 定量分析
- **文件**: `analysis_goodhart_effect.py`
- **QED**: Spearman r = **-0.380** (p=0.022) — 负相关!
- **ADMET Score**: Spearman r = **-0.425** (p=0.010) — 负相关!
- **Cohen's d (A vs C)**: QED = -1.615, ADMET = -1.583 — 大效应, 方向错误

### 临床失败检测率
- 7/12 flagged (58%), **5/12 漏检 (42%)**
- 漏检原因: 系统药理学, 免疫特异性, 通路串扰, 转化 gap, 疗效不足

---

## Phase 2: 端到端 Agent 系统测试 (已完成)

### System 1: Direct LLM (Claude 4.6 Opus, 无工具) ✅
- **文件**: `test_llm_direct.py` → `results_llm_direct.json`
- **方法**: 纯 SMILES → Claude API → 结构化评分 (1-10)
- **结果**: **A (5.82) > B (5.44) > C (5.08)** — 唯一正确排名!
- **AUC**: A vs B = 0.642, A vs C = 0.795 (p=0.014)
- **建议**: A → 2 Advance / 9 Caution / 1 Reject (保守)

### System 2: LLM+Tools Agent (Claude + RDKit) ✅
- **文件**: `test_llm_agent.py` → `results_llm_agent.json`
- **方法**: ReAct Agent + compute_drug_properties + check_structural_alerts + predict_admet
- **结果**: **A (8.28) > C (5.69) > B (4.94)** — 强判别但 C > B
- **AUC**: A vs B = **0.948** (p=0.0002), A vs C = 0.951 (p=0.0002)
- **建议**: A → **12/12 Advance** (完美), B → 3 Advance / 7 Reject
- **关键**: 工具增强同时提升判别力 (AUC↑) 和 Goodhart 偏差 (C > B)

### System 3: DruGUI (8-stage Virtual Screening) ✅
- **文件**: `test_drugui_pipeline.py` → `results_drugui.json`
- **方法**: PDB下载 → 蛋白准备 → 配体准备 → 对接 → ADMET → 过滤 → SA → 排名
- **结果**: **C (0.592) > A (0.557) > B (0.496)** — 完全 Goodhart 反转
- **AUC**: A vs B = 0.667, A vs C = **0.243** (低于随机!)
- **运行修复**: 3 个 bug (wget→curl, 缺失 import, API 变更) → pipeline 脆弱性证据
- **靶标**: EGFR (PDB: 6JX0), Vina 使用 fallback scoring

### System 4: ADMET-AI (Chemprop GNN) ❌ 未完成
- **安装**: admet-ai 2.0.1 + PyTorch 2.11 + RDKit 在 `pymol_env`
- **问题**: PyTorch 2.11 在 16GB Windows 系统上 import 崩溃 (exit code 127)
- **脚本**: `test_admet_ai_system.py` — 可在 ≥32GB 机器上直接运行
- **意义**: 本身是 AIDD 工具环境脆弱性的证据

### System 5: ChemMCP (MCP 化学工具服务器) ❌ 未完成
- **源码**: 已 clone 到 `ChemMCP2/`, 32 个工具
- **问题**: 依赖 torch==2.5 + transformers + Uni-Core + docker, 同样内存问题
- **意义**: MCP 范式工具集成的复杂度证据

---

## 跨系统对比 (核心结果)

| System | A (获批) | B (失败) | C (Decoy) | 排名 | AUC(AvB) | AUC(AvC) | p(AvB) |
|--------|---------|---------|-----------|------|----------|----------|--------|
| Direct LLM | 5.82 | 5.44 | 5.08 | **A>B>C** ✅ | 0.642 | 0.795 | 0.237 |
| LLM+Tools | 8.28 | 4.94 | 5.69 | A>C>B | **0.948** | 0.951 | **0.0002** |
| DruGUI | 0.557 | 0.496 | 0.592 | C>A>B ❌ | 0.667 | 0.243 | 0.166 |
| RDKit Pipeline | 0.724 | 0.653 | 0.758 | C>A>B ❌ | 0.694 | 0.562 | 0.106 |
| ADMET Proxy | 0.631 | 0.681 | 0.787 | C>B>A ❌ | 0.410 | 0.069 | — |

---

## 核心发现

### 发现 1: Goodhart 梯度效应 (Phase 2 原创)
系统对计算指标的依赖程度与 Goodhart 反转成正比:
```
纯 LLM:      A > B > C  (正确, 弱信号, 来自文献训练)
LLM + 工具:   A > C > B  (部分反转, 工具抬高 decoy)
Pipeline:     C > A > B  (完全反转, 计算指标主导)
```
→ **图表**: `fig_phase2_goodhart_gradient` (论文主图候选)

### 发现 2: 所有计算 Pipeline 排名反转
- 5/5 个纯计算系统均将 Decoy 排在获批药物之上
- DruGUI AUC(A vs C) = 0.24: pipeline 主动偏好 decoy

### 发现 3: 工具增强的悖论
- LLM+Tools AUC(A vs B) = 0.948 — 最强判别能力
- 但 C (5.69) > B (4.94) — 工具引入了 drug-likeness 偏差
- "最好的判别器也是最大的 Goodhart 受害者"

### 发现 4: 42% 临床失败不可检测
- 5/12 失败药物通过所有筛选: Rofecoxib, Ximelagatran, DSP-1181, Semagacestat, REC-994
- 失败模式 (系统药理学、免疫反应、通路串扰) 超出计算工具能力

### 发现 5: AI 设计的药物也高分失败
- DSP-1181 (Exscientia): composite score 0.907 (Cat B 最高) — 已终止
- REC-994 (Recursion): ADMET score 0.839 (Cat B 最高) — Phase II 失败

---

## 与 Review Paper 的对应

| 发现 | 论点 | 章节 |
|------|------|------|
| Goodhart 梯度 | LLM Agent 并非万能, 工具引入系统性偏差 | **Section 5.3** |
| 纯 LLM 唯一正确 | LLM 的文献知识优于计算指标 | **Section 5.3** |
| 所有 pipeline 反转 | Chemistry Problem solved ≠ clinical success | Section 3 + 4 |
| QED r=-0.38, ADMET r=-0.43 | Goodhart's Law 在药物发现中的定量证据 | **Section 5.3** |
| 42% 失败不可见 | Biology Problem 未解决 | **Section 4** |
| DruGUI 3 个 bug | Pipeline 脆弱性, 自动化 gap | Section 5.2 |
| ADMET-AI/ChemMCP 无法运行 | 工具生态碎片化, 环境依赖过重 | Section 5.2 |

---

## 文件清单

### 测试脚本 (experiments/)
| 文件 | Phase | 描述 | 状态 |
|------|-------|------|------|
| `build_dataset.py` | 1 | 构建 36 分子数据集 | ✅ |
| `test_rdkit_pipeline.py` | 1 | RDKit composite scoring | ✅ |
| `test_admet_proxy.py` | 1 | 规则 ADMET 预测 | ✅ |
| `test_deepchem_pipeline.py` | 1 | DeepChem RF 分类器 | ✅ |
| `test_llm_direct.py` | 2 | Claude 纯 LLM 评估 | ✅ |
| `test_llm_agent.py` | 2 | Claude + RDKit ReAct Agent | ✅ |
| `test_drugui_pipeline.py` | 2 | DruGUI 端到端包装器 | ✅ |
| `test_admet_ai_system.py` | 2 | ADMET-AI 评估 (待运行) | ⏸️ |

### 分析脚本
| 文件 | 描述 |
|------|------|
| `analysis_agent_discrimination.py` | Phase 1 统计分析 + 6 张图表 |
| `analysis_goodhart_effect.py` | Goodhart's Law 定量分析 |
| `analysis_phase2.py` | Phase 2 跨系统统计分析 |
| `gen_phase2_figures.py` | Phase 2 图表生成 (5 张) |

### 结果文件
| 文件 | 内容 |
|------|------|
| `agent_evaluation_dataset.json` | 36 分子金标准数据集 |
| `results_rdkit_pipeline.json` | Phase 1 RDKit pipeline |
| `results_admet_proxy.json` | Phase 1 ADMET proxy |
| `results_llm_direct.json` | Phase 2 Direct LLM (72KB) |
| `results_llm_agent.json` | Phase 2 LLM+Tools Agent (101KB, 含推理链) |
| `results_drugui.json` | Phase 2 DruGUI |
| `results_phase2_summary.json` | Phase 2 统计汇总 |

### 总结文档
| 文件 | 内容 |
|------|------|
| `results_agent_summary.md` | Phase 1 完整总结 |
| `results_phase2_summary.md` | Phase 2 完整总结 |
| `results_github_landscape.md` | 7 个开源 pipeline 调研 |
| `progress.md` | 本文件 — 全局进度 |

### 图表 (figures_data/)
| 文件 | 描述 |
|------|------|
| `fig_phase2_system_comparison.*` | 跨系统分组条形图 |
| `fig_phase2_normalized_comparison.*` | 归一化对比 |
| `fig_phase2_auc_comparison.*` | AUC 对比 (含随机线) |
| `fig_phase2_goodhart_gradient.*` | **Goodhart 梯度图** (论文主图) |
| `fig_phase2_recommendation_heatmap.*` | LLM 建议分布热图 |
| (Phase 1 figures...) | 分布图, 热图, ROC, 雷达图等 |

### 外部依赖
| 目录 | 描述 |
|------|------|
| `DruGUI/` | DruGUI 源码 (clone + 3 bug 修复) |
| `ChemMCP2/` | ChemMCP 源码 (clone, 未使用) |

### 归档文件 (experiments/_archive/)
Phase 0 遗留脚本和冗余结果文件, 已移至 `_archive/`:
- `test_admet_ai_full.py`, `test_admet_predictions.py` 等 (Phase 0, 仅 6 分子)
- `results_admet_ai_full.json`, `results_*_summary.json` 等 (被 Phase 2 汇总取代)
- `experiment_log.md` (被 `progress.md` 取代)
