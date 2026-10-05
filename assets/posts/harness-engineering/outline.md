# 기획: 코딩 AI는 모델 바깥에서 뭘 하고 있을까

원장 작성 후 기획: 2026-10-06. 읽기 완료: 본문·부록·참고문헌 83쪽. 유형: 측정·데이터형 중 소스코드 질적 비교. 표본과 관찰 방법→발견→경계→설계 의미. 성능 개선 해결형으로 꾸미지 않음.

독자: 코딩 AI는 써 봤지만 내부 설계는 처음인 개발자/일반 기술 독자. 개발용 라이브러리와 모델 API SDK를 orchestration framework와 혼동할 수 있으므로 예외를 붙여 설명함. 연구 현재 위치는 공식 arXiv 날짜·심사 미확인·공개 후속/재현 미확인으로 날짜를 박음.

도입 질문: 버그 하나 고치라는 요청을 받으면 모델 바깥에서는 무슨 일이 벌어질까?
예시: 함수의 공백 차이 때문에 문자열 수정 대상이 안 잡히는 가정; 테스트 전 종료하려는 장면. 실제 논문 benchmark 장면처럼 제시하지 않음.

- 마디: 모델 바깥 | 표본/계보/7개 장치로 질문을 정확히 정함.
- 마디: 코드를 찾음 | 범용 framework 부재와 코드 검색 부재의 뜻·예외.
- 마디: 수정 다음 | 편집, 도구 선택, 압축, 기억, 허용과 격리.
- 마디: 어디까지 확인 | 플랫폼화 해석, 판본 변화, 방법 한계,90줄 예시와 실제 검증의 거리.

밑밥/회수: (1) 커다란 설계도 기대→linear loop와 framework 부재→SDK·LangGraph 바깥 예외로 범위 회수. (2) 의미 검색으로 코드 찾기 기대→문자열·구조 검색→OpenClaw memory/Moatless code RAG 예외. (3) 고쳤다고 말하면 끝인가→verification-on-stop/permission→마지막 bug 장면에서 다시 답.
재미 재료: framework 부재, vector code retrieval 부재, 일부 기억을 session 중 고정하는 디테일,90줄 코드의 conjecture without proof,원문 memory 문장 충돌. 과장된 성능 수치를 만들지 않음.
전문성: purposive sample, snapshot pin,10+1 denominator, import inspection scope, code vs memory retrieval, static source vs runtime measurement. Dataset/model/hyperparameters/성능 CI는 적용 불가(이 논문은 실험 benchmark 아님). 기능 count와 context 문자 제한은 조건 그대로 제시.

| 파트 | 첫 줄/연결 | 요지 | 원문 그림 | 원장 |
|---|---|---|---|---|
|1|버그 하나 고쳐 달라고 했음|설명용 요청과 모델 바깥 질문|q_definition|F6|
|2|그 바깥을 소스코드로 들여다본 논문임|제목·저자·당시 소속·날짜·심사|header|P1 W1 W2 F41|
|3|비교표를 보기 전에 표본부터|11=10+1,별도Omnigent,고정snapshot|tab3|F1–5|
|4|모델 바깥 코드는 갑자기 생긴 건 아님|ReAct2022 행동→관찰|prior_react|L1|
|5|그 반복을 코드 작업으로 옮기면|SWE-agent2024ACI,저자교집합|prior_swe|L2 L5 P2|
|6|이런 바깥 코드를 나란히 조사한 연구도 있음|Rombaut2026의13개·12차원,자기전작아님|prior_scaffold|L3 F31|
|7|이번은 그 바깥을 일곱 장치로 나눔|anatomy와harness의뜻|fig1|F6|
|8|그 일곱 장치의 가운데부터|minimal loop 설명|listing1|F7|
|9|반복은 모델이 끝내자고 할 때도 문제임|Aiderlint/test3회, Hermesstopverification|q_verify|F8 F9|
|10|이 반복을 묶는 거대한 framework부터 찾았는데|source audit의부재와범위|q_framework|F10|
|11|그렇다고 전부 맨손으로 짠 건 아님|AiderdocRAG/OpenCodeSDK|q_exceptions|F11 F12|
|12|그 라이브러리들이 코드를 찾는 방식도 봤음|rg/tree-sitter/RepoMap,vectorcode0|tab13_top|F13–15|
|13|이0을 기억 검색까지 넓히면 틀림|OpenClawembedding,원문충돌,Moatless표본밖|tab13_memory|F16 F17 L4|
|14|찾은 코드를 고칠 때도 인터페이스가 갈림|exact/fuzzy/editmodel조건|tab7|F19 F20|
|15|수정 도구가 늘면 모델에게 뭘 보여줄지도 문제|deferredtool load 설명|q_deferred|F21|
|16|도구 설명뿐 아니라 대화도 계속 늘어남|compaction,inputvsarchive|fig4|F22 F23|
|17|대화 기록과 다음에 쓸 기억도 다름|추출/검토/고정 기억,2200/1375chars|q_memory|F24–26|
|18|기억 파일이든 코드 파일이든 쓰기 전에|permission vs isolation|fig5|F27|
|19|이 허용·실행 규칙 위로 확장 기능이 붙음|skills9/11MCP8/11역할차이|tab10|F28 F29|
|20|확장하다 보니 완성 하네스가 SDK로도 나옴|양방향platform해석·DeepAgentsoutside|tab15|F30|
|21|이런 변화는4월판과 비교해 적은 것임|8→11 retainedsample,동일task아님|q_evolution|F31 F32 L6|
|22|그 비교도 어디까지 읽었는지에 묶여 있음|source/runtime·MarchCC·dynamicimports·AIassist|q_limits|F33–36 F39|
|23|그 한계를 알고90줄 예시를 보면|illustrative4tools,효과추측|q_conjecture|F37 F38|
|24|처음의버그요청으로돌아가면|검색→수정→검증→종료→허용의모델외장치|fig2|F6 F7 F9 F27|
|25|그래서다음엔같은버그를같은모델로고치게해야함|미래평가,현재상태,3줄요약|없음|F40 W1 W2 L6 F10 F13 F33|

25/25파트 척추·밑밥에 연결(100%). 모든밑밥24–25에서회수. 마지막답: 모델의말을실제파일변경과검증결과로연결하는런타임. 맺음: snapshot구조관찰을실효성검증과구분,현재원문·심사·후속확인상태를적고3줄요약. 출처links는part2·25,세줄뒤에는붙이지않음.
