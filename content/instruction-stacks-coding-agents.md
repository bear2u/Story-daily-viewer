# 사용자 한 줄이 0.03%였던 코딩 에이전트 요청

논문: *Hidden in Plain Sight:
an Empirical Study about
The Instruction Stacks of Coding Agents* <!-- F1 -->
저자: Felipe de Sant'Anna Paixão,
Dhyego Tavares, Eduardo Almeida,
Iftekhar Ahmed <!-- F1 -->
공개: arXiv:2610.37332v1, 2026년 10월 27일 <!-- F1 W1 -->
상태: cs.SE 프리프린트 <!-- W1 -->
확인 가능한 동료평가·게재 정보 없음 <!-- W1 -->

제목과 저자부터 보셈

![Hidden in Plain Sight 제목과 저자 (원문 p.1)](assets/posts/instruction-stacks-coding-agents/p1_header.webp)

---

사용자 한 줄을 보냈을 때
모델은 정말 그 한 줄만 읽을까

논문 실험에서 사용자가 입력한 건
한 문장이었음

`I AM THE USER PROMPT.`

21자짜리 문장 하나였음 <!-- F19 -->

Claude Code 2.1.243이
모델에 보낸 첫 요청은 74,078자였음 <!-- F5 -->

사용자 문장은 그중 0.03%였음 <!-- F5 -->

아래 그림 가운데 가느다란 한 줄이
사용자가 실제로 쓴 부분임

![Claude Code 첫 요청의 구성 (Figure 1)](assets/posts/instruction-stacks-coding-agents/fig1_full.webp)

---

그 나머지에서 지시 역할을 하는 두 덩어리를
instruction stack이라 부름 <!-- F4 -->

쉽게 말하면
사용자가 편지를 한 줄 썼는데
에이전트가 업무 지침과 도구 설명을 붙여
모델에게 건네는 구조임

정확히는 두 덩어리임

사용자 프롬프트를 뺀 instruction text와
구조화된 tool definitions임 <!-- F4 -->

모델명과 생성 설정,
JSON 문법 자체는 stack에서 뺌 <!-- F4 -->

원문은 이 글을 12가지 기능으로 나눴음

![instruction text 분류 기준 (Table II)](assets/posts/instruction-stacks-coding-agents/table2_codebook.webp)

---

이 Claude 예시에서는
system prompt만 보면
stack 대부분을 놓침

Claude 예시의 top-level system field는
9,517자였음 <!-- F6 -->

그 뒤에 system message가 또 붙고
도구 정의 20개가 57,346자를 차지함 <!-- F6 -->

도구 설명만 instruction text의
2.6배 길이였음 <!-- F17 -->

그래서 system prompt만 공개해서는
모델 입력 전체를 재현할 수 없음

---

이런 차이는 전작에서
이미 비용으로 드러났음

2026년 7월 나온 Qwen Code 연구는
같은 모델을 두고
실행과 도구 사용을 맡는 agent 프로그램의
릴리스만 바꿨음 <!-- L1 L2 -->

35개 릴리스를
SWE-bench Verified 50개 과제로 비교함 <!-- L2 -->

해결률에는 유의한 상승 추세가 없었음

근데 과제당 평균 토큰은
초기 9개 릴리스 약 391K에서
최신 버전 약 668K로 늘었음 <!-- L3 -->

70% 넘게 증가한 값임 <!-- L3 -->

이번 논문이 확인한 건
그때 모델 앞에 실제로 붙은 글임

---

그래서 이번 팀은 결과 대신
첫 요청을 직접 잡았음

Claude Code, Codex, Gemini CLI,
Qwen Code, OpenCode를 고름 <!-- F3 -->

2026년 8월 25일 이전
npm에 공개된 정식 릴리스
1,911개를 시도함 <!-- F7 -->

새 홈과 빈 작업 폴더를 갖춘
linux/amd64 컨테이너에서 하나씩 실행함 <!-- F10 -->

고정 프롬프트를 넣고
주 모델로 간 첫 요청 1,886개를 건짐 <!-- F7 F8 -->

전체 흐름은 위에서 아래가 아니라
왼쪽에서 오른쪽으로 이어짐

![요청 수집부터 변경 이유 분석까지 (Figure 2)](assets/posts/instruction-stacks-coding-agents/fig2_p5.webp)

---

1,886개 요청의 instruction text를
주로 문장 단위 349,404개로 나눔 <!-- F12 -->

두 사람이 66개 요청의
12,862개 segment를 따로 분류함 <!-- F13 -->

사람끼리 Cohen's κ는 0.75였음 <!-- F13 -->

우연히 같은 답을 고른 경우를 뺀
분류 일치도임

둘의 판정 차이는 세 번째 저자가 조정해
기준표로 만들었음 <!-- F13 -->

자동 분류에 쓴 GLM 5.3 Flash는
그 기준표와
93.4%, κ 0.92로 일치함 <!-- F13 -->

commit·PR 추적에서 검증한 link
798개 중 795개가 맞았음 <!-- F14 -->

표 가운데가 agent별 릴리스 수임

![다섯 에이전트의 릴리스와 요청 수 (Table I)](assets/posts/instruction-stacks-coding-agents/table1_agents.webp)

---

이렇게 검증한 최신 첫 요청에서
가장 큰 덩어리는 도구 정의였음

최신 릴리스의 request 전체 중
Claude Code는 77.4%,
Qwen Code는 72.3%,
OpenCode는 63.2%가 도구 정의였음 <!-- F16 -->

Codex는 40.5%,
Gemini CLI는 18.9%였음 <!-- F16 -->

다섯 agent가 똑같다는 결과가 아님

세 agent에서는
도구 정의가 request 절반을 넘었다는 측정임

맨 아래 진한 줄이 최신 릴리스 값임

![instruction text와 도구 정의의 비중 (Figure 3)](assets/posts/instruction-stacks-coding-agents/fig3_p7.webp)

---

맨 앞의 0.03%는
다섯 agent에서도 비슷했음

각 agent의 최신 릴리스는
29,387자에서 124,873자였음 <!-- F19 -->

21자 고정 프롬프트 비중은
0.02%에서 0.07%였음 <!-- F19 -->

모두 0.1% 미만임 <!-- F18 -->

근데 여기서 기억할 게 있음

사용자가 긴 요구사항을 쓴 실전 비율이 아님
논문이 일부러 같은 21자를 넣은 비교임 <!-- F8 F18 -->

굵은 두 문단에 조건과 결과가 같이 적혀 있음

![최신 첫 요청의 사용자 프롬프트 비중 (원문 5.1절)](assets/posts/instruction-stacks-coding-agents/p7_first_request_results.webp)

---

같은 첫 요청에서
role 이름조차 작성자를 보장하지 않았음

여기서 role은 요청 JSON에 붙는
발화자 칸임

Gemini CLI와 Qwen Code는
user-role message에도 agent text를 넣었음 <!-- F20 -->

둘은 때때로 assistant message에
`Got it. Thanks for the context!`도 넣었음 <!-- F20 -->

실제 모델이 말한 문장이 아니었음

user role만 모아 사용자 지침이라 부르면
에이전트가 쓴 글을 사용자에게 돌릴 수 있음

---

이 첫 요청들을 릴리스 순서로 놓으면
같은 제품 안에서도
stack 크기가 달라졌음

최초 릴리스에서 최신 릴리스까지
Codex는 7.8배,
Qwen Code는 4.5배,
Claude Code는 2.3배가 됐음 <!-- F21 -->

Gemini CLI는 1.4배였고
OpenCode는 약 4분의 1 줄었음 <!-- F21 -->

다만 Codex 구간에는
TypeScript에서 Rust로의 재작성과
기본 모델 변경도 함께 있음 <!-- F11 F21 -->

stack 증가의 원인을
한 가지로 찍은 실험은 아님

위쪽 면적 그래프가 request 크기임

![릴리스별 request 크기와 edit size (Figure 4)](assets/posts/instruction-stacks-coding-agents/fig4_p9.webp)

---

그 릴리스별 변화는
몇몇 버전에 몰렸음

버전 번호처럼 계속 바뀌는 값을 가린
1,867개 전환 중
segment나 tool이 바뀐 건 544개였음 <!-- F22 -->

29%임 <!-- F22 -->

각 agent의 누적 문자 변경 절반이
5개에서 10개 전환에 몰렸음 <!-- F23 -->

segment 3,108개를 넣고
2,751개를 빼는 동안
부분 수정은 537개였음 <!-- F24 -->

조금씩 고치기보다
덩어리를 통째로 넣고 뺀 흔적이 많았음

파란색이 segment·tool이 바뀐 릴리스임

![실제 stack 내용이 바뀐 릴리스 비중 (Figure 5)](assets/posts/instruction-stacks-coding-agents/fig5_p9.webp)

---

집중된 릴리스 변화 중에는
하루짜리도 있었음

Claude Code 2.1.69가
도구 정의 18개를 ToolSearch 하나로 바꿈 <!-- F25 -->

request가 77,601자에서
20,380자로 줄었음 <!-- F25 -->

필요할 때 도구를 찾게 한 구조임

근데 2.1.70에서
도구 정의를 다시 복원함 <!-- F25 -->

바로 다음 날이었음 <!-- F25 -->

같은 Claude Code라는 이름만으로는
그날 모델이 본 도구 목록을 알 수 없음

왼쪽 단의 Large transitions를 보셈

![집중된 릴리스 변화와 ToolSearch 사례 (원문 5.2절)](assets/posts/instruction-stacks-coding-agents/p8_evolution.webp)

---

릴리스가 바꾼 건
도구 목록뿐이 아니었음

commit 저자 표시에도 손댐

Claude Code 요청 493개 중 492개는
Bash 설명에 commit trailer를 넣으라 했음 <!-- F26 -->

`Co-Authored-By: Claude`

OpenCode는 907개 중 312개에
비슷한 지침이 있었음 <!-- F26 -->

주석 정책도 다섯 번 변함 <!-- F27 -->

한때는 요청받지 않으면
어떤 주석도 넣지 말라고 했음 <!-- F27 -->

나중에는 주변 코드의
주석 밀도를 맞추라고 바뀜 <!-- F27 -->

같은 모델이 낸 코드라도
릴리스 지침이 흔적을 바꿀 수 있음

---

그럼 왜 릴리스 변화를 줬는지
기록돼 있었나

네 오픈소스 agent에서
PR 하나나 단독 commit 하나를
변경 묶음으로 세었음

모두 496개였음 <!-- F28 -->

440개 pull request와
56개 단독 commit이었음 <!-- F28 -->

어떤 이유든 적은 unit은 444개,
90%였음 <!-- F29 -->

근데 stack 자체를 왜 바꿨는지
직접 설명한 건 236개였음 <!-- F29 -->

48%임 <!-- F29 -->

208개는 함께 바뀐 기능이나 코드만 설명함 <!-- F29 -->

윗그래프의 파란색만
stack 변경 이유를 직접 말한 경우임

![stack 변경 이유와 명시 동기 (Figure 6)](assets/posts/instruction-stacks-coding-agents/fig6_p9.webp)

---

이유를 적은 444개 unit 중
safety and security를 든 건 13개였음 <!-- F31 -->

되돌리기 어려운 작업과 권한을 다루는
execution policy 변화도 따로 봤음

이 text를 바꾸고 이유를 적은 24개 중
안전을 든 건 2개,
model behavior를 든 건 13개였음 <!-- F31 -->

안전 관련 지침이 안 바뀌었다는 뜻은 아님

개발 기록에서 안전이
명시 이유로 드물었다는 측정임

오른쪽 단 맨 아래 안전 막대를 보셈

![변경 이유와 안전 동기의 빈도 (원문 5.3절)](assets/posts/instruction-stacks-coding-agents/p8_motivations.webp)

---

변경 이유 기록과 별개로
다섯 stack을 서로 비교한 결과도 있음

agent끼리 문장은 달랐음

agent 쌍 10개 중 6개는
30자 이상 같은 segment가 한 번도 없었음 <!-- F32 -->

2026년 8월에는
각 agent segment의 95% 이상이
다른 agent에 나타나지 않았음 <!-- F32 -->

근데 쓸 수 있는 기능 목록인
capability catalog와
하위 agent에 일을 나누는
subagent delegation은
다섯 agent 모두에 들어옴 <!-- F33 -->

같은 문구로 수렴하지 않았어도
비슷한 기능이 각 stack에 나타남

이 측정만으로는
효과나 호환성까지 알 수 없음 <!-- F34 -->

위는 문구 공유, 아래는 기능 비중임

![문구 공유 감소와 기능 비중의 변화 (Figure 7)](assets/posts/instruction-stacks-coding-agents/fig7_p10.webp)

---

이 agent별 차이를 재현할 때
48% 기록 공백이 바로 걸림

연구자가 논문에
`Claude Code + 모델명`만 적었다고 해보겠음

어느 릴리스인지 없으면
도구 18개를 직접 받은 날인지
ToolSearch 하나만 받은 날인지 모름 <!-- F25 -->

실제로 잡아 둔 stack 원문도 없으면
주석·저자 표시 지침도 재현하기 어려움 <!-- F26 F27 -->

저자들은 그래서
agent release와 model 설정,
저장소 지침과 켜 둔 기능을
함께 기록하라고 권고함 <!-- F35 -->

가능하면 실제로 잡아 둔 stack도
보관하라고 적었음 <!-- F35 -->

원문 결론에도 이 권고가 적혀 있음

![agent release와 captured stack 기록 권고 (원문 Discussion·Conclusion)](assets/posts/instruction-stacks-coding-agents/p10_conclusion.webp)

---

내가 쓴 한 줄만
모델이 읽은 게 아님

해당 릴리스가 조립한 instruction text와
도구 정의도 첫 요청에 함께 들어갔음 <!-- F4 F5 -->

다만 0.03%를
모든 실전 대화의 비율로 쓰면 안 됨

빈 작업 폴더,
사용자 상호작용 없음,
21자 고정 프롬프트,
주 모델의 첫 요청만 본 결과임 <!-- F9 F10 F36 -->

2026년 8월 25일 뒤 릴리스도
이번 표본 밖임 <!-- F37 -->

오른쪽 위 한계 문단에 범위가 적혀 있음

![첫 요청 연구의 범위와 한계 (원문 Threats to Validity)](assets/posts/instruction-stacks-coding-agents/p10_limits.webp)

---

논문 기준 앞의 세 저자는 UFBA,
마지막 저자 Iftekhar Ahmed는 UCI 소속임 <!-- F2 P1 -->

UFBA TRC와 UCI 저자 프로필에는
소프트웨어공학·AI·테스팅 연구가 적혀 있음 <!-- P2 P3 -->

2026년 10월 30일 기준
직접 후속 연구는 아직 확인하지 못했음 <!-- L5 -->

논문이 제안한 다음 검증은 구체적임

모델·과제·조건을 고정하고
captured stack만 바꾸는 실험을 제안함 <!-- F39 -->

3줄 요약

1. 첫 요청 대부분은 agent text와 도구 정의였음 <!-- F4 F18 -->
2. 직접 이유를 적은 변경 묶음은 48%였음 <!-- F22 F29 -->
3. stack과 성능의 인과는 아직 시험 전임 <!-- F36 F38 -->

내용 추가하면

[arXiv 원문](https://arxiv.org/abs/2610.37332) <!-- W1 -->

[공개 PDF](https://arxiv.org/pdf/2610.37332) <!-- W1 -->

[직접 선행 연구](https://arxiv.org/abs/2607.03691) <!-- W3 -->

[UCI 저자 프로필](https://ics.uci.edu/?people=iftekhar-ahmed) <!-- P3 -->

[UFBA 연구센터](https://trc.ufba.br/) <!-- P2 -->

[그림 라이선스 CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) <!-- W2 -->
