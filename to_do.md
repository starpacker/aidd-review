# Experiment Progress & Next Steps

> **Updated**: 2026-04-06 19:15
> **Status**: Phase 1 完成, Phase 2 完成 (4/6 系统), 进入论文写作阶段

---

## 已完成实验总览

### Phase 1: 本地 Pipeline 测试 ✅

| Pipeline | 脚本 | 结果 | 排名 | AUC(A vs B) |
|----------|------|------|------|-------------|
| RDKit Composite | `test_rdkit_pipeline.py` | `results_rdkit_pipeline.json` | C > A > B ❌ | 0.694 |
| ADMET Proxy | `test_admet_proxy.py` | `results_admet_proxy.json` | C > B > A ❌ | 0.410 |
| DeepChem RF | `test_deepchem_pipeline.py` | `results_deepchem_summary.json` | 不可分 | 0.531 |
| QED alone | (内嵌分析) | — | C > B > A ❌ | — |

### Phase 2: 端到端 Agent 系统测试 ✅

| System | 脚本 | 结果 | 排名 | AUC(A vs B) | 状态 |
|--------|------|------|------|-------------|------|
| Direct LLM (Claude 4.6) | `test_llm_direct.py` | `results_llm_direct.json` | **A > B > C** ✅ | 0.642 | ✅ 完成 |
| LLM+Tools Agent (Claude+RDKit) | `test_llm_agent.py` | `results_llm_agent.json` | A > C > B | **0.948** | ✅ 完成 |
| DruGUI (8-stage VS) | `test_drugui_pipeline.py` | `results_drugui.json` | C > A > B ❌ | 0.667 | ✅ 完成 |
| ADMET-AI (Chemprop GNN) | `test_admet_ai_system.py` | — | — | — | ❌ PyTorch OOM |
| ChemMCP (MCP 工具) | — | — | — | — | ❌ 依赖过重 |

### 统计分析 & 图表 ✅

| 分析 | 脚本 | 产出 |
|------|------|------|
| Phase 1 统计 | `analysis_agent_discrimination.py` | 6 张图表 (SVG+PNG) |
| Goodhart 定量 | `analysis_goodhart_effect.py` | QED r=-0.38, ADMET r=-0.43 |
| Phase 2 跨系统 | `analysis_phase2.py` | `results_phase2_summary.json` |
| Phase 2 图表 | `gen_phase2_figures.py` | 5 张图表 (PNG+PDF) |

---

## 核心发现 (论文可用)

1. **Goodhart 梯度效应**: 纯 LLM → LLM+Tools → Pipeline, 计算指标依赖越深, 排名越偏离临床实际
2. **纯 LLM 唯一正确**: Claude 4.6 Opus 无工具时 A > B > C, 所有工具/pipeline 系统均反转
3. **工具增强悖论**: LLM+Tools AUC=0.948 (最强判别) 但 C > B (Goodhart 偏差)
4. **DruGUI AUC(A vs C)=0.24**: 低于随机, pipeline 主动偏好 decoy
5. **42% 临床失败不可见**: 5/12 失败药物通过所有计算筛选
6. **3 个 bug 才能运行 DruGUI**: wget/import/API 兼容问题 → pipeline 脆弱性证据

---

## 下一步工作

### 高优先级 — 论文写作

- [ ] **Draft Section 5.3**: 整合 Phase 2 数据, 用 Goodhart 梯度作为核心论证
- [ ] **更新 Figure 计划**: 将 `fig_phase2_goodhart_gradient` 定为论文主图之一
- [ ] **Draft Section 4**: 整合 42% 不可见失败 + 级联衰减数据

### 中优先级 — 补充实验

- [ ] **ADMET-AI**: 在更大内存机器 (≥32GB) 上运行 `test_admet_ai_system.py`
  - 已安装 `admet-ai 2.0.1` 在 `pymol_env`
  - 输入文件已准备: `admet_input.csv`
- [ ] **ClinTox 数据集扩展**: 从 1,491 分子中系统抽样, 增加统计效力
  - 脚本: `build_clintox_dataset.py` (待写)
  - 数据源: `dc.molnet.load_clintox()`

### 低优先级 — 额外工作

- [ ] **ChemMCP**: 源码已 clone 到 `ChemMCP2/`, 但依赖 torch + transformers
- [ ] **重复实验**: 用不同 temperature 运行 LLM 评估, 检验稳定性
- [ ] **更多 Agent 系统**: AgentD, RepurAgent (需 GPU)

---

## API 资源 (保留)

```yaml
model: "cds/Claude-4.6-opus"
api_type: "openai-compatible"
base_url: "https://ai-gateway-internal.dp.tech/v1"
api_key: "${AIDD_API_KEY}"
temperature: 0.7
```

## 环境信息

| 环境 | Python | 关键包 | 用途 |
|------|--------|--------|------|
| `.venv38` | 3.8 | RDKit 2024.03.5, openai, numpy, matplotlib | Phase 1 pipeline + 分析 |
| `pymol_env` | 3.11 | openai, admet-ai 2.0.1, torch 2.11 | Phase 2 LLM + ADMET-AI |
| `druGUI` | 3.11 | RDKit 2026.03.1, pdbfixer, openmm | Phase 2 DruGUI |
