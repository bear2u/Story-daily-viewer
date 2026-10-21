# 팩트 원장: Train An Imaginative Agent

기준일: 2026-10-21
원문 버전: arXiv:2610.26845v1
날짜 기준: arXiv 최초 공개

## F: 논문 본문

- F1 | p.1 저자란 | "TRAIN AN IMAGINATIVE AGENT" / 12 authors | 제목과 저자 12명
- F2 | p.1 저자란 | "1University of California, Berkeley / 2Impossible Research / 3University of Washington / 4Duke University" | 논문 기준 참여 기관 4곳
- F3 | p.1 각주 | "*, †: Equal contribution." | PDF 각주 자체는 별표와 칼표를 함께 equal contribution으로만 설명하며 역할을 구분하지 않음
- F4 | p.1 arXiv 표기 | "arXiv:2610.26845v1 [cs.AI] 19 Oct 2026" | v1 최초 공개일은 2026-10-19 UTC
- F5 | p.1 초록 | "A seemingly reasonable push in Sokoban can make the puzzle unsolvable." | 소코반의 합법적인 한 번 밀기가 퍼즐을 불능으로 만들 수 있음
- F6 | p.1 초록 | "a single omni model to propose actions, generate images of their outcomes, and then reason over these imagined futures" | 한 옴니 모델이 행동 제안·결과 이미지 생성·미래 비교를 함께 수행
- F7 | p.2, Fig.1 | "Each prediction serves as an internal observation for the next decision." | 예측 이미지가 다음 행동을 정하는 내부 관측으로 다시 들어감
- F8 | p.2 | "A linear rollout ... Counterfactual branching ... Forward thinking ..." | 선형 롤아웃, 반사실 분기, 전방 사고의 세 형식
- F9 | p.3-4, Sec.2.2 | "BAGEL backbone ... 14B total parameters and 7B active parameters" | BAGEL 기반, 총 140억/활성 70억 파라미터
- F10 | p.4, Table 1 | "K indicates the number of actions generated before feedback." | K는 실제 피드백 전에 생성·실행하는 행동 수
- F11 | p.4, Table 1 | K=5, Sokoban: Agima-A7B No Imagine 2%, Agima-A7B 40% | 2상자 학습→4상자 hard 평가, 실제 관측 5행동마다, 40% 대 2%
- F12 | p.4, Table 1 | K=5: Pacman 37 vs 1, Maze 40 vs 23, Sokoban 40 vs 2, PushT 18 vs 1 | K=5에서 같은 BAGEL 기반 action-only 대비 전 환경 우세
- F13 | p.4, Table 1 | K=∞ Agima: Pacman 6%, Maze 3%, Sokoban 19%, PushT 3% | 실관측을 중간에 전혀 안 주면 절대 성능이 크게 하락
- F14 | p.5, Table 2 | Own predictions 40/37/40/18; Blank 1/0/8/1; Stale 0/0/8/0 | 자체 예측 이미지를 빈/낡은 프레임으로 바꾸면 네 환경 모두 하락
- F15 | p.5, Table 2 | Oracle GT 43/81/69/47 | 제안 행동의 정답 프레임을 넣으면 Pacman·Maze2D·PushT가 크게 상승, Sokoban은 3%p 상승
- F16 | p.5 Sec.2.3 | "GRPO updates the language tokens ... generated images remain in the multimodal context but receive no direct RL loss." | RL은 언어 토큰만 직접 최적화하고 생성 이미지는 직접 이미지 손실을 받지 않음
- F17 | p.5 Sec.2.3 | "group size of 8 and batch size of 16" | RL 그룹 8, 배치 16
- F18 | p.6 Sec.3.1 | training simpler, harder/unseen test configurations | 4개 환경에서 쉬운 설정 학습, 어려운 미학습 설정 평가
- F19 | p.7, Table 3a | Structural Fork 4-box: linear 22%, branching 32%; Deadlock 2-box: linear 22%, forward 60% | 분기와 긴 계획 비교의 대표 개선 수치
- F20 | p.7, Table 3b | Pacman G8/F4 22→54%, G10/F8 5→12% | 전방 사고가 모든 평가 구성에서 개선, 대표 두 조건
- F21 | p.8 Sec.4 | RL on ordinary three-box Sokoban, 200 steps, held-out 3/4-box Deadlock and Structural Fork | RL은 일반 3상자 퍼즐로 200스텝, 별도 3·4상자 함정 세트 평가
- F22 | p.8 Fig.4 text | No Imagine rises to about 15% training reward but held-out near zero; imagination variants improve held-out | 행동만 모델의 훈련 보상 상승은 함정 세트로 거의 전이되지 않음
- F23 | p.8-9, Fig.5-6 | after 100 RL steps a new unified format emerges | SFT에 없던 통합 형식이 RL 100스텝 이후 나타남
- F24 | p.9 | "When a second candidate is generated, the first plan fails in 100% of cases, compared to 32% before RL." | 두 번째 후보를 꺼낼 때 첫 계획을 실패로 판정하는 비율 32%→100%
- F25 | p.9 | branches per trace 1.70→1.95 at 150 RL steps | 분기 평균은 1.70에서 150스텝 때 1.95로 증가
- F26 | p.9 | total number of imagined frames does not increase | 분기 효율 개선은 전체 상상 프레임 증가 없이 나타남
- F27 | p.16 App.A | Maze 11×11 train; Sokoban 7×7 2-box; Pacman 9×9 8-food; PushT center-near starts | 각 환경 학습 조건
- F28 | p.16 App.A | test Maze larger; Sokoban 4-box; Pacman 12×12 12-food closer ghost; PushT far starts | easy-to-hard 평가 조건
- F29 | p.16 App.A | PushT success is final coverage greater than 0.80 | PushT 성공 기준은 목표 영역 덮기 80% 초과
- F30 | p.16 App.A.1 | 100 episodes per set, K=∞ for planning evaluation | Deadlock/Fork는 2·3·4상자 각 100개, 중간 실관측 없음
- F31 | p.17 App.B.2 | same underlying expert episodes; only trace structure changes | 선형·분기·전방 사고는 같은 기반 전문가 에피소드, 추적 형식만 바꿈
- F32 | p.18 Table 4 | training action budgets: Maze 40, Sokoban 20, Pacman 80, PushT 30 | 학습 롤아웃 행동 예산
- F33 | p.18 Table 5 | Sokoban forward: both solve 79%, at least one deadlocks 21%; Pacman both succeed 96.4%, a candidate dies 3.6% | 대안 학습 데이터의 실패 사례 비율
- F34 | p.21 Table 6 | SFT 5,000 steps, batch 8, 40,000 presentations, AdamW, lr 2e-5 | SFT 최적화 조건
- F35 | p.21 App.B.4 | RL lr 2e-6, temp 1.0, no extra expert demonstrations | RL 추가 조건
- F36 | p.22 Table 7 | from RL100 almost every comparison hybrid; actual first-candidate failure at RL200 95.5-100% | 통합 형식과 실제 실패의 일치 범위
- F37 | p.23 Table 9 | Forward success 30.3→41.0%, imagined actions 27.82→22.18 | 전방 사고는 성공률 상승과 상상 행동 수 감소가 함께 나타남
- F38 | p.23 Table 9 | Branching success 30.0→50.3%, imagined actions 23.62→21.59 | 분기도 성공률 상승과 상상 행동 수 감소가 함께 나타남
- F39 | p.23 | "These are action counts; we do not measure inference time or FLOPs here." | 비용은 행동 수만 셌고 시간·FLOPs는 측정하지 않음
- F40 | p.24 App.D | selected trajectories are qualitative evidence; no aggregate prediction accuracy | 부록 롤아웃 그림은 선별된 정성 예시이며 예측 정확도 통계가 아님
- F41 | p.63 App.D.7 | real execution can disagree with model's outcome assessment | 모델이 성공이라고 쓴 계획도 실제 실행에서 실패할 수 있음
- F42 | p.65 Fig.51 | ghost catches Pacman at action 17; remaining seven predicted states never executed | 실패 예시에서 17번째 행동 충돌 뒤 7개 예측은 실행되지 않음
- F43 | p.66 Fig.52 | PushT failure ends at 32.4% coverage below 80% threshold | PushT 실패 예시의 구체 수치
- F44 | p.10 Conclusion | claims across four environments; no real-world deployment experiment | 결론의 범위는 네 시뮬레이션 환경
- F45 | p.9, Fig.6(d) | critical branch rate increases after RL | RL 뒤 분기가 중요한 의사결정 상태에 더 집중됨

## L: 계보와 관계

- L1 | Racanière et al., NeurIPS 2017, 원문 초록·이번 논문 p.9 | I2A uses learned environment rollouts as additional context for a model-free policy on Sokoban/MiniPacman | 관계: 직접 문제 제기·비교되는 선행
- L2 | 이번 논문 p.9 | "I2A leaves the choice of imagined actions to a rollout policy ... In Agima, action proposals and visual predictions come from the same model." | 관계: I2A와의 핵심 차이
- L3 | Deng et al., arXiv:2505.14683v3 / 이번 논문 p.4 | BAGEL is a unified model for image/text understanding and generation; Agima builds on it | 관계: 기반 모델 도구로 사용
- L4 | Wang et al., arXiv:2510.16907 / 이번 논문 p.10 | VAGEN predicts state in textual reasoning and rewards accuracy; Agima reasons in language over generated visual predictions with binary success reward | 관계: 가까운 선행·방법 차이
- L5 | Wang et al., arXiv:2601.16973 / 이번 논문 p.2, p.16 | VisGym provides Maze2D; Junyi Zhang, Jiaxin Ge, XuDong Wang, Sewon Min overlap with current authors | 관계: 저자 연속성과 평가 환경
- L6 | arXiv:2610.26845v1 / 웹 검색 2026-10-21 | 최초 공개 이틀째이며 검증 가능한 피인용 후속작을 찾지 못함 | 후속 연구 없음으로 단정하지 않고 검색 시점 한정

## P: 사람과 기관

- P1 | p.1 저자란 | Jiaxin Ge, Junyi Zhang, Tianning Chai are marked * | 공동 제1기여 3명
- P2 | 공식 프로젝트 페이지 https://agima.net/ (2026-10-21 확인) | Trevor Darrell and Haiwen Feng are marked "Equal Advising" | 공식 페이지 기준 동등 지도 2명
- P3 | p.1 저자란 | affiliations UC Berkeley, Impossible Research, University of Washington, Duke University | 논문 기준 기관
- P4 | p.1 감사의 글 p.10 | thanks to seven named people for manuscript feedback | 기여 범위는 원고 피드백으로만 표현

## W: 외부 원문

- W1 | https://arxiv.org/abs/2610.26845 (2026-10-21 확인) | submitted 19 Oct 2026, v1, no journal-ref/commented venue | arXiv 프리프린트이며 심사 통과 발표를 확인하지 못함
- W2 | https://agima.net/ (2026-10-21 확인) | project page lists paper, code, 12 authors and four affiliations | 공식 프로젝트 페이지
- W3 | https://github.com/Agentic-Imagination/Agima (2026-10-21 확인) | code, training/evaluation launchers, released checkpoints/data, Apache-2.0 repository license | 코드·체크포인트·데이터 공개 맥락
- W4 | same repo (2026-10-21 확인) | training recipes use eight large-memory GPUs; minimum VRAM not measured | 재현 비용의 공개된 한계
- W5 | https://proceedings.neurips.cc/paper/2017/file/9e82757e9a1c12cb710ad680db11f6f1-Abstract.html | I2A published in NIPS 2017 | 선행 I2A의 심사·발표처
- W6 | https://arxiv.org/abs/2505.14683 (2026-10-21 확인) | BAGEL first submitted 2025-05-20, open-source unified model | 기반 모델의 공개일·역할
- W7 | https://arxiv.org/abs/2510.16907 (2026-10-21 확인) | VAGEN accepted to NeurIPS 2025 | 가까운 선행의 심사 상태
- W8 | https://arxiv.org/abs/2601.16973 (2026-10-21 확인) | VisGym first submitted 2026-01-23, 17 environments | 저자팀의 바로 전 연구선

## 파생·표현 규칙

- D1 | F11 | 40%/2%=20배, 하지만 글에서는 분모가 작은 배수 대신 38%p 차이를 주로 씀
- D2 | F24 | 100%-32%=68%p 상승
- D3 | F37 | 성공 +10.7%p, 상상 행동 -5.64개
- D4 | F38 | 성공 +20.3%p, 상상 행동 -2.03개
- D5 | F4, 기준일 | 공개 후 2일(한국 날짜 기준 2026-10-21 확인)
