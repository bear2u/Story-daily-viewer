# 팩트 원장
기준일: 2026-10-16 KST. 원문 arXiv2610.13732v1, 본문·참고문헌·부록24쪽 전체 정독.
날짜는 arXiv 최초공개 UTC. 소속·기여는 원문 당시.

## F: 원문
- F1 | p.1 및meta.json | "LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos" | 제목.
- F2 | p.1 저자란 | "Zhiyuan Xiang", "Peidong Liu", "Mingyang Li", "Jiawei Li", "Wenhow Li", "Wenbo Ding", "Xiang Deng" | 저자7명. 공동기여Xiang/Liu/MingyangLi, 교신Liu/JiaweiLi/Deng.
- F3 | p.1 소속번호 | "Joy Future Academy, JD"; "Harbin Institute of Technology, Shenzhen"; "Tsinghua SIGS, Tsinghua University"; "The Hong Kong University of Science and Technology (Guangzhou)" | JD·하얼빈공대선전·칭화SIGS·HKUST광저우 공동소속. 모두같은기관아님.
- F4 | p.1 §1 | "human videos lack robot action labels"; "cannot be directly mapped to robot control spaces" | 사람영상과로봇명령의라벨간격.
- F5 | p.4 §3.2; p.15 B.1; p.16 Table9 실제설정 | "Given adjacent frames"; "The latent action is parameterized as a 32-dimensional continuous Gaussian posterior." | 두프레임을본encoder가평균·분산으로정한32차원연속잠재분포를냄. decoder는현재장면과잠재를받아다음장면복원. 라벨제작시미래프레임도봄.
- F6 | p.4 §3.2 | "decoder that separately receives current visual context"; "encourages" | 배경은현재프레임에서받고잠재에는변화정보담도록유도,완전분리보장아님.
- F7 | pp.2–5 §3 | "continuous Latent Action Model"; "fixed discrete codebook can over-compress" | 연속표현으로미세한변화보존하려는설계. 이산방식전부불가능/최초연속주장금지.
- F8 | pp.4–5 §3.2 | "LPIPS", "Frozen DINOv2", "A frozen RAFT" | 픽셀차이와지각특징·의미특징·광류를맞춤. 광류=영상위치별겉보기이동장. 물리접촉힘/정확한관절상태측정아님.
- F9 | p.5 §3.3; pp.15–16 B.1 | "same action expert across three stages"; "No separate human-video head, adapter, or reinitialization is introduced." | 1사람잠재예측→2로봇행동정렬→3과제후학습. 동일행동모듈,목표전환. 입력은시각·언어등context, 실제추론은실행가능로봇명령.
- F10 | p.5 §3.3 | "LAM-encoded actions are used only as scalable Stage-1 supervision." | LAM은사전라벨용,실제추론때미래정답프레임보고명령만드는것아님.
- F11 | pp.3,14 Table8 | "23.3K-hour"; "5.1K-hour cleaned subset" | LAM학습23,300시간, 정책mainStage1 5,100시간. scale1K/3K/5K=1000/3000/5000;이둘구별.
- F12 | p.14 Table8; p.15 | "10.0K", "0.0K"; "2.9K" | Egocentric10K는LAM에는포함/Stage1scale에는제외, 손pose없는비교공정성. 자체사람영상8500h→Stage1 2900h,전부웹수집아님.
- F13 | pp.14–15 A.2 | "remove near-duplicate clips"; "discard segments dominated by strong blur, extreme ego-camera motion" | 깨짐/흐림/카메라주도움직임/가림/손-물체약한영상필터. scale집합가능한범위내중첩,모든원본동일분포보장아님.
- F14 | p.5 §4.1; p.18 D | "AgiBot G1"; "250 hours"; "50 demonstrations per original real-robot task" | 로봇한플랫폼,정렬데이터250h+원래3과제각50시연후학습. 사람영상만으로제로샷아님.
- F15 | p.18 D.1, D.3 | "20 evaluation trials per task"; "Mouse Pad, Headphones, and Cup" | 주scaling3과제각20회=60회. 성공기준종료때과제목표상태. 더어려운4과제별도.
- F16 | p.7 Figure4; p.19 Table14,15 | "63.3% at 1K hours to 80.0% at 3K hours and 85.0% at 5K hours" | LAM은23.3K항상고정,Stage1양만변경. 로봇데이터·구조·후학습schedule고정.
- F17 | p.19 Table15 직접전사 | LAPT행 Cup:1K70.0,3K95.0,5K75.0;Mouse50.0/70.0/85.0;Head70.0/75.0/95.0 | 평균증가가모든과제단조증가아님. 원문 Table15 3K→5K 컵95.0→75.0.
- F18 | p.7 §4.3; p.19 Table14 | Hand motion "58.3", "75.0", "55.0"; DreamDojo5K "76.7" | 같은데이터늘려도손추정baseline3K75→5K55. 추정오류누적설명은"may explain"가설. LAM기법모두동일효과아님.
- F19 | p.7 Table4; p.19 Table16 | "None Standard 55.0"; "Extended, compute-matched 53.3"; "5K hours Standard 85.0" | Stage1제거동일초기화·로봇데이터·2/3schedule55,Stage2연산량보충53.3,full85. 추론단순학습시간효과만으로설명어렵지만모든요인인과분리증명아님.
- F20 | p.7 Table5 | Fullw/oflow "34.3012", "77.8"; Full "34.4217", "89.3" | PSNR높아도RoboTwinHarddrop11.5pp. 두경우사전라벨→정책재학습. 실제로봇성공률77.8이라고쓰면오류.
- F21 | p.6 Tables1–2 | RoboTwinEasy90.0/Hard89.3;RoboCasa64.8 | simulation수치, main5.1K. RoboCasa24tasks×50rollouts(p18). 실제로봇주표85와별개.
- F22 | p.8 §4.5; p.24 H | "200 demonstrations per task"; "20 trials per task per domain" | 어려운4과제종이공버리기/펜/자가가림지우개잡기/책넣기. 한공동정책,과제당200시연. 4과제×4domain×20=320회/방법.
- F23 | p.8 Table6;p.24 Table19 | LAPT85/75/70/70/75;π0.5 85/50/45/40/55 | seen/position/light/background/all4domainavg. 익숙한조건동률85,변경조건70–75vs40–50. 작업별개별70~75라는뜻아님각domain4taskavg.
- F24 | p.9 Figure6 §4.7 | "keep the target visual context fixed but replace its latent action"; "Across the examples" | 사람ego 영상세donor-target예시잠재교체,장면대체없이단기변화경향달라짐. 실제로봇에서자유행동교환증명아님.
- F25 | p.9 §5 | "not guaranteed to align with independently controllable robot degrees of freedom" | 잠재축이관절제어축아님,로봇정렬필요. weakmotion/occlusion/egocamera/embodimentgap한계.
- F26 | p.9 §5 | "seven tasks and one target platform, with 20 trials per condition" | coverage작음,추정정밀도한계·broaderdeploymentvalidation필요. 논문은평가seed반복·통계유의성입증제시안함(본문과부록확인).
- F27 | p.16 Table9 | "32 H200 GPUs"; "4,938 H200 GPU-hours"; "1,700 H200 GPU-hours" | LAM학습4938GPUh+오프라인주석1700GPUh,policy비용별도. 영상데이터접근성≠연산공짜.
- F28 | p.8 Table7;p.20 Table17 | "PSNR"; "LARY" | 영상복원/행동분류진단은실제로봇실행평가와다름. 원문Table17 LAPA값과Table7 VQ-LAM값동일하나baseline설명혼동가능,성과비교에사용안함.
- F29 | p.5 §3.3; p.15 A.2 | "posterior mean for one human-video transition"; "posterior means" | LAM학습분포샘플링과정책Stage1라벨의평균값사용을구분.

## W: 공개상태
- W1 | https://arxiv.org/abs/2610.13732v1 (2026-10-16) | "Fri, 9 Oct 2026 15:29:20 UTC"; "Accepted at CoRL 2026; 24 pages including appendix" | 공개10월9일UTC/한국10월10일00:29. 저자등록상CoRL채택,공식결정독립확인상태lineage-audit따름.
- W2 | https://arxiv.org/html/2610.13732v1 (2026-10-16) | "License: CC BY 4.0" | 출처/원저자/크롭·resize변경명시.
- W3 | https://doi.org/10.48550/arXiv.2610.13732 (2026-10-16),abs | "pending registration" | arxivDOI등록대기표기. 학술지DOI아님.

## I: 계산·해설
- I1 | F15–F17 원문과제별셀 | 1K:10+14+14=38;5K:17+19+15=51;분모60 | 63.3%=38/60반올림,85%=51/60. 총성공13회차이. 별도반복학습일반통계확정아님.
- I2 | F17 | 95%×20=19;75%×20=15 | 컵3K19/20→5K15/20,20%p차이. 단발표본수제한함께.
- I3 | F8,F20 | 광류=프레임사이영상겉보기이동 | 픽셀복원점수가행동성공보증안함. 89.3−77.8=11.5%p.
- I4 | F5,F6,F9 | 예시 | 손이물체로다가가는두장면의변화를짧은숫자로담는설명은직관용,힘·로봇관절정답라고하지않음.
- I5 | F11 | 23.3×1000=23,300;5.1×1000=5,100;1K=1000;3K=3000;5K=5000 | 데이터크기한국어변환.
- I6 | F19,F26 | 해설자추론·제안 | 반복학습seed/신뢰구간/다른기체/긴작업실험은추가로확인할검증제안,완료연구아님.
- I7 | p.16 Table9 | 32×154.3=4937.6≈4938 | GPU시간은장수×가동시간누적단위,실험경과시간4938h라는뜻아님.

## L: 계보 및 사람
- L1 | priors/arxiv-2410.11758/paper.pdf pp.1,4–5 §§3.1–3.3,공식abs (2026-10-16) | "latent actions are not actual delta end-effector actions or joint actions" | LAPA 2024-10-15 UTC공개,SeonghyeonYe/JoelJang등16명,KAIST/UW/MSR/NVIDIA/AI2. 이산VQ잠재행동사전학습후로봇행동미세조정. ICLR2025논문표기확인. 선택논문의선행접근·비교대상,직접확장인과아님.
- L2 | priors/arxiv-2510.21571/paper.pdf pp.1,4–6 §3; https://microsoft.github.io/VITRA/ (2026-10-16) | "Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos" | VITRA 2025-10-24 UTC,QixiuLi등17,Tsinghua/MSRA. 3D손+카메라복원→행동분절→명령라벨. 공식프로젝트ICRA2026. 이번handbaseline이VITRA전체재현이라고하지않음.
- L3 | priors/arxiv-2511.16407/paper.pdf p.3 §4.1;공식CVF https://openaccess.thecvf.com/content/CVPR2026/html/Bu_LAOF_Robust_Latent_Action_Learning_with_Optical_Flow_Constraints_CVPR_2026_paper.html (2026-10-16) | "LAOF: Robust Latent Action Learning with Optical Flow Constraints" | LAOF 2025-11-20 UTC,XizhouBu등6,Fudan/NorthwesternPolytechnical. latent→flow전용decoder,이번은재구성영상RAFT정렬. CVPR2026공식게재. 광류/연속잠재최초주장불가.
- L4 | priors/arxiv-2609.15870/paper.pdf pp.1–3;이번p3[40] | "WLA³: World Latent Action Modeling for Semantics, Dynamics, and Kinematics" | 2026-09-14 UTC공개. PeidongLiu/ZhiyuanXiang/MingyangLi/JiaweiLi4명같고교신메일2일치. 팀당시JoyFutureAcademy/JD. 이번이인용한같은팀전작이지후속아님. WenhaoLi/WenhowLi동일인확인안해제외.
- P1 | 선택p1/전작WLA3p1비교, lineage-audit.md | "Equal contribution"; "Corresponding authors" | 공동기여3명·교신3명F2매핑. 저자역할은표기이상추정안함. 개발학습연구맥락으로같은팀이전작을인용함만주장.
- W4 | title/ID와officialCoRL/OpenReview검색, lineage-audit.md (2026-10-16) | 공식결정·직접후속원문미확인 | 저자arXiv에Accepted표기있으나공식결정독립미확보. 직접후속/독립재현찾지못함,절대없음단정금지.
