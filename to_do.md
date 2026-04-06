# Experiment Progress & Next Steps

> **Updated**: 2026-04-07 02:30
> **Status**: Phase 1-2 完成, Phase 3 (初稿) 完成, 进入修订阶段

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

## 已完成工作

### Phase 3: 论文初稿 ✅ (2026-04-07)

- [x] **draft_v1.md**: 完整初稿, ~8,100 词, 7 个章节 + 摘要 + 41 条参考文献
- [x] **6 张论文图表**: `figures/gen_paper_figures.py` 生成
  - Fig 1: Precision Paradox (Phase I/II 对比)
  - Fig 2: Pipeline 假设 vs 生物学现实
  - Fig 3: Cascading Valley of Death
  - Fig 4: Goodhart Gradient (核心实证发现)
  - Fig 5: Integration Framework (三层方案)
  - Fig 6: Strategic Timeline 2020-2030
- [x] **Table 1**: 2D / Animal / OoC 对比 (内嵌 Section 6.1)
- [x] **Table 3**: 跨系统实证评估 (内嵌 Section 5.3)
- [x] **GitHub**: https://github.com/starpacker/aidd-review

---

## 下一步工作

### 高优先级 — Phase 4: 修订 & 完善

- [ ] **Self-review**: 逻辑连贯性, 论证一致性, 缺失引用, 冗余
- [ ] **引用检查**: 交叉验证所有 41 条参考文献, 确保 DOI 正确
- [ ] **补充引用**: 目前 41 条, 目标 100-150 条 (每节补充)
- [ ] **语言润色**: Nature 级别英语, 主动语态, 无填充词
- [ ] **图表优化**: 发布质量 (考虑 BioRender 替代 matplotlib 概念图)

### 中优先级 — 补充实验

- [ ] **ADMET-AI**: 在更大内存机器 (≥32GB) 上运行 `test_admet_ai_system.py`
- [ ] **ClinTox 数据集扩展**: 从 1,491 分子中系统抽样, 增加统计效力
- [ ] **重复实验**: 用不同 temperature 运行 LLM 评估, 检验稳定性

### 低优先级

- [ ] **Cover letter**: 投稿封面信
- [ ] **格式化**: 按期刊要求格式化 (结构化摘要, 参考文献格式)
- [ ] **补充材料**: 实验细节, 数据集描述, 完整统计结果

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
