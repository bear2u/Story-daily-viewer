# 팩트 원장
기준일: 2026-10-15 KST. 원문: arXiv 2609.32961v1, 31쪽 전체 정독.
날짜 기준: arXiv 최초 공개 UTC. 소속은 원문 당시.

## F: 원문
- F1 | p.1 제목·저자란 | "Beyond Token Savings: A Systematic Study of Context Compression in LLM Agents"; "Ritul Satish, Prasoon Sinha, Akiho Kawada, Neeraja J. Yadwadkar"; "The University of Texas at Austin" | 제목·저자 네 명·전원 UT Austin 표기.
- F2 | pp.1–2 | "Across nearly 35,000 agent runs"; "65 compression policies" | 약 3만5천 실행, 65정책. 정확히35,000이라고 안 함. 같은 조합 반복 포함.
- F3 | p.3 §2.1 | "system prompt and task instruction are always kept verbatim" | 압축 대상은 assistant와 tool 기록, 시스템·작업지시 보존.
- F4 | p.3 §2.1 | "Truncation (TR) removes the oldest messages" | TR은 오래된 메시지부터 삭제.
- F5 | p.3; p.15 A.2.1 | "[output cleared]"; "three most recent tool-result messages"; "fall back to TR" | TRC는 오래된 도구출력 치환, 주위 assistant기록·최근도구출력3개 유지. 목표 못 맞추면 TR fallback 있음.
- F6 | p.3; pp.15–16 | "produces a summary that replaces the original text"; "can omit or alter information" | SU 전체자유요약, SS 구조화요약, 부분요약은 최근기록 원문 보존. 같은 모델 요약이 기본.
- F7 | pp.3–4 | "D = 0.5 reduces the compressible window to half" | primitive/trigger/depth분리, 목표반감 D=.5; .3/.5/.7. TRC 같은 depth-invariant에는 depth sweep 안 함.
- F8 | p.4; p.17 A.3 | "100 issues"; "40 tasks"; "Django (34), SymPy (34), and scikit-learn (32)" | SWE Verified선택100, TerminalBench1.0 선택40, 전체벤치마크 아님.
- F9 | p.4; Table5 p.18 | "Qwen3.5-35B-A3B, Devstral-Small-2-24B, and GLM-4.7-Flash"; "vLLM"; "mini-swe-agent"; "2.2.6" | 세모델, 로컬vLLM, 수정mini-swe-agent2.2.6.
- F10 | pp.18–19 A.5 | "Each task–policy–model configuration is repeated three times"; "95% confidence intervals" | 조합3회, task-level bootstrap95%CI.
- F11 | pp.6–8 Figure2,5 | "0.57×, 0.79×, and 0.71×"; "SU uses a similar 0.59× the tokens but reduces success by 11.0 pp." | Qwen SWE100 주실험 TRC token.57/time.79/inputcost.71, success53.7 vsFC53.0. SUtoken.59 success42.0 =−11pp.
- F12 | p.6 §4.1; Figure2 | "using roughly one-third ... take 20–80% longer"; "All policies increase latency" | Qwen Terminal40에서 모든압축정책time늘어남. 일부약1/3tokens 정책time20–80%증가. 다른모델전체주장금지.
- F13 | pp.6–7 | "We suspect"; "repository can act as an external source of truth" | repo에서회수가능성, transientterminalstate차이 저자가설. 원인을 격리한 실험 아님.
- F14 | pp.7,19–20 A.5.2 | "Nfresh + 0.1 Ncached + Nsummary"; "Output tokens contribute to token consumption but are excluded from this input-cost metric." | 비용=신규input+cachedinput*.1+summaryinput. output비용제외. 로컬실험 hypothetical입력비용 단위, 실제API청구아님.
- F15 | p.20 A.5.2 | "not a measured provider bill or cache-hit rate"; "Qwen was served with prefix caching disabled" | Qwen실측prefixcache꺼짐, 캐시비용추정과실측time별개.
- F16 | p.19 A.5.1 | "including the summarization calls"; "cumulative consumption sums usage across calls" | tokens입력+출력+요약호출누적. 최대한번prompt와다름.
- F17 | p.19 A.5 | "exclude runs that reach the time limit"; "Runs that reach only the step limit are included"; "retain tasks with measurements for both" | mainresource시간초과제외, step초과포함, 최소prompt기록2회, 정책FC공통eligibletasks. 성공시도만조건 아님. success모든시도.
- F18 | p.4 §3 표본; p.7 Figure3; p.19 A.5 포함규칙 | "subsets of 25 and 15"; "The controlled-sweep table in Figure 3 (right) includes all attempts in its cost and latency averages" | Qwen SWE25 sweep table모든시도costtime. 주실험100/곡선시간초과제외와분모차이.
- F19 | p.7 Figure3(c) | "50.7% to 62.7%"; "1.10× to 0.92×"; "653 to 599" | Qwen SWE25 D=.5 SU trigger10K→20K, success50.7→62.7,estimatedinputcost1.10→.92,time653→599s.
- F20 | p.7 Figure3(c) | "61.3% to 50.7%"; "50.7% to 60.0%" | SWE25 trigger15K D.3→.7 TRsuccess61.3→50.7,SU50.7→60.0. 깊게줄이기의효과삭제방식따라반대.
- F21 | p.8 Figure4 직접시각확인; p.19 A.5 | "at least two of its three runs succeed"; Figure4 FC행 Solved=53,TRC+SU행 Solved=52/Gained=+7/Lost=−8 | tasksolved2/3, FC53,stack52=53+7−8. 표 전사값이며 연속문장인용 아님. 평균resolve%와별도지표.
- F22 | p.8 Figure5a | OTRC Qwen51.3/.88,Devstral38.7/1.42,GLM41.3/.94 | SWE100 stepclearing정책서로다른model적용. 모델별threshold다르고복잡도조건같지않음. relative timeFC 대비.
- F23 | p.9 Figure5b | "6.7, 8.7, and 8.0" | SWE100 SS-p vsSS success+6.7/+8.7/+8.0pp. Qwen/Devstral/GLM,실험상평균pointestimate.
- F24 | pp.28–29 Figure13 A.6.3 수치; p.17 A.3 15K설정 | "resolve rate falls from 53.3% with self-summarization to 37.3% with Qwen3.5-9B and 28.0% with Gemma-4-12B."; "achieving 62.7% and 66.7%, respectively." | Qwenagent고정 SWE25 trigger15K. self/fullSU53.3,smallQwen9B37.3,Gemma12B28.0;TRC+SU68.0/62.7/66.7.
- F25 | pp.28–29 A.6.3; p.29 Figure13 | "Neither alternative reduces mean end-to-end latency on the shared eligible tasks."; "resource ratios use 10 shared tasks for SU and 23 for TRC+SU" | summarizer대체timecomparison SU공통eligible10,stack23. 작은모델전부일반화금지.
- F26 | pp.4,17–18 A.3 | "four A100 80GB GPUs ... four RTX A6000 48GB" | SWE/TBhardware차이, workload간time절대비교금지.
- F27 | pp.9,17–20 | "two coding benchmarks and three open-weight models"; cohort/inclusion/costdefinitions | 실제상용CLI전체동작·과금 재현아님.3모델2coding부분표본과설정안결과.
- F28 | Figure5a p.8 직접시각확인 | "FC 53.0", "SU 42.0", "TRC 53.7" | Qwen SWE100success평균%. 숫자사이공백보존.
- F29 | Figure5b p.8; §4.3 p.9 | "−12.5, −7.5, and −12.5 percentage points" | TerminalBench OTRC+SS-p vsOTRC Qwen/Devstral/GLM 성공률 변화. step-clearing에partialstructured요약추가 조건,모든요약금지아님.

## W: 공개 상태
- W1 | https://arxiv.org/abs/2609.32961v1 (2026-10-15) | "Sat, 26 Sep 2026 21:46:40 UTC" | UTC9월26일,한국9월27일. journal_ref/comment없음, 동료심사채택미확인. PDF내ICLRpolicy언급만으로채택단정금지.
- W2 | https://arxiv.org/html/2609.32961v1 (2026-10-15) | "CC BY 4.0" | 원저자·arXiv·license·crop수정출처기재.
- W3 | https://doi.org/10.48550/arXiv.2609.32961 (2026-10-15) | arXiv DOI | 원문DOI주소. 독립학술지DOI/심사인증으로해석금지.

## I: 해설/계산
- I1 | F12 | 1.2−1=.2;1.8−1=.8 | time1.2~1.8배는20~80%더오래. 일부정책·QwenTB조건 유지.
- I2 | F14 | inputfresh100,cached100→100+10=110 | 비용식직관은가정설명,실측청구값으로쓰지않음.
- I3 | F21 | 53+7−8=52 | 비슷한총점이이전성공보존보증못함.
- I4 | F17,F21,F27 | 적용 체크 제안 | 실제개발에성공/실패task변화,walltime,inputcost조건같이볼것은해설자제안. 새효능검증주장아님.

## L: 전작 원문 대조
- L1 | https://arxiv.org/pdf/2310.08560v2 pp.1–3, Figure3; abs/v1 최초공개 | "move data between main context and external context" | MemGPT 2023-10-12 UTC, 현재입력과외부기억함수호출이동. UC Berkeley, Charles Packer 등 v2저자7. 선택논문참고문헌v1저자6차이명시, 이번연구저자중복없음.
- L2 | https://arxiv.org/html/2508.21433v3 §3.1, 공식abs와JetBrains https://kairos.jetbrains.com/research/publications/complexity-trap (2026-10-15) | "preserving the full history of agent reasoning and actions" | ComplexityTrap 2025-08-29 UTC, Tobias Lindenbauer 등5, JetBrains/TUM. 관측마스킹·요약비교, 요약일관우세아님. DL4C@NeurIPS2025워크숍camera-ready확인,본학회채택주장금지.
- L3 | https://arxiv.org/pdf/2608.00101v1 §3.1, §6 Table6, Figure19,abs (2026-10-15) | "sessions that contain at least one compaction event"; "7.8%"; "44.2%" | Agentic Coding in the Wild 2026-07-30 UTC, Banruo Liu 등6, UIUC+MS. 미국일부지역6월첫주 sampled telemetry13.5M/초록13M. 압축세션비율7.8%,그세션전체tokens44.2%. 원문제목Traces없음/메타에는있음.
- L4 | 선택논문 A.1 p.14 및 세전작저자목록 | "varies what is compressed, when ... and how aggressively" | 전작은 배경/선행관찰로인용. 같은팀후속시리즈아님, 이번은3축통제비교. 저자중복없음.
- P1 | https://ece.utexas.edu/people/faculty/neeraja-yadwadkar (2026-10-15) | "Assistant Professor"; "Most of her research straddles the boundaries of Systems and ML." | UT Austin ECE교수, 시스템과ML접점. 논문개별담당/교신역할부여안함.
- W4 | 제목·ID검색, PAIR2609.36526원PDF참고문헌대조, lineage-audit.md (2026-10-15) | 직접 인용 원문 미확인 | 확인가능한직접후속작없음, 존재자체부정아님. PAIR는직접인용없어후속작으로제외.
- I5 | F3,F6,F16 | 설명용 장면 | 파일열기/테스트로그/이미바꾼부분이 요약누락될수있는 장면은 방법설명 예시, 실험에서그실패원인분리확인한사례라고주장안함.
- I6 | F14,F15,F27 | 후속 검증 제안 | 출력과금과실제cache측정+상태고정분기실험은 글의제안, 논문완료성과아님.
- F30 | p.19 A.5.1; §2 compressiontokenaccounting | "prompt and output tokens" | token은모델텍스트처리단위. 입력/출력tokens합산이라는원문용어를해설하는기초정의.
