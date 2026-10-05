# 코딩 AI는 모델 바깥에서 뭘 하고 있을까

버그 하나 고쳐 달라고 했음.
예를 들어 빈 입력에서 함수가 터지는 상황임.

모델이 수정할 코드를 써 줄 수는 있음.
근데 어느 파일을 열어야 할까?
수정은 누가 적용하고, 테스트는 언제 돌릴까?
모델이 다 고쳤다고 말하면 끝내도 될까?

이 요청을 실제 작업으로 잇는
모델 바깥의 코드가 따로 있음.
논문은 그 런타임을 하네스라고 부름. <!-- F6 -->

원문의 정의에서도 모델과 하네스를 나눔.

![모델과 세상을 이어 주는 하네스의 정의 (Barbaste 외, 원문 p.3)](assets/posts/harness-engineering/q_definition.webp)

---

그 바깥을 소스코드로 들여다본 논문임.

제목은 Harness Engineering:
Anatomy, Architecture,
and Evolution of Coding Agents
A Source-Code Study of Eleven Systems임. <!-- F42 -->
Paul Barbaste, Tristan Darrigol,
Germain Vu, Tom Wiltberger가 썼음. <!-- P1 -->
논문 당시 Barbaste는 Inclusive Brains와
Wavestone AI Lab 소속이고,
나머지 세 명은 Wavestone AI Lab임. <!-- P1 -->

공식 arXiv 최초 공개일은 2026-07-15.
읽은 건 v1 원문 83쪽 전체임. <!-- W1 F41 -->
2026-10-06 확인 기준 프리프린트임.
공식 심사 통과나 게재처는 확인 못했음. <!-- W2 -->

아래 제목부에 저자와 당시 소속이 있음.

![Harness Engineering 제목·저자·소속 (원문 p.1)](assets/posts/harness-engineering/header.webp)

[arXiv 원문](https://arxiv.org/abs/2609.00006v1) · [PDF](https://arxiv.org/pdf/2609.00006v1) · [DOI](https://doi.org/10.48550/arXiv.2609.00006)

---

그 논문의 비교표를 보기 전에
표본부터 봐야 함.

Claude Code, Codex CLI, Gemini CLI,
Mistral Vibe, OpenHands, Aider,
Mini-SWE-Agent, Hermes, Pi,
OpenCode, OpenClaw의 11개임. <!-- F2 -->

엄밀히는 코딩 하네스 10개와
개인 비서 연결 허브인 OpenClaw 대조점임.
Omnigent는 이 분모 밖의 별도 대조 사례임. <!-- F3 F4 -->

설계 철학과 성숙도 등을 보고 골랐고
성능 순위를 매긴 실험은 아님. <!-- F1 F2 -->
주로 2026년 7월 버전을 고정해 읽었음.
Claude Code는 3월 유통 소스가 예외임. <!-- F5 -->

표의 버전 칸이 관찰 시점을 고정해 줌.

![조사한 11개 시스템의 소스 버전과 날짜 (원문 Table 3)](assets/posts/harness-engineering/tab3_p10.webp)

---

모델 바깥 코드는 갑자기 생긴 건 아님.

2022-10-06 공개된 ReAct는
추론과 행동을 번갈아 만드는 방법을 보였음.
2023년 ICLR에 실린 연구임. <!-- L1 -->

쉽게 말하면 답을 머릿속에서만 완성하지 않고
검색을 해 본 뒤 그 결과를 읽으며 이어 가는 것임.

정확히는 추론 기록과 작업 행동을 섞고,
환경에서 돌아온 관찰로 다음 행동을 정함.
이번 논문도 이 반복을 계보의 기초로 인용함. <!-- L1 -->

그림에서 Thought, Action, Observation이
번갈아 나오는 곳을 보셈.

![추론·행동·관찰을 섞는 ReAct 예시 (Yao 외, Figure 1)](assets/posts/harness-engineering/prior_react.webp)

---

그 반복을 코드 작업으로 옮기면
행동을 어떻게 표현할지가 문제가 됨.

2024-05-06 공개된 SWE-agent는
모델이 파일을 찾고 수정하고 테스트하는
전용 인터페이스를 연구했음.
NeurIPS 2024에 실린 논문임. <!-- L2 -->

명령만 있는 게 아님.
컴퓨터가 돌려주는 결과의 형식도 포함함.
이걸 agent-computer interface, ACI라고 부름. <!-- L2 -->

ReAct와 SWE-agent에는
Shunyu Yao와 Karthik Narasimhan이 함께 있음.
이번 Wavestone 연구팀과는 다른 저자들임. <!-- L5 P1 -->

아래 가운데 ACI가 모델과 파일 사이에 있음.

![파일 탐색·수정과 반환 결과를 잇는 ACI (Yang 외, SWE-agent Figure 1)](assets/posts/harness-engineering/prior_swe.webp)

---

이런 바깥 코드를 나란히 조사한 연구도 있음.

Benjamin Rombaut가 쓴
Inside the Scaffold임.
최초 공개일은 2026-04-03이고,
오픈소스 코딩 에이전트 13개를
12개 차원으로 비교했음. <!-- L3 -->

이번 저자들은 자기 연구의 4월판과
동시기에 진행된 상보적 연구라고 소개함. <!-- L3 -->
Rombaut 논문이 이번 팀의 전작인 건 아님. <!-- L3 -->

표본이 다르다는 점을 기억해두셈.
뒤의 코드 검색 이야기에서 다시 나옴.

아래 제목부에도 단독 저자가 적혀 있음.

![동시기 구조 조사 Inside the Scaffold의 제목·저자 (Rombaut, p.1)](assets/posts/harness-engineering/prior_scaffold.webp)

[Rombaut 원문](https://arxiv.org/abs/2604.03515v2)

---

이번은 그 바깥을 일곱 장치로 나눴음. <!-- F6 -->

가운데는 모델을 부르는 반복문임.
모델 연결과 도구 실행이 붙고,
기억과 입력 문맥도 관리함. <!-- F6 -->
실행을 허용할지 판단하는 장치,
다른 에이전트를 부르는 장치,
기능을 더 붙이는 인터페이스도 있음. <!-- F6 -->

쉽게 말하면 모델이 제안한 일을
실제 파일과 프로그램에 이어 주는 코드임.
정확히는 이 반복·도구·문맥·통제 등을
묶는 런타임이 하네스임. <!-- F6 -->

그림 가운데 Agent Loop에서
주변 장치로 이어지는 화살표를 보셈.

![코딩 하네스의 일곱 하위 시스템과 인터페이스 (원문 Figure 1)](assets/posts/harness-engineering/fig1_p4.webp)

---

그 일곱 장치의 가운데부터 열어 보면
의외로 반복문이 그대로 보임.

Mini-SWE-Agent의 압축된 예시는
모델 호출, 행동 실행, 결과 기록을 반복함. <!-- F7 -->

예를 들어 모델이 테스트 명령을 제안하면
런타임이 명령을 실행함.
실패 로그를 기록해 다시 모델에 보냄.
모델은 그 로그를 보고 다음 행동을 제안함. <!-- F7 -->

모델의 생각과 실제 실행 결과 사이를
이 반복문이 계속 이어 주는 구조임. <!-- F7 -->

아래 query와 execute_actions,
마지막 observation 기록을 보셈.

![호출·실행·관찰 기록을 반복하는 최소형 루프 (원문 Listing 1 일부)](assets/posts/harness-engineering/listing1.webp)

---

반복은 모델이 끝내자고 할 때도 문제임.

파일은 바뀌었는데 테스트 없이
다 고쳤다고 말하는 장면을 생각해 보셈.

Aider는 수정 뒤 lint와 테스트의 실패를
모델에 돌려 다시 고치게 하는 경로가 있음.
기본 reflection 상한은 3회임. <!-- F8 -->

Hermes는 종료 쪽에 장치를 둠.
코드를 바꾼 뒤 최신 검증 흔적이 없으면
텍스트로만 끝내려는 답을 계속 실행으로 바꿈. <!-- F9 -->
이게 verify-on-stop임.
검증 흔적이 버그 해결을 보장하진 않음. <!-- F9 -->

원문에서도 종료를 막는 guard로 설명함.

![최신 검증 없이 끝내려는 응답을 이어 가게 하는 장치 (원문 p.15)](assets/posts/harness-engineering/q_verify.webp)

---

이 반복을 묶는 프레임워크부터
찾았는데, 저자들이 발견한 건 부재였음.

LangChain, LangGraph 같은
범용 에이전트 프레임워크를 검사했음.
고정한 11개에서 에이전트 실행 경로의
해당 import를 찾지 못했다고 함. <!-- F10 -->

여기서 프레임워크는
에이전트의 진행 순서를 묶는 공통 틀을 뜻함.
모델 API 연결 라이브러리와는 구분한 것임. <!-- F10 F12 -->

조사는 의존성 목록과 소스 검색에 기반함.
다른 방식을 쓰면 성능이 나빠진다는 실험은 아님. <!-- F10 F33 -->

원문에서 production agent code path라는
범위 표현을 놓치면 안 됨.

![범용 프레임워크의 실행 경로 import를 못 찾았다는 관찰 (원문 p.53)](assets/posts/harness-engineering/q_framework.webp)

---

그렇다고 전부 맨손으로 짠 건 아님.

Aider는 선택 기능인 /help에서
LlamaIndex로 자기 도움말 문서를 검색함.
에이전트 진행 순서를 맡긴 건 아님. <!-- F11 -->

OpenCode는 Vercel AI SDK를 사용함.
이건 모델 제공자 연결과 도구 호출을
다루는 라이브러리로 분류했음. <!-- F12 -->

검색 결과를 모델 답에 붙이는 걸
RAG, 검색 증강 생성이라고 부름.
도움말 RAG가 있다는 사실과
범용 에이전트 틀을 쓴다는 말은 다른 이야기임. <!-- F11 F12 -->

원문도 두 예외를 바로 붙여 적었음.

![Aider 도움말 검색과 OpenCode AI SDK의 경계 사례 (원문 p.53)](assets/posts/harness-engineering/q_exceptions.webp)

---

그럼 하네스는 코드 파일을 어떻게 찾을까?

여기서 또 하나의 0이 나옴.
이 11개 표본은 코드 탐색에
벡터 임베딩 검색을 쓰지 않았다는 관찰임. <!-- F13 -->

임베딩은 내용을 숫자 벡터로 바꿔
의미가 가까운 것을 찾게 하는 표현임.
이 조사에서 코드를 찾는 주된 수단은
문자열 검색과 파일·구문 구조였음. <!-- F13 F15 -->

예를 들어 ripgrep로 함수 이름을 찾고
필요한 파일을 열어 읽는 방식임. <!-- F15 -->
tree-sitter는 코드를 구문 구조로 읽고
함수 이름 같은 심벌을 뽑는 도구임.
Aider는 그 관계를 순위화한
RepoMap도 만듦. <!-- F14 -->

표 오른쪽에서 실제 검색 수단을 보셈.

![문자열·파일·구문 구조를 쓰는 코드 탐색 (원문 Table 13 일부)](assets/posts/harness-engineering/tab13_top.webp)

---

이 0을 기억 검색까지 넓히면 틀림.

OpenClaw의 기본 대화 기억 검색은
임베딩과 문자열 검색을 함께 씀.
sqlite-vec KNN과 FTS5/BM25의 조합임. <!-- F16 -->
코드 탐색과 대화 회상은 검색 대상이 다름.

원문 앞쪽의 기억 부재 문장은
뒤쪽의 이 구체적 설명과 맞지 않음.
여기서는 Table 13의 예외를 따랐음. <!-- F17 -->

아까 Rombaut의 다른 표본도 기억해두셈.
그 논문에는 이번 11개 밖의 Moatless Tools가
FAISS와 LlamaIndex로 코드를 검색하는 사례가 있음. <!-- L4 -->
모든 코딩 AI에서 벡터 검색이 없다는 뜻은 아님.

아래에는 conversation memory only가 적혀 있음.

![코드 탐색과 구분한 OpenClaw의 기본 대화 기억 검색 (원문 Table 13 일부)](assets/posts/harness-engineering/tab13_memory.webp)

---

찾은 코드를 고칠 때도 인터페이스가 갈림.

예를 들어 모델이 찾아 바꿀 문장을 냈는데
실제 파일과 공백 하나가 다르다고 해 보셈.
정확 문자열 교체라면 대상을 못 찾을 수 있음.
비슷한 문자열까지 찾는 fuzzy matching은
허용할 차이를 따로 정해야 함. <!-- F19 -->

이번 표에는 문자열 교체, 패치,
fuzzy matching 같은 설계가 나란히 있음. <!-- F19 -->
어떤 편집 방식이 항상 더 좋다는 실험은 아님. <!-- F1 F33 -->

OpenCode는 모델에 따라 갈라짐.
GPT 계열에는 apply_patch,
그 밖에는 string edit 경로를 씀. <!-- F20 -->

표에서 Matching과 Fallback 칸을 보셈.

![파일을 찾고 수정 실패를 처리하는 편집 방식들 (원문 Table 7)](assets/posts/harness-engineering/tab7_p28.webp)

---

수정 도구가 늘면
모델에게 뭘 보여줄지도 문제가 됨.

도구 이름과 사용법도 모델 입력을 차지함.
전부 처음부터 펼치기보다
필요할 때 찾아 불러오는 설계가 있음. <!-- F21 -->
이걸 deferred tool loading이라고 부름. <!-- F21 -->

Claude Code의 ToolSearch,
Codex의 MCP 도구 검색이 그 사례임. <!-- F21 -->
검색으로 선택한 도구의 정의를
모델이 쓸 수 있게 하는 방식임. <!-- F21 -->

원문의 구현 설명이지
실제 속도나 비용 절감량을 잰 결과는 아님. <!-- F33 -->

아래 tool_search와 defer_loading을 보셈.

![도구 정의를 검색해 필요한 시점에 불러오는 설계 (원문 p.28 일부)](assets/posts/harness-engineering/q_deferred.webp)

---

도구 설명뿐 아니라 대화도 계속 늘어남.

테스트 로그와 수정 결과를 계속 붙이면
언젠가는 모델 입력 한도에 닿음.
그전에 입력을 줄이는 context compaction을 함. <!-- F22 -->

쉽게 말하면 다음 호출에 보낼 기록을
요약하거나 일부 덜어 내는 것임.
정확히는 모델 입력 문맥을 압축하는 작업임.
저장한 기록 전체의 삭제와는 다름. <!-- F22 -->

Hermes는 압축 후 새 child session을 만들고
SQLite에서 원래 parent와 연결함.
입력은 줄어도 기록의 계보는 남길 수 있음. <!-- F23 -->

아래에는 여러 입력 관리 전략이 나옴.

![전체 기록 유지부터 요약·선별까지의 문맥 관리 전략 (원문 Figure 4)](assets/posts/harness-engineering/fig4_p31.webp)

---

대화 기록과 다음에 쓸 기억도 다름.

다음 작업에 남길 내용을 누가 고르고
언제 파일에 반영할지 설계해야 함.

Codex는 추출과 합치기를 나눔.
먼저 session에서 정보를 뽑고,
격리된 별도 에이전트가
뽑은 기억을 합쳐 관리함. <!-- F24 -->
Gemini CLI에는 추출한 기억 수정안을
검토함에 두는 경로가 있음. <!-- F25 -->

Hermes는 MEMORY.md 2,200자,
USER.md 1,375자로 제한함.
토큰 수가 아니라 글자 수임. <!-- F26 -->
또 대화 시작 때 모델 입력 앞쪽에 붙일
기억 내용을 고정함.
중간 수정이 이 입력을 바로 바꾸진 않음. <!-- F26 -->

아래 frozen snapshot을 보셈.

![기억 크기와 고정 스냅샷을 설명한 문장 (원문 p.34 일부)](assets/posts/harness-engineering/q_memory.webp)

---

기억 파일이든 코드 파일이든
쓰기 전에 허용할지 판단해야 함.

근데 실행 승인을 받는 것과
프로그램이 갈 수 있는 범위를 막는 건 다름. <!-- F27 -->

쉽게 말하면 실행해도 되느냐는 permission이고,
실행한 코드가 어디까지 접근하느냐는 isolation임. <!-- F27 -->
예를 들어 Git worktree로 파일 작업을 나눠도
그 자체가 OS 샌드박스가 되는 건 아님. <!-- F27 -->

논문은 이런 통제 층을 구분해 비교했음.
보안 공격에 얼마나 버텼는지 실험한 건 아님. <!-- F27 F33 -->

그림의 규칙 검사·모델 분류·사용자 확인을
따로 보셈.

![여러 단계로 실행을 검사하는 Claude Code 설계 (원문 Figure 5)](assets/posts/harness-engineering/permission_layers.webp)

---

이 허용·실행 규칙 위로
확장 기능도 붙음.

정해 둔 작업법을 읽어 실행하는 skills와
외부 도구를 연결하는 MCP가 그 사례임. <!-- F29 -->
둘은 같은 역할을 겨루는 기능이 아님. <!-- F28 F29 -->

고정한 버전에서 SKILL.md는 9/11,
MCP는 8/11이 채택했음.
OpenClaw를 빼면 코딩 하네스는 8/10, 7/10임. <!-- F28 -->
사용자 점유율이나 작업 성공률은 아님.

Skills는 설명부터 보여 주고
필요할 때 전체 지침을 읽는 방식이 많았음.
Pi는 skills와 CLI를 선호하며 MCP는 안 썼음. <!-- F29 -->

아래 Skills? 칸에서 채택 여부를 보셈.

![확장 방식의 채택 여부를 비교한 표 (원문 Table 10)](assets/posts/harness-engineering/tab10_p49.webp)

---

이런 하네스를
SDK로 제공한 사례도 있음.

SDK는 다른 프로그램에서 기능을
가져다 쓸 수 있게 묶은 개발 도구임.
논문은 Claude Agent SDK와
OpenHands SDK 등을 이 방향의 사례로 듦. <!-- F30 -->

반대 방향도 있음.
LangGraph 위에 만든 Deep Agents는
프레임워크 쪽에서 하네스가 된 사례임. <!-- F30 -->
이번 11개 표본 바깥이라는 점도 붙여야 함.

저자들은 이런 양방향 변화를
도구에서 플랫폼으로 가는 흐름으로 해석함. <!-- F30 -->
프레임워크가 사라졌다는 결론과는 거리가 있음.

아래 표의 두 방향을 같이 보셈.

![하네스의 SDK화와 프레임워크의 하네스화 (원문 Table 15)](assets/posts/harness-engineering/tab15_p60.webp)

---

이런 변화는 4월판과 비교해 적은 것임.

저자들은 4월의 8개를 유지하고
7월판에서 11개로 넓혔다고 설명함. <!-- F31 -->
같은 시스템의 과거 소스를 남겨 두고
새로 고정한 소스와 차이를 본 것임. <!-- F31 -->

행동 정책 일부가 프롬프트 문장에서
설정으로 옮겨간 변화도 소개함. <!-- F32 -->

다만 별도 4월 원문은 확보 못했음.
이 변화 설명은 이번 원문에 근거함. <!-- L6 F31 -->
같은 버그를 같은 모델로 고친 성능 실험도 아님. <!-- F33 F36 -->

원문은 같은 시스템을 다시 고정했다고 적음.

![4월 snapshot을 유지해 분기 사이 변화를 본 방법 (원문 p.62)](assets/posts/harness-engineering/q_evolution.webp)

---

그 비교도 어디까지 읽었는지에 묶여 있음.

이 연구는 소스를 읽었고
실행 시간·비용·안전 효과는 직접 재지 않았음. <!-- F33 -->
모델과 배포 조건이 다른 성능 숫자도
직접 비교처럼 읽히지 않게 표에서 뺐음. <!-- F36 -->

특히 Claude Code는 3월 유통 소스임.
저자도 재현성에서 가장 약한 부분이라고 적음. <!-- F5 F35 -->
내부 fork와 동적 import로 불리는 plugin 등은
실행 경로를 끝까지 추적하지 않았음. <!-- F34 -->

소스 분석과 집필에 Claude Code의
상당한 도움을 받았다는 공개도 있음. <!-- F39 -->
저자들의 확인과 독립 재현은 구분해야 함.

아래 source-code reading과
not runtime measurement를 보셈.

![소스 독해와 실제 실행 측정을 구분한 한계 (원문 p.66 일부)](assets/posts/harness-engineering/q_limits.webp)

---

그 한계를 알고 90줄 예시를 보면
뜻이 달라짐.

마지막에는 bash, 읽기, 쓰기,
문자열 교체의 네 도구를 가진 코드가 있음.
약 90줄로 최소 하네스를 설명하는 예시임. <!-- F37 -->

샌드박스와 여러 에이전트,
MCP와 skills는 생략했음.
실제 배포용 코드가 아니라고 명시함. <!-- F37 -->

좋은 모델을 붙이면 Mini-SWE-Agent 수준에
가까울 거라는 문장도 있음.
근데 바로 conjecture, without proof임.
증명 없이 둔 추측이라는 뜻임. <!-- F38 -->

아래 문장에서 conjecture를 보셈.

![90줄 최소형의 성능 예상은 증명 없는 추측임을 명시 (원문 Observation 13)](assets/posts/harness-engineering/q_conjecture.webp)

---

처음의 버그 요청으로 돌아가면
모델 바깥에서 할 일이 보임.

코드가 어디 있는지 찾음.
제안한 수정을 실제 파일에 적용함.
실행 결과를 다음 모델 호출로 돌려줌. <!-- F6 F7 -->

테스트 없이 끝내려는 응답을
계속 실행으로 바꾸는 장치도 있을 수 있음. <!-- F9 -->
그동안 허용 여부와 실행 격리를 관리함. <!-- F27 -->

이 연결을 어떻게 구현했는지가
하네스의 설계 차이였음. <!-- F6 -->
어느 설계가 같은 버그를 더 잘 고치는지는
이번 소스 비교만으로 답할 수 없음. <!-- F1 F33 -->

아래 반복·수정 후 검증·작업 분담을
각기 다른 설계로 읽으면 됨.

![반복형·수정 후 검증형·작업 분담형의 루프 설계 (원문 Figure 2)](assets/posts/harness-engineering/fig2_p17.webp)

---

그래서 다음엔 같은 버그를
같은 모델로 고치게 해야 함.

저자들도 하네스 사이의 통제된 평가와
비용·안전·사용 경험을 다음 과제로 듦. <!-- F40 -->

2026-10-06 기준 공개 원문은 확보됐고
공식 심사 통과·게재처는 확인 못했음. <!-- W1 W2 -->
확인 가능한 직접 후속 논문이나
독립 재현 원문도 찾지 못했음. <!-- L6 -->
90줄 예시가 그 빈칸을 대신 채우진 않음. <!-- F37 F38 -->

[이번 논문 PDF](https://arxiv.org/pdf/2609.00006v1)

3줄 요약
코딩 AI의 모델 바깥 런타임을 11개 표본으로 비교했음. <!-- F2 F3 F6 -->
범용 틀과 벡터 코드 검색의 부재는 표본·기능 범위를 지켜 읽어야 함. <!-- F10 F13 F16 L4 -->
설계 차이는 봤지만 같은 조건의 효과는 아직 재지 않았음. <!-- F33 F36 -->
