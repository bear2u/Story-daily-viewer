# 계보·저자·발표 상태 확인 메모

확인일: 2026-10-19 UTC. 본문 저술용 조사 메모이며 공개 해설 초안이 아님. 모든 선행논문은 arXiv 공식 PDF를 내려받아 관련 절을 직접 읽었음. 쪽수는 PDF 물리 쪽과 인쇄 쪽이 일치하는 범위로 표기. `filesources/`에 PDF 및 `pdftotext -layout` 텍스트 저장.

## 한눈에 보는 실제 관계

| 선행연구 | 이번 논문과 확인된 관계 | 독자가 오해하기 쉬운 표현 |
|---|---|---|
| CREATE (Wadhwa 등, 2026) | 동일 제1저자의 평가 지표 Creative Utility를 학습 보상으로 개조. 이번 논문 §2, p3에서 명시 | 'CREATE의 후속 학습 연구'는 가능. 'CREATE 전체 과제를 그대로 풀었다'는 아님 |
| DARLING (Li 등, 2025) | 품질·다양성을 함께 최적화하는 가장 가까운 경쟁 목적함수. 이번 연구가 자기 과제에 재구현 | '다양성 RL을 처음 제안'하면 틀림. 원래 DARLING의 학습된 모델을 그대로 비교한 것도 아님 |
| AI Can Learn Scientific Taste (Tong 등, 2026) | off-the-shelf SciJudge-30B를 품질/잠재 영향력 보상 모델로 사용, 이번 논문 p4 | 실제 과학적 타당성·장기 영향력을 실측한 채점기가 아님 |
| GIANTS (He-Yueya 등, 2026) | GiantsBench 학습 target 풀과 별도 평가 벤치마크를 사용. GIANTS-4B와 비교 | 동일 목표를 완전히 공정하게 이긴 일반 AI 과학자 비교로 확대하면 안 됨. GIANTS는 gold insight 재구성 유사도 학습 |

정리용 서술: **여러 답의 가치를 재는 지표(CREATE), 서로 다른 답을 학습시키는 경쟁 방법(DARLING), 아이디어의 영향력을 비교하는 심사 모델(SciJudge), 기존 논문에서 다음 아이디어를 재구성하는 데이터와 모델(GIANTS)이 이번 연구에서 만남.** 이는 조사자의 종합이며 저자들이 명명한 공식 4단계 계보는 아님.

## 1. CREATE

- 정식 제목: CREATE: Testing LLMs for Associative Creativity.
- 저자: Manya Wadhwa, Tiasa Singha Roy, Harvey Lederman, Junyi Jessy Li, Greg Durrett.
- 첫 공개: 2026-03-10 17:58:44 UTC. 조사에 읽은 버전: v2, 2026-05-11.
- 당시 소속(PDF p1): Wadhwa·Roy·Durrett = New York University; Lederman·Li = The University of Texas at Austin.
- 공식 원문: https://arxiv.org/pdf/2603.09970v2
- 메타데이터: https://arxiv.org/abs/2603.09970
- 공식 프로젝트: https://manyawadhwa.github.io/projects/create/
- 로컬: `filesources/create-2603.09970v2.pdf`, `.txt`.
- 직접 읽은 관련절: p3 §3.1의 수식 (1)과 (2), p4 §3.2, p1 저자·소속.
- 내용: 개념 사이의 참이고 구체적인 연결 경로를 여러 개 생성하게 하는 벤치마크. 집합의 각 경로 품질에 앞서 선택된 경로와의 최소 거리를 곱해 누적하며, 사용자 인내 γ와 최선 순서를 고려. NoveltyBench를 바탕으로 연속 거리를 사용하고 정규화 항을 없앴다고 각주에 밝힘. 따라서 CU가 아무 선행 없이 새로 나온 지표라고 쓰지 말 것.
- 이번 논문의 개조: 학습할 때 γ를 없애 후반 아이디어도 동등하게 취급. 최선 순서를 찾는 대신 모델이 출력한 순서를 그대로 사용. 평가에서는 원래 CU 사용(이번 논문 p3).
- 발표 상태: Wadhwa 홈페이지의 CREATE 항목은 **Arxiv 2026**. TAUR 공식 연구실 목록도 preprint. 이번 조사에서 정식 학회 채택은 확인하지 못함. 미채택이라고 단정하지 않음.
- 사용할 수 있는 짧은 직접 인용(6 words, p3): “We evaluate on two dimensions.” 추가 원문 인용 총량은 이 논문 출처 합계 25 words 이내 권장.

## 2. DARLING

- 정식 제목: Jointly Reinforcing Diversity and Quality in Language Model Generations.
- 저자: Tianjian Li, Yiming Zhang, Ping Yu, Swarnadeep Saha, Daniel Khashabi, Jason Weston, Jack Lanchantin, Tianlu Wang.
- 첫 공개: 2025-09-02 17:38:47 UTC. PDF p1의 본문 날짜는 September 3, 2025. arXiv 첫 공개 시각과 혼동하지 말 것.
- 당시 소속(PDF p1): Li = Meta FAIR / Johns Hopkins University, Zhang = Meta FAIR / Carnegie Mellon University, Khashabi = Johns Hopkins University, Yu·Saha·Weston·Lanchantin·Wang = Meta FAIR. Li와 Zhang은 Meta 인턴십 중 수행 각주.
- 공식 원문: https://arxiv.org/pdf/2509.02534v1
- 메타데이터: https://arxiv.org/abs/2509.02534
- 로컬: `filesources/darling-2509.02534v1.pdf`, `.txt`.
- 직접 읽은 관련절: p3 §3.1과 p4 §3.2 수식 (5)–(6), p1.
- 내용: 같은 프롬프트의 여러 rollout을 의미상 동등한 집단으로 묶고 각 응답의 그룹 내 다양성을 품질 보상에 곱함. 응답 하나를 뽑을 때마다 그 응답과 다른 rollout들의 관계로 보상. 이번 논문은 한 번의 생성 안에서 아이디어 세 개를 함께 쓰고, 그 세트 내부의 순차적 최소 거리로 보상.
- 발표 상태: Tianjian Li 본인 홈페이지 https://tianjianl.github.io/ 의 September 2026 업데이트가 **NeurIPS 2026 채택** 명시. Selected Works에도 NeurIPS 2026. 검색되는 OpenReview의 'Under review as a conference paper at ICLR 2026' PDF는 과거 심사 버전이며 최종 상태 근거로 쓰지 말 것. 이번 조사에서 NeurIPS 공식 proceedings/OpenReview decision까지는 교차 확인하지 못했으므로 '저자 홈페이지에 따르면 NeurIPS 2026 채택'이 가장 정확함.
- 인용 후보(8 words, p4): “We choose to multiply the two reward scores”.

### 중요한 비교 제한

이번 논문 p5는 DARLING 재현과 Proposed 사이의 의도한 차이가 다양성을 강제하는 위치라고 설명함. 그러나 Appendix B.3는 DARLING이 **task-specific SFT 없이 Qwen3-8B에서 GRPO로 시작**, Proposed는 **SFT 후 GRPO**라고 명시. 또 DARLING 원래의 learned equivalence classifier와 품질 보상을 이번 논문의 gpt-oss-120b 및 SciJudge로 바꿈. 따라서 '다른 것은 오직 set 내부/rollout 사이 하나뿐인 통제실험'으로 서술하면 지나침. no-SFT ablation을 따로 보고 위치 차이와 warm-start 차이를 함께 해석해야 함.

## 3. GIANTS

- 정식 제목: GIANTS: Generative Insight Anticipation from Scientific Literature.
- 저자: Joy He-Yueya, Anikait Singh, Ge Gao, Michael Y. Li, Sherry Yang, Chelsea Finn, Emma Brunskill, Noah D. Goodman. He-Yueya와 Singh 공동 기여.
- 첫 공개: 2026-04-10 18:13:55 UTC, v1.
- 당시 소속(PDF p1): Sherry Yang = New York University; 나머지 7명 = Stanford University.
- 공식 원문: https://arxiv.org/pdf/2604.09793v1
- 메타데이터: https://arxiv.org/abs/2604.09793
- 공식 프로젝트: https://giants-insights.github.io/
- 로컬: `filesources/giants-2604.09793v1.pdf`, `.txt`.
- 직접 읽은 관련절: p3 §2 task, p5 evaluation 및 §3.1, p6 §3.2, p12 limitations, p1.
- 내용: 두 parent paper의 요약을 받아 실제 downstream paper의 핵심 통찰을 재구성. GIANTS-4B는 gold와의 의미 유사도를 GRPO 보상으로 사용. 학습 심사는 Gemini-2.5-Flash, 주 평가 심사는 Gemini-3-Pro로 구분. 즉 좋은 아이디어를 여러 갈래 탐색하는 이번 목표와 다름.
- 이번 논문 연결: GiantsBench 학습 split의 논문을 target로 삼지만, 전체 인용 맥락에서 source를 다시 고르고 3개 이상 source 문서인 사례를 남김(이번 p4). 기존 두-source GiantsBench에서도 별도 평가(p5). 따라서 'GIANTS 데이터 그대로'보다 'target 풀을 재사용하고 문서 구성을 다시 만듦'이 정확함.
- 발표 상태: 공식 프로젝트·arXiv와 NYU 그룹 공개 목록에서는 preprint로 확인. 이번 조사에서 별도 채택 공지는 확인 못함.
- 인용 후보(7 words, p12): “Citations do not always reflect true conceptual influence”. 실제 문장은 뒤에 and절로 이어짐.

## 4. SciJudge / Scientific Taste

- 정식 제목: AI Can Learn Scientific Taste.
- 저자(v3 순서): Jingqi Tong, Mingzhe Li, Hangcheng Li, Yongzhuo Yang, Yurong Mou, Weijie Ma, Hongji Chen, Xiaoran Liu, Qinyuan Cheng, Ming Zhang, Qiguang Chen, Weifeng Ge, Qipeng Guo, Tianlei Ying, Tianxiang Sun, Yining Zheng, Zhiheng Xi, Xinchi Chen, Jun Zhao, Ning Ding, Xuanjing Huang, Yu-Gang Jiang, Xipeng Qiu.
- 첫 공개: 2026-03-15 16:31:51 UTC. 읽은 버전: v3, 2026-08-19.
- 당시 소속(PDF p1): 중심은 Fudan University / Shanghai Innovation Institute / OpenMOSS Team. Ning Ding = Tsinghua University; Qiguang Chen = Central South University. Tong·Mingzhe Li·Hangcheng Li 공동 기여.
- 공식 원문: https://arxiv.org/pdf/2603.14473v3
- 메타데이터: https://arxiv.org/abs/2603.14473
- 저자 저장소: https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste
- 로컬: `filesources/scijudge-2603.14473v3.pdf`, `.txt`.
- 직접 읽은 관련절: p3 정의, p5 §3.1, p6 §3.2–3.3, p13 limitations, p1.
- 내용: 같은 분야·비슷한 시기 논문의 상대 인용수를 community feedback으로 삼아 비교 심사 모델 Scientific Judge를 학습. 그 심사 모델로 아이디어 생성 모델도 학습. 이번 연구는 SciJudge-30B를 만들어진 외부 품질 채점기로 가져옴. 이는 실제 인용수를 미리 아는 모델이 아니라, 제목·초록 등에서 상대 영향력을 예측하도록 학습한 모델.
- 제한: 원논문 p13은 인용수에 남은 편향, 지연된 영향력, 아이디어 실험 미검증, 제목·초록 중심 학습을 인정. 따라서 이번 연구의 SciJudge win rate를 '과학적으로 참일 확률'이나 '실제 인용 성공률'로 해석하면 안 됨.
- 발표 상태: arXiv에 학회 게재 정보 없음. 이번 조사에서 채택은 확인하지 못함. 검색 결과의 다른 논문 AAAI 2026 채택 문구가 인접 노출되므로 연결 금지.
- 인용 후보(9 words, p13): “citations are an imperfect form of community feedback.”

## 이번 논문 저자와 근황을 분리해서 쓰기

- 이번 논문 PDF p1: Manya Wadhwa = NYU, Pranav Narayanan Venkit·Hiroaki Hayashi·Yu Li·Chien-Sheng Wu = Salesforce AI Research, Tuhin Chakrabarty = Stony Brook University. Wadhwa 연구가 Salesforce 인턴십 중 진행되었다는 각주 있음.
- 현재 자기소개(본인 홈페이지 https://manyawadhwa.github.io/, 확인 2026-10-19): NYU PhD student, Greg Durrett·Jessy Li 공동지도. 2026년 9월 Meta/FAIR NYC Visiting Research Scientist 시작. 2026년 5월 Salesforce Research 인턴 시작 공지. 따라서 '현재 Salesforce 소속'으로 적으면 부정확할 수 있음.
- 연구 흐름은 본인이 홈페이지에 직접 구분: CREATE 등 모델 평가 연구와 SkillFactory·Set-level RL 등 모델 학습 개선 연구. 권위를 내세우기보다 '평가 지표를 만든 사람이 이번엔 그 지표와 닮은 목표로 학습시켰다'가 논문 내용에 맞는 맥락.
- 기관 이름만으로 성과나 신뢰도를 추론하지 않음. 다른 공동저자의 실시간 근황은 이번 조사 범위에서 확인하지 않았음.

## 현재 상태·독립 후속 검증 검색

- https://arxiv.org/abs/2610.22324 는 2026-10-15 v1 한 번의 제출, Comments에 Under Review 명시. PDF 매 페이지에도 Preprint. Under Review. 저자 홈페이지도 Under review.
- 2026-10-19 현재 검색어: 정식 제목 + replication / accepted, arxiv ID 2610.22324 + replication / reproduce / follow-up / accepted. routine 검색과 최신 system1 검색을 모두 수행.
- 결과는 원문·저자 페이지 및 10월17–18일 소개/요약 페이지 위주. **이번 조사에서 독립 후속 논문·독립 재현 실험·정식 채택 공지는 확인하지 못함.** 공개 4일 전 논문이라 찾지 못했다는 사실과, 존재하지 않는다는 단정은 구분. arXiv 페이지의 Replicate는 범용 서비스 토글이지 재현 성공 표식이 아님.
- code and data URL이 논문에 있다는 것은 공개 실행 가능한 완전 재현 패키지가 검증됐다는 뜻이 아님. 이 조사에서는 저장소 설치/실행/모델 가중치 공개 여부를 검증하지 않음.

## 웹 근거 참조 ID (root는 실제 인용 전에 해당 URL을 다시 open해야 함)

- 메인 arXiv 상태: `turn224view0` https://arxiv.org/abs/2610.22324
- CREATE 메타: `turn218view0`; 원문 HTML `turn220view0` https://arxiv.org/html/2603.09970v2
- DARLING 메타: `turn218view1`; 원문 HTML `turn220view1` https://arxiv.org/html/2509.02534v1 ; 주의: HTML은 p1 날짜가 August24,2026로 보이지만 내려받은 고정 v1 PDF는Sep3,2025. 발표일은 arXiv submission history 기준으로 삼음.
- GIANTS 메타 `turn218view2`; 원문 HTML `turn220view2`; 프로젝트 `turn222view2` https://giants-insights.github.io/
- Scientific Taste 메타 `turn218view3`; 원문 HTML `turn220view3` https://arxiv.org/html/2603.14473v3
- Wadhwa 본인 근황/이번 논문 Under review/CREATE 상태 `turn222view0` https://manyawadhwa.github.io/
- Li 본인 NeurIPS2026 채택 공지 `turn222view1` https://tianjianl.github.io/
- TAUR 공식 CREATE preprint 목록 `turn219search9` https://cims.nyu.edu/taur/publications.shtml
