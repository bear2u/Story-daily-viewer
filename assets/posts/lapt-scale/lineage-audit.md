# 계보·저자 감사 — LAPT-Scale

확인일: 2026-10-16 KST. 전작의 날짜는 arXiv v1 최초 공개 UTC로 통일함.
이 파일은 조사 기록이며 report.md/ledger.md는 수정하지 않았음.

## 확보·열람 범위

- 대상 LAPT-Scale 원문 첫 페이지·관련 연구 §2·방법 §3과 참고문헌을 직접 대조함.
- 전작 4편의 공개 PDF를 `priors/arxiv-<ID>/paper.pdf`로 확보함. 각각 meta.json, text.txt, references.txt도 존재함.
- LAPA 27쪽, VITRA 36쪽, LAOF 16쪽, WLA³ 23쪽. 전작 모두 첫 페이지·서론·해당 방법 절을 직접 읽었음. 전작 전체 정독을 했다는 뜻은 아님.
- 이번 본문에서 전작 성과 수치는 쓰지 않고, 확인한 방법·관계만 이용하는 것을 권장함.
- LAPA 제목·저자·소속 크롭 `figures/prior_header.png` 생성, atomic 저장 후 직접 열어 선명함과 잘림을 확인함. 원본 arXiv v2 PDF p.1, 비율 bbox(0.10,0.06,0.91,0.265), 확대 2.8. 논문 CC BY 4.0을 공식 HTML에서 확인함.

## 전작 선택과 연대기

| 공개일 UTC | 논문·기관 | 확인한 방법 | 이번 논문과의 관계·근거 | 주의 |
|---|---|---|---|---|
| 2024-10-15 16:28:09 | Latent Action Pretraining from Videos (LAPA), KAIST·UW·Microsoft Research·NVIDIA·AI2 | 영상 두 프레임에서 VQ-VAE 기반 이산 잠재행동을 얻음. 관측과 지시문으로 잠재행동을 예측하도록 VLM을 사전학습하고 실제 로봇 행동으로 미세조정함 | 이번 p.1–3 [5]로 인용, VQ 방식 논의와 Appendix F Table 17 비교 대상. 무라벨 영상→잠재행동→로봇 정렬이라는 공통 계보. '확장' 인과 대신 '선행 접근·비교 대상'이 정확함 | LAPA도 로봇 라벨 데이터로 마지막 미세조정이 필요했음. LAPT-Scale이 처음 영상학습을 발명한 것 아님 |
| 2025-10-24 15:39:31 | Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos (VITRA), Tsinghua·Microsoft Research Asia | 3D 손·카메라 움직임 복원, 원자 행동 분절, 언어 명령 생성 후 VLA 사전학습 | 이번 p.1–2 [3]이 명시적 손 움직임 기반 의사행동 접근으로 언급. LAPT-Scale은 대신 LAM 기반 암묵행동을 생성한다고 §2에서 대조함 | 이번 hand-motion 비교선이 VITRA 전체 시스템을 동일하게 재현한 것이라고 하면 안 됨. 이번 Appendix C의 hand-motion baseline 구현으로 제한 |
| 2025-11-20 14:26:49 | LAOF: Robust Latent Action Learning with Optical Flow Constraints, Fudan·Northwestern Polytechnical | 다음 상태 재구성에 더해 잠재행동에서 광류 특징을 직접 예측하는 전용 flow decoder로 제약함 | 이번 p.3 [41]에서 재구성+광류 제약이라는 선행 연구로 명시. 이번은 재구성된 미래 프레임의 RAFT 광류와 관측 광류를 맞추는 방식이므로 동일 구현 아님 | '움직임을 학습 신호로 쓰는 건 이번이 최초' 금지. LAOF는 연속 표현도 논의·사용하므로 '연속 잠재행동 최초' 금지 |
| 2026-09-14 16:59:00 | WLA³: World Latent Action Modeling for Semantics, Dynamics, and Kinematics, Joy Future Academy·JD Group | 동기화 카메라와 가능한 로봇 상태 변화를 통합한 전이 표현. 잠재행동을 물리 동역학, VLM 의미 감독, 행동 전문가에 재사용 | 이번 p.3 [40] 잠재행동 모델 관련 연구로 인용. 같은 팀 저자 4명과 교신메일 2개가 겹침 | 이 논문이 먼저 공개됨. 이번의 후속작으로 배치하면 오류. 이번의 직접 방법 확장이라는 표현도 근거 부족 |

선택 권장: LAPA→VITRA→LAOF 세 편을 핵심 방법 계보로 쓰고, WLA³는 같은 팀 연구 맥락 한 문장만 추가함. 네 방법을 한 줄 인과 사슬로 만들지 말 것.

## 전작 메타데이터·원문 근거

### LAPA

- 제목: Latent Action Pretraining from Videos.
- arXiv: https://arxiv.org/abs/2410.11758 ; PDF https://arxiv.org/pdf/2410.11758v2 ; 원문 HTML https://arxiv.org/html/2410.11758v2.
- 저자 16명(arXiv 목록): Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Sejune Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter Fox, Minjoon Seo.
- PDF 표기는 Yuchen Lin, arXiv 표기는 Bill Yuchen Lin. 동일 목록 위치 차이로 기록하고 두 별개 저자로 세지 않음.
- p.1: Ye·Jeon·Joo·Kimin Lee·Minjoon Seo = KAIST, Joel Jang·Luke Zettlemoyer = UW, Jianwei Yang·Baolin Peng·Reuben Tan·Lars Liden·Jianfeng Gao = Microsoft Research, Ajay Mandlekar·Yu-Wei Chao = NVIDIA, Yuchen Lin = AI2, Dieter Fox = UW+NVIDIA.
- Ye와 Jang 공동기여. p.1 각주는 Ye MSR 인턴 당시 작업, Jang NVIDIA 인턴 당시 작업, 마지막 다섯 교수/연구자 equal advising 표기. 인턴·공동지도와 교신저자를 혼동하지 않음.
- 심사 상태: PDF 전 페이지 머리글 'Published as a conference paper at ICLR 2025', arXiv 코멘트 ICLR 2025, 공식 코드 저장소도 ICLR 2025로 표기. https://openreview.net/forum?id=VYOe2eBQeh 는 실제 열람 시 브라우저 확인 화면으로 막혀 리뷰 결정 세부 내용은 확인하지 못함.
- 방법 위치: PDF §3.1–3.3 p.4–5. §3.1 짧은 근거 'latent action quantization model following Bruce et al. (2024)' — LAPA 자체도 Genie 계보임.
- §3.3 p.4: 'latent actions are not actual delta end-effector actions or joint actions' — 잠재행동 자체를 로봇 명령으로 설명하면 오류.
- 공식 프로젝트(저자·소속·방법 교차 확인): https://latentactionpretraining.github.io/ . 라이선스 CC BY 4.0은 공식 arXiv HTML license 링크 확인.

### VITRA

- 정확한 제목: Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos.
- arXiv https://arxiv.org/abs/2510.21571 ; PDF https://arxiv.org/pdf/2510.21571v1 ; 공식 프로젝트 https://microsoft.github.io/VITRA/ .
- 저자 17명: Qixiu Li, Yu Deng, Yaobo Liang, Lin Luo, Lei Zhou, Chengtang Yao, Lingqi Zeng, Zhiyuan Feng, Huizhi Liang, Sicheng Xu, Yizhong Zhang, Xi Chen, Hao Chen, Lily Sun, Dong Chen, Jiaolong Yang, Baining Guo.
- 첫 페이지 기준 Qixiu Li·Zhiyuan Feng·Huizhi Liang = Tsinghua University+Microsoft Research Asia, 나머지 = Microsoft Research Asia. Qixiu Li·Yu Deng·Yaobo Liang·Lin Luo 공동기여. Jiaolong Yang 교신.
- 심사: 공식 Microsoft 프로젝트 첫 화면이 ICRA 2026 표기. arXiv 메타데이터만 보면 학회 미표기이므로 공식 프로젝트로 보강함. 논문 세부 리뷰는 미확인.
- 방법 원문 §3.1 p.4–5: 카메라 intrinsics 추정·손 재구성·카메라 pose tracking을 결합해 world-space 3D hands를 복원함. §3.2 p.5: 손목 속도 최소점을 분절 기준으로 사용. §3.3 p.6: GPT-4.1로 행동명령 생성. 이 원문 근거로 '손을 추적해 명시적 동작 라벨을 만든다'라고 쓰는 것은 허용.
- 이번 논문의 '손 추적이 그럴듯하게 틀릴 수 있다'는 해석을 VITRA 자체의 실패 입증처럼 전달하지 말 것. VITRA는 자기 실험에서 scaling을 보고하며, 이번 다른 조건의 hand-motion 결과가 이를 일반 반박한 것은 아님.

### LAOF

- 제목: LAOF: Robust Latent Action Learning with Optical Flow Constraints.
- arXiv https://arxiv.org/abs/2511.16407 ; PDF https://arxiv.org/pdf/2511.16407v2 ; 공식 CVF https://openaccess.thecvf.com/content/CVPR2026/html/Bu_LAOF_Robust_Latent_Action_Learning_with_Optical_Flow_Constraints_CVPR_2026_paper.html .
- 저자 6명: Xizhou Bu, Jiexi Lyu, Fulei Sun, Ruichen Yang, Zhiqiang Ma, Wei Li.
- p.1: 앞 네 명·Wei Li = Fudan University, Zhiqiang Ma = Northwestern Polytechnical University. Wei Li 교신.
- 심사: CVF 공식 CVPR 2026 proceedings, pp.27334–27344; arXiv v2 코멘트 CVPR 2026도 일치함.
- 방법 §4.1 p.3: IDM이 전후 상태에서 z를 추정, FDM이 현재 상태+z에서 다음 상태를 예측. 별도 flow decoder가 z에서 optical-flow features를 복원함. §4.2에서 sparse action labels를 더 쓰는 LAOF-Action을 별도 제안함.
- 이번 §3.2의 RAFT 정렬은 재구성 영상의 흐름을 정답 영상 흐름에 맞추는 것이므로 LAOF의 전용 latent→flow decoder와 구별해야 함.
- 결과 수치와 '라벨 없이도 1% 라벨 방법 이상' 같은 주장은 과제 조건 설명 없이는 보고서에 넣지 않는 편을 권장함.

### WLA³ — 사람 맥락용

- 제목: WLA³: World Latent Action Modeling for Semantics, Dynamics, and Kinematics.
- arXiv https://arxiv.org/abs/2609.15870 ; PDF https://arxiv.org/pdf/2609.15870v1 ; 저자 프로젝트 https://wla-3.github.io/ .
- 저자: Peidong Liu, Zhiyuan Xiang, Mingyang Li, Wenhao Li, Jiale Zhang, Jiahao Sun, Jiawei Li. PDF p.1 소속 전원 Joy Future Academy, JD Group.
- Peidong Liu·Zhiyuan Xiang 공동기여, Peidong Liu·Jiawei Li 교신.
- arXiv 코멘트/첫 페이지에서 학회 채택 확인 못함. 확인일 기준 프리프린트로만 표현.
- p.1–3의 world-state transition modeling 및 semantics/dynamics/kinematics 활용을 직접 확인함. 이번은 이를 인용하나 'WLA³의 확장'이라고 선언하는 근거는 없음.

## 이번 저자 7명 정확 매핑 (PDF p.1 기준)

| 이름 | 논문상 소속 | 기여·교신 |
|---|---|---|
| Zhiyuan Xiang | Joy Future Academy, JD + School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen | 공동기여 |
| Peidong Liu | Joy Future Academy, JD | 공동기여·교신 |
| Mingyang Li | Joy Future Academy, JD + Tsinghua SIGS, Tsinghua University | 공동기여 |
| Jiawei Li | Joy Future Academy, JD | 교신 |
| Wenhow Li | Joy Future Academy, JD + Artificial Intelligence, The Hong Kong University of Science and Technology (Guangzhou) | 별도 공동기여 표기 없음 |
| Wenbo Ding | Tsinghua SIGS, Tsinghua University | 별도 공동기여 표기 없음 |
| Xiang Deng | School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen | 교신 |

교신메일: lpd19@tsinghua.org.cn / li-jw15@tsinghua.org.cn / dengxiang@hit.edu.cn.
메일 도메인이 칭화라도 Peidong Liu를 이번 논문상 칭화 소속으로 바꾸면 안 됨.
이번 Wenhow Li와 WLA³ Wenhao Li는 철자가 다름. 원문만으로 동일인 판단 못하므로 교집합에서 제외함.
확실한 공통 저자는 Peidong Liu·Zhiyuan Xiang·Mingyang Li·Jiawei Li 네 명. Joy Future Academy 소속과 Liu·Jiawei Li 교신메일 두 개가 양쪽 PDF에서 일치함. LAPA/VITRA/LAOF와 이번 사이에는 명시 목록상 이름 교집합 없음.

## 심사·발표일·현재성

- 대상 최초 공개 2026-10-09 15:29:20 UTC = 2026-10-10 00:29:20 KST. 원문 상단 날짜 '9 Oct 2026'와 로컬 날짜를 섞지 말 것.
- arXiv v1 코멘트에 'Accepted at CoRL 2026; 24 pages including appendix', PDF p.1 하단 '10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA.'가 있음.
- 그러나 확인일의 검색 `"LAPT-Scale" site:openreview.net`, `"2610.13732" site:openreview.net`, `"LAPT-Scale" site:corl.org`, `site:corl2026.org`에서 공식 결정문을 찾지 못함. 외부 aggregator의 CoRL 분류는 독립 학회 확인으로 계산하지 않음.
- 권장 본문: '저자 arXiv 등록 정보에는 CoRL 2026 채택으로 표기돼 있음. 학회 공식 결정문은 이번 확인에서 확보하지 못했음.'
- DOI https://doi.org/10.48550/arXiv.2610.13732 는 arXiv abs 페이지에서 DataCite pending registration으로 표시됨. DOI를 출판사 저널 게재 증거로 쓰지 않음.
- 직접 후속·독립 재현: 확인일 기준 정확한 제목/ID 검색에서 본 논문을 방법으로 인용한 후속 연구나 독립 재현을 찾지 못함. 이는 '존재하지 않는다'는 단정이 아님. WLA³는 날짜상 전작. 시점상 일주일 남짓이므로 후속 연구 부족을 기술 실패로 해석하지 않음.

## 보고서에 옮길 수 있는 짧은 문장

> 2024년 LAPA도 영상 변화에서 잠재행동을 만들고, 나중에 로봇 행동으로 맞추는 길을 썼음.
> 다만 그쪽은 이산 코드북이었음. 이번은 연속 표현과 세 정렬 신호를 같이 씀.
> 손 추적 라벨을 만드는 VITRA와 광류로 잠재행동을 제약한 LAOF도 그 사이에 있었음.
> 그러니 영상학습이나 광류를 처음 발명했다는 이야기는 아님.

이 문장들은 report 집필 시 각각 별도 원장 ID와 원문 위치를 붙여야 함. 이 파일만 링크하고 사실 추적을 생략하지 말 것.

## 웹 검증 참조(부모가 인용하려면 직접 열기 필요)

- 이번 abs 공식: https://arxiv.org/abs/2610.13732v1 (`turn174view0`).
- 이번 HTML 공식: https://arxiv.org/html/2610.13732v1 (`turn173view0`).
- LAPA 공식 abs/HTML: `turn177view0`, `turn179view1`.
- VITRA Microsoft 공식 프로젝트: https://microsoft.github.io/VITRA/ (`turn179view0`).
- LAOF 공식 CVF proceedings PDF: https://openaccess.thecvf.com/content/CVPR2026/papers/Bu_LAOF_Robust_Latent_Action_Learning_with_Optical_Flow_Constraints_CVPR_2026_paper.pdf (`turn177search13`).
- WLA³ 공식 abs: https://arxiv.org/abs/2609.15870 (`turn176view3`).
