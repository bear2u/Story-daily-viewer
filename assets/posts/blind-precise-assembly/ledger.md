# 팩트 원장: Blind Precise Assembly

확인일 2026-10-20. 원문 arXiv:2610.23849v1. 최초 공개 UTC 기준. PDF 21쪽, text.txt 1742줄 처음부터 끝까지 정독.
원문 https://arxiv.org/pdf/2610.23849v1 . 그림·표는 해당 PDF와 직접 대조. 수치는 실험 종류/정책/분모가 다르면 합치지 않음.

## F: 본문·부록

- F1 | pp1–2 Abstract/Introduction | "joint encoders and previous actions" | 관절 위치·속도와 이전 행동, 이로부터 계산한 그리퍼상태만으로 접촉조립하는 정책. 센서 자체를 로봇에서 제거했다는 주장이 아니라 정책 입력 제한.
- F2 | p1 Introduction | "move differently from what their commands alone would produce" | 접촉력이 링크·관절로 전달되어 명령만 있을 때와 움직임이 달라짐. 엔코더 기록에서 접촉 정보를 추론. 관절이 힘을 직접 측정하거나 정확한 외력역산을 입력으로 주는 방법 아님.
- F3 | p5 §2.3, p14 Architecture | "last 0.6 s"; "30 observations" | 50Hz/최근30개 약0.6초 기록. 관절q/속도dq, 순기구학으로 계산한그리퍼위치·자세/속도, 이전action. TCN이32차원latent, MLP가7관절위치증분출력. 구멍위치·물체기하·영상·wrench estimate 입력없음.
- F4 | p3 §2.1,p10 Limitations | "Episodes start with the part touching the fixture"; "last-mile manipulation skill" | 물체는이미잡혀있고고정부품에닿은채정렬이틀어진상태로시작. 전체작업대에서부품집고찾는시스템아님. 구멍근처로가져오는별도동작필요.
- F5 | p3 §2.1,p14 A.1 | "Peg insertion"; "Gear meshing"; "Nut threading" | 세시뮬레이션과제. peg착좌,gear축에착좌하며기어맞물림,nut는나사산잡힌뒤¼회전. 끝까지너트조임시험아님. 실제물리전이는peg만.
- F6 | p3 Tasks,p15 Table1,p16 Table2 | "1.0–1.5 mm ... per side" | peg정책학습의한쪽틈1.0–1.5mm. 실물tight0.5mm는범위밖시험. 기하벤치마크20µm와물리정밀도혼동금지.
- F7 | p4 §2.2,Fig5 | "wall material inside the hole" | CoACD/V-HACD등근사분해가시험한설정에서틈을잠식. concavity허용오차가작은조립틈보다클수있어충돌결과변경. 전용정밀조립설정에서비교한결과,범용분해전체가항상쓸모없다는뜻아님.
- F8 | p4 Exact convex decomposition,Fig4 | "the user specifies the clearance directly" | mjfit:구멍둘레판을볼록조각으로분할·돌출,peg윤곽은틈만큼안쪽offset. 곡선은다각형근사라모서리에추가유격이생길수있지만구멍쪽침범하지않게구성. '모든기하오차0'아님.
- F9 | pp4–5 Fig6,p17 B | "c = 20 µm" | 중앙정렬peg1mm위에서떨어뜨리는충돌기하벤치마크,특정default판에서baseline멈춤/걸림과mjfit통과. 20µm는실물삽입정확도가아님. GPUFig6b256worlds,Table4는512worlds라성능집계혼용금지.
- F10 | p5 §2.3,p14 A.1 | "12,288 worlds"; "PPO" | 시뮬레이션12,288병렬세계에서형상/잡은자세/마찰등랜덤화. 성공·중간이정표희소보상으로PPO학습. 모든조립을실제시연한데이터셋아님.
- F11 | p5 Training,p6 Contact supervision,Fig7 | "asymmetric critic"; "decoder is dropped at deployment" | 훈련용critic은정답상대pose/contact접근. latent접촉분류decoder도시뮬레이터label로학습시키나예측결과를actor에직접넣지않고배포때버림. teacher/critic정보가정책실행입력으로누출되는것아님.
- F12 | p18 Contact supervision,Fig14p19 | "2.7 (peg), 3.8 (gear), and 5.1 (nut)" | 접촉손실제거해도세과제학습가능하나90%훈련성공률까지환경step이각2.7/3.8/5.1배필요. wall-clock훈련시간·청구비용비교아님.
- F13 | p6 Visual policies,p14 Architecture | "The visual policy sees only images"; "64×64" | 비교는손목RGB64×64영상만입력하는정책,같은30step/0.6초기록. 과제/리셋/랜덤화/보상/행동/성공조건맞춤. 영상+관절융합제거실험아님. 인코더도CNNvsproprioTCN으로다름,모든vision정책일반우열아님.
- F14 | p18 Table5 | blind99.4%,visual97.2%;time0.80s/0.44s;rate65/82 | study peg분포내시험,seed당8192episode를두seed평균。Time은중앙값을두seed평균。성공시험만의시간이라는한정은caption에없어추가안함。gear/nut별도속도본문은성공episode한정명시。blind는peg에서더느림。실제공장속도아님。Gear속도는blind.58vsvisual.64라전과제blind느리다고일반화금지。
- F15 | p7 §3.2,Fig9,p18Table5 | "median 37 mm ... 95 mm" | 같은3964개시작상태에서blind이동중앙값37mm,낙관적spiral95mm,visual20mm. 4096matchedstarts중양seed1정책이모두성공한3964에대한이동비교. Spiral에는peg방향과최적출발방향제공. 사진한번시간1.42/.32를평균속도로쓰지않음.
- F16 | p7§3.2,p18 Probe details | "Balanced accuracy ... 70% ... 56% ...33%" | deployed peg정책의7상태분류선형probe. simulationheldoutworlds에서historylatent70%,현재관측56%,랜덤encoder33%,chance14%. 조립성공률아님,정확pose추정오차아님. 기어61/너트73은별도fullrange정책.
- F17 | p19 Fig15/Probe details | "each state keeps its own current observation" | 현재관측고정·다른mode의historylatent교환시행동변화가같은mode교환보다큰경향. latent이실제행동에관여한다는시뮬레이션분석. 모든mode완전분리/정확접촉모델증명아님.
- F18 | p20 Table7,p18 Behaviour | randomconvexblind36.2%,visual3.9%;extremesize91.9%/16.4% | study정책peg새형상시험. 훈련은stadium,새형상은볼록다각형. 2trainingseeds평균. 36.2%가3.9%보다높아도절반미만성공. 실패63.8%=100−36.2,약64%는파생값. 실물73%와전혀다른시험/정책.
- F19 | p14 introStudy/deployed,p16Table2 | "more narrow"; "random convex" | 통제연구용study와실제배포용학습범위다름. study는stadium단면,배포는polygonal/smooth/mixedequalshares+handle,widerpose/contact. 같은학습정책이시뮬레이션99.4→실물73으로떨어졌다고빼면오류.
- F20 | p9 §3.4 | "Flexiv Rizon 4S ... Robotiq 2F-85 at 50 Hz" | 실제팔·그리퍼고정정책을50Hz로실행. 과제실물시연·미세조정없음. 다만팔armature/damping/friction은실제측정동역학식별p5,모든실물정보0이라고말하면과장.
- F21 | p9 Results,Fig12 | "173 of 237 trials (73%)" | 실물8종peg,173/237=72.9958%→73%. 새parameter변경없음. operator가착좌성공판정. 5개분포내+3개형상속성분포밖.
- F22 | p9 Fig12/Results | 23/30,24/30,22/30,22/30,23/30,19/29,19/29,21/29 | 합173/237. 앞5종분포내73–80%,tight/large/handle각66/66/72%(반올림). 3개29분모이유는원문설명없어지어내지않음. Errorbar95%WilsonCI. 시뮬레이션동일peg각2048ep별도.
- F23 | p20 Real-world pegs,p21 | "20 s horizon, which counts as a failure" | 각peg30plannedresets중판정에도달한첫attempt각1회count. operator성공/실패혹은20초한계실패. 실물은한쪽틈1.11–1.49mm5종,tight.5mm1종. 시작위치는훈련리셋분포·이미표면접촉.
- F24 | p10 Limitations | "local"; "slides out from the grasp and lands far from the hole" | 마지막근거리탐색·오정렬수정정책. 잡은물체떨어져멀리간것같은큰복구상황처리못함. 현실3과제모두실증했다고쓰지않음.
- F25 | p18–19 Probe details | "6.6 mm"; "62% ... against100%" | 실물추가30회I3시험,관절+계획grasp로계산한peg위치가착좌시중앙6.6mm틀림,지나친슬립/회전때문. inside선형probe도실물62%vs같은시작simulation100%. '정확구멍pose를복원했다'고추론하면과장.

## P: 저자·기관

- P1 | p1저자란·각주 | "Massachusetts Institute of Technology"; "Equal contribution" | Antonia Bronars, Younghyo Park공동기여, Kushal Kedia, Pulkit Agrawal4명모두논문기준MIT. 순서만으로단독최초기여추정안함.
- P2 | p10 Acknowledgments | "Ministry of Trade, Industry, and Energy (MOTIE), Korea"; "KIAT" | 한국산업통상자원부GlobalIndustrialTechnologyCooperationCenter프로그램/KIAT지원명시. MIT소속을한국기관소속으로바꾸거나국적추정안함.

## W: 발표·외부자료

- W1 | https://arxiv.org/abs/2610.23849v1 (2026-10-20) | "Fri, 16 Oct 2026 17:58:48 UTC" | 최초공개2026-10-16UTC. KST+9h=2026-10-17 02:58:48. PDF고정v1읽음.
- W2 | 같은arxiv공식페이지 (2026-10-20) | "pending registration" | DOI10.48550/arXiv.2610.23849등록대기표시. 학회게재정보arxiv없음,공식채택확인전에는심사결과확정안함.
- W3 | 공식license링크 https://creativecommons.org/licenses/by/4.0/ (2026-10-20) | "CC BY 4.0" | 원문그림표BY4.0. 출처·저자·원문URL·라이선스·크롭/확대변경표시. 별도폰트OFL유지.
- W4 | https://younghyopark.me/blind-proprioceptive-assembly/ (2026-10-20) | "Preprint"; "2026" | 저자프로젝트에영상·interactive simulations공개주소. 공개만확인,보고서제작중직접시뮬레이션재현실행한것아님.

## 선정·검증 범위

- W5 | https://younghyopark.me/ 및 https://tonibronars.github.io/ (2026-10-20) | "Under review" | 공식 저자 홈페이지는 심사 중으로 표시. 채택·동료심사 완료 논문으로 소개하지 않음. Park은 MIT EECS/CSAIL 박사과정, 지도교수 Pulkit Agrawal로 소개하며 과거 NAVER LABS 연구원 경력. 현재 논문 소속은 p1의 MIT로 한정.
- W6 | arXiv 제목·인용/공식 프로젝트·저자 목록 검색 (2026-10-20) | 확인 가능한 독립 후속 연구 미확인 | 이번 검색 범위에서 후속 검증을 찾지 못했음. 후속 연구가 없다고 단정하지 않음. 프로젝트 영상 공개와 재현 실험 완료도 구분.
- W7 | https://github.com/younghyopark/mjfit (2026-10-20) | "MIT license" | 공개된 충돌기하 생성기. 전체 정책/학습 파이프라인 공개라고 넓히지 않음. 논문 그림은 코드 MIT 라이선스 아닌 CC BY 4.0 적용.

## L: 직접 읽은 선행 원문과 관계

- L1 | Chen et al., arXiv:2111.03043v1 pp1–3; https://proceedings.mlr.press/v164/chen22a.html | A System for General In-Hand Object Re-Orientation; Tao Chen, Jie Xu, Pulkit Agrawal, MIT | CoRL 2021 심사 논문, proceedings 2022. 시뮬레이션 안 손안재배향, 비시각 정책도 물체 위치·목표회전 정보를 입력받음. 이번과 Pulkit Agrawal 공유/본문 p9 인용이나 순수 관절입력 실물조립의 직접 전작이라고 부르지 않음.
- L2 | Pinto et al., arXiv:1710.06542v1; RSS 2018 DOI10.15607/RSS.2018.XIV.008 | Asymmetric Actor Critic for Image-Based Robot Learning | 훈련 critic은 전체상태, 실행 actor는 부분관측. 이번 p5의 asymmetric critic은 이 구조 계승. 이전 DDPG/HER과 이번 PPO가 같다는 주장 아님. 공개 2017-10-18UTC와 학회 2018 구분.
- L3 | Wei et al., arXiv:2205.02961v1; NSF 공개 원문 wei2022_nsf.pdf; DOI10.1145/3528223.3530103 | Approximate Convex Decomposition for 3D Meshes with Collision-Aware Concavity and Tree Search | Xinyue Wei, Minghua Liu, Zhan Ling, Hao Su; UCSD. TOG 41(4), SIGGRAPH 2022 journal track 심사 논문. 범용 메시 충돌기하 근사분해. 이번의 비교 기준이지 mjfit 내부 구성요소 아님.
- L4 | Bhatt et al., arXiv:2608.29487v1 pp1,7 | Blind Dexterity: Whole-Body Humanoid Manipulation via Pure Proprioception | Aditya Bhatt, Oleg Kaidanov, Puze Liu, Jan Peters. 2026-08-30UTC 공개. Unitree G1 관절+IMU 물체조작(보행만 IMU-free), 부드러운 가방 조작도 있음. 다른 연구팀의 선행 프리프린트, 이번 후속작 아님. 모든 비시각 선행연구는 강한 접촉뿐이라는 일반화 배제.

기존20편ID/제목대조후미중복선정. 최신cs.RO공식목록에서후보확인,21쪽원문확보후전체정독. 2610.23438은다른후보로만읽고미선정. 원문확보CLI의부수외부통신차단으로해당경로재시도하지않음. 공식PDF만curl직접확보해21쪽파싱확인. API계보값0은조회생략에따른빈필드이지실제인용0주장아님. 원문참고문헌·직접선행원문및저자공식자료로보완.
