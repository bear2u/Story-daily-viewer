# 팩트 원장: Harness Engineering

기준일: 2026-10-06 (한국 날짜). 읽은 원문: 사용자가 제공한 arXiv:2609.00006v1 PDF, 83쪽 전체(본문·부록·참고문헌). 날짜 기준: 공식 arXiv 제출 기록. 원장 먼저 작성 후 기획·집필함. 예시는 관찰된 실험과 구분함.

## F: 이번 논문 본문

- F1 | p.1 Abstract | "It does not benchmark or rank; it describes and compares how the systems are built." | 소스코드 구조 비교이며 성능 순위·벤치마크 실험이 아님.
- F2 | pp.9–11 §4.1, Table 3 | "The study covers eleven harnesses plus one meta-harness contrast point" | Claude Code, Codex CLI, Gemini CLI, Mistral Vibe, OpenHands, Aider, Mini-SWE-Agent, Hermes, Pi, OpenCode, OpenClaw의 11개. 무작위가 아니라 설계 철학·성숙도·시장 위치에 따른 목적 표집.
- F3 | p.10 OpenClaw as an External Contrast Point | "personal AI assistant gateway, not a coding agent" | 11개 중 OpenClaw는 개인 비서 gateway 대조점. native code editing tool이 없어 코딩 하네스로 좁히면 10개.
- F4 | pp.10–11 Omnigent as a Meta-Harness Contrast Point | "not a coding harness but an orchestration layer above harnesses" | Omnigent는 본 11개 분모 밖의 별도 meta-harness 대조 사례.
- F5 | p.10 Table 3, p.12 Table 4 caption | "source snapshot Mar. 2026" | 2026년7월 release 중심으로 고정하되 Claude Code 분석은 3월 유통 소스 snapshot. 7월 shipping binary와 같은 소스라 할 수 없음.
- F6 | pp.3–4 §2, Figure 1 | "the same seven subsystems (Figure 1)" | agent loop, LLM integration, tools/actions, memory/context, safety/permissions, orchestration, extensibility. Interface layer는 그림에 함께 표시되지만 7개 목록에는 들어가지 않음.
- F7 | p.14 Listing 1 | "The message list grows linearly" | Mini-SWE-Agent의 query→execute→observe 반복. 모델이 행동을 제안하고 런타임이 실행 결과를 기록해 다음 호출로 보냄.
- F8 | p.16 §6.3 | "default: 3 reflections" | Aider는 수정 뒤 lint/test 실패 신호를 모델에 돌려주는 reflection loop. default 최대 3회, 무제한 수정이 아님.
- F9 | p.15 Hermes: Budgeted Loop with Stop-Guards | "verify-on-stop" | 코드가 바뀌었는데 최신 검증이 없을 때 text-only 종료 응답을 continuation으로 전환하는 장치. 테스트가 올바르거나 버그 해결을 보장하는 실험은 아님.
- F10 | p.53 §13.2 Absence 1 | "no production agent code path imports any of them" | 고정한 11개에서 검사한 범용 agent orchestration framework(LangChain/LangGraph 등)의 production runtime import를 발견 못했다는 저자 조사. 모든 라이브러리·SDK 부재가 아님.
- F11 | p.53 §13.2 caveat | "its /help command can install llama-index to run doc-RAG" | Aider의 optional LlamaIndex 기반 자기 문서 doc-RAG는 존재함. agent-loop orchestration과 구분함.
- F12 | p.53 §13.2 caveat | "OpenCode delegates its inner LLM/tool plumbing to Vercel’s AI SDK" | OpenCode는 provider abstraction SDK를 사용함. 모든 코드를 직접 만든다거나 SDK가 없다는 결론은 틀림.
- F13 | pp.54–55 §13.2, Table 13 | "For code retrieval the result is unchanged and now spans eleven systems: zero." | 표본의 source-tree code retrieval에 vector embedding retrieval 없음. OpenClaw는 이 기능 N/A. 검색·RAG 일반의 부재가 아님.
- F14 | p.55 Table 13 Aider | "tree-sitter symbol extraction with token-budget-constrained PageRank-style ranking" | Aider RepoMap은 코드 구문에서 심벌을 추출하고 관계를 PageRank 스타일로 순위화하여 토큰 예산 안의 저장소 지도를 만듦. tree-sitter는 구조 파서, ripgrep는 문자열 검색 도구.
- F15 | p.55 Table 13 Claude Code/Codex/Gemini/Pi/OpenCode | "ripgrep keyword search" | 문자열 검색, 파일명 패턴(glob), 필요할 때 파일 읽기, 프로젝트 지침 탐색 등 결정적 검색 수단이 코드 탐색에 사용됨. 코드 문서 전체를 매번 넣는다는 뜻은 아님.
- F16 | p.54 §13.2, p.55 Table 13 OpenClaw | "Default hybrid memory search" | OpenClaw의 기본 대화 회상은 sqlite-vec KNN + FTS5/BM25 embedding hybrid. 코드 검색과 별개. Hermes core 대화 검색은 lexical FTS5, embedding plugins는 opt-in.
- F17 | p.34 Observation 5 vs pp.54–55 §13.2/Table 13 | "none of the eleven uses embedding-based retrieval as its primary memory substrate" / "Default hybrid memory search" | 원문 내부 memory 보편 부재 주장은 뒤의 OpenClaw 구체 설명과 충돌. 해설은 코드 탐색만의 부재와 명시된 memory 예외를 따름.
- F18 | pp.55–56 §13.2 explanations | "The reasons are domain-specific." | 코드의 구조·바뀌는 index·debuggability 설명은 저자 해석. vector와 keyword 검색을 동일 조건에서 비교한 인과 실험이 아님.
- F19 | pp.28–29 §8.4, Table 7 | "Exact string replacement" / "fuzzy matching" | 정확 문자열 교체와 fuzzy matching의 설계 차이. 공백 차이로 못 찾는 예시는 설명용 가정. 논문의 실패율 측정값이 아님.
- F20 | p.28 Table 7 OpenCode | "Model-conditional" | OpenCode가 GPT 계열에는 apply_patch, 그 밖에는 string edit 경로를 쓰는 모델 조건부 편집 인터페이스. 특정 방식의 보편적 우월함 입증 아님.
- F21 | pp.27–28 §8.3 | "Deferred Tool Loading" | Claude Code ToolSearch와 Codex BM25 기반 MCP tool search처럼 필요할 때 tool schema를 불러오는 설계. Tool 이름을 처음부터 전부 prompt에 노출하는 것과 구분. 실제 속도·토큰 절감 측정은 없음.
- F22 | pp.31–33 §9, Figure 4 | "the conversation outgrows the context window" | context 압축에는 summarize/truncate/select 등이 있으며 모델 입력 한도에 맞추려는 설계. 저장된 history를 반드시 삭제하는 것은 아님.
- F23 | p.33 §9 Hermes | "rotates to a child" | Hermes compaction은 SQLite child session을 만들어 parent와 연결. 원래 기록이 압축된 모델 입력과 함께 사라지는 것이 아님.
- F24 | pp.33–34 §9.6 Codex | "two-phase" | 먼저 session에서 정보를 추출하고, 이후 sandboxed consolidation agent가 파일 기반 기억을 관리함. 추출과 합치기 단계가 나뉨.
- F25 | p.34 §9.6 Gemini CLI | "review inbox" | 추출된 memory patch를 검토 inbox에 두는 경로. 추출 즉시 영구 기억에 반영하는 설계로 옮기지 말 것.
- F26 | p.34 §9.6 Hermes | "2,200" / "1,375" | MEMORY.md 2200자, USER.md 1375자 제한; session 시작 시 frozen prefix. 글자 제한이며 토큰 제한 아님. 중간 memory 수정이 같은 session의 고정 prefix를 자동갱신하지 않음.
- F27 | pp.30,35–38 Table 8, Figure 5, §10 | "Permission" / "Isolation" | 허용 판단과 실행 격리는 다른 층. worktree는 작업 파일 분리이며 OS sandbox와 동의어가 아님. permission dialog만으로 containment를 보장하지 않음.
- F28 | pp.48–50 §12.2–12.3, Table 10 | "9/11" / "8/11" | SKILL.md 9/11, MCP 8/11. OpenClaw를 빼면 코딩 하네스 8/10, 7/10 (9−1,8−1;11−1). 사용률·성공률 아님. 서로 다른 역할이라 대체/승패로 읽지 말 것.
- F29 | pp.48–50 §12.2–12.3 | "progressive disclosure" | Skills는 설명 먼저, 필요 시 전체 지침을 읽는 점진적 공개; MCP는 외부 tool connection/protocol. Pi는 skills+CLI 선호로 MCP를 채택하지 않는 사례.
- F30 | p.60 Table 15, §14.2 | "Harness →framework" / "Framework →harness" | 완성 harness의 SDK화(Claude Agent SDK, OpenHands SDK 등)와 framework 기반 harness(Deep Agents on LangGraph) 양쪽을 듦. 후자는 본 11-system 표본 바깥.
- F31 | pp.62–63 §14.5 | "April edition" / "quarter" | 저자들은 April판 8개의 snapshot을 보존해 July판에서 11개+meta 대조점으로 넓혔다고 설명함. 같은 시스템의 source diff이지 같은 task/model 성능 실험이 아님. 과거판 별도 공개 PDF는 확보 못함.
- F32 | p.62 §14.5 | "Policy migrated out of prose." | source diff에서 일부 정책이 prompt text에서 configuration으로 옮겨감을 설명. 실제 사용자 작업시간 단축량은 미측정.
- F33 | pp.66–67 §15.6 | "The analysis rests on source-code reading, not runtime measurement." | source 독해와 질적 판단. latency/cost/security 실효성을 직접 실험한 것이 아님.
- F34 | p.67 §15.6 | "we did not trace internal forks, plugins loaded via dynamic importlib/require, or transpiled distributions" | dynamic import/plugin/internal fork까지 완전 추적한 부재 증명은 아님. manifests/source grep 범위의 관찰.
- F35 | p.67 §15.6 | "The Claude Code analysis is the weakest link on reproducibility." | 3월 유통 source snapshot 때문에 해당 분석 재현성이 가장 약하다고 저자가 명시.
- F36 | p.11 footnote 4, pp.66–67 §15.6 | "obtained on different model generations and configurations" | 모델·배포·벤치마크 조건이 다른 self-reported 수치의 head-to-head 오독을 막으려 이전 성능 수치를 뺐음. 성능 차이가 없다는 결과도 아님.
- F37 | pp.71–72 Listing 3 | "Illustrative scaffold, not production code." | 약90줄 minimum viable harness는 4tool(bash/read/write/search-replace) illustrative scaffold. 실제 배포용 라이브러리 아니며 sandbox/MCP/skills/multi-agent 등을 생략.
- F38 | p.72 Observation 13 | "We conjecture, without proof" | 이 최소형이 frontier model에서 Mini-SWE-Agent에 가까운 성능을 낼 것이라는 말은 측정 없이 둔 추측.
- F39 | p.74 Acknowledgments | "used both for the source-code analysis and for drafting the manuscript" | Claude Code의 상당한 도움을 source 분석·집필 둘 다에 받았음을 공개. 저자 자체 검증 주장과 독립 재현은 다름.
- F40 | pp.73–74 §17 | "Unified evaluation frameworks that assess safety, user experience, cost efficiency, and extensibility alongside correctness" | 다음 과제로 같은 model 아래 cross-harness 평가, 비용/안전/사용경험/확장성 등을 제안. 앞으로 입증된다고 단정 안 함.
- F41 | https://arxiv.org/abs/2609.00006v1 Comments (2026-10-06), PDF p.1–83 | "83 pages, 7 figures, 18 tables" | 83쪽 원문. 전체 독해를 완료했으며 추출 그림 7개/표18개 확인. 해설은 부록까지 읽고 핵심 구조 중심으로 선별.
- F42 | p.1 title block | "Harness Engineering:" / "Anatomy, Architecture, and Evolution of Coding Agents" / "A Source-Code Study of Eleven Systems" | 본 제목과 부제 전체. 공식 arXiv metadata도 같은 전체 제목을 기재함.

## L: 계보·표본 바깥 원문

- L1 | ReAct arXiv:2210.03629v3 pp.1–3, Figure 1; 공식 abs https://arxiv.org/abs/2210.03629 (2026-10-06) | "Published as a conference paper at ICLR 2023"; "reasoning traces and task-specific actions in an interleaved manner" | v1 2022-10-06. 추론·행동·관찰을 섞는 계보. 이번 p.6 §3.2가 loop의 기초로 연결함. ICLR 2023 게재.
- L2 | SWE-agent arXiv:2405.15793v3 pp.1–4, Figure 1; 공식 abs https://arxiv.org/abs/2405.15793 (2026-10-06) | "custom agent-computer interface (ACI)"; "38th Conference on Neural Information Processing Systems (NeurIPS 2024)." | v1 2024-05-06. 파일 탐색·수정·테스트 도구와 반환 feedback 포맷을 모델 사용자에 맞춰 설계. 이번 p.6 §3.2가 전작 개념으로 인용. NeurIPS 2024 게재.
- L3 | Inside the Scaffold arXiv:2604.03515v2 pp.1–3,6–9; 공식 abs https://arxiv.org/abs/2604.03515 (2026-10-06) | "13 open-source coding agent scaffolds"; "12 dimensions" | Benjamin Rombaut 단독 저자, v1 2026-04-03 / v2 2026-04-10. 이번 p.6 §3.3은 April판과 동시 개발된 상보적 연구로 설명. 같은 팀 전작·후속작 아님.
- L4 | Inside the Scaffold v2 p.18 Table 8 | "FAISS" / "vector store via LlamaIndex"; "Moatless Tools" | 이번11개 밖의 Moatless Tools embedding 코드 검색 사례. 0/11을 모든 coding agent로 일반화하지 않는 경계 근거. 성능 우월함을 입증하는 숫자로 쓰지 않음.
- L5 | ReAct v3 p.1 vs SWE-agent v3 p.1 | "Shunyu Yao"; "Karthik Narasimhan" | 두 논문 공동 저자 교집합. ReAct 당시 Princeton/Google, SWE-agent 당시 Princeton. 이번4명과 저자 교집합 없음.
- L6 | 이번 p.6 §3.3, pp.62–63; 공식 arXiv Comments; source-audit.md 검색기록 (2026-10-06) | "developed concurrently with our April edition" | April 자기 판본 별도 원문 미확보. 저자 교집합 비교 불가. 공개 확인 가능한 직접 후속 논문·독립 재현도 못 찾음. 없다고 단정하지 않음.

## P: 사람·기관

- P1 | 이번 p.1 title block | "Paul Barbaste ... Tristan Darrigol ... Germain Vu ... Tom Wiltberger"; "Inclusive Brains"; "Wavestone AI Lab" | 논문 당시 Barbaste는 두 소속, Darrigol/Vu/Wiltberger는 Wavestone AI Lab. 현재 소속·이직 여부 추정은 제외.
- P2 | ReAct/SWE-agent 각 p.1 authors | "Princeton University"; "Google Research, Brain team" | ReAct와 SWE-agent에서 Yao/Narasimhan 교집합을 설명할 때 당시 소속만 사용. 이번 연구팀과 동일하지 않음.

## W: 날짜·심사·배포 확인

- W1 | https://arxiv.org/abs/2609.00006v1 (2026-10-06) Submission history | "[v1] Wed, 15 Jul 2026 10:33:30 UTC" | 공식 공개 날짜 2026-07-15. ID 앞의2609를9월 날짜로 추론하지 않음. DOI10.48550/arXiv.2609.00006. 판본v1.
- W2 | 같은 arXiv metadata + 저자 공개 게시글, source-audit.md (2026-10-06) | "Our preprint is available!" | 프리프린트. 공식 심사 통과·학회/저널 게재처는 확인 못함. 심사를 한 번도 안 받았다고 단정하지 않음.
- W3 | https://arxiv.org/html/2609.00006v1 및 arXiv view license → https://creativecommons.org/licenses/by/4.0/ (2026-10-06) | "CC BY 4.0" | 원문 그림·표·짧은 문장 크롭은 출처와 라이선스, 크롭/크기조절 정보를 별도 ATTRIBUTION에 표시.
- W4 | https://arxiv.org/abs/2604.03515 ; https://arxiv.org/abs/2210.03629 ; https://arxiv.org/abs/2405.15793 (2026-10-06) | "Submission history" | 각 최초 공개일2026-04-03/2022-10-06/2024-05-06. 옆 논문 판본 날짜를 최초 공개와 혼동하지 않음.

## 파생 수치·제외한 주장

11개=10 coding harness+1 OpenClaw contrast. Skills 9/11 중 OpenClaw1을 빼서8/10; MCP8/11 중 OpenClaw1을 빼서7/10. 그림의 counts는 source snapshot 기능 채택 여부이며 현재 시장 사용률 아님.
8→11은3개 추가, 시스템 수3배 아님. 약4M lines는 집계 관례에 따른 approximate size라 해설에서 생략.
Paper의 AHE[85] 저자·수치가 실제 arXiv:2604.25850v4와 맞지 않아 제외. 원문p.34 memory 보편 부재 문장도 pp.54–55 구체 예외와 충돌해 보편 문장 제외. 성능·비용·보안 효과,90줄 production 성능,현재 소속, April저자표는 추정하지 않음.
