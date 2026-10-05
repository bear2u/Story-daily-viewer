# Source audit — Harness Engineering, arXiv:2609.00006v1

검토 기준: 2026-10-06 (Asia/Seoul). 첨부 PDF 83쪽의 본문·부록·참고문헌 전체를 읽었음. 이 문서는 계보·범위 조사이며 최종 원고의 독립 팩트체크는 아님. 원문 페이지는 PDF의 인쇄 페이지와 같음. 작업 대상 외 파일은 수정하지 않았음.

## 1. 공개 메타데이터와 저자

| 항목 | 확인값 | 좁은 위치·원문 근거 |
|---|---|---|
| 제목 | Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems | 첨부 PDF p.1 title block; [arXiv v1](https://arxiv.org/abs/2609.00006v1) title |
| 저자 | Paul Barbaste, Tristan Darrigol, Germain Vu, Tom Wiltberger | PDF p.1; arXiv authors |
| 소속 | Barbaste: Inclusive Brains와 Wavestone AI Lab; 나머지 세 명: Wavestone AI Lab | PDF p.1 affiliation superscript 1,2 / 2 / 2 / 2 |
| 교신·선도 저자 | Paul Barbaste | p.1 footnote: “Lead and corresponding author.” |
| 날짜 | 공식 arXiv v1 제출기록 2026-07-15 10:33:30 UTC; PDF July 2026 및 15 Jul 2026 | arXiv Submission history. ID의 2609를 보고 9월 공개라고 추론하면 안 됨. 여러 2차 인덱스는 9월2일을 보여주지만 공식 원문 기록과 다름. |
| 판본 | 확인 가능한 arXiv history에는 v1만 있음 | arXiv v1 Submission history |
| DOI | 10.48550/arXiv.2609.00006 | arXiv “arXiv-issued DOI via DataCite” |
| 분량 | 83쪽, 7 figures, 18 tables | arXiv Comments; PDF p.1–83 |
| 라이선스 | CC BY 4.0 | [arXiv HTML](https://arxiv.org/html/2609.00006v1) 상단 license; arXiv abs “view license”가 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)로 연결됨. 크롭의 출처·라이선스·크롭/크기조절 표시 유지 필요. |
| 심사 | 2026-10-06 확인 범위에서 공식 심사 통과·학회/저널 게재 확인 못함. 프리프린트로 표현 | arXiv에 journal-ref/게재처 없음. [저자 게시글](https://www.linkedin.com/posts/paulbarbaste_our-preprint-is-available-last-project-activity-7501576072845705219-raIK)은 “Our preprint is available!”라고 직접 부름. “심사 안 받았다”까지 단정할 근거는 없음. |

웹 참조: `turn22view0` arXiv metadata; `turn21view1` arXiv HTML; `turn21view2` main PDF; `turn23view0` CC license; `turn24view1` author preprint post. 루트가 최종 citation을 쓰려면 해당 페이지를 직접 open/find해야 함.

저자 현재 소속을 소개할 필요는 없음. 논문 당시 소속으로 충분함. 저자 개인 사이트는 Wavestone 현재 재직이라고 쓰지만 최근 저자 게시글은 leaving Wavestone이라고 해 서로 업데이트 시점이 다름. 현재 소속 추정은 제외 권장.

## 2. 무엇을 조사했는가

- 본 코퍼스는 **11개**: Claude Code, Codex CLI, Gemini CLI, Mistral Vibe, OpenHands, Aider, Mini-SWE-Agent, Hermes, Pi, OpenCode, OpenClaw. **Omnigent는 11개 분모 밖의 meta-harness 대조점**임. p.9 §4.1, p.10 Table 3, pp.10–11 boundary paragraphs.
- OpenClaw는 README상 personal AI assistant gateway이고 native code-edit tool 없음. p.10 “OpenClaw as an External Contrast Point”에 코드 작업은 전용 SWE agent로 위임한다고 적음. 엄밀히 코딩 하네스만 말하려면 10개 분모. 이번 핵심 부재 주장은 논문의 11개 샘플 분모로 소개하되 구성 설명 필요.
- 선택 축: design philosophy, maturity, market position. 무작위·전수조사가 아님. p.9 §4.1.
- 비교 차원: loop, LLM integration, tools/actions, memory/context, safety/permissions, multi-agent orchestration, extensibility. p.11 §4.2.
- 2026년7월 release snapshot 중심. **Claude Code는 예외: 2026년3월 circulated source snapshot**이며 7월 shipping binary 2.1.206과 같다고 간주할 수 없음. p.10 Table 3; p.12 Table 4 caption.
- April판의 8개 시스템을 유지·re-pin하여 July판과 source diff. 이는 같은 시스템을 따라 본 longitudinal source sample이지, 동일 모델·동일 task를 통제한 성능 실험이 아님. pp.62–63 §14.5; pp.66–67 §15.6.
- 약4M LoC는 저자 집계의 대략 규모. 모든 agent loop 자체가 4M줄이라는 뜻이 아님. p.11 §4.2: “not reproducible metrics across counting conventions”; p.12 Table 4 note: 언어/계수방법 때문에 직접 비교 불가.
- 8→11은 시스템 수의 3배가 아님. 초록의 “threefold corpus expansion”을 시스템 개수 3배로 번역하면 오류임.

## 3. 부정 주장 1: 일반 agent framework 0의 정확한 범위

주장의 안전한 문장: **저자들이 고정한 11개 소스에서 검사한 범용 에이전트 orchestration framework가 production agent runtime에 import되는 경로는 발견하지 못했음.**

PDF p.53 §13.2 “Absence 1”:

> Every dependency manifest was inspected, and every source tree grepped for imports ... Across roughly 4 M lines ... no production agent code path imports any of them.

검사 목록: LangChain, LangGraph, LlamaIndex, AutoGen, CrewAI, Pydantic AI, Genkit, Haystack agents, Semantic Kernel, Google ADK, Smolagents, Swarm, Agno. p.53.

예외·경계는 같은 문단에 명시됨:

1. **Aider `/help` optional extra:** llama-index 설치로 Aider 자체 documentation의 doc-RAG 수행 가능. agent-loop orchestration이 아님. “Aider는 LlamaIndex 전혀 안 씀”은 잘못임.
2. **OpenCode Vercel AI SDK:** inner LLM/tool plumbing을 외부 SDK에 맡김. 논문은 provider-abstraction layer로 분류하고 agent-orchestration framework와 구별함. 따라서 “11개 전부 SDK 없이 모델 API를 raw 구현”은 잘못임.
3. OpenHands/Aider/Mini-SWE-Agent의 LiteLLM도 provider abstraction dependency임. p.18 §7.1. 다른 도구 라이브러리(Pydantic, Zod, TypeBox, Effect Schema) 및 runtime(Tokio/asyncio)은 당연히 존재함. “외부 라이브러리 0”이 아님.
4. Omnigent는 본 분모 밖이고 baseline dependencies로 claude-agent-sdk와 openai-agents를 import함. pp.60–62 §§14.2–14.4. 저자들은 harness SDK category merger로 해석함. “meta-layer도 모든 SDK/framework dependency 0”으로 옮기면 안 됨.
5. §14.2 Table 15 (p.60)는 **Deep Agents built on LangGraph**, Pydantic AI Harness, Strands harness-sdk를 본 코퍼스 바깥 framework→harness 사례로 명시함. 따라서 범용 framework가 쓸모없다는 일반법칙으로 읽을 수 없음.

pp.66–67 §15.6 limitation:

> we did not trace internal forks, plugins loaded via dynamic importlib/require, or transpiled distributions.

Manifest/import grep의 관찰 범위임. 실제 모든 실행 경로를 trace한 검증이나 기업 private fork까지 확인한 결과가 아님. p.53 footnote는 counterexample sweep을 여러 주 했다고 쓰지만, 최종 threat paragraph의 tracing omission을 제거하지 못함.

## 4. 부정 주장 2: code vector retrieval 0의 정확한 범위

주장의 안전한 문장: **저자들의 11개 샘플은 source tree의 코드를 찾아 읽는 기능에 vector embedding retrieval을 사용하지 않았음.**

PDF p.54 §13.2 “Absence 2”:

> For code retrieval the result is unchanged and now spans eleven systems: zero. The exceptions all concern conversation memory.

검사 대상: vector-store deps(Chroma, Pinecone, Weaviate, Qdrant, Milvus, FAISS, LanceDB, sqlite-vec, vector-mode Elasticsearch), embedding libraries 및 embedding/vector_store/vectordb/rag/retrieval 이름 파일·폴더. pp.54–55 Table 13은 코드탐색 방법을 시스템별로 표시함.

정확한 예외:

- **OpenClaw default memory-core:** chat/conversation recall에 sqlite-vec KNN + FTS5/BM25 hybrid; embeddings 기본 ON, 기본 provider OpenAI, local GGUF opt-in. 기존 LanceDB conversation extension도 optional로 존속. p.54 및 p.55 Table 13. source tree code retrieval은 N/A.
- **Hermes:** core past conversation search는 SQLite FTS5 BM25/CJK trigram lexical; embedding은 opt-in memory plugins. p.54.
- **Aider `/help`:** Aider docs의 optional embedding doc-RAG. code retrieval이 아님. p.53 및 p.55 Table 13.
- **코드 RAG**를 keyword/structural search까지 포함하는 넓은 뜻으로 사용하면 원문의 0/11과 정의가 달라짐. 실제로 grep/glob/file read/Tree-sitter/PageRank 등 retrieval 자체는 존재함.

내부 불일치 주의:

- p.34 Observation 5는 “none ... embedding-based retrieval as its primary memory substrate”라고 쓰고 OpenClaw를 optional LanceDB로만 소개함.
- 더 구체적인 pp.54–55 §13.2/Table 13은 OpenClaw default hybrid embeddings를 적음.
- 따라서 보고서에서는 “메모리까지 전부 embedding 없음”이라는 p.34 보편 문장은 쓰지 말 것. 코드 탐색/대화 회상을 명시적으로 나누는 쪽이 정확함.

관찰과 해석/권고 구별:

- “index가 stale해짐”, “code에는 deterministic structure가 많음”, “debuggability outweighs reuse”는 저자들의 §13.2 해석임. 이 연구가 여러 검색기를 matched benchmark로 비교해 입증한 인과가 아님.
- p.69 Recommendation 8 및 p.70 Recommendations 15–16은 저자 **처방**임. 같은 원문 p.70 Recommendation 16은 semantic code retrieval을 원하면 held-out task set에서 ripgrep+tree-sitter보다 좋아지는지 먼저 증명하라고 조건을 붙임.
- 안전한 해설: “샘플에서 자주 보인 출발점을 권고했음. framework나 semantic retrieval이 본질적으로 성능을 망친다는 실험은 없음.”

## 5. 방법론·성능·재현성의 한계

| 공개 원고에서 꼭 좁혀야 할 주장 | 원문 위치 | 독자가 읽어야 할 범위 |
|---|---|---|
| 가장 좋은 coding agent 순위? | p.1 abstract; pp.66–67 §15.6 | benchmark/rank 하지 않는 구조 조사. 동일 task set을 11개에 실행하지 않음. |
| 단순 loop가 복잡한 것보다 더 잘함? | p.11 footnote 4; p.58 Axis1 | spring self-reported 수치들은 모델·시점·배포 설정이 달라 head-to-head 결론 없음. Table 4에서 해당 수치를 제거했음. 성능 숫자를 표지 punchline으로 사용하지 말 것. |
| 90줄 하네스로 production 완성? | pp.71–72 Listing3, Observation13 | illustrative scaffold, not production code. sandbox/multi-agent/MCP/skills 생략. frontier model에서 Mini-SWE와 맞먹을 것이라는 문장은 “conjecture, without proof”. |
| 실제 latency/cost/safety effect? | p.66 §15.6 | source reading; runtime measurement 아님. “더 빠름/저렴함/안전함을 확인”이 아니라 구현된 설계를 기술. |
| qualitative scoring이 객관적 수치? | pp.66–67 §15.6 | judgment calls라고 저자 명시. 개별 implementation details를 근거로 했음. |
| source evidence를 누구나 동일하게 복원? | p.67 §15.6 | release tags/commits를 pinned했다고 주장하고 Table3에서 tags를 제공하지만 세부 line citations를 deliberately avoid. Claude source는 공식 release가 아님. |
| 7월 Claude Code 구조? | p.12 Table4 caption; p.67 §15.6 | March circulated source 기준; shipping binary 진화를 changelog로만 따라갔고 changelog를 source evidence 취급하지 않음. |
| Anthropic 가이드 때문에 다들 이 구조를 채택? | p.56 Observation10; p.67 §15.6 | influence/shared empirical reality/both는 open question. 엔지니어 interview 안 함. |
| AI 도움 없이 사람이 모든 code read? | p.74 disclosure | Claude Code로 source-code analysis와 manuscript drafting 모두 substantial assistance 받았다고 공개. findings를 authors가 referenced codebases against verified했다고 주장. |

원장 후보로 붙일 짧은 원문:

- p.66: “The analysis rests on source-code reading, not runtime measurement.”
- p.67: “We also compared each system independently rather than running all eleven on a shared task set.”
- p.67: “The Claude Code analysis is the weakest link on reproducibility.”
- p.72: “We conjecture, without proof ...”
- p.74: “used both for the source-code analysis and for drafting the manuscript.”

현재 기능과 논문 snapshot을 혼합하지 말 것. 특히 tool counts, pins, prompt text, SDK/API surfaces, stars, market transactions를 2026-10-06 현재 사실처럼 쓰면 안 됨. §3.7 p.8 footnote는 market events가 source-verified 아니고 2026-07-10 vendor announcements/release notes/repository metadata라고 자체 구분함. 이 부분은 중심 서사에 필요 없으면 생략하는 것이 좋음.

## 6. April 자기 전작 — 찾은 것과 못 찾은 것

직접 공개된 April manuscript PDF/원문 URL/독립 arXiv ID는 확보하지 못했음.

근거와 조사:

1. 이번 논문 arXiv Comments는 “Second, substantially expanded edition of an April 2026 study”라고 명시함. 본문 pp.2,9,11,62–63,67에서 April edition/retained snapshots를 설명하지만 별도 April 논문을 참고문헌에 URL/ID로 싣지 않음.
2. 공식 arXiv v1 history에 앞선 April version은 없음.
3. 저자 본인 [개인 사이트](https://paulhb7.github.io/) publications의 항목은 “Inside coding agents: a comprehensive review of SWE agentic systems”, “To be published · May 2026”임. 해당 항목에는 PDF/논문 링크가 없음. 사이트 자체가 Wavestone current job 등 업데이트가 느릴 수 있으므로 이 제목을 April manuscript의 확정 제목이라 단정하지 말 것.
4. 제목/저자/April/scaffold/8 agents 조합을 두 검색 엔진에서 찾았으나 공개 원문을 확인하지 못함. arXiv author search endpoint는 fetch 실패함. 이를 “전작이 존재하지 않음”의 증거로 쓸 수 없음.

따라서 계보 원고에는 **“저자들은 April판의 8개를 다시 고정해 7월판과 비교했다고 설명함. 별도 April 원문은 확보하지 못했음”**이라고 한정할 수 있음. April판 저자와 이번 4명의 교집합은 **확인 불가**. 앞선 판본이 동일 연구팀일 가능성은 있지만 저자표를 확인하지 않아 author relationship으로 확정할 수 없음.

## 7. 확보한 실제 동시기 원문: Rombaut

[Inside the Scaffold: A Source-Code Taxonomy of Coding Agent Architectures](https://arxiv.org/abs/2604.03515), Benjamin Rombaut, v1 2026-04-03; 읽은 v2 2026-04-10; [PDF](https://arxiv.org/pdf/2604.03515) 42쪽.

- PDF p.1 first page에 Benjamin Rombaut 단독 저자. 소속 표시 없음. 특정 기관을 붙이지 말 것.
- 이번 논문 p.6 §3.3은 “developed concurrently with our April edition”, “complementary rather than redundant”라고 명시하며 loop primitives vocabulary가 sharper여서 adopt했다고 씀. **같은 연구팀의 April 전작이 아님.** 저자 교집합 없음.
- 실제 Rombaut p.6 §3.1에서 open source/readable source criterion을 이유로 Claude Code를 제외함. 이 내용은 이번 논문이 그린 보완 관계와 일치함.
- Rombaut p.1 및 pp.6–9: 13개 open-source agents, pinned commit hashes, 12 dimensions/3 layers, qualitative source taxonomy.
- **Rombaut Table8 PDF p.18**: Moatless Tools에 FAISS vector store via LlamaIndex `code_index.py:57`를 명시. 표 문구는 “The only agent with embedding-based retrieval as an LLM-callable tool.”
- Moatless Tools는 이번 11개 본 코퍼스 바깥임. 따라서 이번 0/11이 전체 coding agents에서 vector code retrieval 부재라는 보편 주장은 아니라는 구체 예시가 됨. **반박 논문/직접 후속**이라 부르지 말고 동시기 연구의 다른 표본 사례로만 쓰면 됨.

웹 refs: `turn25view1` arXiv; `turn30view0` PDF; `turn31view0` Table8 찾기; `turn30view1` HTML.

## 8. 잘못 인용된 AHE — 숫자·저자 전재 금지

이번 논문 ref[85] p.83은 X. Lin, C. Ruan, B. Rozière, M. Tufano, M. Velez, B. Shen을 적고, p.6·p.66은 AHE SWE-Bench Verified **71.9%**를 적음.

하지만 실제 [arXiv:2604.25850](https://arxiv.org/abs/2604.25850)의 공식 PDF는 다름:

- 제목은 Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses로 맞음.
- 저자 PDF p.1: **Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Zhiheng Xi, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui, Yu-Gang Jiang**.
- 소속 p.1: Fudan University, Peking University, Shanghai Qiji Zhifeng Co., Ltd. 위 4명 연구팀과 저자 교집합 없음.
- v1 2026-04-28, 읽은 v4 2026-05-18, [원문 PDF](https://arxiv.org/pdf/2604.25850v4) 35쪽.
- actual PDF p.1 abstract 및 p.2 Figure1: Terminal-Bench2 **69.7→77.0%**; **71.9%는 Codex 비교 baseline**임. 이번 논문의 SWE 71.9%는 정확한 인용이 아님.
- actual PDF p.6 §4.1: Terminal-Bench2 89 tasks, SWE-bench-verified 500 tasks/7 repos; prompt+completion 전체 LLM calls tokens/trial. 이를 새 해설에 넣으려면 actual full PDF 전체 정독·별도 원장 필요.

지금 원고에서는 AHE 세부 수치를 생략하는 것이 가장 간단함. `tools +3.3pp / middleware +2.2pp / memory +5.6pp / prompt -2.3pp`도 실제 AHE table에서 따로 확인하기 전에는 main paper 요약만 믿지 말 것.

웹 refs: `turn25view2` actual metadata; `turn29view1` actual PDF first page; `turn31view1` §4.1.

## 9. 문맥 선행 자료와 후속 상태

### 공식 선행 가이드

- Erik Schluntz·Barry Zhang, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 2024-12-19. 공식 페이지 “When and how to use frameworks”는 먼저 direct APIs를 권하되 framework 사용시 내부 코드를 이해하라고 함. framework가 전혀 쓸모없다고 말하지 않음. 현재 페이지에 당시 tooling landscape가 바뀌었다는 안내가 추가되어 있음. 기존 December 가이드의 조언과 최신 제품 예시를 혼합하지 말 것. refs `turn25view3`/`turn26search20`.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025년9월 가이드. 공식 페이지는 runtime exploration의 latency·engineering tradeoff와 **hybrid strategy** 가능성을 명시함. 이번 논문이 권한 “코드 RAG 만들지 말라”의 일반 명제를 원문 가이드가 확정했다고 말할 수 없음. refs `turn30view2`/`turn31view2`, 공식 page lines62–65.

### 직접 후속·독립 재현

2026-10-06 확인 범위에서 **원문을 확보해 관계와 재현 내용을 검증한 직접 후속 논문/독립 재현은 없음**. 이를 “후속이 존재하지 않음”이라고 쓰지는 말 것.

검색 결과에는 교육용 tutorials, author post comments, architecture atlas/handbook, blog summaries가 있었음. 그것들은 동일 소스 snapshot/방법을 따라 absence counts를 독립 재실행한 학술 재현으로 볼 근거를 확보하지 못했음. 후속 수치·citation count를 추정해 넣지 말 것. Rombaut·AHE는 April 공개 연구여서 July 공개 이번 논문의 후속이 될 수 없음.

## 10. 공개 원고에 권장하는 중심 제한 문장

1. “이번 결과는 2026년7월 중심으로 고정한 11개 샘플의 소스 조사임. Claude Code만 3월 유통 스냅샷을 읽었음.”
2. “framework 0은 범용 orchestration framework import를 발견하지 못했다는 뜻임. provider SDK·LiteLLM·Vercel AI SDK까지 없는 건 아님.”
3. “embedding 0은 코드 탐색만의 결과임. 대화 기억은 OpenClaw 기본 hybrid search처럼 embedding을 쓰는 예외가 있음.”
4. “속도·비용·성능 우승자를 가린 실험은 없음. 이 지도에서 설계를 고른 뒤 같은 task/model로 시험할 일은 남았음.”
5. “April판과 직접 후속의 원문을 확인 못했고, AHE의 원문 숫자·저자가 이번 논문의 인용과 달라 그 세부 비교는 뺐음.”

