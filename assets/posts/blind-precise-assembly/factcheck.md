# 독립 팩트체크 — arXiv:2610.23849v1

판정: **수정 필요 1건, 그 외 아래 주요 주장 PASS.** report.md는 수정하지 않았음.

집필자 반영 확인: Table5의 '성공한 시험의' 삭제를 원문 p18 caption과 직접 대조한 뒤 반영했음. gear 속도에는 별도 한 시드·성공시험 조건을 추가했음. 그 외 검증된 숫자·조건은 유지. 최종 검사 ERROR0.

검토 자료: paper.pdf의 text.txt를 p1–21 끝까지 정독하고, report.md 전체 및 ledger.md·lineage_research.md와 대조. 원문 p18–19 렌더 이미지도 직접 확인. 선행 원문은 chen2021.txt p1–3, pinto2018.txt 서두 및 방법 절, wei2022.txt 서두·방법 개요, bhatt2026.txt 소개·관측 정의·가방 조작 절을 직접 대조함. 선행 논문 전체 정독을 주장하지 않음.

외부 재확인 시각: 2026-10-19 23:39 UTC = 2026-10-20 08:39 KST. 따라서 원고의 10월 20일 확인일은 한국 날짜로 성립함. 공식 arXiv·저자 홈페이지·학회 proceedings만 상태/서지 근거로 사용함.

## 반드시 고칠 부분

| 판정 | 원고 위치/주장 | 원문 근거 | 권장 수정 |
|---|---|---|---|
| 수정 필요 | F14: “시간은 성공한 시험의 중앙값을 집계함” | p18 Table 5 caption은 seed당 8,192 episode, success/time/rate의 두 seed 평균, 별도 언급 없으면 중앙값이라고 명시함. **Table 5의 peg 시간에 성공 시험만 집계했다는 한정은 명시하지 않음.** 성공한 episode만 센다는 한정은 바로 아래 별개 gear/nut 속도 문단에만 있음. 이를 peg Table 5로 옮기면 임의 추론임. | “시간은 중앙값을 집계하고 / 두 학습 시드 결과를 평균함”으로 변경. 또는 “성공한 시험의”만 삭제하고 앞 문장의 두 시드 평균 설명을 유지. ledger F14도 성공시험 한정을 추가하지 말 것. |

## 우선 검증 항목

| 판정 | 주장/ID | 원문 쪽 | 짧은 근거와 경계 |
|---|---|---|---|
| PASS | 정책 입력은 관절·그리퍼 계산값·이전 행동, 카메라/힘 측정 미입력 — F1–3 | pp1–2,5,14 | q/dq, 순기구학 그리퍼 pose/twist, 이전 action. 실제 로봇에서 센서를 제거했다는 주장이 아닌 정책 입력 제한으로 정확히 서술함. |
| PASS | 최근 0.6초, 50Hz×30개, TCN 32차원, 7관절 증분 — F3 | p5 Fig7, p14 Architecture | 수치·인코더·출력 모두 일치. encoder가 힘을 직접 측정한다는 표현도 피함. |
| PASS | 잡힌 부품이 표면 접촉 상태로 시작, 마지막 구간 작업 — F4,F24 | p3 Tasks, p9 Setup, p10 Limitations | 로봇이 멀리서 찾기·집기·큰 복구를 해결한다는 확대 없음. |
| PASS | 세 시뮬레이션 과제와 너트 ¼회전 기준, 실물 peg만 — F5 | pp1–3,9,14 | nut는 thread catch 이후 quarter turn. 완전 체결이라고 하지 않음. |
| PASS | peg 학습 틈 1.0–1.5mm/side, 실물 tight 0.5mm — F6 | pp3,15–16,20 | deployed Table2도 clearance는 study와 같다고 명시. 20µm와 분리함. |
| PASS | CoACD 근사 오차, mjfit의 빈 공간 보존·곡선 추가 유격 — F7–9 | pp4–5,17 | 제한된 조립 기하 비교로 설명. USB-C 실물 조립이나 20µm 실물 정밀도를 주장하지 않음. |
| PASS | 12,288 병렬 환경, 접촉 보조학습은 훈련만 — F10–11 | pp5–6,14 | decoder 예측은 actor 입력에 들어가지 않으며 배포 때 제거. critic의 privileged inputs도 학습용으로 분리함. |
| PASS | 90%까지 step 2.7/3.8/5.1배 — F12 | pp18–19 Fig14 | peg/gear/nut 순서 정확. wall-clock·비용의 배수로 확대하지 않음. |
| PASS | 영상 전용 64×64 손목 RGB baseline, 같은 0.6초 — F13 | pp6,14 | 이미지+관절 융합 정책이 아님. task/reset/randomization/reward/action/check 동일, encoder 구조 상이. 보편적 vision 열등 주장 없음. |
| PASS(위 한정 삭제 후) | Table5 99.4/97.2%, 0.80/0.44초 — F14 | p18 Table5 | study peg 분포 내, 각 seed 8,192회, 두 seed 평균. 실물/배포용 정책 수치로 혼동하지 않음. |
| PASS | gear 0.58/0.64초로 순서 반전 — F14 | p18 속도 문단 | 이 수치는 study, 한 seed, deterministic actions, 성공 episode만의 중앙값. Table5 peg 시간과 같은 실험 집계라고 추가 단정하지 말 것. 원고의 단순 순서 반전 주장은 성립. |
| PASS | 3,964 matched starts, 37/95/20mm — F15 | p7 Fig9, p18 Table5 | 4,096 시작 상태 중 seed-1의 두 정책이 모두 성공한 3,964. blind37, 낙관적 spiral95, visual20 중앙값 일치. spiral에 orientation/유리한 시작 방향 제공. |
| PASS | 7상태 probe 70/56/33%, chance14% — F16 | pp7–8 Fig10, p18 Probe details | **deployed peg 정책의 시뮬레이션 balanced accuracy**임. 1,536 worlds의 짝수 world로 probe 학습, 홀수로 시험. 실물 정확도나 조립 성공률로 쓰지 않음. |
| PASS | latent만 교환해 행동 변화 — F17 | p19 Fig15 | current observation은 각 상태 자체 값을 유지. near/far 교환까지 항상 큰 변화라고 일반화하지 않아 정확함. |
| PASS | 새 볼록 단면 36.2/3.9%, 두 seed, 시뮬레이션 — F18 | pp18,20 Table7 | study training stadium, unseen convex 별도. 약64% 실패는 100−36.2=63.8 반올림. 실물73%와 분리함. |
| PASS | study와 deployed 학습 범위가 다름 — F19 | p14 도입, pp15–16 Tables1–2 | deployed는 polygonal/smooth/mixed equal shares+handle 및 더 넓은 contact/pose. 99.4→73을 같은 정책 sim-real 하락으로 계산하지 않음. |
| PASS | 실물 팔·그리퍼·50Hz·미세조정 없음, 동역학 실측 있음 — F20 | pp5,9 | Flexiv Rizon4S/Robotiq2F-85/50Hz 및 frozen policy 정확. 실물 정보가 전혀 없다는 과장도 p5 실측 문장으로 교정함. |
| PASS | 실물 173/237≈73%, 8종 부품 — F21–22 | p9 Fig12/Results | 23+24+22+22+23+19+19+21=173; 5×30+3×29=237. 종별 반올림73–80%,66/66/72 일치. 29분모 이유는 원문 미설명이며 지어내지 않음. |
| PASS | 초기 접촉·operator 판정·20초면 실패 — F4,F21,F23 | p9 Setup, pp20–21 Real-world pegs | 각 peg 30 planned resets에서 판정에 도달한 첫 attempt를 한 번 count. operator success/failure 또는20s horizon, timeout은 실패. 같은 peg simulation2048 worlds도20s. 원고의20초 설명 정확. |
| PASS | 실물 위치오차 중앙6.6mm — F25 | pp18–19 Probe details | 추가30회 I3 시험에서 성공한 trial 끝의 encoder+planned grasp pose와 seated pose 간 거리. 정확한 구멍 위치 복원으로 해석하지 않아 정확함. |
| PASS | 실물 probe와 simulation의 성능 차이를 한계로 제시 — F25 | p19 Probe details | inside states recall은 robot62% vs 같은 starts simulation100%; 성공24회 중 최종 state17회 inside. Fig10a 실물 패널은 예시 시퀀스이며 실물 전체70%를 입증하지 않음. 원고도70%를 명확히 simulation으로 한정함. |
| PASS | 저자4명 MIT, 첫2명 공동기여, MOTIE/KIAT — P1–2 | p1 저자란/각주, p10 Acknowledgments | 소속·공동기여·지원기관 정확. 국적/한국기관 소속 추정 없음. |

## 선행·공개 상태 대조

| 판정 | 주장 | 직접 근거 |
|---|---|---|
| PASS | Chen CoRL2021은 시뮬레이션 손안 재배향, 비시각 student도 object position/goal-relative quaternion 입력 | chen2021.txt pp1–3. source p2 simulation 제한, p3 §2.2.1 관측을 명시. PMLR 공식서지는 proceedings2022이므로 원고의 “CoRL2021 연구”와 모순 없음. 공통저자 Agrawal 확인. |
| PASS | Pinto RSS2018의 정보 비대칭 actor-critic 계승 | pinto2018.txt Abstract/§IV-A 및 메인p5 명시 인용. RSS 공식 proceedings가2018 및 DOI 확인. 이전 visual actor/현재 proprio actor 또는 이전DDPG/현재PPO를 동일시하지 않음. |
| PASS | CoACD SIGGRAPH2022의 범용 충돌기하 분해, 이번 비교 기준 | wei2022.txt p1 및 메인p4/17. arXiv 공식 metadata에 SIGGRAPH2022 journal track. mjfit 내부 구성요소라고 하지 않아 정확. |
| PASS | Blind Dexterity 2026년8월, 다른팀 UnitreeG1 관절+IMU·가방의 gentle manipulation | bhatt2026.txt pp1–3 관측 정의, p7 suitcase. arXiv 공식 최초공개2026-08-30. object actor의 IMU와 walking의IMU-free를 구분. 후속/동일연구팀으로 쓰지 않아 정확. |
| PASS | 최초 공개2026-10-16UTC, 심사중 preprint | arXiv 고정v1 submission2026-10-16 17:58:48UTC; Park/Bronars 공식 홈페이지 둘 다 해당 논문 Under review. 채택venue는 확인되지 않아 원고처럼 확정하지 않아야 함. |
| PASS | arXiv DOI 등록 대기 | 공식 arXiv v1에 pending registration 표시 재확인. |
| PASS | mjfit 공개와 전체 정책훈련 코드/독립 재현 구분 | 공식 GitHub repo의 exact collision geometry 생성기 공개 확인. 원고는 전체 코드/재현 공개라고 확대하지 않음. |
| 조건부 PASS | 확인 가능한 독립 후속 검증을 이번 검색 범위에서 찾지 못함 | lineage_research.md에 검색질의/범위를 남겼고 원고도 범위를 명시함. 이번 추가 exact-title/ID+follow-up/replication 검색에서는 검증 논문이 확인되지 않았으나, 포괄적 부재의 증명은 아니므로 현 표현보다 강하게 쓰지 말 것. |

외부 공식 재확인 URL: https://arxiv.org/abs/2610.23849v1 ; https://younghyopark.me/ ; https://tonibronars.github.io/ ; https://github.com/younghyopark/mjfit ; https://proceedings.mlr.press/v164/chen22a.html ; https://www.roboticsproceedings.org/rss14/p08.html ; https://arxiv.org/abs/2205.02961 ; https://arxiv.org/abs/2608.29487 .

웹 참조 ID(부모가 최종 인용하려면 직접 open/search+find 필요): turn242view0–3, turn244view0–1, turn245search0–1. 실패한 fixed-v1 open 결과와 비공식/무관한 검색결과는 근거로 사용하지 않음.

## 최종 확인 지침

Table5 시간 집계에서 “성공한 시험의”를 삭제하면, 검토한 원고에서 추가 필수 사실 수정은 없음. 실물 probe62%/100%를 꼭 본문에 넣을 필요는 없으나, Fig10의 실물 예시를 보고 전체실물정확도70%로 오해할 여지를 줄이고 싶으면 해당 수치를 추가할 수 있음. 현재 원고는70%가 simulation이라고 명시하고 실물성능차이를 별도 설명하므로 사실오류는 아님.
