# 일부 수학 풀이를 끝까지 안 쓰고 AI를 훈련한 방법

수학 풀이 마지막 줄 하나만 틀리면
앞에서 맞힌 과정도 전부 틀린 걸까?

기존 GRPO식 학습은
완성된 풀이의 끝 점수로
그 풀이의 모든 토큰에 같은 advantage를 줌. <!-- F2 -->

논문이 든 예시는 더 구체적임.
마지막의 작은 계산 실수 하나 때문에
앞의 쓸모 있는 추론까지 함께 벌점받을 수 있음. <!-- F1 -->

원문 문장 그대로 아래에 있음.

![마지막 계산 오류가 앞선 추론 전체를 벌줄 수 있다는 예시 (원문 p.2)](assets/posts/trust-the-critic-more/q_minor.webp)

---

그 한 줄을 붙잡은 논문이 나옴.

제목은 Trust the Critic More.
Kaiyue Wen, Luke Bailey,
Arvind Mahankali, Tengyu Ma가 썼음. <!-- P1 -->
논문 당시 네 사람 모두 Stanford 소속임. <!-- P1 -->

최초 공개는 2026-09-30,
읽은 판본은 2026-10-01의 arXiv v2임. <!-- W1 -->
2026-10-05 확인 기준 프리프린트이고
공식 심사 통과나 게재처는 확인하지 못했음. <!-- W2 -->

별표 두 명이 공동 기여자임.
저자란을 아래에서 보셈. <!-- P1 -->

![논문 제목과 Stanford 저자 네 명 (원문 p.1)](assets/posts/trust-the-critic-more/header.webp)

[arXiv](https://arxiv.org/abs/2609.39247v2) · [원문 PDF](https://arxiv.org/pdf/2609.39247v2) · [DOI](https://doi.org/10.48550/arXiv.2609.39247)

---

이 끝 점수 방식은 강화학습에서 나옴.

한쪽은 답을 쓰는 actor,
다른 쪽은 현재 상태의 앞날을 채점하는 critic임.

2016년 A3C는
몇 단계를 진행한 뒤 critic 값을 붙여
actor를 갱신하는 방법을 보여줬음. <!-- L1 -->

이번 저자들도 AC2라는 이름이
A3C와 닮은 건 방법의 성격도 닮았기 때문이라고 적음. <!-- L1 -->

당시 A3C가 Atari 다섯 게임에서
얼마나 빨리 배웠는지 아래 곡선에 나옴.

![A3C와 다른 비동기 강화학습법의 Atari 학습 속도 (Mnih 외 2016, Figure 1)](assets/posts/trust-the-critic-more/prior_a3c.webp)

---

근데 LLM 쪽은 critic을 빼는 길로 감.

2024년 DeepSeekMath가 소개한 GRPO는
별도 value model을 두지 않았음. <!-- L2 -->

같은 질문에 답을 여러 개 만들고
그 답들의 끝 점수 평균을 기준선으로 삼음. <!-- L2 F2 -->

쉽게 말하면
각 풀이가 반 평균보다 잘했는지 보는 방식임.

정확히는
한 완성 응답 안의 모든 토큰이
그 terminal reward로 계산한 같은 advantage를 받음. <!-- F2 -->

아래에서 PPO에 있던 Value Model이
GRPO 줄에서는 사라지는 걸 보셈.

![PPO의 value model을 group 점수 평균으로 바꾼 GRPO (Shao 외 2024, Figure 4)](assets/posts/trust-the-critic-more/prior_grpo.webp)

---

그러다 critic을 다시 데려온 연구가 나옴.

2026년 8월 Le Critique는
정답 같은 추가 정보를 critic에 주는
privileged value function을 제안했음. <!-- L4 -->

근데 그 critic은 기준선을 더 잘 잡는 역할이었고
advantage에는 여전히 완성 답의 끝 점수가 들어감. <!-- L4 -->

이번 AC2는 여기서 한 발 더 나감.
준비된 문제에서는
끝 점수를 아예 보지 않는 갱신을 함. <!-- F3 -->

아래 왼쪽은 풀이 중간,
가운데 위는 critic만 보는 정답 예시임.

![정답 정보를 critic에만 주는 privileged value function (Venkatraman 외 2026, Figure 1)](assets/posts/trust-the-critic-more/prior_lecrit.webp)

---

행동을 묶는 생각은 로봇 쪽에도 있었음.

2025년 UC Berkeley의 Q-chunking은
로봇이 다음 동작 하나 대신
짧은 동작 묶음을 예측하게 했음. <!-- L3 -->

critic도 그 묶음 전체의 가치를 계산함. <!-- L3 -->

이번 논문이 그대로 복사한 실험은 아님.
로봇 행동 대신 수학 증명의 토큰을 묶고
online 탐색 대신 LLM 증명 학습을 다룸. <!-- L3 F3 -->

아래 파란 상자 하나가
시간 순서로 묶인 행동 조각임.

![시간상 이어진 행동 묶음을 평가하는 Q-chunking (Li 외 2025, Figure 1)](assets/posts/trust-the-critic-more/prior_chunking.webp)

---

이번 AC2는 두 줄기를 수학 풀이에 붙임.

왼쪽 GRPO는 문제 처음부터 답 끝까지
여러 갈래를 전부 생성함. <!-- F2 -->

오른쪽 AC2는 저장된 풀이 중간 s에서 시작해
짧은 후속 조각 a를 여러 개 만듦. <!-- F3 -->
critic이 각 조각 끝의 가치를 매기고
그 그룹 평균과의 차이로 학습함. <!-- F3 -->

그래서 준비된 문제의 이 갱신에는
완성 답의 terminal reward가 필요 없음. <!-- F3 -->

왼쪽 가지가 전부 끝까지 가는지,
오른쪽 가지는 중간에서 멈추는지 보셈.

![GRPO 완성 rollout과 AC2 행동 조각 비교 (Figure 1)](assets/posts/trust-the-critic-more/fig1_p1.webp)

---

쉽게 말하면 저장된 풀이 중간에서 다시 시작함.

그 뒤를 여러 갈래로 조금씩 이어 씀.
main 실험에서는 prefix마다 16갈래였음. <!-- F29 -->
어느 갈래가 더 유망한지 critic에게 물어봄.

정확히는 replay buffer에서 prefix를 자르고
같은 최대 길이 예산의 continuation 그룹을 샘플링함. <!-- F3 -->
준비된 문제면 critic endpoint value를,
아니면 끝까지 생성한 reward를 씀. <!-- F3 F5 -->

actor와 critic은 같은 모델 가중치를 공유함. <!-- F7 -->
critic은 별도 숫자 head를 두지 않고
프롬프트를 받고 0부터 1까지
0.1 간격 숫자를 출력함. <!-- F7 -->

전체 순서는 아래 알고리즘에 적혀 있음.

![replay prefix와 준비도에 따라 조각 또는 완성 rollout을 고르는 절차 (Algorithm 1)](assets/posts/trust-the-critic-more/algorithm.webp)

---

critic을 전체적으로 한 번 믿는 게 아님.
문제마다 준비됐는지 따로 판단함. <!-- F5 -->

최근 다섯 단계 평균 오차가 0.20 아래,
그 문제를 직전에 뽑았을 때
오차가 0.18 아래여야 함. <!-- F5 -->
정답 풀이를 하나 이상 찾았고
0이 아닌 critic 예측도 있어야 함. <!-- F5 -->

샘플된 준비 문제의 약 1/4은
끝까지 생성함. <!-- F6 -->
critic이 계속 맞는지 검사하는 audit임.

전역 문턱은 7단계 끝에 처음 넘었고
200단계에는 표본 문제 약 70%가 준비됨. <!-- F11 -->

아래 첫 그래프가 준비된 문제 비율임.

![문제별 준비 비율과 critic 오차 변화 (Figure 2)](assets/posts/trust-the-critic-more/fig2_p8.webp)

---

10k라는 숫자는 그냥 크게 잡은 게 아님.

전체 응답 예산은 50,000토큰이고
준비된 문제의 조각은 10,000 새 토큰임. <!-- F4 -->

한 토큰씩 점수를 주지 않아도 됨.
10k는 prefix까지 포함한
50k 응답 상한의 1/5인 새 토큰 상한임. <!-- F4 -->

더 잘게 2,000토큰으로 자르면
더 세밀하게 가르칠 것 같음.
이 숫자는 뒤에서 다시 나옴.

그 전에 main 설정을 보셈.
group 16개와 audit 1/4도 함께 적혀 있음. <!-- F6 F29 -->

![AC2 main run의 모델·조각·준비도 설정 (Table 4)](assets/posts/trust-the-critic-more/tab4_p27.webp)

---

시험장은 수학 올림피아드 증명이었음.

Qwen3-4B-Thinking-2507을
FineProofs-RL 약 5,200문제로 학습함. <!-- F8 -->

검증은 IMO-ProofBench 60문제,
문제마다 답 16개를 생성했음. <!-- F8 -->

DeepSeek-V4-Flash가
각 증명을 0점부터 7점까지 채점함. <!-- F8 -->

학습 때 judge는 정답 풀이를 못 봤고
검증 때는 reference solution과
문제별 rubric을 함께 받았음. <!-- F8 -->

그러니 이 결과는 4B 수학 증명 모델에서 잰 것임.
일반 채팅이나 코딩 에이전트 성능으로
바로 옮겨 말할 수는 없음.

![Qwen3-4B·FineProofs-RL·IMO-ProofBench 조건을 요약한 초록 (원문 p.1)](assets/posts/trust-the-critic-more/abstract_conditions.webp)

---

이제 계산량 곡선에서 파란 선을 보셈.

GRPO 최고 평균 점수는 18.50%였음. <!-- F9 -->
그 지점까지 decoding 계산은 1.99×10^20 FLOPs였음. <!-- F9 -->

AC2는 0.79×10^20에서
처음으로 그 점수를 넘었음. <!-- F9 -->
그래서 논문이 말한 차이가 2.5배임. <!-- F9 -->

그 18.50%를 넘는 데도
120단계 대신 90단계가 걸렸고
AC2 최고 평균은 20.57%까지 갔음. <!-- F9 -->

replay 중간에서 시작하되 끝까지 생성하는
Prefix GRPO는 파란 선을 따라오지 못했음. <!-- F10 -->

중간에서 시작한 것만으로 생긴 차이는 아니었음.

![AC2·GRPO·Prefix GRPO의 decoding FLOPs 대비 평균 점수 (Figure 1)](assets/posts/trust-the-critic-more/fig1_p1.webp)

---

그럼 끝 점수 없이 critic을 믿어도 되는지 직접 재봄.

80단계에서 준비된 256개 문제를 골라
prefix마다 후속 답 16개를 끝까지 생성함. <!-- F17 -->

그룹 평균값의 MAE는 0.065,
prefix 하나의 critic 값은 0.211이었음. <!-- F17 -->
여러 후속을 평균낸 값이
실제 끝 보상 평균에 더 가까웠다는 뜻임.

critic advantage와 Prefix GRPO advantage는
critic 예측이 하나 이상 있는 165그룹,
2,640개 응답에서 MAE 0.150,
Pearson 상관 0.388이었음. <!-- F18 -->

정답 참고를 critic에게 주면
40·80·120·160단계 모두 MAE가 낮아졌음. <!-- F19 -->

critic이 완벽하다는 뜻은 없음.
문제별 문턱과 그룹 평균으로 쓸 만하게 만든 것임.

![critic 값·끝 보상과 advantage 진단 (Figure 4)](assets/posts/trust-the-critic-more/fig4_p10.webp)

---

critic은 7단계부터 조금씩 맡기 시작함. <!-- F11 -->

준비된 문제도 audit에서는
끝까지 답을 써서 critic 오차를 다시 확인함. <!-- F6 -->

audit를 아예 뺀 변형도
160단계에서 최고 평균 18.66%를 기록했음. <!-- F12 -->
다만 흔들림이 조금 더 컸고
저자들은 건강 상태를 추적하려면
audit를 남기라고 권함. <!-- F12 -->

오래된 replay를 쓴 변형은 17.90%,
준비된 문제에서 그룹을 1개로 줄인 변형도
학습 자체는 가능했음. <!-- F13 -->

왼쪽의 파랑·청록·보라 곡선을 보셈.

![audit·group·오래된 replay 변형과 실패 ablation (Figure 3)](assets/posts/trust-the-critic-more/fig3_p9.webp)

---

앞에서 미뤄둔 2k 조각은 뒤에서 무너짐.

50단계까지는 거의 붙어 갔음.
2k가 16.03%, 10k가 16.41%였음. <!-- F14 -->

근데 2k는 100단계 16.62%가 최고였고
120단계에는 13.57%로 내려감. <!-- F14 -->

짧을수록 항상 정교해진다는 결과가 아니었음.

단, 이 실험은 조각 길이만 바꾼 게 아님.
prefix를 자르는 간격도 10k에서 2k로 바꿈. <!-- F14 -->
둘 중 무엇 때문인지 따로 분리할 수 없음.

두 곡선이 50단계 뒤 갈라지는 곳을 보셈.

![10k와 2k 조각의 학습 성적 비교 (Figure 7)](assets/posts/trust-the-critic-more/fig7_p18.webp)

---

정답 풀이만 남긴 변형도 처음엔 앞섬.

replay buffer에 7점 중 6점 이상 받은
풀이만 저장했음. <!-- F15 -->

60단계에는 17.35%로
AC2의 16.88%보다 높았음. <!-- F15 -->

그 우세가 오래가진 않음.
110단계에는 14.67%로 떨어짐. <!-- F15 -->

문제별 준비도 비교는 두 run 모두
group과 audit를 뺀 조건임. <!-- F16 -->
main AC2의 20단계 checkpoint에서 갈라졌음. <!-- F16 -->

local readiness까지 없앤 쪽은
30단계 13.56%에서 40단계 13.10%로 내려감. <!-- F16 -->
준비도를 둔 비교 run은 15.33%였음. <!-- F16 -->

정답만 남기기와 전부 믿기,
둘 다 오른쪽 그래프에서 뒤처짐.

![정답만 저장하거나 local readiness를 없앤 변형의 하락 (Figure 3)](assets/posts/trust-the-critic-more/fig3_p9.webp)

---

local readiness 비교에서 평균 점수가 갈렸다면
최고 답 하나만 고를 때도 앞설까?

논문은 16개 검증 궤적을 bootstrap해
최고점을 고르는 best-of-16도 추정했음. <!-- F20 -->

계산량 대비로는 AC2가 더 빨리 올라감. <!-- F20 -->

근데 마지막 plateau는
AC2와 GRPO가 대략 비슷했음. <!-- F20 -->

평균 답 품질에서 보인 20.57% 대 18.50%를
최고 답 하나의 격차로 바꿔 읽으면 안 됨.

오른쪽 끝 두 곡선의 높이가 비슷한 걸 보셈.

![AC2와 GRPO의 best-of-16 성적 (Figure 9)](assets/posts/trust-the-critic-more/fig9_p19.webp)

---

best-of-16의 계산량도 봤지만
앞의 평균 점수 2.5배 범위도 확인해야 함.

논문이 센 건 rollout 생성의 decoding FLOPs임. <!-- F21 -->

prefill과 검증,
critic·judge 호출,
학습 forward와 backward,
통신 비용은 제외했음. <!-- F21 -->

그래서 전체 GPU 비용이 2.5배 줄었다는 뜻은 아님.

다만 main AC2 안에서
decoding FLOPs와 GPU-hours의 상관은 0.874였음. <!-- F23 -->
32개 GPU를 쓴 완전한 196단계를 비교한 값임. <!-- F23 -->

GRPO의 일부 비용 추정은 실제보다 4.01% 낮았고
AC2 곡선은 정확한 길이 기록을 썼음. <!-- F22 -->

무엇을 빼고 셌는지는 아래 문장에 박혀 있음.

![decoding FLOPs 계산에서 제외한 항목 (원문 p.25)](assets/posts/trust-the-critic-more/q_cost.webp)

---

부록에는 숨은 조건 하나가 더 적혀 있음.

main run에서 버그 때문에
정답 참고가 있어야 준비됐다고 보는 조건이
42단계부터 켜졌음. <!-- F25 -->

저자들은 정답 참고가 critic MAE를 낮췄으니
이 버그가 보고된 AC2 성능을
해친 방향일 거라고 예상함. <!-- F19 F25 -->

실제로 다시 돌려 확인한 수치는 없음.
Figure 2를 근거로 한 저자들의 예상임.

judge 출력 실패는 actor 보상 0으로 들어가고
critic target에서는 빠졌음. <!-- F26 -->
critic 값이 잘못 나오면 해당 continuation은
actor loss에서 가중치 0을 받았음. <!-- F26 -->

버그를 밝힌 원문을 그대로 보셈.

![reference-proof 준비 조건이 42단계부터 켜진 버그 (원문 p.29)](assets/posts/trust-the-critic-more/q_bug.webp)

---

그 조건보다 더 큰 한계는 반복 학습임.

문제별 준비도를 재려면
같은 학습 문제를 다시 만나야 함. <!-- F24 -->

critic의 ground truth에 가까운 값을 얻으려고
일부 답은 여전히 끝까지 생성해야 함. <!-- F6 F24 -->

데이터를 한 번만 훑고 지나가는 규모에서는
이 준비도 판정이 현실적이지 않다고
저자들이 직접 적었음. <!-- F24 -->

그래서 single-epoch 조건의 AC2는
향후 과제로 남음. <!-- F24 -->

한계 문단이 짧고 명확함.

![local readiness가 반복 데이터와 완성 rollout을 요구한다는 한계 (원문 p.12)](assets/posts/trust-the-critic-more/q_limit.webp)

---

이제 첫 질문에 답할 수 있음.

마지막 줄을 틀렸다고
앞의 모든 토큰까지 같은 벌을 줄 필요는 없었음. <!-- F1 F3 -->

저장된 풀이 중간에서 최대 10k 새 토큰씩 이어 쓰고
critic이 그 조각 끝을 비교하게 하면
완성 답 없이도 일부 actor 갱신이 가능했음. <!-- F3 F4 -->

다만 아무 critic이나 바로 믿은 건 아님.
그 문제에서 오차가 낮았고
정답 풀이를 찾은 경우부터 맡겼음. <!-- F5 -->

그 신뢰도를 재는 동안에는
같은 데이터를 반복하고
일부 답을 끝까지 써야 했음. <!-- F6 F24 -->

끝까지 안 써도 된다는 말은
모든 rollout을 없앴다는 뜻이 아님.

![끝까지 쓰는 GRPO와 준비된 조각만 평가하는 AC2 (Figure 1)](assets/posts/trust-the-critic-more/fig1_p1.webp)

---

지금 공개된 건 주장만은 아님.

2026-10-05 기준 코드 저장소가 공개돼 있고
Apache 2.0으로 배포됨. <!-- W3 -->
논문 그림은 CC BY 4.0 조건임. <!-- W4 -->

근데 공개 5일 뒤 시점이라
공식 심사 통과와 독립 재현은 확인하지 못했음. <!-- W2 W5 -->

논문 결론은 이 critic으로
beam search나 MCTS를 붙일 수도 있다고 제안함. <!-- F28 -->
그건 이번에 실험한 결과가 아님.

실제로 다음에 확인할 건
같은 문제를 반복하지 않는 single epoch에서도
준비도를 만들 수 있느냐임. <!-- F24 -->

[코드](https://github.com/WhenWen/AC2)

3줄 요약
AC2는 준비된 문제 일부를 최대 10k 조각으로 갱신했음. <!-- F3 F4 F5 -->
18.50% 돌파 FLOPs는 GRPO보다 2.5배 적었음. <!-- F9 -->
반복 학습·완성 rollout 필요. GPU 비용 비교·심사는 미확인임. <!-- F21 F24 W2 W5 -->

![논문 첫 페이지 하단의 공개 코드 링크 (원문 p.1)](assets/posts/trust-the-critic-more/code_link.webp)
