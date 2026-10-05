# 계보 자료: Harness Engineering

확인일: 2026-10-06. lineage.py를 실행한 뒤 공식 원문으로 수동 보강. 인용 수는 확인되지 않아 사용하지 않음. 각 선행작은 연결에 필요한 본문·그림·저자란을 확인했으며 선행작 전체 독해를 주장하지 않음. 본 논문은83쪽 전체 독해.

| 공개일 | 연구 | 원문에서 확인한 관계 | 원장 |
|---|---|---|---|
|2022-10-06|[ReAct](https://arxiv.org/abs/2210.03629v3), Yao·Zhao·Yu·Du·Shafran·Narasimhan·Cao|추론과 행동을 교차, 관찰을 다음 행동으로 연결. 이번 §3.2가 기초 loop 계보로 인용. ICLR2023 게재본 첫페이지 확인.|L1|
|2024-05-06|[SWE-agent](https://arxiv.org/abs/2405.15793v3), Yang·Jimenez·Wettig·Lieret·Yao·Narasimhan·Press|명령과 feedback의 ACI. 이번 §3.2가 코드 작업 인터페이스 계보로 인용. NeurIPS2024 게재본 첫페이지 확인.|L2|
|2026-04-03|[Inside the Scaffold](https://arxiv.org/abs/2604.03515v2), Rombaut|13개·12차원 source taxonomy. 이번 §3.3이 자기 April판과 동시기의 상보적 연구라 표현. 같은 팀 자기 전작 아님.|L3|
|2026-04, 구체 공개일 미확인|이번 저자들이 설명한 April edition|8개 retained snapshots로July판과비교. 별도 공개 PDF/ID/저자표는확보못함. 자기 전작 author교집합 추정안함.|F31 L6|
|2026-07-15|[Harness Engineering v1](https://arxiv.org/abs/2609.00006v1), Barbaste·Darrigol·Vu·Wiltberger|현재해설. 공식arXiv제출기록의날짜. ID2609/2차인덱스9월과혼동안함.|W1 P1|

## 저자 교집합

ReAct와 SWE-agent의 교집합은 Shunyu Yao, Karthik Narasimhan 두 명. ReAct 당시 Princeton University/Google Research, SWE-agent 당시 Princeton University. 이번4명과 세선행원문의교집합은없음. Rombaut원문에는기관을붙이지않음. 이번4월자기판본은저자표미확보이므로교집합확인불가.

이번저자당시소속: Barbaste Inclusive Brains+Wavestone AI Lab; Darrigol/Vu/Wiltberger Wavestone AI Lab. 현재재직/이직·개인이력은서로갱신시점이달라사용안함.

## 표본 바깥 예외

Rombaut Table8 p.18: Moatless Tools FAISS+LlamaIndex code embedding retrieval. 이번11개에없으므로 이번0을전체codingagent로확장할수없음. 반박/후속이라는연구관계로부르지않음.
이번Table15 p.60: Deep Agents on LangGraph도본11개밖. framework사용이없다는보편명제와다름.

## 후속·독립 재현

2026-10-06 확인범위에서직접후속논문/독립재현원문확보못함. 존재하지않는다는단정은안함. 이번논문은같은model/task 아래비용·안전·UX·확장성을측정하는futurework를제안함.
검색과한계의자세한기록은 source-audit.md. AHE인용오류확인으로해당저자/성능수치전재는제외.
