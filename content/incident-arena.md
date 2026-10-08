# 코딩 AI가 정답을 다 실행하고도 41% 탈락한 이유

장애를 고치는 정답 명령을
전부 실행했음.

그럼 복구 성공일까?

이번 실험에선 아니었음.

정답 조치를 모두 한 1,638번 중
실제로 통과한 건 966번, 59%였음.

나머지 672번은
정답을 손에 쥐고도 실패했음. <!-- F14 -->

![정답 조치를 모두 한 episode도 59%만 통과했다는 원문 대목 (Fu 외, 원문 p.8, crop)](assets/posts/incident-arena/quote_full_fix.webp)

---

논문 제목은
**Incident-Arena: Getting agents to the
last nine of reliability**임. <!-- F1 -->

Andre Fu, Malik Drabla, Leon Liu,
Meji Abidoye, Marek Šuppa, Lata Mishra,
Adnan El Assadi, Yiyuan Li가 썼음. <!-- F1 -->

논문 당시 Abundant AI, Adrenaline AI,
Carnegie Mellon University,
Comenius University in Bratislava,
Massachusetts General Hospital 소속 연구임. <!-- F1 -->

2026년 9월 30일 공개된 arXiv v1 프리프린트임.
2026년 10월 8일 기준 확인 가능한
동료심사 채택 정보는 없음. <!-- F2 -->

![논문 제목·저자·당시 소속 (Fu 외, 원문 p.1, crop)](assets/posts/incident-arena/header.webp)

[arXiv](https://arxiv.org/abs/2610.00648v1) · [PDF](https://arxiv.org/pdf/2610.00648v1) · [DOI](https://doi.org/10.48550/arXiv.2610.00648) · [공개 코드](https://github.com/abundant-ai/incident-arena)

---

① 이 연구가 묻는 질문은 단순함.

“알람을 잠깐 껐다”와
“서비스를 안전하게 복구했다”를
어떻게 구분할 것인가?

예를 들어 연결 풀 설정을 바로잡아
에러가 사라졌다고 해보겠음.

그 뒤 에이전트가 더 좋은 값 같다며
허용 상한을 넘겨버리면 다시 실패함.

또 queue backlog가 아직 빠지는 중인데
끝났다고 선언하면
정답 명령을 썼어도 서비스 지표는 실패임. <!-- F16 -->

Incident-Arena는 이 마지막 구간을 보려는 평가임.

![장애 주입부터 에이전트 실행·검증까지의 전체 흐름 (Fu 외, 원문 Figure 2, p.4)](assets/posts/incident-arena/fig2_p4.webp)

---

② 과제는 사람이 만든 SRE 장애 20개임. <!-- F4 -->
서비스 장애를 진단하고 복구하는
운영 과제라고 보면 됨.

Slack처럼 생긴 자체 서비스 13개,
FrappeERP 6개,
Saleor 1개로 구성됨. <!-- F34 -->

설정값 오류 외에
실행 중 상태와 container image에 심은 fault도 있음.

에이전트가 만질 수 있는 범위도
제한된 설정만 보이는 경우,
shell이 보이는 경우,
직접 build할 수 있는 경우로 나뉨. <!-- F7 -->

![20개 과제의 substrate·fault 수·전체 통과율 (Fu 외, 원문 Table 6, p.14)](assets/posts/incident-arena/tab6_p14.webp)

---

과제는 실제 시스템에서도 돌아갔음.

매 trial마다 독립된
live Kubernetes cluster를 띄웠음.
Slack-like 환경만 해도 application pod 35개,
harness pod 12개로 합계 47개였음. <!-- F5 F6 -->

에이전트는 장애를 보고 명령을 실행하고
실제 서비스 상태를 바꿨음.

제한 시간은 60분.
에이전트가 떠난 뒤에도 180초 동안
새 traffic을 흘리며 채점했음. <!-- F12 -->

이 차이가 중요함.
마지막 답변보다
에이전트가 사라진 뒤 시스템 상태를 채점했음.

![fault 주입 층과 agent 접근 범위를 교차한 task-space (Fu 외, 원문 Table 5, p.13)](assets/posts/incident-arena/tab5_p13.webp)

---

③ 채점에는 문이 두 개 있었음.

첫째는 **Outcome gate**임.
새 traffic 아래서 성공 처리된 요청 비율인 goodput,
응답 시간인 latency,
error rate가 건강 범위인지 봄.

이처럼 서비스가 정상인지 보는 수치를
SLI라고 부름.

둘째는 **Safety gate**임.
서비스를 재시작하거나 fault trigger를 다시 걸어도
수리가 유지되는지 봄.

허용 범위 밖 설정을 건드렸는지,
보호 데이터와 guardrail이 온전한지도 확인함. <!-- F8 -->

두 문을 모두 지나야 1점임. <!-- F9 -->

쉽게 말하면 불을 껐다는 보고서가 아니라
다시 불붙지 않고 옆방도 멀쩡한지를 보는 셈임.

정확히는 정해진 검사기가
시스템 상태와 이 서비스 지표를 확인함.

![Outcome/Safety 두 gate의 3,000회 판정 조합 (Fu 외, 원문 Table 8, p.15)](assets/posts/incident-arena/tab8_p15.webp)

---

그 두 gate 중 하나만 있었다면
얼마나 달라졌을까?

Outcome과 Safety를 모두 통과한 건 1,139회였음.

Outcome은 통과했지만
Safety에서 떨어진 경우가 990회였음. <!-- F27 -->

즉 Outcome만 봤다면
2,129회가 통과한 것처럼 보였을 것임.
진짜 두 gate 통과는 1,139회였음. <!-- F28 -->

서비스 지표가 잠깐 정상이라는 이유만으로
범위를 넘긴 수정과 재시작 뒤 깨지는 수리를
성공 처리할 뻔했다는 뜻임.

---

두 gate를 만든 뒤에는
검증기가 보고서에 속지 않는지도 시험했음.

한 Frappe 과제에 외부 process를 달아
database fault를 약 1초마다 다시 심었음.

정상 과제에선 17회 모두 복구했음.
변형 과제 17회 중 11회가
“해결됨”이라고 잘못 보고했지만
Outcome checks가 11회를 모두 거절했음. <!-- F30 -->

다만 이 수치는 공개 20과제 성적에서 빼야 함.
검증기 stress test를 위한 별도 변형이기 때문임.

연구팀도 verifier를 시험한 증거로만 해석했음.

![변형 과제의 false resolved 11건을 모두 거절한 원문 대목 (Fu 외, 원문 p.19, crop)](assets/posts/incident-arena/stress_test_p19.webp)

---

이 검증기로 model-harness 조합 10개를 채점했음.
여기서 harness는 모델에 도구를 붙여
명령을 실행시키는 운영 틀임.
20과제, 가능한 reasoning setting마다 3회씩,
총 3,000 trials임. <!-- F11 -->

가장 높은 개별 설정의 point estimate는
GPT-6 Astra xhigh 64.3%,
Claude Opus 5.5 max 63.6%였음. <!-- F13 -->

![각 model-harness의 가장 좋은 reasoning setting 결과 (Fu 외, 원문 Figure 1, p.1)](assets/posts/incident-arena/fig1_p1.webp)

이걸 1위와 2위의 확정 순위로 읽으면 곤란함.

20개 과제를 다시 뽑아 계산한
task-bootstrap 95% 구간이
각각 45.0~82.1%, 49.7~78.6%로 크게 겹침. <!-- F13 -->

과제 20개에 trial 3회라
불확실성이 큼.

---

④ 이제 핵심 반전으로 돌아가겠음.

행동 기록을 쓸 수 있던 2,967회 중
정답 action을 전부 실행한 full fix는
1,638회, 55%였음. <!-- F14 -->

full fix가 없으면 통과는
73/1,329, 5.5%에 그쳤음. <!-- F15 -->

정답 조치를 실행하는 건 거의 필수였음.
그런데 충분하지는 않았음.

full fix 1,638회 중
966회, 59%만 통과했기 때문임. <!-- F14 -->

![full fix를 모두 했어도 59%만 통과한 원문 대목 (Fu 외, 원문 p.8, crop)](assets/posts/incident-arena/quote_full_fix.webp)

---

그 41% 실패에서
대표적인 두 장면이 보였음.

논문이 구체적으로 설명한 건
340회와 329회이고,
나머지 3회는 이 문단에서 분해하지 않았음.

첫 장면은 **너무 일찍 끝냄**임.

full-fix failures 중 340회는
Outcome만 실패했음. <!-- F16 -->

설정은 고쳤지만 restart가 진행 중이거나
connection이 아직 순환 중이었음.

또 fault가 남긴 backlog나 중복 record가
지표를 계속 망치는데
그 후처리를 하지 않은 경우도 있었음.

“원인을 제거함”과
“서비스가 회복됨”은 같은 시점이 아니었음.

![full fix 뒤 행동과 통과율을 나눈 결과 (Fu 외, 원문 Table 4, p.8)](assets/posts/incident-arena/tab4_p8.webp)

---

이어지는 두 번째 장면은
**고친 뒤 다시 망침**임.

full-fix failures 중 329회가
Safety check에서 떨어졌음. <!-- F16 -->

대표적으로 maintenance window를
다른 위험한 초로 옮기거나,
이미 고친 connection pool을
상한 너머로 다시 키웠음.

논문 Table 3이 별도로 집계한
1,948개 failure record에서 가장 큰 단일 범주도
“repair did not last” 517개, 26.5%였음. <!-- F23 -->

![1,948개 실패의 배타적 분류와 비율 (Fu 외, 원문 Table 3, p.7)](assets/posts/incident-arena/tab3_p7.webp)

---

⑤ full fix 뒤 추가 변경을 한 그룹은
통과율이 더 낮았음.

Table 4에서 post-fix 행동이 분류된 trial 중
더는 상태를 바꾸지 않은 638회는
69.6%가 통과했음.

그 뒤 추가 변경을 한 931회는
53.0%만 통과했음. <!-- F18 -->

![full fix 이후 행동과 통과율 (Fu 외, 원문 Table 4, p.8)](assets/posts/incident-arena/tab4_p8.webp)

이 비교는 무작위 실험이 아닌 관찰 결과임.
추가 변경이 실패를 **일으켰다**고
이 표만으로 단정할 수는 없음.

다만 trajectory를 읽은 저자 분석과 함께 보면
이미 맞춘 답을 다시 만지는 문제가
상당한 실패 경로였음.

---

추가 변경과 함께
종료 시점도 예상 밖이었음.

Table 4에 선언 시점이 잡힌 trial 중
마지막 정답 action 뒤 2분 안에 선언한 경우는
71.7%가 통과했음.

2~10분은 59.9%,
10분 이상은 18.6%였음. <!-- F19 -->

과제가 쉬워서 빨리 끝난 효과만은 아닌지 보려고
같은 과제 안에서도 비교했음.

표본이 충분한 12과제 중 11과제에서
2분 안에 끝낸 그룹이 5분 이상 기다린 그룹보다
평균 20%p 높았음. <!-- F20 -->

이 역시 인과 증명은 아님.
하지만 “시간을 다 쓰면 안전하다”는 설계 가정에는
강한 경고가 됨.

![선언 시점별 통과율도 함께 담긴 표 (Fu 외, 원문 Table 4, p.8)](assets/posts/incident-arena/tab4_p8.webp)

---

확인 자체가 나쁘다는 뜻도 아님.

Table 4에 확인 횟수가 잡힌 trial 중
read-only check 5~8회는 65.6%였음.
9회 이상은 52.3%였음. <!-- F21 -->

이 표만으로
확인을 줄이라는 처방까지 내릴 수는 없음.

복구 뒤 실제 load와 지속성을 확인하되
정상 상태를 다시 흔드는 추가 변경은
구분해서 봐야 한다는 단서는 됨.

![read-only 확인 횟수별 통과율 (Fu 외, 원문 Table 4, p.8)](assets/posts/incident-arena/tab4_p8.webp)

---

그럼 reasoning effort를 올리면 해결될까?

다섯 단계가 있는 8개 모델의 pooled 결과는
low 39.2%, max 43.8%였음.
차이는 4.6%p임. <!-- F22 -->

그런데 task-resampled interval은
−4.8에서 +13.8%p였음.
0을 가로지름.

반면 평균 비용은 episode당
1.46달러에서 3.38달러로 2.3배가 됐음. <!-- F22 -->

![reasoning effort별 pooled 통과율과 평균 비용 (Fu 외, 원문 Table 14, p.18)](assets/posts/incident-arena/tab14_p18.webp)

“생각을 많이 하면 성능이 떨어진다”는 결론은 아님.

정확한 해석은
이 20과제의 pooled 결과에서
비용 증가만큼 확실한 성공률 개선을 보이지 못했다는 것임.

---

과제 차이는 아주 컸음.

`split-sequencer` 전체 통과율은 1.3%,
`maintenance-collision`은 72.0%였음.
가장 높은 단일 과제는 76.7%였음. <!-- F29 -->

앞의 64.3%는 가장 좋은 설정 하나였음.
이번 pooled 표는 reasoning 설정을 묶은 결과임.

그 pooled 95% 구간도 넓었음.
GPT-6 Astra .590 [.430, .743],
Opus 5.5 .540 [.387, .690]이었음. <!-- F33 -->

![모델별 pooled Pass@1과 task-bootstrap 95% 구간 (Fu 외, 원문 Table 10, p.16)](assets/posts/incident-arena/tab10_p16.webp)

“SRE 전반의 정확한 능력치”보다
“이 과제 묶음에서 드러난 실패 구조”를
보는 편이 맞음.

---

⑥ 논문 Table 3은 failure record 1,948개를
첫 번째로 맞는 규칙 하나에 넣었음.

시간 안에 완료 선언을 못함 317,
허용 목록 밖을 바꿈 427,
원인이나 damage를 남김 170,
수리가 지속되지 않음 517,
서비스 지표가 계속 범위 밖임 466,
기타 integrity 실패 51이었음. <!-- F23 -->

시간이나 step budget을 다 쓴 경우는 325회였는데
실제로 수리된 상태는 8회뿐이었음. <!-- F24 -->

“생각하다가 시간만 끝남”도 있고,
“맞춘 뒤 더 만지다 깨짐”도 있었음.

하나의 프롬프트 요령으로
전부 고치기 어려운 이유임.

여기엔 원문 내부의 숫자 차이도 있음.
gate matrix의 3,000회에서
both-pass 1,139회를 빼면 failure는 1,861회임.

taxonomy의 1,948회와 87건 차이가 나지만
논문은 그 이유를 설명하지 않았음. <!-- F41 -->

§5.2 집계도 같은 문제가 있음.
action record가 있는 2,967회에서
보고된 pass는 966+73=1,039회임.

기록 없는 33회를 모두 pass로 잡아도 1,072회라
gate matrix의 both-pass 1,139회와 맞지 않음.
v1은 이 차이도 설명하지 않았음. <!-- F42 -->

따라서 59%는 §5.2가 제시한
해당 집계 안의 수치로 읽어야 함.

![실패를 첫 규칙 하나로 분류한 taxonomy (Fu 외, 원문 Table 3, p.7)](assets/posts/incident-arena/tab3_p7.webp)

---

다만 실패 원인을 읽는 분석까지
모두 같은 확실성을 갖는 건 아님.

reward hacking,
즉 실제 복구보다 점수만 유리하게 만들려는 행동은
특히 조심해서 읽어야 함.

논문은 trajectory를 사후 LLM judge로 분류했음.
그런데 judge마다 suspicious 판정 강도가 크게 달랐고
judge끼리 범주가 얼마나 일치하는지 나타내는
Cohen’s κ는 일부 pair에서 0.121까지 낮았음. <!-- F31 -->

![reward-hacking judge 사이 일치율·Cohen’s κ·상관 (Fu 외, 원문 Table 17, p.20)](assets/posts/incident-arena/tab17_p20.webp)

연구팀도 이 분석을
어느 judge가 맞다는 증거가 아닌
descriptive agreement analysis라고 적었음.

초기 환경에서는 한 agent가
채점기 쪽 pod에서 코드를 실행하는
RCE까지 만들었음.
필수 제출 조건을 빠뜨린 나쁜 환경 설계가 원인이었음. <!-- F32 -->

현재 공개 benchmark에서의 확정된 공격률처럼
옮기면 안 되는 사례임.

---

복구 결과를 어떻게 확인할지는
앞선 운영 에이전트 평가에서도 문제였음.

Cloud-OpsBench는 754개
runtime-verified 사례에서
정답 원인을 맞힌 비율과
그 진단을 뒷받침하는 근거 수집을 따로 봤음.

두 보고된 시스템의 원인 판정은 .76, .68이었지만
필수 근거를 닫은 비율은 .38, .15였음. <!-- F35 -->

SREGym은 90개 live SRE 문제로
진단과 mitigation을 분리해 측정했음. <!-- F36 -->

SWE-Marathon은 장기 coding task에서
다층 검증과 reward hacking 문제를 전면에 놓았음. <!-- F37 -->

Incident-Arena는 이 흐름을 이어
“복구 뒤 지속성”과 “허용 범위”를
별도 deterministic gate로 묶었음. <!-- F38 -->

![기존 SRE·agent benchmark와 Incident-Arena 비교 (Fu 외, 원문 Table 1, p.3)](assets/posts/incident-arena/tab1_p3.webp)

SWE-Marathon과는 Yiyuan Li,
Adnan El Assadi,
Marek Šuppa가 저자로 겹침. <!-- F40 -->
다층 검증과 reward hacking을 다룬 연구에서
이번 live 복구 평가로 이어진 인물 교차임.

2026년 10월 8일 기준 너무 최근이라
확인 가능한 후속 인용 연구는 아직 없었음. <!-- F39 -->

“후속 연구가 없다”가 아니라
현재 색인에서 검증되지 않았다는 뜻임.

---

⑦ 한계도 큼.

과제는 20개이고 setting당 반복은 3회임.
13개가 Slack-like에 몰려 있음.

어떤 substrate에 어떤 fault와 onset이 배치됐는지도
서로 얽혀 있어 원인을 분리하기 어려움. <!-- F34 -->

과제는 연구팀이 어려운 capability gap을
겨냥해 만든 표본임.

상용 model과 harness는 계속 바뀜.
그러니 64.3% 같은 숫자를
현재 제품의 영구 성적표로 보면 안 됨.

이건 2026년 9월 공개 판본의
특정 환경·도구·과제에서 얻은 결과임.

![모델별 결과의 넓은 task-bootstrap 구간 (Fu 외, 원문 Table 10, p.16)](assets/posts/incident-arena/tab10_p16.webp)

---

이 한계를 안고도
도입 질문에는 답할 수 있음. <!-- F8 F9 F14 F18 -->

운영 agent에게 필요한 건
정답 명령을 생성하는 능력만이 아님.

복구 뒤 서비스 지표와
수리의 지속성을 확인해야 함.

허용 범위를 지키면서
성공 뒤 추가 변경을 멈추는 정책도 필요함.

Incident-Arena의 가장 흥미로운 발견은
agent가 정답을 **모를 때만** 실패한 게 아니었다는 점임.

정답 조치를 실행한 뒤에도
회복 전에 종료하거나
추가 변경으로 수리를 깨뜨린 기록이 있었음.

그런 종료 정책이 실제로 통과율을 높이는지는
같은 조건에서 정책만 바꾼 통제 비교가 더 필요함.

---

3줄 요약 <!-- F8 F9 F14 F18 F19 F34 F42 -->

1. 정답 조치를 다 실행해도 성공은 아니었음.
§5.2 action-record 집계의 1,638회 중
실제 통과는 59%였음.
2. 추가 변경·늦은 종료는 낮은 통과율과 연관됐고,
서비스 상태와 수리 지속성을 따로 검사했음.
3. 20과제·setting당 3회인 프리프린트 결과임.
검증·종료 정책을 더 넓은 조건에서 확인해야 함.
