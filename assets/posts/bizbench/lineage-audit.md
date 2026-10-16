# BizBench 계보·저자 맥락 독립 감사

확인일: 2026-10-17 KST. paper-report의 lineage.md, people-context.md, figures.md를 직접 읽고 적용했음. 이 파일은 원장 후보 자료이며 report.md와 ledger.md는 수정하지 않았음.

## 확보·열람 범위

- τ-bench: `priors/arxiv-2406.12045/paper.pdf` 50쪽 확보. v1 첫 페이지와 pp.1–5 서론·관련연구·방법·평가 정의 직접 읽음.
- τ-Knowledge: `priors/arxiv-2603.04370/paper.pdf` 29쪽 확보. v1 첫 페이지와 pp.1–6 서론·관련연구·방법·지식베이스·문맥관리·평가지표 직접 읽음.
- OneModel: `priors/2026-acl-industry-91/paper.pdf` 14쪽 확보. ACL 공식 게재본 첫 페이지, pp.1303–1306 서론·구조·배포·방법 직접 읽음.
- 세 전작 모두 스킬의 fetch_paper.py로 확보했으며 text.txt/meta.json도 남겼음. 전작 전체를 정독했다는 뜻은 아님. 선택 논문 BizBench 전체 정독과 구분할 것.

## 연대기와 관계

| 공개 기준 | 논문·당시 기관 | 실제 한 것 | BizBench와 확인된 관계 | 사용 가능한 범위 |
|---|---|---|---|---|
| arXiv v1 2024-06-17 19:33:08 UTC | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains; Sierra | API·정책 문서·LLM 사용자 사이의 대화를 평가하고, 마지막 DB 상태·필요 응답으로 보상 계산. 여러 번 모두 성공하는 pass^k 제안 | BizBench p.1 서론 및 p.3 §2에서 정책 기반 대화·사용자 협업의 선행 연구로 인용. p.12 참고문헌의 Yao et al.2025가 이 논문임 | '문제 제기' 계보. BizBench가 τ-bench 코드를 직접 확장했다거나 수치를 동일 조건으로 비교했다고 쓰면 안 됨 |
| arXiv v1 2026-03-04 18:34:47 UTC | τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge; Sierra + Princeton University | τ-Bench를 명시적으로 확장. τ-Banking의 698 문서, 발견형 도구, 지식 검색과 상태 변경을 함께 시험 | BizBench p.2는 여러 출처에 흩어진 업무 규칙을 설명하며 Shi et al.2026 인용. p.3 §2는 지식 기반 업무 선행 연구로 인용. p.6 §5.1은 문맥 초과 시 오래된 검색·문서읽기 출력 1/4 교체 정책을 따른다고 명시 | 지식 검색 평가의 '문제 제기', 문맥관리 부품의 '도구로 사용'. 전체 BizBench가 τ-Knowledge의 직접 확장이라는 문장은 근거 없음 |
| ACL 게재 월 2026-07; PDF 표기 학회기간 2026-07-02–07 | How to Train a Real-World Silicon Concierge? Internalizing Complex Business Workflow to Only OneModel; Ant International | 정적 원리는 CPT, 준정적 SOP는 SFT, 동적 거래정보는 문맥 주입으로 구분하는 단일모델 사업시스템. RL 정렬도 포함 | BizBench p.1의 자율 업무 실행 배경에 Tong et al.2026으로 인용. p.11 참고문헌은 정확히 ACL Industry91 게재본. BizBench와 이름·기관이 겹치는 2명 확인 | 같은 기관·일부 저자가 참여한 '문제 제기' 전작. OneModel이 BizBench 결과표에 평가됐거나 BizBench가 모델의 개선판이라는 근거 없음 |
| arXiv v1 2026-10-14 16:16:51 UTC | BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business; Ant International + Peking University | 끝 상태뿐 아니라 실행 기록의 승인·자금·보호 조건을 따로 체크 | 이번 논문 | 프리프린트. 2026-10-17 기준 확인한 공식 arXiv에 학회 채택 표기 없음 |

OneModel은 공식 ACL 페이지가 월 단위만 제공하므로 '최초 공개일 7월2일'이라고 단정하지 않음. 나머지는 arXiv 최초 공개 UTC 기준. 공개일 정밀도가 다름을 표에 명시했음.

## 전작 방법에서 중요한 원문 대조

### τ-bench

- v1 p.4 §3 Reward는 최종 DB 일치와 응답 정보 포함 여부를 곱함. 정책 준수 자체를 전부 추적하는 완전한 평가가 아니라는 한계를 저자 스스로 설명함.
- 같은 페이지에는 고객 명시 승인 없이 반품해도 보상 1이 될 수 있다는 예시가 있음. 따라서 “전작은 정책을 전혀 다루지 않았음”은 틀림. **정책은 제공하고 준수를 요구했지만, 마지막 상태 보상만으로 승인 위반까지 전부 검증되지는 않았음**이 정확함.
- pp.4–5 pass^k는 k번 중 하나 성공인 pass@k와 달리 **k번 모두 성공**하는 일관성 지표임. BizBench pass^3 설명의 계보에 쓸 수 있으나 동일 데이터셋 결과로 수치 비교하면 안 됨.

### τ-Knowledge

- p.1·p.3은 τ-Bench 직접 확장이라고 명시. 따라서 τ-bench → τ-Knowledge의 '확장' 관계는 사용 가능.
- p.3 §3 및 p.4 Table1: 지식베이스 698개 문서, 발견형 도구 51개, 상시 도구14개, 97개 과제. BizBench의 789/601/9/50과 섞지 말 것.
- p.3의 보상 정의는 목표 최종 DB 상태를 중심으로 함. 검색이 올바른 행동에 필요한 조건이 되도록 설계했음. 단순 RAG 질의응답 평가라고 축소하면 안 됨.
- p.6 Context Management는 문맥 초과 때 오래된 검색출력 1/4을 제거하고 재검색 가능함을 placeholder로 알림. BizBench p.6 §5.1에 이 방법을 따른다는 직접 문장이 있음.

### OneModel

- p.1303 첫 페이지는 ACL 게재본 저자 6명과 모두 Ant International 소속을 명시.
- pp.1304–1306 §3: 업무 원리·절차·실시간 데이터를 구분하여 모델 파라미터와 동적 문맥에 넣음. 모든 시시각각 변하는 정보를 가중치에 외운 모델이라는 설명은 틀림.
- 배포 성과 수치는 원문 pp.1304–1305에서 자체 온라인 A/B로 보고됨. 본 해설의 핵심은 BizBench 평가 설계이므로 전작 세부 성능 수치는 본문에 넣지 않아도 됨. OneModel을 BizBench에 측정한 성능으로 연결할 수 없음.

## 저자·소속·동일인 근거

| 논문 | 전체 저자 | 당시 소속·각주 | BizBench와 교집합 |
|---|---|---|---|
| τ-bench v1 | Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan | 첫 페이지는 네 명 모두 Sierra라고 표기. Shunyu Yao의 작업은 인턴십 중 수행 각주 있음. 현재 소속으로 바꾸지 않았음 | 없음 |
| τ-Knowledge v1 | Quan Shi, Alexandra Zytek, Pedram Razavi, Karthik Narasimhan, Victor Barres | Sierra: Shi/Zytek/Razavi/Barres; Princeton: Narasimhan. Shi와 Zytek 공동기여. 교신 Quan Shi, ben.s@sierra.ai | 없음 |
| OneModel ACL본 | Yongqi Tong, Xiaoyun Feng, Lyuxin Xue, Jianshe Li, Xin Zhang, Jiang-Ming Yang | 모두 Ant International | Yongqi Tong, Jianshe Li. Tong은 두 논문에 동일 메일 tongyongqi.yq@ant-intl.com. Li는 동일 이름·Ant International 기관에 더해 BizBench가 이 6명 전작을 명시적으로 인용하는 근거. Li의 메일은 BizBench에 개별 표기 없어 동일 메일 교차 확인이라고 쓰지 않음 |
| BizBench | Enhan Zhao, Yongqi Tong, Xuejun Yu, Hang Wang, Pan Wang, Yichao Wang, Di He, Jianshe Li, Wei Wu | Enhan Zhao: Peking + Ant; Di He: Peking; 나머지7명: Ant. Enhan Zhao와 Yongqi Tong 공동기여. Wei Wu 교신(wuwei19850318@gmail.com) | 위와 같음 |

τ-bench와 τ-Knowledge 두 전작의 이름 교집합은 Pedram Razavi와 Karthik Narasimhan임. 동일 Sierra 연구라인, 두 논문의 직접적인 확장 명시가 있어 이름만 기계적으로 합친 것과 다름. 다만 τ-bench 첫 페이지에 없는 개인 메일을 확인했다고 쓰지 않음.

OneModel 동일 제목 arXiv2608.20350 검색결과는 35명 저자와 ACL본의 6명 저자가 다르게 나옴. 검색 스니펫 날짜도 ID 월과 어긋남. 원문이 확인된 **BizBench가 실제 인용한 ACL DOI 10.18653/v1/2026.acl-industry.91의 6명 게재본만 사용**했음. 그 다른 버전과 저자·날짜·교집합을 합치지 않았음. 현재 소속·h-index·피인용 수·개인 경력 이동은 조사 확정 못했으며 본문에 넣지 않음.

## 공식 심사·게재 근거

확인일 2026-10-17.

- τ-bench: ICLR 2025 공식 proceedings에 논문과 네 저자·conference 표기 확인. arXiv v1의 'Under review'는 최초 버전의 상태이며 현재 게재 상태와 구분해야 함. OpenReview forum은 브라우저 검증벽이 있어 리뷰·결정 세부 내용은 사용하지 않았음.
- τ-Knowledge: **공식 PMLR v306, pp.112443–112471, ICML2026** 확인. PMLR BibTeX에 06–11 Jul 행사기간. arXiv v1은 Work in progress라고 적지만 현재도 미심사라고 쓰면 틀림. 별도 리뷰 점수·결정문은 읽지 않았음.
- OneModel: ACL Anthology 공식 2026.acl-industry.91, Industry Track, pp.1303–1316, 2026-07, DOI 확인. 심사 학회 게재본임. 비공개 리뷰를 확보했다는 주장 없음.
- BizBench: arXiv v1 2026-10-14 UTC, 공식 arXiv에 채택 주석이나 게재 정보 없음. 공식 학회 페이지 검색에서도 채택 근거를 얻지 못했음. 따라서 이 확인범위에서 프리프린트로 제시.

## 후속·독립 재현 조회 범위

2026-10-17 KST 웹 검색: 정확한 제목, arXiv2610.20424, BizBench+Enhan Zhao, reproduction/replication/extension/followup 조합을 사용. 두 검색엔진을 사용했으나 한쪽은 관련 없는 결과가 많았음. 확인 결과는 원문, 색인·자동 요약·뉴스 재서술뿐이었고 **이번 BizBench를 방법으로 인용한 직접 후속이나 결과를 독립 재현한 원문은 확보하지 못했음**. 논문이 공개된 지 얼마 안 됐으며 검색 색인 지연이 있을 수 있음. '후속 논문이 없다', '독립 재현이 전혀 없다'로 보편 단정하지 말 것.

## 전작 이미지

`figures/prior_tau.png`: τ-bench arXiv v1 p.1 제목·저자·Sierra 소속. 스킬 crop page1 bbox0.12,0.05,0.90,0.28. 직접 열어 보며 잘림 확인함. 원본 arXiv의 license 링크를 직접 따라가 **CC BY 4.0** 확인. 공개 시 저자4명, 제목, arXiv v1 URL, CC BY4.0 링크 및 제목부 크롭 변경 표시를 별도 출처/ATTRIBUTION에 둘 것.

## 원문·공식 링크

- τ-bench arXiv 최초공개·라이선스: https://arxiv.org/abs/2406.12045v1
- τ-bench PDF: https://arxiv.org/pdf/2406.12045v1
- τ-bench ICLR 공식: https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b126cc38b8638e07bef37e7b2bb72bf-Abstract-Conference.html
- τ-Knowledge arXiv 최초공개: https://arxiv.org/abs/2603.04370v1
- τ-Knowledge PDF: https://arxiv.org/pdf/2603.04370v1
- τ-Knowledge ICML 공식: https://proceedings.mlr.press/v306/shi26ah.html
- OneModel ACL: https://aclanthology.org/2026.acl-industry.91/
- OneModel ACL PDF: https://aclanthology.org/2026.acl-industry.91.pdf
- OneModel DOI: https://doi.org/10.18653/v1/2026.acl-industry.91
- BizBench: https://arxiv.org/abs/2610.20424v1
- 그림 라이선스: https://creativecommons.org/licenses/by/4.0/

## 편집 권고

이야기에서 쓸 수 있는 연결은 '2024년 τ-bench는 승인 위반이 최종 상태 보상에 걸리지 않을 수 있다고 스스로 적었음 → 2026년 τ-Knowledge는 문서 검색과 발견형 도구를 결합했음 → BizBench는 승인·자금 등이 **행동 당시** 맞았는지를 실행 기록으로 확인함'임. 이는 연구 설계 차이의 설명이며, BizBench가 두 전작에서 유일하게 처음 발견했다거나 모든 위반을 완벽히 검사한다는 뜻은 아님. 같은 팀 전작 OneModel은 업계 문제 맥락을 짚는 한두 줄이 적절함.
