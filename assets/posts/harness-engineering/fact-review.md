# 독립 팩트체크: Harness Engineering 해설

검토 대상: `report.md`, `ledger.md`, `text.txt`, `lineage.md`, `source-audit.md`, 게시글에 연결된 `figures/` 24장, 선행 원문 `arxiv-2210.03629v3`, `arxiv-2405.15793v3`, `arxiv-2604.03515v2`.

검토 기준: paper-report `references/fact-check.md`. 원문의 PDF 페이지 표시는 `text.txt`의 `=== [p.N] ===` 경계를 따랐고, 줄바꿈 때문에 갈린 단어만 이어서 읽었음. 원문에 없는 근거는 보충하지 않았음.

## 1. 판정

**최종 PASS.**

초기 검토에서는 `verification-on-stop` 명칭, 파트 21의 근거가 다른 병렬 읽기 문장, 원장의 비직인용 문구, 본문의 축약 제목을 차단 오류로 판정했음. 재검토 시 모두 수정됐음을 확인함.

- 파트 9는 원문 명칭 `verify-on-stop`으로 교정됨.
- 파트 21은 종단 변화 근거가 없던 병렬 읽기 문장을 삭제하고 p.62의 prompt prose→configuration 변화만 남김.
- 파트 2는 전체 제목을 텍스트로 제시하고 새 원장 F42로 연결함.
- F1–F40·F42의 따옴표 문구를 전체 PDF에서 공백·줄바꿈·PDF 하이픈만 정규화해 재검색한 결과 모두 원문과 일치함. F41은 PDF 본문이 아니라 명시된 공식 arXiv Comments 문구임.

핵심 숫자, 날짜, 소속, 표본 범위, 심사 상태, 계보, 비유, 그림 설명에도 남는 공개 차단 오류가 없음.

## 2. 파트별 대조

| 파트 | 판정 | 확인 항목 수 | 대조 결과와 근거 |
|---:|---|---:|---|
| 1 | 문제 없음 | 5 | 도입의 버그·파일·테스트 장면은 설명용 가정으로 쓰였고 연구 결과처럼 제시하지 않음. 하네스 정의는 p.1·p.3 및 F6과 일치. `q_definition.png`도 p.3 정의 문단을 정확히 보여 줌. |
| 2 | 문제 없음(수정 확인) | 10 | 전체 제목 **Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems**가 읽을 수 있는 본문에 추가되고 F42로 연결됨. 저자·당시 소속은 p.1, 공개일과 v1은 로컬 `meta.json`, 83쪽은 PDF/metadata, 프리프린트·게재 미확인은 `source-audit.md`와 일치. `header.png`도 p.1 제목·저자·소속과 일치. |
| 3 | 문제 없음 | 8 | 11개 목록, 10개 coding harness+OpenClaw 대조점, Omnigent의 분모 밖 위치, 목적 표집의 세 축, 비벤치마크 범위, July pins와 Claude March 예외 모두 pp.9–12와 일치. `tab3_p10.png`도 Table 3의 11+1 구분을 보존함. |
| 4 | 문제 없음 | 7 | ReAct v1 2022-10-06, ICLR 2023, reasoning/action interleaving과 observation 연결은 ReAct v3 p.1 및 이번 논문 p.6과 일치. `prior_react.png`는 Figure 1의 Thought/Action/Observation 예시임. |
| 5 | 문제 없음 | 8 | SWE-agent v1 2024-05-06, NeurIPS 2024, ACI가 명령과 반환 feedback 형식을 포함한다는 설명은 SWE-agent v3 p.1 Figure 1과 일치. Yao·Narasimhan 저자 교집합 및 이번 팀과의 비동일성도 각 제목부와 일치. |
| 6 | 문제 없음 | 7 | Rombaut 단독 저자, v1 2026-04-03, 13개 open-source scaffold·12차원은 원문 p.1과 metadata에 일치. 이번 논문 p.6은 이를 자기 April edition과 동시에 개발된 상보적 연구로 명시함. `prior_scaffold.png`도 제목·저자를 정확히 보여 줌. |
| 7 | 문제 없음 | 8 | seven canonical subsystems와 interface layer의 구분은 pp.3–4 Figure 1과 일치. 쉬운 설명도 loop/tools/context/safety/orchestration/extensions의 기능 관계를 훼손하지 않음. |
| 8 | 문제 없음 | 6 | Mini-SWE-Agent의 query→execute→observation 반복은 pp.13–14 Listing 1과 일치. 테스트 명령·실패 로그는 “예를 들어”로 분리된 합리적 설명이며 실험 결과로 오인시키지 않음. `listing1.png`는 해당 코드의 핵심 줄을 포함함. |
| 9 | 문제 없음(수정 확인) | 6 | Aider의 최대 3 reflections는 p.16과 일치. Hermes 동작 설명과 교정된 명칭 `verify-on-stop`은 p.15와 일치. 검증 흔적이 정답을 보장하지 않는다는 제한은 과장 방지에 적절함. `q_verify.png`도 같은 명칭을 표시함. |
| 10 | 문제 없음 | 7 | 저자들이 dependency manifest와 source import를 검사했고, 고정된 11개 production agent path에서 검사 대상 범용 framework import를 찾지 못했다는 좁은 범위를 유지함. 성능 실험이 아니라는 문장도 p.53 및 pp.66–67과 일치. |
| 11 | 문제 없음 | 7 | Aider `/help`의 optional LlamaIndex doc-RAG와 OpenCode의 Vercel AI SDK를 orchestration framework와 구분한 설명은 p.53과 일치. `q_exceptions.png`는 두 경계 사례를 같은 문맥으로 보존함. |
| 12 | 문제 없음 | 8 | 0/11을 source-tree code retrieval로 한정했고, embedding 정의와 deterministic search 예시는 pp.54–55 및 Table 13과 일치. Aider RepoMap의 tree-sitter+PageRank-style ranking도 정확함. `tab13_top.png`는 관련 열을 읽을 수 있게 포함함. |
| 13 | 문제 없음 | 9 | OpenClaw의 default conversation-memory hybrid search, sqlite-vec KNN+FTS5/BM25, 코드 검색과의 분리는 pp.54–55와 일치. p.34의 보편 memory 문장과 뒤 구체 설명의 내부 불일치를 숨기지 않음. Rombaut v2 p.18 Table 8의 Moatless Tools FAISS+LlamaIndex 사례도 정확하며 표본 밖이라고 한정함. |
| 14 | 문제 없음 | 7 | exact replacement와 fuzzy matching의 차이는 설명용 가정으로 표시되어 있고 Table 7의 설계를 왜곡하지 않음. OpenCode의 GPT-family `apply_patch` 대 기타 모델 string edit는 pp.27–29와 일치. 그림 안내의 `Matching`·`Fallback` 열도 실제 표와 일치. |
| 15 | 문제 없음 | 7 | deferred tool loading, Claude ToolSearch, Codex의 `defer_loading`+BM25 `tool_search`는 pp.27–28과 일치. 속도·비용 절감의 직접 측정이 없다고 한정해 확신 수준이 안전함. |
| 16 | 문제 없음 | 7 | compaction을 모델 입력 문맥의 요약·선별로 설명하고 저장 history 삭제와 구분한 점은 pp.31–33과 일치. Hermes child session과 `parent_session_id` 계보도 p.33과 일치. `fig4_p31.png`의 전략 범위와 설명이 맞음. |
| 17 | 문제 없음 | 10 | Codex two-phase extraction/consolidation, sandboxed consolidation agent, Gemini review inbox, Hermes의 2,200/1,375 **characters**, frozen snapshot 및 mid-session cache behavior는 pp.33–34와 일치. 토큰 제한으로 잘못 옮기지 않았음. |
| 18 | 문제 없음 | 7 | permission과 isolation을 분리하고 worktree를 OS sandbox와 동일시하지 않은 설명은 p.30 Table 8 및 pp.35–38과 일치. 보안 공격 실험이 아니라는 제한도 p.66의 연구 범위와 일치. |
| 19 | 문제 없음 | 8 | Skills 9/11, MCP 8/11은 p.50; OpenClaw를 제외한 8/10·7/10은 명시된 분모에서의 정확한 파생값. 채택 수를 사용률·성공률로 확대하지 않음. Pi의 skills+CLI 선호/MCP 거부와 progressive disclosure도 pp.48–50과 일치. `tab10_p49.png`는 Skills 표이며 본문도 `Skills?` 열로 안내함. |
| 20 | 문제 없음 | 8 | Table 15 p.60의 harness→framework와 framework→harness 양방향, Claude Agent SDK/OpenHands agent SDK, Deep Agents on LangGraph 및 corpus 밖이라는 조건을 모두 보존함. “플랫폼”은 저자 해석으로 표시됨. |
| 21 | 문제 없음(수정 확인) | 7 | April의 8개 retained snapshots를 July에 re-pin하고 11개로 확장한 source diff는 pp.62–63과 일치. prompt prose→configuration 변화도 p.62에 있음. 근거가 다른 병렬 읽기 문장은 삭제됨. `q_evolution.png`도 retained/re-pinned methodology를 정확히 보여 줌. |
| 22 | 문제 없음 | 9 | source reading not runtime measurement, self-reported benchmark 비교 제외, Claude March snapshot의 재현성 약점, internal forks/dynamic imports/transpiled distributions 미추적, Claude Code의 substantial assistance는 pp.66–67·p.74와 일치. `q_limits.png`도 p.66 문장을 정확히 보존함. |
| 23 | 문제 없음(표현 권고 1) | 9 | Listing 3은 약 90 LoC, bash/read/write/search-replace 네 도구, illustrative/not production, sandbox/multi-agent/MCP/Skills 생략과 일치. `conjecture, without proof`도 p.72와 동일함. `좋은 모델`은 틀리진 않지만 원문의 조건인 `frontier model`을 `최전선급 모델`로 옮기면 범위가 더 정확함. |
| 24 | 문제 없음 | 7 | 루프·편집·관찰·permission/isolation 회수와 비벤치마크 제한은 정확함. 테스트 없이 끝내려는 응답을 계속 실행으로 바꾸는 동작 설명도 p.15와 일치하며 이 파트는 잘못된 장치명을 다시 쓰지 않음. `fig2_p17.png`는 iterative/reflection/coordinator-worker 세 설계를 정확히 보여 줌. |
| 25 | 문제 없음 | 10 | controlled cross-system evaluation과 cost/safety/user experience/extensibility future work는 p.74와 일치. 2026-10-06 현재 게재 미확인·직접 후속/독립 재현 원문 미확보라는 한정도 `source-audit.md`와 일치하며 “존재하지 않음”으로 단정하지 않음. 3줄 요약은 표본·기능 범위·비실험 한계를 정확히 보존함. |

## 3. 숫자·날짜·소속·범위 총점검

| 항목 | 판정 | 근거 |
|---|---|---|
| 공개일 2026-07-15 | PASS | `meta.json`의 `published=2026-07-15T10:33:30Z`; PDF p.1 하단 `15 Jul 2026`. arXiv ID `2609`를 공개월로 오독하지 않음. |
| v1·83쪽 | PASS | `meta.json` v1/page_count 83, arXiv comment `83 pages, 7 figures, 18 tables`, PDF p.1–83. 단, F41의 위치는 p.1이 아니라 arXiv Comments/PDF 전체로 좁힐 것. |
| 저자·소속 | PASS | PDF p.1: Barbaste `1,2`, 나머지 세 저자 `2`; `1 Inclusive Brains`, `2 Wavestone AI Lab`. 현재 소속으로 확대하지 않음. |
| 심사 여부 | PASS | `journal_ref=null`, source audit의 공식 기록/저자 preprint 표현에 따라 “프리프린트, 공식 심사 통과·게재처 확인 못함”으로 한정. “심사를 안 받음”이라고 단정하지 않음. |
| 11개 표본 | PASS | p.9·Table 3 p.10. 11에는 OpenClaw가 포함되고 Omnigent는 별도 meta-harness contrast. |
| 10 coding harnesses | PASS | p.10이 OpenClaw를 coding agent가 아닌 external contrast로 설명하고 strict coding-agent 독자는 10-system figures를 쓰라고 명시. |
| Skills 9/11·MCP 8/11 | PASS | p.50. OpenClaw 포함. 8/10·7/10 파생도 정확함. |
| Aider 기본 reflection 상한 3 | PASS | p.16 “up to a configurable maximum (default: 3 reflections).” |
| Hermes 2,200/1,375 characters | PASS | p.34. tokens가 아니라 characters로 옮김. |
| 0/11 code embedding retrieval | PASS | pp.54–55. 코드 검색으로 한정하고 OpenClaw conversation-memory 예외를 분리함. |
| 8→11 longitudinal sample | PASS | p.1, p.9, pp.62–63. 8개 retained/re-pinned; 동일 task/model 성능 실험으로 쓰지 않음. |
| 약 90 LoC·4 tools | PASS | pp.71–72 Listing 3. production-ready나 검증된 성능으로 확대하지 않음. |

## 4. 원장 직인용·페이지 감사

다음 표는 **초기 검토에서 발견한 비직인용·페이지 문제와 교정에 사용한 정확 문구**를 기록함. 현재 원장에는 모두 반영됐음.

| ID | 현재 문제 | 교체 가능한 정확 원문 | 정확 위치 |
|---|---|---|---|
| F2 | `"Eleven primary harnesses were selected"`는 없음 | `"The study covers eleven harnesses plus one meta-harness contrast point"` | p.9 §4.1 |
| F3 | `"OpenClaw is not a coding agent"`는 주어를 재작성함 | `"Its README describes it as a personal AI assistant gateway, not a coding agent"` | p.10, OpenClaw paragraph |
| F4 | `"separately as a contrast point, not a twelfth member"`는 없음 | `"The top eleven rows are the study corpus; Omnigent is analyzed as a meta-harness contrast point only."` | p.10 Table 3 caption |
| F5 | `"March 2026 circulated source snapshot"`는 어순을 합친 문구이고 pp.10·12에 그대로 없음 | `"It draws on a publicly circulated source snapshot from March 2026 rather than an official release"` | p.67 §15.6 |
| F7 | `"linear while"`는 원문에 있으나 기재한 pp.13–14가 아님 | `"Linear while"` | p.17 Table 5. Listing 1을 직접 고정하려면 p.14의 `"while True:"` 사용 가능 |
| F8 | `"max_reflections (default 3)"`는 없음 | `"up to a configurable maximum (default: 3 reflections)"` | p.16 §6.3 |
| F9 | `"verification-on-stop"`는 없음 | `"The verify-on-stop guard rewrites a text-only response into a continuation whenever the turn mutated code files without producing fresh verification evidence"` | p.15 Hermes paragraph |
| F11 | `"Aider's optional /help extra"`는 축약 재서술 | `"Aider ships one optional framework-adjacent extra: its /help command can install llama-index to run doc-RAG over aider's own documentation"` | p.53 §13.2 |
| F12 | `the Vercel AI SDK`는 원문의 소유격을 바꿈 | `"OpenCode delegates its inner LLM/tool plumbing to Vercel's AI SDK"` | p.53 §13.2 |
| F17 | 첫 인용은 편집용 말줄임이므로 원문 그대로 규칙에 맞춰 완문 권장 | `"Notably, none of the eleven uses embedding-based retrieval as its primary memory substrate"` | p.34 Observation 5. 이 문장은 pp.54–55의 OpenClaw default memory 설명과 충돌한다고 계속 명시할 것 |
| F18 | `"offers a parsimonious explanation"`은 원문 전체에 없음 | `"The inconsistency of these gains may help explain why production SWE agents skip the RAG layer entirely rather than investing in task-dependent retrieval routing."` | p.56 §13.2 |
| F19 | `"String replace" / "Fuzzy matching"`은 Table 7의 셀을 정확히 옮기지 않음 | `"Exact string replacement"` / `"9-strategy fuzzy chain"` | p.28 Table 7 |
| F30 | 화살표 주위 공백이 원표기와 다름 | `"Harness →framework"` / `"Framework →harness"` | p.60 Table 15 |
| F32 | `"safe parallel reads"`는 원문 전체에 없음. 또 현재 위치의 진화 근거와 불일치 | `"behavioral policy is moving from the prompt (where the model reads it) to configuration (where the platform enforces it)"` | p.62 §14.5. 병렬 조건을 별도 보존하려면 p.13 `"Read-only tools (grep, glob, file read) are safe; write tools (edit, bash) are not."` 또는 p.15 Hermes 문장을 별도 ID로 만들 것 |
| F36 | 여러 문장을 합친 `"different models, deployment configurations, and benchmark harnesses"`는 없음 | `"different underlying models, different evaluation runs, different deployment configurations"` | p.58 §13.4 Axis 1 |
| F37 | `"illustrative"`는 caption에서 대문자로 시작함 | `"Illustrative scaffold, not production code."` | p.72 Listing 3 caption |
| F40 | 단어와 순서를 재작성함 | `"Unified evaluation frameworks that assess safety, user experience, cost efficiency, and extensibility alongside correctness"` | p.74 §17.2 |
| F41 | quote 자체는 arXiv comment와 일치하나 p.1에는 없음 | `"83 pages, 7 figures, 18 tables"` | arXiv Comments; 83쪽은 PDF 전체로 교차 확인 |

최종 원장의 **F1–F40·F42**는 줄바꿈·PDF 하이픈을 복원해 대조했을 때 인용과 위치가 맞았음. **F41**은 공식 arXiv Comments 문구이며 위치가 Comments/PDF p.1–83으로 분리돼 있음. **L1–L6, P1–P2**도 각 선행 원문과 제목부에서 확인됨. F22·F27처럼 짧은 일반어 인용은 사실과 위치는 맞지만, 향후에는 완문 또는 표·그림의 좁은 셀을 쓰면 감사 가능성이 더 높아짐.

W1은 로컬 metadata와 일치함. W2–W4의 외부 페이지 문구는 `source-audit.md`에 기록된 조회 결과와 모순이 없으나, 이 검토에서는 해당 외부 페이지를 새로 재수집하지 않았으므로 그 기록 범위에서만 PASS로 둠.

## 5. 그림 대조

- `report.md`에 연결된 24개 그림 파일을 직접 열어 확인함. 모두 존재하고 비어 있지 않으며, 캡션이 가리키는 원문 요소와 페이지가 맞음.
- 핵심 검증 그림 `q_definition.png`, `q_verify.png`, `q_framework.png`, `q_exceptions.png`, `tab13_top.png`, `tab13_memory.png`, `tab7_p28.png`, `q_deferred.png`, `q_memory.png`, `q_evolution.png`, `q_limits.png`, `q_conjecture.png`는 주변 문맥을 심하게 잘라 의미를 뒤집지 않음.
- `q_verify.png`와 교정된 본문이 모두 `verify-on-stop`으로 일치함.
- `q_evolution.png`는 “eight systems … re-pinned … source-diffed across one quarter”를 보여 주며, 교정된 파트 21의 방법 설명과 일치함.
- 교체된 `q_memory.png`를 다시 열어 확인함. Hermes의 두 문자 제한과 `frozen snapshot`을 문맥째 포함하며 현재 캡션과 일치함. 교체된 `tab13_top.png`도 Aider·Claude Code·Codex 행을 완결된 상태로 보여 줌.
- 새로 연결된 `permission_layers.png`도 직접 확인함. 원문 Figure 5의 세 층과 `allow / ask / deny`, `approve / reject / edit` 표기를 보존하고, 주변의 저자 평가 문장은 제외해 현재 캡션과 일치함.
- `figures/tab14_p57.png`는 0바이트 빈 파일이지만 게시글에서 참조하지 않음. 공개 HTML에는 영향이 없으나 결과물 묶음의 미사용 불량 파일이므로 삭제하거나 정상 크롭으로 교체하는 편이 좋음.

## 6. 계보·비유·확신 수준

- ReAct→SWE-agent→이번 하네스 구조 조사라는 설명은 “직접 후속”이나 “같은 팀”으로 과장하지 않았고, 각 원문의 실제 개념 연결만 사용해 PASS.
- Rombaut 논문은 이번 팀의 전작이 아니라 동시기 상보 연구라고 정확히 구분함. Moatless Tools 사례도 반박 논문/후속작이 아니라 표본 밖 예외로만 사용해 PASS.
- “임베딩=내용을 숫자 벡터로 바꿔 의미가 가까운 것을 찾는 표현”, “permission=허용 판단 / isolation=접근 범위 제한”, “compaction=다음 호출의 입력 문맥 축소” 비유는 원인 구조를 보존하며 전문적 오해를 만들지 않음.
- 성능, 비용, 속도, 보안 효과를 입증했다고 쓰지 않았고, self-reported benchmark를 비교 결과로 재사용하지 않아 PASS.
- p.34 memory 보편 부재와 pp.54–55 OpenClaw default hybrid memory의 원문 내부 충돌을 감추지 않고 더 구체적인 뒤 설명을 따랐음.
- `conjecture, without proof`, `source-code reading, not runtime measurement`, `공식 심사 통과 확인 못함`, `직접 후속 원문을 찾지 못함` 등의 확신 수준이 원문·감사 기록보다 세지지 않았음.

## 7. 수정 확인 체크리스트

- [x] 파트 2에 전체 논문 제목과 F42 근거 추가.
- [x] 파트 9의 `verification-on-stop`을 `verify-on-stop`으로 교정.
- [x] 파트 21에서 근거가 다른 병렬 읽기 문장 삭제, p.62 policy migration만 유지.
- [x] 초기 비직인용 원장 문구와 위치 교정. F41은 arXiv Comments 출처임을 명시.
- [x] 교체된 `q_memory.png`, `tab13_top.png`를 다시 열어 캡션·가독성·문맥 확인.

## 8. 최종 재검토 결론

**PASS. 새 공개 차단 오류 없음.**

현재 `report.md`의 25개 파트는 수치·날짜·소속·분모·조건·확신 수준·비유·계보·그림 설명이 제공된 원문과 원장 범위 안에서 일치함. 3줄 요약도 “11개 표본”, “framework/code-vector-retrieval 부재의 제한된 범위”, “동일 조건 효과 미측정”을 정확히 유지함.

비차단 정리 사항은 하나임. `figures/tab14_p57.png`가 0바이트지만 `report.md`와 게시글의 24개 연결 그림에는 포함되지 않음. 공개 페이지 사실성·렌더링에는 영향 없음.
