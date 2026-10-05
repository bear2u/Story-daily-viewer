# 팩트 원장: Trust the Critic More
기준일: 2026-10-05 KST
원문 버전: arXiv:2609.39247v2, 29쪽
날짜 기준: arXiv 최초 공개일

## F: 논문 본문
- F1 | p.2 | “a minor calculation error at the end of a math proof can cause an otherwise correct and valuable reasoning trajectory to be penalized” | 마지막의 작은 계산 오류가 앞의 유용한 추론 전체에 같은 불이익을 줄 수 있음.
- F2 | p.2, p.4 | GRPO samples complete responses; every token receives the same advantage from terminal reward minus group mean | GRPO 비교 조건은 완성 응답의 끝 보상으로 응답 전체 토큰에 같은 advantage를 줌.
- F3 | p.1–2, Fig.1 | AC2 samples short chunks from replayed prefixes and scores endpoints with a learned critic | AC2는 저장된 풀이의 중간에서 짧은 후속 조각을 생성하고 critic 값으로 갱신해 일부 경우 끝 보상이 필요 없음.
- F4 | p.2, p.27 Table 4, p.29 | local readiness; reference solution; at most 10k new-token chunks with 50k total response budget | 신뢰성을 위한 세 요소는 문제별 준비도, 성공 풀이 참고, 최대 10,000 새 토큰 조각이며 prefix를 포함한 전체 응답 예산 상한은 50,000 토큰.
- F5 | p.5, p.27, p.29 | last-five-step global error <0.20; prior local error <0.18; one correct trajectory; nonzero critic prediction | 준비됨 판정은 전역·지역 오차, 정답 풀이 발견, 0이 아닌 예측 조건을 모두 봄.
- F6 | p.5, p.27, p.29 | audit fraction α=1/4 among sampled ready problems | 각 단계에 샘플된 준비 문제 중 약 1/4은 끝까지 생성해 critic 건강을 계속 측정함.
- F7 | p.6–7 | critic shares policy parameters, is prompted, greedily emits {0,0.1,…,1} | 별도 scalar head가 아니라 policy와 같은 가중치의 모델을 프롬프트로 critic처럼 쓰고 0.1 간격 값을 출력함.
- F8 | p.7, p.27 Table 4 | Qwen3-4B-Thinking-2507; FineProofs-RL roughly 5,200; IMO-ProofBench 60; 16 evaluation responses/problem; DeepSeek-V4-Flash judge 0–7 | 실험은 4B 모델, 약 5,200개 학습 문제와 60개 검증 문제, 문제당 16개 응답, 0–7점 자동 채점 조건임.
- F9 | p.2, p.7 | 18.50% at 1.99e20 FLOPs; AC2 first exceeds it at 0.79e20; 2.5×; 90 vs 120 steps; peaks 20.57% | 평균 검증 점수 18.50%를 넘는 데 AC2가 decoding FLOPs 2.5배 적게 썼고 90단계 대 120단계, 최고 평균은 20.57% 대 18.50%.
- F10 | p.7, Fig.1 | Prefix GRPO falls behind AC2 by decoding FLOPs | replay prefix 자체만으로 AC2 차이를 설명하지 못함.
- F11 | p.8, Fig.2 | global threshold crossed end step 7; about 70% ready by step 200 | critic 준비도는 7단계 끝에 전역 문턱을 넘었고 200단계에 표본 문제 약 70%가 준비됨.
- F12 | p.8 | no-audit peak 18.66% at step 160, slightly larger instability | 감사를 빼도 최고 18.66%이지만 더 불안정했고 저자는 감사를 권함.
- F13 | p.8 | stale replay reaches 17.90%; group-size-1 variant performs similarly | 오래된 replay와 그룹 1 변형도 학습은 됐으나 stale 변형은 17.90% 부근 plateau로 보임.
- F14 | p.9, p.18 | 2k chunk 16.62% at step100 then 13.57% step120; comparison also changes prefix-cut spacing | 2,000 토큰 변형은 100단계 16.62% 뒤 120단계 13.57%로 떨어졌으며 조각 길이와 cut 간격을 같이 바꿔 원인을 분리하지 못함.
- F15 | p.9 | correct-only 17.35% vs AC2 16.88% at step60; 14.67% at step110 | 정답 풀이만 저장하면 초반엔 앞섰지만 뒤에 14.67%로 하락함.
- F16 | p.9, p.18 Fig.8 | both comparison runs omit group and audit; no-local variant branches at main AC2 step 20; 13.56% step30 to 13.10% step40; with local 15.33%; 18.23% ready vs 100% | group·audit를 뺀 공통 조건에서 step 20에 분기했으며, local readiness까지 없애면 성적이 내려가고 문제별 문턱을 둔 비교 run은 올라감.
- F17 | p.10, Fig.4 | step80, 256 prefixes, group mean MAE 0.065 vs prefix value 0.211 | 16개 후속의 평균은 prefix 단독 예측보다 끝 보상 평균에 가까웠음.
- F18 | p.10, Fig.4 | advantage MAE 0.150, Pearson 0.388, 2,640 responses in 165 groups | critic advantage는 Prefix GRPO advantage와 양의 상관이지만 완벽한 대용물은 아님.
- F19 | p.10, Fig.2 | reference lowers MAE at steps 40,80,120,160; about 1,500 prefixes/checkpoint | 정답 참고를 주면 네 checkpoint 모두 critic MAE가 낮았음.
- F20 | p.18–19, Fig.9 | best-of-16: AC2 more compute-efficient, both plateau at roughly same score | 최고 하나를 고르는 지표에서는 계산 효율 차이는 남지만 최고 성적 plateau는 비슷함.
- F21 | p.25 | decoding FLOPs exclude prefill, validation, value and judge calls, training fwd/bwd, elementwise, communication | 2.5배 계산 비교는 생성 decoding FLOPs만 포함하며 전체 학습비용 비율이 아님.
- F22 | p.25 | mean estimate 4.01% below exact GRPO selected span and 5.51% below main AC2; GRPO plotted estimate, AC2 exact | 비교의 GRPO 비용 추정은 오히려 실제보다 약간 낮게 잡힐 수 있다고 저자들이 설명.
- F23 | p.26 | 196 complete steps; 32 GPUs; per-step correlation r=0.874 | main AC2 run 안에서 decoding FLOPs와 GPU-hours 상관은 0.874였음.
- F24 | p.12 | local readiness requires epoching and complete rollouts for ground-truth value; single-epoch left future work | 최대 한계는 같은 학습 데이터를 반복하며 끝까지 생성해 critic 정확도를 확인해야 한다는 점.
- F25 | p.29 | due to bug, reference-proof readiness condition activated only at step 42 | main run은 버그로 reference-proof 준비 조건이 42단계부터 켜졌고 저자들은 성능을 해친 방향이라고 예상함.
- F26 | p.29 | judge failure/unparseable output: excluded from critic targets but actor reward 0; invalid critic gets zero actor weight | 채점 실패와 critic 출력 실패는 서로 다른 방식으로 손실에서 처리됨.
- F27 | p.11 | “to our knowledge AC2 is the first method to date to use λ=0 for LLM RLVR” | 최초 주장은 저자들이 아는 범위라는 유보를 붙임.
- F28 | p.12 | suggested future combinations: beam search chunks or AlphaGo-style MCTS | beam search·MCTS는 실험 결과가 아니라 결론의 제안임.
- F29 | p.7, p.27 Table 4 | main AC2 group size g=16 continuations per prefix | main 실험은 prefix마다 continuation 16개를 샘플링함.

## L: 계보와 관계
- L1 | arXiv:1602.01783v2 p.1–2; 이번 논문 p.10–11 | A3C, Google DeepMind·MILA, 2016-02-04, ICML 2016 | 짧은 n-step return과 critic bootstrap을 쓴 actor-critic 계보이며 이번 논문이 이름 유사성을 직접 밝힘.
- L2 | arXiv:2402.03300v3 p.1, p.13 Fig.4 | DeepSeekMath, DeepSeek-AI·Tsinghua·Peking, 2024-02-05 | GRPO는 추가 value model을 없애고 같은 질문의 group reward 평균을 baseline으로 삼음.
- L3 | arXiv:2507.07969v4 p.1–2 | UC Berkeley, 2025-07-10, NeurIPS 2025 | 로봇 장기 과제에서 action chunk를 policy·critic 단위로 쓰는 선례.
- L4 | arXiv:2608.16739v1 p.1–2; 이번 논문 p.11 | Mistral AI·Mila·Université de Montréal, 2026-08-17 | privileged solution을 critic에 주는 가까운 선행. 끝 보상을 advantage에 유지해 AC2와 다름.

## P: 사람과 기관
- P1 | p.1 저자란 | “Stanford University”; * Equal contribution; correspondence to Kaiyue Wen and Luke Bailey | 논문 당시 네 저자 소속 Stanford, Wen·Bailey 공동 기여 및 교신.
- P2 | p.12 감사의 글 | Stanford Graduate Fellowship; Stanford Graduate and Vitalik Buterin Fellowship | 공개된 연구지원만 소개하고 현재 경력·동기는 추정하지 않음.

## W: 외부·현재 상태
- W1 | https://arxiv.org/abs/2609.39247v2 (2026-10-05) | v1 2026-09-30; v2 2026-10-01; DOI 10.48550/arXiv.2609.39247 | 읽은 판본과 공개일.
- W2 | arXiv·공식 검색 (2026-10-05) | journal reference 없음 | 프리프린트이며 공식 심사 통과·게재처 미확인.
- W3 | https://github.com/WhenWen/AC2 (2026-10-05) | public repository, code for paper, Apache-2.0 | 논문 코드는 공개돼 있으나 독립 재현 완료의 증거로 쓰지 않음.
- W4 | arXiv license link (2026-10-05) | CC BY 4.0 | 그림 크롭과 변형·재배포는 출처·변경 표시 조건으로 허용.
- W5 | 웹·Semantic Scholar 확인 (2026-10-05) | 직접 재현·반박 후속 원문 미확인 | 공개 5일 후라 후속 부재를 단정하지 않음.
