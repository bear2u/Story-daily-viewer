# 검증한 계보와 저자 맥락
확인일: 2026-10-05 KST
날짜 기준: arXiv 최초 공개일. 게재가 확인된 경우 학회도 함께 표시.

| 공개일 | 연구 | 이번 연구와 관계 | 원문에서 확인한 범위 | 원장 |
|---|---|---|---|---|
| 2016-02-04 | Mnih 외, *Asynchronous Methods for Deep Reinforcement Learning* (Google DeepMind·MILA, ICML 2016) | 방법 계보 | A3C는 짧은 n-step return 뒤 critic 값을 붙여 actor를 갱신. 이번 논문은 이름과 성격이 A3C와 닮았다고 직접 설명 | L1 |
| 2024-02-05 | Shao 외, *DeepSeekMath* (DeepSeek-AI·Tsinghua·Peking) | 직접 비교의 기반 | GRPO는 별도 value model 대신 같은 질문의 여러 완성 답 보상 평균을 baseline으로 사용 | L2 |
| 2025-07-10 | Li·Zhou·Levine, *Reinforcement Learning with Action Chunking* (UC Berkeley, NeurIPS 2025) | 방법 선례 | 로봇의 offline-to-online RL에서 단일 행동 대신 행동 묶음을 critic과 policy의 단위로 사용 | L3 |
| 2026-08-17 | Venkatraman·Dinot·Aitchison, *Le Critique* (Mistral AI·Mila·Université de Montréal) | 가까운 선행 연구 | 정답 등 privileged 정보를 critic에 주지만 advantage는 여전히 완성 답 terminal reward를 사용 | L4 |
| 2026-09-30 | Wen·Bailey·Mahankali·Ma, *Trust the Critic More* (Stanford) | 이번 논문 | 문제별 준비도와 10k 토큰 묶음으로 일부 갱신에서 terminal reward 없이 critic을 직접 사용 | F3 F4 |

## 원문 관계 문장
- 이번 논문 p.11: “our method name is very similar to A3C ... this reflects the similarity in the methods themselves”.
- 이번 논문 p.11: GRPO 계열은 완성 응답 그룹의 terminal reward 평균을 baseline으로 쓰고 모든 토큰에 같은 advantage를 준다고 설명.
- 이번 논문 p.11: action chunking의 강화학습 선례로 Li et al. (2025)을 인용.
- 이번 논문 p.11: Le Critique와 BPCO도 critic에 privileged information을 준다고 설명하지만 terminal reward 의존은 유지한다고 구분.

## 저자와 기관
- 이번 논문 저자 네 명은 첫 페이지 기준 Stanford University 소속.
- Kaiyue Wen과 Luke Bailey는 공동 기여 표기(*)가 있음.
- 교신 이메일은 Kaiyue Wen과 Luke Bailey 두 명으로 적힘.
- 감사의 글 기준 Kaiyue Wen은 Stanford Graduate Fellowship, Luke Bailey는 Stanford Graduate and Vitalik Buterin Fellowship 지원을 밝힘.

## 교차 확인과 후속
- 위 네 전작의 첫 페이지 저자 명단과 이번 저자 네 명을 대조했으며 겹치는 저자는 확인되지 않음.
- 2026-10-05 기준 공개된 지 5일인 논문이라 직접 인용해 재현·반박한 후속 원문은 확인하지 못함. 이는 후속 연구가 없다는 뜻이 아님.
- arXiv에는 공식 게재처가 표시되지 않았고, 공개 심사 결정도 확인하지 못함.
