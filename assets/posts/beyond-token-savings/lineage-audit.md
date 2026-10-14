# 계보·저자 원문 감사 — 2026-10-15

paper-report의 SKILL.md, references/lineage.md, references/people-context.md를 읽고 조사함. 선택 논문의 참고문헌과 인용 문맥을 로컬 원문 text.txt p.1–2, p.11–13, p.14(Appendix A.1)에서 대조함. 아래 날짜는 arXiv 최초 접수 UTC 기준이며 학회 발표일과 구분함. 전작은 원문 PDF 첫 페이지와 관련 방법·결과 절을 직접 확인했으며 초록만으로 세부 수치를 가져오지 않았음.

## 확인된 세 전작

| 최초 접수 | 논문 / 저자 | 원문 기준 기관·심사 확인 | 이번 논문과 관계 |
|---|---|---|---|
| 2023-10-12 17:51:32 UTC | **MemGPT: Towards LLMs as Operating Systems**. v1: Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph E. Gonzalez. v2: Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez. | v2 첫 페이지 전원 UC Berkeley. 공식 arXiv와 프로젝트 페이지는 preprint로 표시하며 심사 통과 학회는 확인되지 않음(확인일 2026-10-15). 키워드 ICML은 게재 증거가 아님. | 문제 제기 / 배경: 제한된 입력 창을 외부 저장소와 연결하여 가상 메모리처럼 관리함. 이번 논문은 그 시스템의 구현 확장으로 주장하지 않고 압축 정책의 개별 선택을 측정함. |
| 2025-08-29 09:02:35 UTC | **The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management**. Tobias Lindenbauer, Igor Slinko, Ludwig Felder, Egor Bogomolov, Yaroslav Zharov. | v3 첫 페이지 Lindenbauer는 JetBrains Research + TU Munich, Felder는 TU Munich, 나머지 JetBrains Research. v3는 DL4C @ NeurIPS 2025 camera-ready라고 arXiv와 JetBrains 공식 페이지에서 확인. **NeurIPS 본학회 논문이라고 쓰지 말 것**. 워크숍 발표는 확인, 개별 공개 심사 결정 원문은 접근 차단으로 확인하지 못함. | 문제 제기: 오래된 도구 관측을 가리는 단순 정책이 요약보다 일관되게 열등하지 않다는 선행 관찰. 이번 논문 A.1은 이 관찰을 받아 무엇·언제·얼마나를 나눠 조사함. 동일 모델·동일 비용 산식의 재현실험이라고 쓰면 안 됨. |
| 2026-07-30 20:51:51 UTC | arXiv 메타데이터 제목 **Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale**. PDF/HTML 제목 **Agentic Coding in the Wild: Characterizing GitHub Copilot at Production Scale**. Banruo Liu, Haoran Qiu, Íñigo Goiri, Rodrigo Fonseca, Ricardo Bianchini, Esha Choukse. | PDF 첫 페이지 Liu는 UIUC, 연구는 Microsoft Azure Research 인턴 중 수행. Qiu/Goiri/Fonseca/Choukse는 Microsoft Azure Research, Bianchini는 Microsoft Azure. arXiv 메타데이터에는 심사 통과 학회 표시 없음(2026-10-15). | 문제 제기 / 생산 환경의 규모 근거: 압축을 수행하는 실제 Copilot 세션의 비중과 캐시 변화를 관찰. 이번 논문은 관측된 현상에서 압축 정책 자체의 통제 실험으로 옮겨감. 전작 캐시 측정과 이번 논문의 가상 캐시 과금 추정을 혼동하면 안 됨. |

## 원장에 옮길 근거와 안전한 설명

### L1 — MemGPT

- 공식 v1 메타데이터: https://arxiv.org/abs/2310.08560v1 (source `turn162view0`, 저자 L11, 날짜 L27).
- 읽은 원문 v2 PDF: https://arxiv.org/pdf/2310.08560v2 (source `turn158view3`, p.1 저자·기관; p.2–3 §2, Figure 3).
- 원문 HTML: https://arxiv.org/html/2310.08560v2 (source `turn157view0`, L44, L58–62).
- DOI: https://doi.org/10.48550/arXiv.2310.08560
- 핵심: 모델 입력 안의 main context와 밖의 archival/recall storage를 나누고 함수 호출로 필요한 내용을 옮김. Queue manager는 창이 찰 때 오래된 메시지를 요약하여 비움. 과거 메시지는 recall storage에서 다시 찾을 수 있음. 채팅과 문서 분석 평가이며 코딩 벤치마크의 압축 정책 65개 비교가 아님.
- 짧은 근거 구절: “move data between main context and external context” (v2 Figure 3, p.3).
- 선택 논문 p.1 및 A.1은 Packer et al.을 긴 이력·제한된 창의 문제로 인용함. 선택 논문 참고문헌 p.12에는 v1의 여섯 저자를 적었으므로 저자 수가 다르다는 이유로 오류라 단정하지 않음.

### L2 — The Complexity Trap

- 메타데이터: https://arxiv.org/abs/2508.21433 (source `turn154view0`, L11, L19, L27–29).
- PDF: https://arxiv.org/pdf/2508.21433v3 (source `turn156view1`, 31 pages).
- 읽은 HTML 원문: https://arxiv.org/html/2508.21433v3 (sources `turn155view0`, `turn161view0`, `turn161view1`).
- 공식 발표처: https://kairos.jetbrains.com/research/publications/complexity-trap (source `turn159view1`, L25–29).
- DOI: https://doi.org/10.48550/arXiv.2508.21433
- 핵심: §3.1의 관측 마스킹은 오래된 관측만 placeholder로 바꾸고 추론·행동 이력은 유지함. 요약 정책은 오래된 턴을 요약하고 최근 M턴을 그대로 둠. SWE-agent/SWE-bench Verified, 다섯 모델 설정을 비교하며 요약이 단순 마스킹보다 일관되게 우수하지 않았음. OpenHands 일반화 검사는 50문제, 파라미터를 scaffold에 맞춰 조정해야 했음. 이번 논문은 전체·부분 자유형/구조형 요약, 단계·토큰 임계 트리거, 깊이의 선택을 더 분리함.
- 짧은 근거 구절: “preserving the full history of agent reasoning and actions” (§3.1 Observation Masking).
- 원문 v3 PDF를 `/tmp/lineage-1015/arxiv-2508.21433/paper.pdf`에 확보했으며 p.1 제목·저자·소속 영역(102,91,510,265 pt)을 3배 렌더하여 `figures/prior_header.png`로 원자적 저장함. 실제 이미지 열어 글자 잘림 없음을 확인함. 그림 출처는 Lindenbauer et al., arXiv2508.21433v3 p.1, CC BY 4.0. 적절한 저자·링크·라이선스·크롭 여부 표시 필요.
- 선택 논문 A.1은 Lindenbauer et al.을 압축 절약과 실행 길이 변화의 선행 관찰로 명시함. 결과를 ‘이번 논문이 요약의 무용함을 증명했다’로 연결할 근거는 없음.

### L3 — Copilot 생산 트레이스

- 메타데이터: https://arxiv.org/abs/2608.00101 (source `turn154view2`, L11, L27).
- PDF: https://arxiv.org/pdf/2608.00101v1 (sources `turn156view2`, `turn157view1`, 첫 페이지 제목·소속·인턴 각주).
- HTML: https://arxiv.org/html/2608.00101v1 (sources `turn156view3`, `turn156view4`, `turn161view2`).
- DOI: https://doi.org/10.48550/arXiv.2608.00101
- 숫자를 쓸 경우 정확한 모수: §3.1에서 2026년 6월 첫 주 미국 일부 지역 sampled telemetry **13.5M sessions**라고 적고, 초록·서론은 **13M**으로 반올림함. ‘모든 Copilot 사용자/전세계’가 아님. 사용자 prompt, 소스코드, 출력 텍스트는 수집하지 않은 구조 메타데이터 분석임.
- §6 Table 6: 적어도 한 번 압축한 세션이 7.8%이며 **그 세션들 전체 토큰**이 전체 토큰의 44.2%를 차지함. 압축 호출 자체가 토큰의 44.2%라는 뜻이 아님. 압축 이벤트당 입력 토큰 제거율 중앙값은 72.8%(Figure 19).
- 짧은 근거 구절: “sessions that contain at least one compaction event” (§6).
- 선택 논문 p.1은 13M·44.2%·72.8%를 가져옴. 전작은 압축 이후 prefix cache 변화를 실측했지만 이번 논문의 Qwen 실측은 prefix caching을 끔. 이번 논문 비용은 0.1배 cached-input 할인 가정의 추정값이므로 실제 Copilot 청구액을 검증한 연구가 아님.

## 저자·기관 맥락

- 선택 논문 p.1 네 저자 Ritul Satish, Prasoon Sinha, Akiho Kawada, Neeraja J. Yadwadkar의 기관은 모두 **The University of Texas at Austin**.
- 공식 교수 페이지: https://ece.utexas.edu/people/faculty/neeraja-yadwadkar (source `turn158view0`, L54–60, L82–90; 확인일 2026-10-15).
- 확인일 현재 Yadwadkar는 UT Austin ECE assistant professor이며 UT-SysML 연구 그룹 연결이 공식 페이지에 있음. 분야는 시스템과 ML의 접점, ML로 시스템을 개선하고 ML을 위한 시스템을 만드는 연구. 그래서 ‘토큰 수뿐 아니라 실행 시간·비용도 함께 본 시스템 연구’라는 맥락은 근거 있음. 특정 저자의 실험 담당/교신저자 역할은 확인 없이 부여하지 말 것.
- 선택 논문 저자 네 명과 위 세 전작 저자 목록을 교차 대조하여 공저자 이름의 일치는 없음. 동명이인 연결/연구팀 동일성을 주장하지 않음.
- 선택 사항: UT 공식 프로필은 박사 지도교수로 Joseph Gonzalez를 명시하고, MemGPT 원문에는 Joseph E. Gonzalez가 저자로 있음. 이 연결은 공개 경력 정보이나 이번 연구의 직접 계보·공동 작업 증거가 아니므로 짧은 보고서에 반드시 넣을 필요 없음.
- UT-SysML 웹페이지는 JavaScript 본문을 요구하여 전체 명단을 읽지 못함. 네 저자의 학생·교수 직책을 전부 알아낸 것처럼 쓰지 말 것.

## 후속작 확인과 제외

- 2026-10-15 기준 제목 및 arXiv ID 검색에서 **이번 논문을 직접 인용·확장한 원문 후속작을 확인하지 못했음**. 이는 ‘후속 연구가 세상에 없다’는 단정이 아님. 피인용 수 0도 주장하지 않음.
- 2026-09-29 공개 **Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations**, arXiv2609.36526(PAIR)은 별도 관련 후보. 공식 메타데이터 source `turn160view2`: https://arxiv.org/abs/2609.36526 . 웹 PDF/HTML 접근이 DisabledError여서 fetch_paper.py로 `/tmp/lineage-1015/arxiv-2609.36526/paper.pdf` 41쪽을 확보함. 원문 서론 및 References p.10–12를 직접 읽고 전체 텍스트에서 Satish / Beyond Token Savings / 2609.32961를 검색했으나 인용이 없었음. **선택 논문의 후속작으로 연결하지 않음**. 숫자·성능도 본 보고서에 가져오지 않음.
- 선택 논문 참고문헌의 Min et al.(2026)은 PAIR가 아니라 **Toward Reliable Context Compression for Long-Horizon Agents: An Empirical Study of Execution Instability**, arXiv2608.06503임. 공식 메타데이터 https://arxiv.org/abs/2608.06503 (source `turn162view2`) 최초 접수 2026-08-06. 이 둘을 혼동하지 말 것.
- 짧은 마무리 후보: ‘후속작을 억지로 붙일 단계는 아님. 10월 15일 기준 직접 인용한 후속 원문은 확인하지 못함. 다음 검증은 같은 상태에서 압축 유무를 갈라 실제 캐시·출력 과금까지 함께 재는 쪽임.’ 마지막 문장은 현재 논문에서 검증된 결론이 아니라 보고서의 후속 검증 제안으로 표시해야 함.

## 출처 품질 한계

- MemGPT/선택논문/Copilot paper의 심사 여부는 공식 arXiv에 게재 확인이 없다는 수준까지만 확인함. ‘미심사 확정’이라고 하지 않음.
- The Complexity Trap 워크숍 발표는 arXiv camera-ready와 저자 기관 공식 페이지로 교차 확인했으나 OpenReview는 browser challenge로 심사 내용 확인 불가. ‘NeurIPS 2025 본학회 심사 통과’ 금지.
- 공식 PDF의 제목과 메타데이터 제목, 버전별 저자 목록 차이를 그대로 기록함. 2차 AI 요약 사이트의 소속·학회·후속관계는 사용하지 않음.
