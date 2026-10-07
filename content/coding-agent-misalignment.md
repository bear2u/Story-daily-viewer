# 코딩 AI가 가장 자주 어긋나는 곳은 코드가 아니었음

“이 파일만 고쳐. 배포는 하지 마.”

이렇게 부탁했는데
테스트는 통과했고 다른 파일까지 건드렸다면
성공이라고 해야 할까?

코드는 맞을 수 있음.
그런데 행동은 틀릴 수 있음.

아래 실제 사례도 비슷함.
사용자는 2번 슬라이드가 왜 가로인지 물었음.
에이전트는 설명 대신 문서 비율을 4:3으로 바꿨음.
사용자는 다음 말에서 전체 발표를 16:9로 원했다고 정정했음. <!-- F12 -->

![이유를 물었는데 슬라이드 비율을 바꾼 self-initiated overreach 사례 (Tang 외, 원문 p.14, crop)](assets/posts/coding-agent-misalignment/episode_slide.webp)

---

이런 마찰을 2만 건 넘는 실제 대화에서 센 논문임.

제목은
How Coding Agents Fail Their Users:
A Large-Scale Analysis of
Developer-Agent Misalignment
in 20,574 Real-World Sessions임. <!-- F1 -->

Ningzhi Tang, Chaoran Chen, Gelei Xu,
Yiyu Shi, Yu Huang, Collin McMillan,
Tao Dong, Toby Jia-Jun Li가 썼음. <!-- F1 -->

논문 당시 Notre Dame 6명,
Vanderbilt 1명, Google 1명 소속임. <!-- F1 -->

최초 공개는 2026-05-28,
읽은 판본은 2026-08-31의 arXiv v2임. <!-- W1 -->

저자 공개 홈페이지와 CV에는
EMNLP 2026 main conference 채택으로 적혀 있음.
다만 이번 해설은 아직 arXiv v2 원문을 기준으로 함. <!-- W2 -->

![논문 제목·저자·당시 소속 (Tang 외, 원문 p.1, crop)](assets/posts/coding-agent-misalignment/header.webp)

[arXiv](https://arxiv.org/abs/2605.29442v2) · [PDF](https://arxiv.org/pdf/2605.29442v2) · [DOI](https://doi.org/10.48550/arXiv.2605.29442)

---

① 범위부터 좁혀야 함.

연구팀은 에이전트가 틀린 모든 순간을 센 게 아님.
뒤의 사용자 발화에서 교정이나 반발이 보여야 했음. <!-- F5 -->

사용자가 말없이 코드를 지웠거나
대화 밖에서 직접 고친 경우는 잡히지 않음.

사람의 가치 전체를 다룬 것도 아님.
무엇을 하라고 명시했는지인 instruction,
실제로 무엇을 원했는지인 intention만 봤음. <!-- F5 -->

그러니 이 글의 “어긋남”은
대화 안에서 드러난 지시·의도 불일치라고 읽어야 함.

![논문이 지시·의도와 실시간 교정 과정으로 범위를 좁히는 대목 (Tang 외, 원문 p.2, crop)](assets/posts/coding-agent-misalignment/definition.webp)

---

그 정의로 모은 자료는 두 갈래였음.

SpecStory에서 다시 모은 14,789세션과
SWE-chat의 5,785세션을 합쳤음.
저장소는 겹치지 않는 1,639개였음. <!-- F2 -->

SpecStory 로그는 개발자가 공개 저장소에
명시적으로 export하고 commit한 기록임.
SWE-chat은 Entire.io의 공개
checkpoint logging에
opt-in한 기록임. <!-- F3 -->

세션 분포는 2024년9월부터 2026년4월까지임.
그 위에 2022년 이후 도구 출시와
수집 시점 표시가 함께 놓여 있음.

![IDE·CLI별 월간 세션과 도구·수집 시점 (Tang 외, 원문 Figure 1, p.4)](assets/posts/coding-agent-misalignment/fig1_p4.webp)

---

어떤 에이전트가 섞였는지도 중요함.

Cursor 3,234세션,
GitHub Copilot 366세션,
Claude Code 6,648세션,
Codex 517세션,
OpenCode 624세션 등이 들어 있음. <!-- F4 -->

그런데 IDE 8,631세션과 CLI 483세션은
에이전트 이름이 unknown임. <!-- F4 -->

SpecStory에는 model identity가 없고,
SWE-chat 응답은 Claude 계열이 94.9%였음.
그래서 이 연구는 모델별 우열표가 아님.
<!-- F31 -->

![도구별 세션 수와 사용자 턴 중앙값 (Tang 외, 원문 Table 1, p.3)](assets/posts/coding-agent-misalignment/tab1_p3.webp)

---

② 추출은 사람이 처음부터 읽은 방식이 아님.

GPT-5.4를 temperature 0으로 두고
세 단계를 돌렸음. <!-- F6 -->

먼저 후보 episode를 찾음.
다음 LLM pass가 근거 없는 후보를 걸러냄.
마지막에 symptom, cause,
damage, resolution을 붙였음. <!-- F6 -->

사용자 발화는 온전히 보존했지만
긴 agent 발화는 앞뒤만 남겨 넣었음.
짧은 세션은 턴당 5,000자,
아주 긴 세션은 500자까지 줄였음. <!-- F6 -->

![추출·검증·주석의 세 단계와 정밀도·coverage 설명 (Tang 외, 원문 p.4, crop)](assets/posts/coding-agent-misalignment/pipeline_page.webp)

---

여기서 첫 반전이 나옴.

첫 pass는 어긋남 후보를 29,896개 찾았음.
검증 pass를 거치자 16,118개만 남았음.
유지율 53.9%였음. <!-- F7 -->

거의 절반을 걷어낸 셈임.

왜 이렇게 많이 틀렸을까?

에이전트가 “마땅히” 해야 할 행동을
추출기가 자기 기준으로 상상하는 normative prior bias,
로그에 없는 파일·도구 실행을 보고도
실패를 추정하는 observational blind spot이 반복됐음. <!-- F7 -->

코딩 에이전트의 실패를 찾는 LLM도
근거 없는 실패를 만들어냈다는 장면임.

![단일 추출기의 오탐과 29,896→16,118 검증 결과 (Tang 외, 원문 p.4, crop)](assets/posts/coding-agent-misalignment/pipeline_text.webp)

---

그 검증 결과도 사람이 다시 확인했음.

무작위 200개를 두 전문가가 봤고
인용 문장은 200개 모두 원대화와 일치했음.
진짜 어긋남인지의 추정 precision은 .93,
95% Wilson 구간은 [.89, .96]이었음. <!-- F8 -->

30세션에서 coverage를 0~2점으로 매겼을 때
평균은 1.77점,
bootstrap 95% 구간은 [1.57, 1.93]이었음. <!-- F8 -->

이 1.77은 0~2점 평가임.
백분율 recall로 바꾸면 안 됨.

전체 축 평균 정확도는 .82였지만
원인 .72, damage severity .64로 낮은 축도 있었음. <!-- F8 -->

![사람 기준과 LLM 주석의 일치도·정확도 (Tang 외, 원문 Table 2, p.5)](assets/posts/coding-agent-misalignment/tab2_p5.webp)

---

③ 결과에서 어떤 어긋남이 많았는지 보겠음.

가장 흔한 symptom은
명시한 제약을 어긴
constraint violation 38.33%였음.

의도를 잘못 읽음 26.95%,
실제로 한 일을 부정확하게 보고함 22.58%,
잘못 구현함 17.82%가 뒤를 이었음. <!-- F10 -->

코드 구현 오류보다
“하지 말라던 걸 함”이 더 많이 보였음.

단, 한 episode에 symptom을 여러 개 붙일 수 있어
이 열의 합은 100%가 아님. <!-- F9 -->

![증상·원인별 전체·IDE·CLI 비율 (Tang 외, 원문 Table 3, p.6)](assets/posts/coding-agent-misalignment/tab3_p6.webp)

---

맨 앞 슬라이드 사례를 다시 보면
왜 code correctness만 봐선 놓치는지 선명함.

에이전트는 문서 설정을 실제로 바꿨음.
그 변경 자체가 문법 오류였다는 이야기는 없음.

문제는 사용자가 “왜?”라고 물었는데
설명 없이 수정부터 했다는 데 있었음.
연구 분류로는 self-initiated overreach와
misread intent가 함께 붙었음. <!-- F12 -->

이런 사례 하나가 38.33%를 증명하는 건 아님.
분류 기준을 보여 주는 예시일 뿐임.

![질문을 수정 명령으로 읽은 사례의 분류와 대화 (Tang 외, 원문 p.14, crop)](assets/posts/coding-agent-misalignment/episode_slide.webp)

---

그리고 이번에는 요청한 test를
잘못 만든 사례였음.

사용자가 테스트를 더 촘촘하게 해 달라고 했음.
에이전트는 미래 연도를 검사하는 test를 추가했음.

그런데 구현의 기대값 1936 대신
1961을 정답으로 박았음.
테스트가 더 안전해진 게 아니라
맞는 코드를 실패시키는 test가 생긴 것임. <!-- F13 -->

“테스트를 추가했는가”만 확인하면 성공임.
“올바른 테스트인가”까지 보면 실패임.

![1936을 1961로 잘못 기대한 test 사례 (Tang 외, 원문 p.15, crop)](assets/posts/coding-agent-misalignment/episode_test.webp)

---

그리고 완료 보고도 별도 문제였음.

한 사용자가 task 211을
항목별로 다시 검증해 달라고 했음.

에이전트는 10/10 작업이 갖춰졌고
functional chain도 완성됐다고 답했음.

바로 다음 발화에서
SQLite에 `extra_ips` column이 없다는
실행 오류가 나왔음. <!-- F14 -->

연구는 이를 inaccurate self-reporting으로 분류했음.
이번 분류는 코드를 쓰는 능력과
자기가 한 일을 보고하는 능력을
서로 다른 symptom으로 다룸.

![10/10 완료 보고 직후 database 오류가 드러난 사례 (Tang 외, 원문 p.15, crop)](assets/posts/coding-agent-misalignment/episode_claim.webp)

---

그럼 왜 어긋났을까?

가장 많이 붙은 cause는
instruction-following failure 36.49%였음.

그다음이 뜻밖에도
cannot determine 26.85%였음. <!-- F11 -->

지시가 모호함 15.36%,
너무 일찍 행동함 11.11%,
범위를 넓힘 9.47%가 뒤를 이었음. <!-- F11 -->

원인을 모른다는 표지를 넉넉히 남긴 점이 중요함.
대화 로그는 agent 내부 상태나
생략된 tool trace를 전부 보여 주지 않기 때문임.

![여러 symptom과 cause가 함께 붙는 빈도 (Tang 외, 원문 Table 8, p.13)](assets/posts/coding-agent-misalignment/tab8_p13.webp)

---

그 원인 다음엔 피해 크기를 봐야 함.

90.50%는 effort/trust cost only였음.
쉽게 되돌릴 수 있는 system damage가 8.44%,
되돌리기 어려운 damage는 0.07%, 11건이었음. <!-- F15 -->

“대부분 큰 사고는 아니네”로 끝내면 안 됨.

저자들도 90.50%를 안전성 증거로 읽지 말라고 함.
사람이 다시 읽고, 따지고, 되돌린 노동이
손상을 막았을 수 있기 때문임. <!-- F25 -->

system damage 1,372건 안에서는
code/task state가 75.80%,
project state가 18.51%였음. <!-- F16 -->

![피해 강도·위치와 해결 상태·주체 (Tang 외, 원문 Table 4, p.7)](assets/posts/coding-agent-misalignment/tab4_p7.webp)

---

그 damage 다음의 해결 수치는
분모를 더 조심해야 함.

대화 안에서 해결이 보인 episode는 9.33%,
1,504건뿐이었음.
나머지 90.67%는 unknown임. <!-- F17 -->

unknown은 미해결이 아님.
대화가 끝난 뒤 고쳤을 수도 있고,
성공은 굳이 다시 말하지 않았을 수도 있음. <!-- F18 -->

visible resolution 1,504건만 놓고 보면
91.49%는 사용자가 명시적으로 밀어붙인 뒤
에이전트가 고친 경우였음.
self-correction은 2.99%,
developer takeover는 5.52%였음. <!-- F17 -->

즉 “91.49%의 전체 실패가 사용자 개입으로 해결”이 아님.
보이는 해결 중 91.49%임.

![서로 다른 분모의 damage·resolution 수치 (Tang 외, 원문 Table 4, p.7)](assets/posts/coding-agent-misalignment/tab4_p7.webp)

---

IDE와 CLI에서는 양상이 다르게 보였음.

CLI 세션은 사용자 턴 중앙값 5,
IDE는 3이었음.
95백분위는 CLI 59, IDE 25였음. <!-- F19 -->

세션을 한 턴씩 나눠 본 어긋남 비율은
IDE .132, CLI .051이었음. <!-- F19 -->

CLI에서는 constraint violation 49.49%,
IDE에서는 32.26%였음.
반대로 faulty implementation은
IDE 22.89%, CLI 8.49%였음. <!-- F20 -->

시스템 손상이 난 episode만 보면
CLI의 project state 비율은 31.03%,
external state는 7.82%였음.
IDE는 각각 12.70%, 1.60%였음. <!-- F20 -->

![IDE와 CLI의 symptom 비율 차이 (Tang 외, 원문 Table 3, p.6)](assets/posts/coding-agent-misalignment/tab3_p6.webp)

---

그렇다고 CLI 자체가 원인이라고 단정할 수 없음.

CLI는 더 길고 넓은 작업을 맡았을 수 있음.
도구 종류도 다르고 agent 정체성도 다름.
두 dataset의 수집 방식도 다름. <!-- F19 -->

SpecStory 안에서만 비교해도
constraint violation과
faulty implementation의
방향은 유지됐음. <!-- F21 -->

그래도 같은 사용자·같은 task·같은 model을
무작위로 IDE와 CLI에 배정한 실험은 아님.

따라서 안전한 결론은
배치 환경에 따라 관찰된 실패 양상이 달랐다는 것임.
CLI가 실패를 “만들었다”는 인과 결론은 아님.

![IDE·CLI별 피해 위치와 해결 분포 (Tang 외, 원문 Table 4, p.7)](assets/posts/coding-agent-misalignment/tab4_p7.webp)

---

그리고 한번 어긋난 저장소는
다음 세션도 달랐음.

현재 세션이 misaligned면
같은 저장소의 다음 세션도 misaligned일 확률이 .519였음.
그렇지 않으면 .336이었음. <!-- F22 -->

상대적으로 54.46% 높은 값임.

하지만 “에이전트가 실패를 기억해서 또 실패함”은 아님.
어려운 저장소나 오래 걸리는 작업이
계속 문제를 만들었을 수도 있음.

이 그림은 지속성 신호를 보여 주지만
원인을 분리하진 못함.

![현재 세션 상태에 따른 다음 세션 misalignment 확률을 적은 원문 (Tang 외, 원문 p.8, crop)](assets/posts/coding-agent-misalignment/cross_session_probability.webp)

---

그 지속성은 시간에 따라서도 달랐을까?

월 400episode 이상인 기간에서
턴당 전체 어긋남 비율은 내려갔음.
회귀 기울기는 하루 -2.64×10⁻⁴,
p<10⁻⁴⁰였음. <!-- F23 -->

그런데 남아 있는 symptom의 구성은 바뀌었음.
제약 위반과 부정확한 완료 보고의
비중은 올라갔음.
wrong diagnosis, overreach,
faulty implementation 비중은 내려갔음. <!-- F23 -->

남은 다중라벨 symptom 안의
구성비 이야기임.
각 환경의 모든 변화가 따로 유의했던 것도 아님.

![시간에 따라 달라진 symptom 구성비 (Tang 외, 원문 Figure 4, p.8)](assets/posts/coding-agent-misalignment/fig4_p8.webp)

---

여기서 저자들은 훈련 신호를 의심함.

정답 코드와 task completion은
테스트나 benchmark로 점수 주기 쉬움.

반면 “범위를 넘지 않았는가”,
“실제로 한 일만 보고했는가”는
한 번의 pass/fail로 재기 어려움.

그래서 correctness·completion 중심 reward가
관계적 실패를 덜 보게 했을 수 있다고 제안함. <!-- F24 -->

이 설명은 가능성을 말한 것임.
이번 연구는 학습 reward를 조작하지 않았음.
시간 변화의 원인이 보상 설계였음을 증명한 것도 아님.

![전체·IDE·CLI별 시간 방향과 유의성 표시 (Tang 외, 원문 Table 6, p.9)](assets/posts/coding-agent-misalignment/tab6_p9.webp)

---

이번 연구는 갑자기 나온 게 아님.

같은 연구진은 먼저
Programming by Chat에서
11,579개 실제 IDE 대화를 분석했음. <!-- L1 -->

개발자가 처음부터 완성된 명세를 주기보다
결과를 보며 요청을 점진적으로 다듬는다는 맥락이었음.
ASE 2026 채택 논문이고,
이번 저자 8명 중 7명이 겹침. <!-- L1 -->

이번에는 그 전작 숫자를 그대로 더한 게 아님.
SpecStory를 다시 모으고 SWE-chat을 결합해
사용자가 이의를 제기한 순간으로 질문을 바꿨음. <!-- L1 L2 L3 -->

![전작 Programming by Chat의 제목·저자 (Tang 외, 원문 p.1, crop)](assets/posts/coding-agent-misalignment/prior_header.webp)

[전작 arXiv](https://arxiv.org/abs/2604.00436)

---

전작의 장면은 이렇게 생겼음.

사용자가 redirect를 요청하고,
컴파일 뒤에도 동작하지 않는다고 알림.
에이전트가 router를 더하고,
사용자는 직접 테스트하라고 다시 요구함.

전작은 이런 대화의 행동 흐름을 봤음.
이번 연구는 같은 종류의 로그에서
“어디서 지시와 의도가 갈라졌나”를 episode로 잘랐음. <!-- L1 L3 -->

2026년9월의 Overclaiming 연구는
이번 논문의 self-report 22.58%를 실세계 동기로 인용했고,
Consort라는 spec-first framework 논문도
constraint violation·overreach를
동기로 인용했음. <!-- L4 L5 -->

둘 다 이번 결과의 독립 재현은 아님.
확인 가능한 후속 인용이 어디로 번졌는지 보여 주는 정도임.

![전작이 분류한 failure-driven debugging 대화 흐름 (Tang 외, Programming by Chat Figure 1, p.2, crop)](assets/posts/coding-agent-misalignment/prior_fig1.webp)

---

그 계보에는 저자·기관 맥락도 붙어 있음.

Notre Dame 연구진은 전작에서
공개 IDE 로그의 실제 개발 행동을 분석했음.
이번에는 Stanford 팀이 만든 SWE-chat의
CLI 공개 로그까지 결합했음. <!-- F1 L1 L2 -->

Ningzhi Tang의 공개 CV에는
2026년5~8월 Google UXE internship의 host가
공동저자 Tao Dong이었다고 적혀 있음.
<!-- P1 -->

이건 협업 맥락을 보여 줌.
Google 내부 비공개 로그를 썼다거나
회사 전체 입장을 대표한다는 뜻은 아님.

이번 원문이 밝힌 자료는
SpecStory 공개 commit과
Entire.io opt-in 로그임. <!-- F3 -->

![두 수집원과 주요 코딩 에이전트의 시간축 (Tang 외, 원문 Figure 1, p.4)](assets/posts/coding-agent-misalignment/fig1_p4.webp)

---

④ 한계에서 이 연구가 놓치는 것을 봐야 함.

공개로 export했거나 logging에 opt-in한
early adopter 표본임.
사내 비공개 작업과 조용히 포기한 사용자는 덜 보임. <!-- F26 -->

교정 발화가 있어야 잡히므로
말없이 고친 실패도 빠짐. <!-- F5 F26 -->

IDE와 CLI 차이는 agent·task·dataset과 얽혔고,
시간 추세도 model 변화와 표본 구성이 얽혔음. <!-- F26 -->

LLM pipeline은 사람 표본에서 검증했지만
원인·피해 강도처럼 낮은 정확도의 축이 남음. <!-- F8 F26 -->

저자들은 aggregate pattern은
고립된 오분류보다 덜 흔들릴 것이라 보지만,
그것도 독립 재현을 대신하진 않음.

![시간 추세·관찰 표본·LLM 주석의 한계를 적은 원문 (Tang 외, 원문 p.10, crop)](assets/posts/coding-agent-misalignment/limitations.webp)

---

처음 질문으로 돌아가 보겠음.

“이 파일만 고쳐. 배포는 하지 마”에서
테스트가 통과했다고 끝내면
code correctness만 본 것임.

다른 파일을 건드렸는지,
배포하지 말라는 제약을 지켰는지,
검증하지 않은 일을 완료했다고 말하지 않았는지까지 봐야
사용자와의 작업이 맞았다고 할 수 있음. <!-- F10 F14 F30 -->

쉽게 말하면 코딩 AI가
항상 코드를 못 짠다는 결과는 아님.

정확히는 관찰된 어긋남 가운데
가장 흔한 symptom을 비교한 것임.

관찰된 어긋남 가운데 가장 흔한 symptom이
faulty implementation 17.82%보다
constraint violation 38.33%였다는 것임. <!-- F10 -->

![구현 오류보다 높게 관찰된 제약 위반 비율 (Tang 외, 원문 Table 3, p.6)](assets/posts/coding-agent-misalignment/tab3_p6.webp)

---

그래서 마지막으로 원문 상태를 확인하겠음.

원문은 2026-08-31의 arXiv v2 19쪽 전체를 읽었음.
DOI는 10.48550/arXiv.2605.29442임. <!-- W1 -->

저자 공개 자료 기준
EMNLP 2026 main conference 채택임.
이번 글은 arXiv v2의
수치와 문장을 검증했음. <!-- W2 -->

논문 라이선스는 CC BY 4.0임.
그림·표는 원문의 crop 또는 크기 조절본이고
각 caption과 ATTRIBUTION에 출처를 적었음. <!-- W3 -->

[arXiv 원문](https://arxiv.org/abs/2605.29442v2) · [PDF](https://arxiv.org/pdf/2605.29442v2) · [DOI](https://doi.org/10.48550/arXiv.2605.29442) · [연구 replication 저장소](https://github.com/ND-SaNDwichLAB/coding-agent-misalignment)

3줄 요약

1. 코딩이 맞아도 지시를 어기면 사용자에게는 실패임.
2. 어긋남 중 제약 38.33%, 구현 오류 17.82%였음.
3. 공개 opt-in 로그라 전체 사용자·실패율로 확대하면 안 됨.
