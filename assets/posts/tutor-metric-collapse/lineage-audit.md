# 계보·저자 맥락 독립 확인

확인일: 2026-10-14. 주 논문 본문·참고문헌, Springer 원 출판사 페이지, ACL Anthology 원 PDF, ICML/PMLR 원 PDF를 대조했음. 주 보고서 파일은 수정하지 않았음.

## 주 논문

- 제목: The learner who does not learn: when optimizing a pedagogical metric degrades LLM tutoring
- 저자: Daniel Domínguez Figaredo, Rafael Fernández De la Cruz.
- PDF p.1에 둘 다 UNED, Madrid, Spain으로 표기. Thinking Machines Lab의 Tinker Research Program 지원을 p.1 각주가 명시함. 이 지원을 공동저자·소속·실험 검증으로 확대하면 안 됨.
- arXiv v1 제출: 2026-10-08 15:18:26 UTC (한국시간 2026-10-09 00:18:26). 2026-10-14 확인 페이지에서 후속 판본·journal reference·acceptance comment 없음.
- https://arxiv.org/abs/2610.12125 ; https://arxiv.org/pdf/2610.12125
- arXiv-issued DOI https://doi.org/10.48550/arXiv.2610.12125 는 2026-10-14 arXiv 페이지에서 `pending registration` 표시. DOI가 즉시 해소되는지 확인하기 전 확정된 등록 DOI라 부르지 않을 것.

## 전작 1 — 같은 저자의 교육이론 기반 감사

- Explainable pedagogical alignment: auditing LLMs with learning theories
- 저자: Daniel Domínguez Figaredo; José Luis Fernández Vindel; Laura Guerrero Puerta. 주 논문과의 실제 저자 겹침은 Daniel 한 명임. Fernández Vindel은 이번 Rafael Fernández De la Cruz와 다른 사람임.
- DOI: https://doi.org/10.1007/s10639-025-13857-2
- 공식 페이지: https://link.springer.com/article/10.1007/s10639-025-13857-2
- Received 2025-06-04; Accepted 2025-11-20; 최초 온라인/Version of Record 2025-12-15; 권31 pp.1283–1311, 2026년 4월 issue. 따라서 `2026년 논문`이라는 참고문헌 연도는 맞지만 `2026년 최초 공개`는 아님.
- 소속: Daniel은 UNED 교육학부; José Luis는 UNED 컴퓨터공학 학교; Laura는 Universidad de Málaga 교육과학부. 현재 주 논문은 두 저자 모두 UNED로만 표기함.
- 출판사 초록에서 직접 확인 가능한 범위: GPT-4/Khanmigo 출력과 학습이론(Active Learning, Behaviorism, Social Learning)을 대조하고, 이론별 skills prompt를 넣은 과정 설계도 감사했음. 추가 교육학적 입력이 모든 이론과의 정렬을 함께 높이지는 않았음. 정확한 실험 세부와 각 수치는 본문 확보 실패이므로 주 보고서에 쓰지 않는 것을 권함.
- 원문 공개 PDF를 찾으려 시도했지만 공식 `content/pdf/...` URL은 PDF 대신 구독 HTML(398,491 bytes)을 반환했고, 출판사 페이지도 subscription preview라고 표시. UNED CRIS가 Open access로 표시하는 것과 불일치함. 공개 원문을 읽었다고 말하면 안 됨. 관련 그림 크롭도 준비하지 않음.
- 주 논문 p.19 §5.2는 이번 감사에서 analytical/evaluative Bloom levels의 어려움이 전작과 다시 관찰됐다고 설명하지만 두 감사 모두 Bloom taxonomy를 쓰므로 공유 방법이 수렴의 일부를 설명할 수 있다고 명시함. 독립 재현으로 부르지 않을 것.

## 전작 2 — 선호 학습으로 튜터 행동 정렬

- Pedagogical Alignment of Large Language Models.
- Shashank Sonkar; Kangqi Ni; Sapana Chaudhary; Richard G. Baraniuk. Rice University(3명), Texas A&M University(Chaudhary), 원 PDF p.1.
- 최초 arXiv: 2024-02-07 16:15:59 UTC; v3 2024-10-05. Accepted at EMNLP 2024 Findings Track를 arXiv comment에서 확인.
- 공식 학회 판본: Findings of EMNLP 2024, 2024년 11월12–16일, pp.13641–13650.
- https://aclanthology.org/2024.findings-emnlp.797/ ; https://aclanthology.org/2024.findings-emnlp.797.pdf ; DOI https://doi.org/10.18653/v1/2024.findings-emnlp.797 ; arXiv https://arxiv.org/abs/2402.05000
- 원 PDF 저장: related/sonkar2024.pdf, related/sonkar2024.txt (10p).
- §3/§4: GPT-4가 만든 CLASS 대화 구조에서 교육적으로 선택된 응답과 거절된 응답을 합성 선호쌍으로 만들고 DPO/IPO/KTO를 SFT와 비교함. 평가 정확도는 `학생 응답 평가`, `그 평가에 따른 행동`, `하위문제 상태` 3개 JSON 분류필드 평균임. 실제 학생 학습 성취도 점수가 아님.
- 따라서 계보 문장: `좋은 튜터 행동을 선호쌍으로 만들고 학습하는 흐름이 이미 있었음. 이번 논문은 그런 평가값을 올린 뒤 교육자의 판단도 좋아지는지 물었음.` 이번 PAI의 결과가 Sonkar 방법 전체를 반증했다거나 같은 실험을 재현했다는 연결은 부당함.
- §6은 실제 교육환경에서 더 포괄적인 user studies가 필요하다고 명시함. 주 논문과 저자 겹침 없음.

## 전작 3 — 보상모델 과최적화의 일반 맥락

- Scaling Laws for Reward Model Overoptimization.
- Leo Gao; John Schulman; Jacob Hilton. 원 PDF p.1 소속 모두 OpenAI.
- 최초 arXiv: 2022-10-19 17:56:10 UTC. 학회 게재는 ICML 2023, PMLR vol.202 pp.10835–10866, 2023년7월23–29일.
- https://proceedings.mlr.press/v202/gao23h.html ; https://proceedings.mlr.press/v202/gao23h/gao23h.pdf ; https://arxiv.org/abs/2210.10760
- 원 PDF 저장: related/gao2023.pdf, related/gao2023.txt (32p).
- §2.1/Fig.2: 인간 평가를 대신하는 고정 6B gold reward model, 3M–3B proxy reward models를 쓴 합성 환경에서 RL/PPO와 best-of-n을 비교. proxy를 너무 올리면 gold reward가 초기 상승 뒤 감소하는 현상을 관찰함. 학습자·교사 실험은 아님.
- 주 논문 p.19 §5.1은 일반 보상 해킹 이야기와 달리, 고정 학습자 조건에 대해 각 활동 점수를 독립적으로 평균내는 목표의 대수적 형식 자체가 반복을 허용한다는 더 좁은 기제를 주장함. 따라서 `Goodhart의 교육판`은 설명 비유로 가능하나, ICML 논문이 이번 PAI 붕괴를 이미 증명했다는 표현은 안 됨.
- 주 논문과 저자 겹침 없음.

## 후속 연구 확인

2026-10-14에 exact title / arXiv ID로 두 검색엔진 및 arXiv 공식 레코드를 확인했음. 식별 가능한 후속 학술 연구나 독립 재현을 찾지 못했음. 검색에는 논문 목록·요약·블로그 소개가 존재했지만 학술 후속으로 세지 않음. `후속 연구 없음`/`피인용 0회` 같은 전수 주장 대신 `확인 가능한 직접 후속·독립 재현은 아직 찾지 못했음(확인일 2026-10-14)`으로 쓸 것.

## 원문 근거 위치·브라우징 참조

- Main author/date/DOI pending: turn143view0 (arXiv, lines8–30).
- Springer author/date/accepted/affiliations: turn139view0 / turn140view0 / turn140view3.
- ACL official metadata: turn139view1. ACL full PDF: turn144view0 / turn146view1 (Table2, §4.3).
- ICML official metadata: turn139view2. Original PDF: turn146view3 (§2.1, Fig2, §4.5).
- Author personal site turn143view3 is stale (`In press` for already published prior), so avoid using it for current job or publication state. Main PDF and publisher affiliation sufficient.

## 사용 권고

계보는 3편으로 짧게 유지할 것: 같은 저자의 이론 기반 감사 → 교육 선호 학습의 흐름 → Goodhart/보상 과최적화 배경 → 이번 연구가 학습자 상태를 고정한 점수의 반복 최적해를 확인. 최신 후속은 확인불가라고 명시. 전작의 구독 본문 미확보는 주 논문 공개 PDF 확보와 무관하며, 전작의 구체 수치/그림은 생략.
