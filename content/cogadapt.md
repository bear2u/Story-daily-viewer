# 사람이 코드를 읽은 뇌파로 AI가 고칠 층을 골라봤더니

사람이 코드 한 줄에서 잠깐 멈춘 흔적이
AI에게도 고칠 곳을 알려줄 수 있음?

이번 연구는 실제로 해봤음.

Qwen-LiveCodeBench 조건에선
48개 블록 가운데 과제마다 평균 6.25개만
gradient를 받게 했음. <!-- F19 F34 -->

그런데 첫 생성 답안이 test를 통과한 비율은
일반 fine-tuning 18.86%에서
29.71%로 올랐음. <!-- F24 F30 -->

논문이 보고한 증가폭은 10.86%p임. <!-- F5 -->

![사람이 어려워한 코드와 모델이 강하게 반응한 영역으로 일부 층만 고르는 발상 (Zhang 외, Figure 1)](assets/posts/cogadapt/fig1_p2.webp)

---

그 숫자를 낸 논문은
**CogAdapt: Cognition-informed Sparse
Adaptation of Code LLMs**임. <!-- F1 -->

Yueke Zhang, Zihan Fang,
Kevin Leach, Yu Huang이 썼고
네 명 모두 논문 당시
Vanderbilt University 소속임. <!-- F1 P1 -->

2026년 10월 5일 공개된
arXiv v1 프리프린트임. <!-- F2 W1 -->

2026년 10월 9일 기준
확인되는 동료평가 채택 정보는 없음. <!-- W5 -->

![논문 제목·저자·당시 소속 (Zhang 외, 원문 p.1)](assets/posts/cogadapt/p1_header.webp)

[arXiv](https://arxiv.org/abs/2610.07446v1) · [PDF](https://arxiv.org/pdf/2610.07446v1) · [arXiv DOI](https://doi.org/10.48550/arXiv.2610.07446)

---

그 논문이 사람의 코드 읽기를
처음 잰 건 아님.

2022년 ESEC/FSE 연구가
37명에게 Java 코드 조각을 최대 32개씩 읽히고
EEG와 눈 움직임을 함께 기록했음. <!-- L1 -->

그 연구는 일을 잘 푼 참가자일수록
더 짧게 보고 덜 되돌아가며
인지 부하도 약간 낮았다고 보고했음.
다만 상관은 rho -0.09로 약했음. <!-- L2 -->

2026년 ACL에 나온 EyeMulator는
사람 시선을 token별 학습 가중치로 바꿨음. <!-- L3 -->

이번 네 저자 중 세 명이
그 EyeMulator에도 참여했음. <!-- L5 P2 -->

CogAdapt는 사람 자료를
어느 블록을 고칠지 정하는 데도 썼음.

전작 그림에선 시선 자료가
코드를 나눈 작은 단위인 token과
코드 문법 구조인 AST에 매핑되는 곳을 보셈.

![사람 시선을 token별 학습 가중치로 옮긴 EyeMulator (Yifan Zhang 외, ACL 2026 Figure 1)](assets/posts/cogadapt/prior_eyemulator_fig1.webp)

---

2022년 원자료에서 가져온 장면이
짧은 이진 탐색 코드임.

개발자는 `if (high < low)`를 지나갔다가
다시 그 줄로 눈을 돌렸음.

논문은 탐색을 멈출 조건과
바로 아래 `return -1`을 함께 이해하는
부담이 드러난 장면으로 설명했음. <!-- F7 -->

같은 부분에서 4~8Hz EEG theta가 강해지고
MoE 모델의 expert 선택 확신은 커졌음.
내부 표현 변화와 expert 기여도
더 컸다고 함. <!-- F7 F10 -->

그림에선 노랑과 보라가
같은 boundary check에서 솟는지 보셈.

![이진 탐색 종료 조건에서 사람과 모델 반응이 함께 커진 예시 (Zhang 외, Figure 2)](assets/posts/cogadapt/fig2_p4.webp)

---

장면 하나로는 부족하니
연구진은 81개 의미 영역을 묶어 비교했음. <!-- F21 -->

control flow, call과 return,
array expression, 나머지 연산으로 나눴음.

표시된 영역의 75.0~83.3%에서
사람 신호와 모델 신호의 상관이
0보다 컸음. <!-- F4 -->

같은 방향으로 움직인 영역은 많았지만
얼마나 비슷하게 움직였는지는 약했음.

하지만 비율만 보면 세 보이기 쉬움.

median Spearman rho는
0.183에서 0.240 사이였음. <!-- F27 -->

EEG-Qwen 중앙값의 95% 재표집 구간은
0.000에서 0.217까지였음. <!-- F27 -->

![네 코드 범주에서 사람 신호와 두 모델 반응의 상관 분포 (Zhang 외, Figure 4)](assets/posts/cogadapt/fig4_p14.webp)

---

그 상관은 층마다 달랐음.

아래 그림의 빨강은 양의 상관,
파랑은 음의 상관임.

Qwen에서는 중간 이후 층의
hidden-state shift가 주로 붉었음.

GLM에선 그 신호가 대체로 파랬고
expert-choice confidence와 MoE write가
더 붉게 나타났음. <!-- F28 -->

사람 반응과 맞는 모델 내부 신호가
아키텍처마다 달랐다는 뜻임.

![모델 깊이와 사람 읽기 시간에 따른 EEG·모델 상관 지도 (Zhang 외, Figure 5)](assets/posts/cogadapt/fig5_p15.webp)

Qwen 41번 블록은 보기 좋은 예지만
연구진도 유일한 뇌 정렬 층이라고
해석하지 않았음. <!-- F29 -->

![Qwen 41번 블록의 hidden-state 변화·읽기 시간·EEG theta 관계 (Zhang 외, Figure 6)](assets/posts/cogadapt/fig6_p15.webp)

---

이 층별 상관과 사람 자료를
새 Python 과제에도 쓰게 요약했음.

쉽게 말하면
사람이 많이 본 코드에 형광펜을 치고
과제마다 고칠 층을 따로 고른 것임.

이전에 관찰한 경향을
새 과제 학습의 기준으로 가져왔고
여기서는 그 기준을 prior라고 부름.

정확히는 prior가 세 종류임.

Java 프로그램의 여덟 구조 특징으로
EEG theta를 예측하는 프로그램 prior,
문법 역할과 AST 문맥으로 옮긴 token prior,
모델 깊이별 상관을 요약한 depth prior임. <!-- F12 F13 F14 -->

새 Python 과제에는 실제 EEG가 없음.
Java에서 배운 구조적 경향만 가져옴. <!-- F13 -->

![사람 자료를 재사용 가능한 prior로 바꾸고 과제별 블록을 고르는 전체 과정 (Zhang 외, Figure 3)](assets/posts/cogadapt/fig3_p6.webp)

---

여기부터는 한 파트만 전문가용임.
건너뛰어도 뒤 결과는 읽힘.

학습 목표 자체는 평범한
다음 token 예측임. <!-- F16 -->

프로그램 prior는 예시 하나의 손실을 키우고
token prior는 정답 코드 안에서
어느 token 손실을 더 볼지 정함.

depth prior와 frozen model 반응은
이 과제에서 업데이트할 블록을 순위화함. <!-- F15 F17 -->

전체 backbone은 forward를 돌지만
고른 블록의 attention adapter와 router만
gradient를 받음. <!-- F17 -->

추론할 때는 EEG도 시선도
정답 코드도 필요 없음. <!-- F18 -->

---

이 방법의 시험 규모도 봐야 함.

사람 쪽은 37명, Java 32개,
의미 영역 81개였음. <!-- F9 F21 -->

모델은 Qwen3-Coder-30B-A3B-Instruct와
GLM-4.7-Flash 두 개임.

Qwen은 48블록에서
token마다 expert 128개 중 8개,
GLM은 47블록에서
routed expert 64개 중 4개를 고름. <!-- F19 F20 -->

학습·평가는 LiveCodeBench와
BigCodeBench를 사용했고
기록된 장비는 RTX A6000 두 장임. <!-- F22 F23 F26 -->

---

Qwen 결과부터 보면 차이가 큼.

Qwen의 LiveCodeBench pass@1은
정규 fine-tuning 18.86,
CogAdapt 29.71이었음. <!-- F30 -->

GLM은 17.71에서 24.00으로 올랐음. <!-- F30 -->

BigCodeBench 차이는 더 작았음.

Qwen은 36.36에서 37.73,
GLM은 28.64에서 31.82였음. <!-- F31 -->

논문이 평가한 네 조합에서는
모두 CogAdapt가 높거나 공동 최고였음.

![두 모델·두 벤치마크의 baseline, ablation, CogAdapt pass@1 (Zhang 외, Table 1)](assets/posts/cogadapt/tab1_p17.webp)

---

사람 자료가 도움 됐는지는
구성요소를 하나씩 뺀 비교에서 확인했음.

사람 신호를 그대로 두고
모든 블록을 고친 All-Block도
네 조합 모두 full method보다 낮았음.

사람 신호를 빼고 모델 반응만 쓴
Model-Only의 LiveCodeBench는
Qwen 24.00, GLM 22.29였음. <!-- F32 -->

full method는 각각
29.71과 24.00이었음. <!-- F30 -->

다만 모든 구성요소가 늘 이긴 건 아님.

Qwen BigCodeBench에선
시선 가중치를 뺀 No-Gaze도
같은 37.73을 냈음. <!-- F33 -->

---

처음의 약 6개 블록으로 돌아가면
숫자 두 종류가 갈라짐.

작업당 평균 6.09~6.55블록만 고르면서
gradient를 받을 수 있는 parameter는
86.21~87.21% 줄었음. <!-- F6 F34 -->

그런데 학습시간 감소는
2.53~5.87%였고
추정 GPU 에너지는 2.12~4.55% 줄었음. <!-- F35 -->

![고른 블록 수·gradient 대상 parameter·시간·GPU 에너지 비교 (Zhang 외, Table 2)](assets/posts/cogadapt/tab2_p17.webp)

전체 backbone이 forward pass를
계속 돌기 때문임. <!-- F17 F36 -->

87%와 6% 미만.
같은 절약이 아니었음.

---

이 방법은 계산 자체를 건너뛴 게 아니라
업데이트 허용 범위만 줄였음. <!-- F36 -->

저자들도 다음에는 block이나 adapter를
조건부로 실행하거나 일찍 끝내야
더 큰 절약으로 이어질 수 있다고 적었음. <!-- F38 -->

![gradient sparsity와 실제 계산 절약이 다르다고 적은 한계 문단 (Zhang 외, 원문 §7)](assets/posts/cogadapt/q_limitation.webp)

일반화 범위도 아직 좁음.
사람 자료는 Java 32개에서 왔고
평가는 모델 두 개와 벤치마크 두 개임. <!-- F9 F19 F20 F22 F23 -->

각 조건은 생성 전체를 한 번만 평가했음.

층 여섯 개를 무작위로 고른 비교만
고정 조합 세 개를 반복해
표준편차를 보고했음. <!-- F24 F25 -->

10.86%p를 모집단 효과로 확정하기보다
후속 반복 실험이 필요한 v1 결과로 보는 게 맞음.

같은 데이터로 독립 반복하고
다른 크기·언어에서도 재현되는지 봐야 함.

conditional execution을 붙였을 때
실제 계산량이 얼마나 줄지도 남아 있음. <!-- F38 -->

---

그 v1 결과만 놓고 첫 질문에 답하면
사람이 코드에서 멈춘 흔적은
이번 설정에선 AI가 어디를 더 학습할지
고르는 prior로 쓸 수 있었음. <!-- F30 F32 -->

그렇다고 사람 뇌와 모델이
같은 방식으로 코드를 이해한다는 뜻은 아님.
논문도 그 주장을 명시적으로 피했음. <!-- F8 -->

이번 논문은 2022년 EEG·시선 원자료를 재사용했고
EyeMulator·ScanCoder의 token 가중치 방법도 이어
과제별 블록 선택까지 확장했음. <!-- L1 L3 L4 -->

2026년 10월 8일 Semantic Scholar 기준
확인 가능한 후속 인용은 0건이었음. <!-- L7 -->

PDF의 학회명과 ACM DOI도 자리표시자라
채택본처럼 읽으면 안 됨. <!-- F3 W5 -->

**3줄 요약**

사람 EEG prior는 task 가중치·블록 수를 정했음.
시선 prior는 token 가중치를 정했음.
depth prior와 모델 반응이 블록을 골랐음. <!-- F12 F14 F15 -->

CogAdapt는 과제마다 약 6개 블록만 고쳐
논문 보고값 기준 최대 10.86%p 높였음. <!-- F5 F34 -->

parameter 대상은 86% 넘게 줄었지만
시간·추정 에너지는 최대 5.87%와 4.55% 줄었음. <!-- F6 F35 -->

---

그 답에 쓴 원문 그림은 arXiv가 표시한
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 조건으로 사용했음. <!-- W2 -->

그림 아래 설명에
논문과 Figure·Table 번호를 적었음.

원문 계보를 직접 볼 링크는 아래 셋임.

전작: [NoviceVsExpert](https://doi.org/10.1145/3540250.3549084) · [EyeMulator](https://aclanthology.org/2026.acl-long.1158/) · [ScanCoder](https://doi.org/10.1145/3808150)

