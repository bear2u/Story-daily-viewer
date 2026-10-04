# 팩트 원장
기준일: 2026-10-04 (Asia/Seoul)
원문: arXiv:2609.36700v1, 35쪽 전체 정독, 부록 E.4까지 확인
날짜 기준: arXiv 최초 공개. CORAL만 공식 게재월 사용.

## F: 이번 논문
- F1 | p.26 Figure 11 | "Answer: March 4, 2008" / "Answer: October 7, 2008" | Llama-3.3-70B·HippoRAG·CURRENT 예시는 두 번째 턴에서 틀린 답을 제시했고 네 번째 턴에서 정답에 도달함. 이것은 예시이지 실패율 추정이 아님.
- F2 | p.3 §3 / p.4 §3.1 | "150 questions from each of these five subsets, for 750 reviewed questions in total" | 데이터셋 원천은 HotpotQA·2WikiMultiHopQA·MuSiQue 세 가지. MuSiQue의 2/3/4-hop을 나눠 평가 묶음 다섯 개. 750문제, 사람의 검토를 거침.
- F3 | p.2 | "1.5 million simulated conversations" | 전체 연구 규모는 150만 모의 대화. 사람이 150만 명 참여했다는 뜻이 아님.
- F4 | p.5 §4.1 | "a closed-book configuration (NONE), two passage retrievers (BM25 and dense vanilla RAG), one hierarchical retriever (RAPTOR), and four graph retrievers (HippoRAG, HippoRAG2, ToG-2, LightRAG)" | 기본 비교는 검색기 7종과 검색 없는 대조군. 초록의 eight retrieval systems 표현을 여덟 검색기로 옮기지 않음.
- F5 | p.3 §3 / p.4 Figure 1 | "CURRENT" / "HISTORY" / "Full dialogue + new evidence" | CURRENT는 최신 사용자 발화만 검색. HISTORY는 지금까지 사용자 발화를 이어 검색. 양쪽에서 답변 모델은 사용자·AI 양쪽의 대화 이력을 받음. 검색 단계의 입력과 답변 단계의 입력이 다름.
- F6 | p.5 Table 1 / p.7 Eq.1 | "FULL The original question, in one turn" / "CONCAT All shards as a list, in one turn" / "SHARDED One shard per turn" | FULL→CONCAT은 질문 표현 변경과 모델 입력 변경, CONCAT→SHARDED는 턴 분산·반복 검색·답변 기회 증가가 함께 일어남. 순수 한 변수 인과 실험으로 부르지 않음.
- F7 | p.15 A.1 | "P1 (Information Equivalence)" / "P2 (Resolution Blindness)" / "P4 (Dependency-ordered revelation)" | 필요한 정보를 보존하고 정답·중간 답을 새로 주지 않으며 추론 관계 순서에 맞춰 단서를 제시함. 원문 질문의 모호함도 보존. 전작의 순서 무관성 가정은 버림.
- F8 | p.3 §3 / p.17 A.2 | "the user simulator and response classifier are fixed GPT-4o-mini modules" | 사용자 시뮬레이터와 답변 유형 분류기는 고정 GPT-4o-mini. 정답이면 멈추고, 아니라면 남은 단서를 줌. 마지막 단서 뒤 종료.
- F9 | p.5 §4.3 / p.6 | "BEST is the maximum F1 over all answer attempts in a conversation" / "Conversations with no answer attempt receive zero" | EM은 정규화 정답 일치, 토큰 F1은 정답과의 토큰 겹침. 한 대화에서 가장 높은 시도 점수를 채택. 앞서 틀렸어도 나중에 맞으면 BEST는 높은 점수. 각 문제 5회 모의 실행.
- F10 | p.6 §5.2 | "a decline of 5.1 F1 points under HISTORY and 7.1 under CURRENT, corresponding to relative losses of 11.7% and 16.3%" | 모델 10개·검색 7종·평가 묶음 5개 평균. 11.7%는 HISTORY, 16.3%는 CURRENT. F1 점수 하락의 상대 비율이고 정답률의 %p 하락이 아님.
- F11 | p.6 §5.2 / p.23 Table 8 | "HippoRAG2 ... FULL score of 50.6, yet loses 6.8 F1 points under HISTORY and 9.9 under CURRENT" | 이 비교의 최고 FULL 검색기인 HippoRAG2가 절대 하락 폭도 가장 큼. 여전히 SHARDED 절대 점수는 가장 높음. FULL 50.6, HISTORY 43.8. 점수가 낮아졌다는 것과 순위가 낮다는 것 구분.
- F12 | p.6 §5.2 / p.23 Table 8 | "despite ranking fifth under FULL, it loses only 0.7 F1 points" | Gemma-4-31B는 HISTORY 평균 44.3→43.6, 작은 평균 하락. 불안정성 U 7.6→15.0이므로 항상 안정적이라고 쓰지 않음.
- F13 | p.8 Table 3 / §5.3 | "BM25 has the largest drop, at 11.7 F1 points" / "BM25 recovers 5.2 F1 points over CONCAT" | BM25 HISTORY는 FULL→CONCAT에서 11.7점 하락, CONCAT→SHARDED에서 5.2점 회복, 총 6.5점 하락. 11.7점과 전체 상대 하락률 11.7%는 다른 값.
- F14 | p.8 §5.3 | "HippoRAG, LightRAG, and ToG-2 ... first use an LLM to extract entities or keywords" / "may make them less sensitive" | 표현 변화에 덜 민감한 세 방법은 검색 전 개체·키워드 추출. 저자 해석이며 동일 검색기에 전처리만 붙인 인과 검증으로 과장하지 않음.
- F15 | p.9 Table 4 | "cumulative is the union of every turn’s top-five passages" | Recall@5는 정답 근거 문단 중 상위 5개 결과에 잡힌 비율. cumulative는 모든 턴 상위5개 합집합으로, 한 번의 상위5개나 최종 턴만 보는 것과 다름. RAPTOR는 요약 노드가 있어 제외.
- F16 | p.9 Table 4 / §5.4 | "HippoRAG2 reaches 74.8 cumulative recall, compared with 70.7 under FULL, while its F1 remains 9.9 points lower" | CURRENT 누적 근거 회수율 74.8 vs FULL 70.7, 답변 F1은 9.9점 낮음. 더 많은 검색 기회라는 조건 포함.
- F17 | p.23 B.4 / p.24 Table 9 | "Among the 54,876 qualifying pairs (24.4% of the 225,000 eligible) ... 73.7 ... 62.1 ... 11.6 points (95% paired bootstrap CI [9.9–13.4])" | 양 조건 모두 모든 정답 근거를 검색한 HISTORY 짝 54,876개, 대상 중 24.4%, F1 73.7→62.1. RAPTOR 제외 6검색기. 여전히 방해 문단이 남음. 무작위 대표 표본 아님.
- F18 | p.22 Eq.2 / p.9 | "A = percentile90(S), U = percentile90(S) − percentile10(S)" / "13.4 ... 19.7 ... a 47% increase" | 5회 점수의 90분위와 10분위 차이 U. HISTORY 평균 U 13.4→19.7, 상위 추정 A는 1.9점 하락. 47%는 U 증가율, 오답률 아님. 5회 분위값은 선형 보간 기술통계.
- F19 | p.19 B.1 | "RECAP appends one final turn ... SNOWBALL ... repeats all previously revealed shards at every turn" | RECAP 마지막에 전체 단서를 다시 말하고 SNOWBALL은 매 턴 누적 단서 반복. RECAP은 마지막 턴을 알아야 하는 제약. 최신 발화 정책에서도 반복된 사용자 발화가 이제 전체 단서 포함.
- F20 | p.19 B.1 / Figure 5 | "three LLMs (GPT-4o-mini, Qwen3-32B, and Llama-3.3-70B)" / "recovering 92–123% ... 7–39%" | 보완 실험은 3개 모델·5묶음·7검색기. CURRENT RECAP에서 세 개체/키워드 방법은 92~123% 격차 회복, 나머지 7~39%. 100%는 FULL 점수 회복, 정답률 100%가 아님.
- F21 | p.20 B.1 / Figure 5 | "BM25 ... remains below plain SHARDED" | CURRENT SNOWBALL BM25 회복량 -33%. 이전 단서 반복이 오히려 일반 SHARDED보다 악화됨. HISTORY를 같은 결과로 일반화하지 않음.
- F22 | p.21 B.2 / p.22 | "eight open-weight models" / "33.4" / "31.3" / "47.5 LLM calls ... against 6.9 for ToG-2" | PoG 실험은 오픈 모델 8개, 5묶음. HISTORY에서 FULL 33.4→31.3(본문 하락2.0점, 반올림 표 숫자 차2.1점). retrieval calls 대화당47.5 vs ToG-2 6.9. 저렴하거나 최고 성적이라고 쓰지 않음.
- F23 | p.25 B.5 / Table 10 | "mean HISTORY gap changes only from 4.1 points under token F1 to 3.8 under the judge" | Llama-3.3-70B·Gemma-4-31B·Qwen3-32B의 후속 채점. GPT-4o-mini 의미 판정에서도 평균 하락. LLM 판정기 편향 가능성이 있어 보강 확인으로 다룸.
- F24 | p.17 Figure 3 | "mean 2.65 turns" / "mean 3.75 turns" | 실험 단서는 대체로 2~5턴, 수백 턴 기억 시험이 아님. 데이터 묶음별 길이 그림에 있음.
- F25 | p.28 D.4 | "1,000-token answer cap" / "10,000-token cap" / "temperature 0.7" | 모델별 추론·답변 예산이 완전히 동일하지 않음. Luna5.6 및 Qwen3.6-27B는1만토큰. Qwen은 thinking 비활성·T0.7. 나머지 기본1000토큰·T1.0. 모델순위를 매개변수 수만의 효과로 볼 수 없음.
- F26 | p.10 Reproducibility / p.30 E | "We plan to publicly release our codebase, experiment results, and project documentation" / "remaining datasets ... will be provided in our code repository" | 코드·결과 공개는 원문상 계획. HotpotQA 프롬프트만 본문에 있음. 이미 모든 자료 공개됐다고 쓰지 않음. p.15 public release 표현과 현황 구분.
- F27 | p.27 Table 12 | "HotpotQA ... 9,772" / "2WikiMultiHopQA ... 6,324" / "MuSiQue ... 11,693" | 검색 대상은 각 고정 코퍼스. 자유 웹검색·현실 서비스 전반·한국어·학습 코칭을 검증한 것이 아님. 영어 단답 multi-hop QA 및 모의 사용자 범위.
- F28 | p.7 Eq.1 / p.9 §5.4 | "changes both the retrieval query and the assistant’s input" / "introduces repeated retrieval and answer opportunities" | 진단 분해는 관측 차이. 각 내부 원인의 순수 인과 기여율 확정이 아님.

## L: 선행 연구
- L1 | priors/rag-2020/text.txt p.1–2 / arxiv.org/abs/2005.11401 (2026-10-04) | "parametric memory ... pre-trained seq2seq model" / "non-parametric memory ... dense vector index of Wikipedia" | Lewis 등, 2020-05-22 최초 공개, NeurIPS2020, 읽은v4. 생성모델과 위키피디아 검색 인덱스 결합. 이번 논문의 배경 인용(p.2). 현재 모든 RAG가 이 학습법 그대로라고 쓰지 않음.
- L2 | priors/hipporag/text.txt p.1–2 / arxiv.org/abs/2405.14831 (2026-10-04) | "LLMs, knowledge graphs, and the Personalized PageRank algorithm" | Gutiérrez 등, 2024-05-23 최초 공개, NeurIPS2024, 읽은v3. 여러 문단의 개체를 그래프로 엮어 관련성 전파. 이번 논문 검색 비교 대상. 당시 소속 OSU·Stanford.
- L3 | priors/coral/text.txt p.1 / aclanthology.org/2025.findings-naacl.72 (2026-10-04) | "passage retrieval, response generation, and citation labeling" | Cheng 등, Findings NAACL2025, 공식 게재월2025-04. 대화 검색·응답·인용 평가. 이번 논문 p.2–3에 관련 평가로 인용. 이번 논문이 CORAL 데이터를 실험에 사용했다고 쓰지 않음.
- L4 | priors/lost-conversation/text.txt p.1–2 / arxiv.org/abs/2505.06120 (2026-10-04) | "sharded instructions ... jointly deliver the same information" | Laban·Hayashi·Zhou·Neville, 2025-05-09 최초 공개, 읽은v1. 소속 Microsoft Research·Salesforce Research. 이번 논문 p.3의 "adapts the multi-turn framework" 관계는 확장. 이전 PDF의 초록39%와그림35%·서론25점 등 불일치 있어 전작 하락 수치 본문에서 제외.
- L5 | 이번 논문 p.3 | "Both studies ... without retrieval. We extend their setup to retrieval-augmented QA" | 이번 연구는 동일과제 턴분산 평가를 검색 결합 QA로 확장함. 이전 저자4명과이번2명 겹치지 않음(명단 대조). 이름 반복으로 같은 팀이라 쓰지 않음.

## P: 저자와기관
- P1 | 이번 PDF p.1 | "Pranav Handa & Ariful Azad" / "Texas A&M University" | 저자2명, 논문 당시 텍사스A&M대. 현재 소속 추정 없음. 2026-10-04 원문 확인.

## W: 변하는 기록
- W1 | https://arxiv.org/abs/2609.36700 (2026-10-04) | "Submitted on 29 Sep 2026" / "v1" / "35 pages, 11 figures" | 최초공개2026-09-29. 읽은v1. arXiv 및PDF는 Preprint. 공식심사통과·게재처를확인하지못함. 저널/학회부재를 미투고로단정하지않음.
- W2 | https://arxiv.org/abs/2609.36700 (2026-10-04) | "https://doi.org/10.48550/arXiv.2609.36700 ... (pending registration)" | arXiv 안내DOI와원문링크제공. DOI등록대기표시유지. DOI발급이동료평가통과뜻아님.
- W3 | arXiv view license → https://creativecommons.org/licenses/by/4.0/ (2026-10-04) | "Attribution 4.0 International" | 이번논문은CC BY4.0. 그림출처·원제·저자·판본·라이선스·크롭변경표시를ATTRIBUTION에기록. 선행논문별라이선스별도표시.
- W4 | 웹검색/arXiv/S2/OpenAlex조회 (2026-10-04) | 조회범위내후속원문미확인 | 공개5일후현재,이번논문을직접인용해재현/확장한후속작확보못함. 없다고단정하지않고해설에서제외. S2는429로제한,인용수도제외.
- W5 | 실제GitHub posts.json (2026-10-04) | generative-agents / darwin-godel-machine / agent-meltdowns / subliminal-learning | 이번선정과기존게시글중복없음.
