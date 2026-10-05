# 기획서: Trust the Critic More

## 판단
- 유형: 해결형. 완성 답을 끝까지 생성해야 하는 LLM RL의 비용과 거친 credit assignment를 AC2로 줄였다는 주장이 첫 기여임 (F2 F3).
- 날짜 기준: arXiv 최초 공개일 2026-09-30, 읽은 판본 v2는 2026-10-01.
- 독자 친숙도: 강화학습은 이름만 앎. “수학 풀이의 마지막 오답 때문에 앞부분도 같이 혼나는 장면”부터 들어감.
- 지금 사회에서 어디쯤 와 있나: GRPO 계열이 LLM reasoning RL에서 널리 쓰이는 비교점이고, 공개 코드가 있으나 이 논문은 아직 심사 통과·독립 재현이 확인되지 않은 5일 된 프리프린트임 (L2 W2 W3 W5).
- 도입 질문: 수학 풀이 마지막 줄만 틀렸는데 앞의 맞는 추론까지 전부 같은 점수를 받아야 하나? → 답은 파트 21.
- 마지막 답: 전체 답 하나에 점수 하나를 붙이는 대신, 신뢰할 수 있는 문제에서만 10k 토큰 조각을 critic으로 평가하면 끝까지 생성하지 않는 갱신이 가능했으나 반복 데이터와 완성 rollout 검사가 필요함.
- 맺음: 공개 코드와 CC BY 4.0, 심사·재현 미확인 상태 / 단일 epoch에서 local readiness를 만드는 것이 실제 다음 검증 (W2 W3 W4 F24).
- 기대 vs 결과: 더 잘게 쪼개면 더 정확할 것 같지만 2k 조각은 10k보다 뒤처졌고, 정답 풀이만 저장하면 초반 상승 뒤 하락함 (F14 F15).

## 척추
- 마디: 끝 점수 | 완성 풀이 하나의 끝 보상을 모든 토큰에 같은 advantage로 배분 | 전작: GRPO가 critic 없이 효율화 | 이번: 끝 보상 없이 일부 갱신 | F1 F2 F3 L2
- 마디: 문제별 신뢰 | critic을 전체적으로 믿지 않고 문제마다 준비도 판정 | 전작: Le Critique 등은 critic을 baseline으로 사용 | 이번: 준비된 문제만 λ=0 전환 | F5 F16 L4
- 마디: 긴 조각 | 단일 토큰이 아니라 10k 토큰 행동 묶음을 평가 | 전작: 로봇 action chunking | 이번: 수학 증명 언어 토큰에 적용 | F4 F14 L3
- 마디: 계산 범위 | 2.5배는 decoding FLOPs 기준이며 전체 비용이 아님 | 전작: 완성 rollout 기반 | 이번: 생성 토큰을 줄였으나 judge·critic·학습 계산 제외 | F9 F21 F22 F23
- 대가·남은 의문: 반복 검사 | local readiness가 같은 데이터를 반복하고 완성 rollout으로 ground truth를 요구 | 회수: 단일 epoch는 향후 과제 | F24 W5

## 밑밥과 회수
- 마지막 한 줄 오답 때문에 앞부분도 같이 혼남 (파트 1) → 조각별 점수의 답과 한계 (파트 21).
- 더 잘게 2k로 자르면 더 세밀할 것 같음 (파트 10) → 2k가 뒤에서 무너짐 (파트 15).
- 정답 풀이만 replay에 남기면 좋아 보임 (파트 12) → 초반 우세 뒤 14.67로 하락 (파트 16).

## 재료
- 재미: AC2 이름이 A3C와 닮았음을 저자들이 직접 밝힘 (L1); 2k가 10k보다 나쁨 (F14); 정답만 저장한 변형이 뒤에 하락 (F15); main run 준비 조건이 버그로 step42까지 늦게 켜짐 (F25).
- 전문성: advantage·terminal reward·critic 정의, λ=0/1, readiness 문턱, replay와 audit, 데이터·judge, ablation, MAE·상관, 계산 범위 (F2–F26).
- 결정적 증거: main curve와 Prefix GRPO (F9 F10), local readiness 제거 (F16), chunk 크기 비교 (F14), critic diagnostics (F17 F18).
- 구체 예시·비유: 마지막 계산 오류가 전체 풀이를 벌주는 원문 예시(q_minor); 저장된 풀이 중간에서 네 갈래를 10k씩 이어 critic이 비교하는 Fig.1.
- 전문가용 파트: 9, 13, 18.
- 비약 지점: critic을 믿는다는 말 → 문제별 readiness 조건과 audit를 풀어 설명; 2.5배 → 포함·제외 계산을 분리; 더 짧은 chunk → cut spacing도 바뀐 confound 명시.
- 뺀 것: 후속 재현·공식 심사 결과·현재 저자 직함은 원문 또는 공식 기록 미확보로 제외. MCTS는 결과가 아니라 제안으로만 언급.

## 파트 목록
| # | 첫 줄 | 연결 | 요지 | 그림 | 원장 ID |
|---|---|---|---|---|---|
|1|수학 풀이 마지막 줄 하나만 틀리면|끝 점수·밑밥|전체 풀이가 같은 점수 받는 문제|q_minor|F1 F2|
|2|그 한 줄을 붙잡은 논문이 나옴|끝 점수|메타데이터·심사 상태|header|P1 W1 W2|
|3|끝 점수 방식이 나온 자리는 강화학습임|끝 점수|actor·critic 직관과 A3C|prior_a3c|L1|
|4|근데 LLM 쪽은 critic을 빼는 길로 감|끝 점수|GRPO 등장과 구조|prior_grpo|L2 F2|
|5|그러다 critic을 다시 데려온 연구가 나옴|문제별 신뢰|Le Critique 계보와 차이|prior_lecrit|L4|
|6|행동을 묶는 생각은 로봇 쪽에도 있었음|긴 조각|action chunking 선례|prior_chunking|L3|
|7|이번 AC2는 두 줄기를 수학 풀이에 붙임|긴 조각|GRPO 대 AC2 구조|fig1|F3 F4|
|8|쉽게 말하면 저장된 풀이 중간에서 다시 시작함|긴 조각|replay prefix·chunk·critic|algorithm|F3 F7|
|9|여기부터 한 파트는 준비도 계산임|문제별 신뢰|문제별 문턱과 audit|fig2|F5 F6 F11|
|10|10k라는 숫자는 그냥 크게 잡은 게 아님|긴 조각·밑밥|50k 대비 10k, 2k 예고|tab4|F4 F14|
|11|시험장은 수학 올림피아드 증명 60문제였음|조건|모델·데이터·judge|header/없음|F8|
|12|이제 계산량 곡선에서 파란 선을 보셈|계산 범위·밑밥|main 2.5x·peak·Prefix GRPO|fig1|F9 F10|
|13|전문가용으로 critic 값이 얼마나 맞았는지 봄|문제별 신뢰|MAE·상관·reference|fig4|F17 F18 F19|
|14|critic은 7단계부터 조금씩 맡기 시작함|문제별 신뢰|ready fraction 70%, audit|fig2|F11 F12|
|15|앞에서 미뤄둔 2k 조각은 뒤에서 무너짐|긴 조각·회수|chunk ablation과 confound|fig7|F14|
|16|정답 풀이만 남긴 변형도 처음엔 앞섬|밑밥 회수|correct-only·no readiness 실패|fig3|F15 F16|
|17|그러면 최고 답 하나만 고를 때도 앞서냐|계산 범위|best-of16 결과 제한|fig9|F20|
|18|2.5배의 분모에는 빠진 계산이 있음|계산 범위|decoding FLOPs 범위·GPU 상관|q_cost fig19|F21 F22 F23|
|19|실험 코드에도 숨은 조건 하나가 남음|문제별 신뢰|step42 bug와 failure handling|q_bug|F25 F26|
|20|그 조건보다 더 큰 한계는 반복 학습임|대가|epoch·완성 rollout 요구|q_limit|F24|
|21|이제 첫 질문에 답할 수 있음|끝 점수 회수|부분 평가가 가능해진 조건과 범위|fig1|F1 F3 F24|
|22|지금 공개된 건 주장만은 아님|지금·앞|코드·라이선스·미심사·미재현, 3줄|header|W2 W3 W4 W5 F24|

연결률: 22/22. 그림 있는 내용 파트 목표 17/21.
