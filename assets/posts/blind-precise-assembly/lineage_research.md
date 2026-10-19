# 계보·저자 조사 보고 (원고/팩트 원장 아님)

확인일: 2026-10-20. 대상: Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts, arXiv:2610.23849v1 (2026-10-16). 메인 원문 페이지는 제공된 paper.pdf/text.txt 기준. 아래 4편은 각각 PDF 첫 페이지와 명시한 관련 절을 직접 읽었음. 전체 정독했다고 주장하지 않음.

## 결론: 서로 다른 종류의 연결을 섞지 말 것

| 선행 연구 | 메인에서 확인한 연결 | 연결의 성격 | 피해야 할 표현 |
|---|---|---|---|
| Chen, Xu, Agrawal 2021 | 메인 p9 §4 Proprioceptive policies의 명시 인용; Pulkit Agrawal 공통 저자 | 동일 저자의 형태 비의존 in-hand manipulation 선행 맥락 | '2021년에도 관절 정보만으로 실물 조작 성공' |
| Pinto et al. 2018 | 메인 p5 §2.3 Training의 asymmetric critic 명시 인용 | 이번 학습에 실제 채택한 학습 설계 | '이 논문도 카메라를 써야 하므로 낡았다'; 이번 actor와 동일하다는 설명 |
| Wei et al. 2022 (CoACD) | 메인 p4 §2.2, p5, p17 Appendix B에서 비교 | 실제 사용한 생성기 부품이 아니라 충돌 형상 비교 기준 | 'mjfit이 CoACD를 사용해 생성'; 일반적 CoACD 열등 주장 |
| Bhatt et al. 2026 (Blind Dexterity) | 메인 p9 §4의 명시 인용 | 다른 연구진의 동시대 proprioceptive manipulation 선행 | 이번 연구의 후속작, 공통 연구실, 또는 '이전은 강한 접촉만 가능' |

## 1. A System for General In-Hand Object Re-Orientation

- 저자: Tao Chen, Jie Xu, Pulkit Agrawal. 원문 소속: Massachusetts Institute of Technology. 공식 프로젝트는 CSAIL, MIT 표기.
- 최초 arXiv 공개: 2021-11-04 17:47:39 UTC, arXiv:2111.03043v1. 발표는 CoRL 2021 (원문 p1 footer). PMLR 서지 출판 연도는 2022, vol.164 pp.297–307. 따라서 '2021 연구/CoRL 2021, proceedings 2022'로 구분하면 연도 혼동 없음.
- 직접 읽은 범위: 원문 p1–3, §1–2.2.2 중심. 2,000개 넘는 형상이 다른 물체의 in-hand 재배향, 새로운 물체에 대한 zero-shot 일반화가 주요 성과. 손 위/아래, 받침대 유무를 포괄함.
- 중요한 단서: 원문 p2에서 실험을 simulation에 한정한다고 명시. p3 §2.2.1의 non-vision student 관측에는 24개 joint positions 외에 **물체 위치 3차원, 현재 물체와 목표의 quaternion 차이 4차원**이 포함됨. 별도 vision student(§2.2.2)는 RGBD point cloud를 사용함. 'shape-agnostic'과 '외부/물체 상태를 전혀 안 받는다'는 서로 다른 주장.
- 이번 연구와 연결: 메인 p9의 proprioceptive policies 문단이 직접 인용하며, Pulkit Agrawal이 공통 저자. 물체 형상 정보를 직접 주지 않는 조작과 새 형상 일반화라는 맥락은 확인되지만, 코드·정책을 직접 이어받았다는 근거는 이 조사에서 확인하지 않음. '같은 저자의 선행 연구'로만 다룰 것.
- URL: https://arxiv.org/abs/2111.03043 ; https://proceedings.mlr.press/v164/chen22a.html ; https://proceedings.mlr.press/v164/chen22a/chen22a.pdf ; https://taochenshh.github.io/projects/in-hand-reorientation
- 로컬: papersources/chen2021.pdf, chen2021.txt.
- 웹 참조: turn238view1 (arXiv), turn233search4 (PMLR), turn233search2 (저자 프로젝트).

## 2. Asymmetric Actor Critic for Image-Based Robot Learning

- 저자: Lerrel Pinto, Marcin Andrychowicz, Peter Welinder, Wojciech Zaremba, Pieter Abbeel.
- 원문 소속: Lerrel Pinto—Carnegie Mellon University; 나머지 4인—OpenAI (PDF p1 표기를 그대로 따름).
- 최초 arXiv 공개: 2017-10-18 01:10:37 UTC, arXiv:1710.06542v1. 공식 발표: Robotics: Science and Systems XIV, 2018년 6월, Pittsburgh; DOI 10.15607/RSS.2018.XIV.008.
- 직접 읽은 범위: 원문 p1–4, 특히 p4 §IV-A, Fig.2, Algorithm 1. 시뮬레이터에서 critic은 full state, actor는 partial visual observation을 받게 하여 학습을 도움. 실물 배포는 actor만 사용하므로 full state를 요구하지 않음. domain randomization과 결합해 pick/push/move를 실물에 옮긴 성과를 보존해서 설명할 것.
- 이번 연구의 **실제 사용 부품**: 메인 p5 §2.3은 asymmetric critic을 위 논문에 명시 귀속함. 이번 critic은 actor 관측에 더해 fixture 대비 part pose 및 true contact labels를 받음. 이번 actor는 visual actor가 아니라 0.6초 proprioceptive history 기반. 따라서 계승한 것은 정보 비대칭 학습 구조이지 카메라 입력 자체가 아님. 기존 DDPG/HER 구현 그대로라고 쓰지 말 것(메인은 PPO 사용).
- URL: https://arxiv.org/abs/1710.06542 ; https://www.roboticsproceedings.org/rss14/p08.html ; https://www.roboticsproceedings.org/rss14/p08.pdf
- 로컬: papersources/pinto2018.pdf, pinto2018.txt.
- 웹 참조: turn233search1 (arXiv), turn238view0 (RSS 공식서지), turn233search15 (PDF).

## 3. Approximate Convex Decomposition for 3D Meshes with Collision-Aware Concavity and Tree Search (CoACD)

- 저자: Xinyue Wei, Minghua Liu (공동 기여), Zhan Ling, Hao Su. 원문 소속: University of California San Diego, USA.
- 최초 arXiv 공개: 2022-05-05 23:40:15 UTC, arXiv:2205.02961v1. ACM Transactions on Graphics 41(4), Article 42, July 2022, 18쪽. arXiv comments는 SIGGRAPH 2022 journal track. DOI 10.1145/3528223.3530103.
- 직접 읽은 범위: 원문 p1–4의 소개, p3 §3 문제 정의/방법 개요, p4 §4.1 concavity 정의; p13의 §7 applications drawer-opening 문단 추가 확인. arbitrary solid mesh를 근사 convex pieces로 바꾸며 concavity threshold로 조각 수와 세부 형상 보존을 절충함. boundary와 interior를 함께 보는 collision-aware 지표, mesh plane cutting, multi-step tree search가 기여. 기존 대비 손잡이/틈 보존과 drawer opening 개선이라는 성과가 있음.
- 이번 연구와 관계: 메인 p4 Fig.5 및 §2.2 Benchmark에서 비교 기준, p17 Appendix B에서 exact watertight plate mesh를 모든 baseline에 제공함을 명시. 이번은 MuJoCo solver를 고정하고 collision representation만 바꾼 비교. CoACD 일반 유용성을 부정하는 게 아니라, tested tight-clearance assembly에서 근사 오차가 clearance를 침범할 수 있다는 차이. mjfit은 필요한 빈 영역을 알고 조립 부품을 직접 구성하는 특화 생성기; 임의 3D mesh를 충실히 분해하는 CoACD와 문제 설정이 다름.
- **실제 사용 여부**: CoACD는 mjfit의 내부 생성 부품으로 확인되지 않음. 메인은 exact convex primitives/prisms를 자체 생성하고 CoACD 결과를 비교함.
- URL: https://arxiv.org/abs/2205.02961 ; https://colin97.github.io/CoACD/ ; https://doi.org/10.1145/3528223.3530103 ; https://par.nsf.gov/servlets/purl/10347843
- 로컬: papersources/wei2022_nsf.pdf (공식 NSF public-access 원문, 정상 파싱), wei2022.txt. 최초 arXiv curl의 wei2022.pdf는 전송 파일이 PDF 파싱 실패하므로 **사용/배포 금지**; 정상 NSF 파일을 사용.
- 웹 참조: turn234search0 (arXiv metadata), turn239view0 (저자 프로젝트), turn234search12 (NSF PDF).

## 4. Blind Dexterity: Whole-Body Humanoid Manipulation via Pure Proprioception

- 저자: Aditya Bhatt, Oleg Kaidanov, Puze Liu, Jan Peters.
- 원문 p1 소속 번호: Bhatt 1,3; Kaidanov 1,3; Liu 1,3,4; Peters 1,2,3,5. 1 Intelligent Autonomous Systems Lab, TU Darmstadt; 2 hessian.AI; 3 German Research Center for AI (DFKI); 4 Tongji University, Shanghai Research Institute for Autonomous Intelligent Systems; 5 Robotics Institute Germany.
- 최초 공개: arXiv:2608.29487v1, 2026-08-30 00:32:01 UTC. PDF p1에 IEEE에 possible publication 제출 상태 안내. 채택 venue는 이 조사에서 확인하지 못함. 'IEEE 출판 논문'으로 표현하지 말 것.
- 직접 읽은 범위: p1–3 소개/§III/§IV-A–C, p7 §V-D Gentle Blind Manipulation (Suitcase), p8 §VI 한계. Unitree G1의 관절-명령 차이를 whole-body tactile channel로 다루며 blind walking, 공 트래핑, 스케이트보드 올라타기, 가방 손잡이 찾고 들기를 보임. object-manipulation actor는 joint positions/velocities, previous action뿐 아니라 stock IMU도 사용함; IMU-free 주장은 walking 실험에 해당.
- 관계 근거: 메인 p9 §4에서 직접 인용, 본문 references p10에 4인 저자 명시. 단순 유사제목이 아니라 본문이 인정한 선행. 그러나 공통 저자나 같은 연구실이 아니며, 메인보다 먼저 나온 연구임. 메인 이후 후속 연구가 아님.
- 보존할 성과/차이: Bhatt에서도 짧은 proprioceptive history로 object state를 추정하는 별도 분석 estimator를 학습시킴(§IV-C). 따라서 '이전에는 관절에 접촉 정보가 있다는 걸 몰랐다'는 주장 금지. 또한 §V-D는 moderate force도 가방을 넘어뜨릴 수 있어 gentle exploration을 강조하고 variable stiffness를 비교함. 메인 p9의 'forceful contact or centimeter tolerances' 요약을 모든 전작에 대한 '세게 만져야만 작동'으로 확대하면 부정확. 안전한 대비는 전신/손잡이 조작에서 이번의 millimeter-clearance precision assembly로 문제 범위가 이동했다는 것.
- URL: https://arxiv.org/abs/2608.29487 ; https://arxiv.org/pdf/2608.29487 ; https://arxiv.org/html/2608.29487v1 ; https://aditya.bhatts.org/BlindDexterity/
- 로컬: papersources/bhatt2026.pdf (9쪽), bhatt2026.txt.
- 웹 참조: turn236search1 (arXiv metadata), turn236search9 (원문 HTML), turn238view2 (저자 프로젝트).

## 메인 논문 상태 및 저자 맥락

- 메인 최초 공개: arXiv v1, 2026-10-16 17:58:48 UTC. 원문 전면에 Preprint, 소속 Massachusetts Institute of Technology. Antonia Bronars와 Younghyo Park 공동 기여.
- 2026-10-20 조회 시 저자 공식 홈페이지 **두 곳 모두 Under review**: https://tonibronars.github.io/ 및 https://younghyopark.me/ . 프로젝트 검색 색인은 Preprint · 2026, MIT Improbable AI Lab 표기. arXiv 메타데이터에는 채택 학회/저널/논문집 정보가 표시되지 않음. 결론은 '저자 홈페이지상 심사 중인 2026년 프리프린트'로 한정. 심사 대상 학회명은 미확인.
- Bronars 공식 소개: MIT PhD student, Pulkit Agrawal 지도, Improbable AI lab. 촉각·proprioception·low-level control이 policy learning과 상호작용하는 정밀/민첩 조작을 연구한다고 설명. 과거 촉각연구도 다수이므로 '촉각연구를 버렸다/실패해서 전환' 같은 전기적 인과는 근거 없음.
- Park 공식 소개: MIT EECS/CSAIL PhD student, Pulkit Agrawal 지도. 서울대 기계공학 학사, 과거 NAVER LABS full-time research scientist. 2023년 8월 MIT 박사 시작을 명시. 사용자에게 필요한 경우 이 확인된 범위만 사용.
- 두 사람이 Agrawal과 함께 쓴 Tune to Learn: How Controller Gains Shape Policy Learning가 Park 공식 페이지에 RSS 2026 표기. Bronars 페이지는 arXiv preprint 2026로 다르게 표기하므로, 현재 채택 상태 인용은 RSS 공식 확인 추가 없이 과도하게 확대하지 말 것. 이번과 공유하는 저자/low-level control 관심이라는 인적 맥락은 맞지만, 본문이 해당 논문을 직접 전작으로 인용하지 않으므로 '이번 방법이 그 성과를 계승'이라고 단정하지 않음.
- mjfit 공식 저장소: https://github.com/younghyopark/mjfit . 논문을 위해 만들었다고 README가 설명. exact convex collision geometry, MIT license. 저장소 존재는 공개 생성기 확인이지 정책훈련 코드/학습된 정책 전체 공개의 증거가 아님.
- 웹 참조: turn235view0 (메인 arXiv), turn237view0 (Bronars), turn237view1 (Park), turn236search2/turn240search2 (프로젝트), turn236search10/turn240search9 (mjfit).

## 독립 후속 연구 확인 범위

2026-10-20에 검색한 질의: `"2610.23849"` (arXiv·요약사이트 일부 제외), `"Blind Precise Assembly" "cite" "2026"`, `"Blind Precise Assembly" "follow"`, 제목+accepted. 확인된 것은 원 논문·저자 사이트·mjfit·동시기 요약 기사/색인. 이번 메인 논문을 방법적으로 계승하고 인용한다고 원문에서 검증 가능한 독립 후속 연구는 **이번 검색 범위에서 확인하지 못함**. '후속 연구가 없다' 또는 '아무도 재현하지 않았다'는 단정은 금지. 최초 공개와 확인일 사이가 4일이므로 전망은 저자 주장/현재 결과와 분리할 것. Bhatt2026은 선행이고, CoACD/Pinto 역시 메인에 앞선 연구이므로 후속 칸에 넣지 말 것.

## 검색/원문 접근 주의

검색 결과의 AI 요약/제3자 기사(Teahose, arXivDaily, alphaXiv 등)는 관계·성과 근거로 사용하지 않았음. 프로젝트 페이지는 직접 open에서 일시 실패했으나 검색 색인으로 내용을 확인했고, 핵심 사실은 메인 원문·공식 저자홈페이지에 교차 확인함. 웹 인용을 최종 답변에 쓰려면 부모 에이전트가 해당 URL을 직접 open 또는 search+find로 확인해야 함.
