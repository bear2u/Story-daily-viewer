# 검증한 계보와 저자 맥락
확인일: 2026-10-04 KST
날짜: arXiv 최초 공개, CORAL은 공식 게재월.

| 공개/게재 | 연구 | 이번 연구와 관계 | 원문에서 확인한 내용 | 원장 |
|---|---|---|---|---|
| 2020-05-22 | Lewis 외, Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Facebook AI Research·UCL·NYU) | 배경 | 위키피디아 검색 인덱스와 생성 모델의 결합, 초기 RAG는 end-to-end fine-tuning | L1 |
| 2024-05-23 | Gutiérrez 외, HippoRAG (OSU·Stanford) | 비교 대상 | 개체 관계 그래프와 Personalized PageRank로 문단 사이 검색 연결 | L2 |
| 2025-04 | Cheng 외, CORAL (Renmin·BAAI·Huawei·Waseda) | 선행 평가 | 대화 검색·생성·인용 및 주제전환 평가. 이번 실험이 CORAL 데이터셋을 사용한 것은 아님 | L3 |
| 2025-05-09 | Laban·Hayashi·Zhou·Neville (Microsoft Research·Salesforce Research) | 방법 확장 | 같은 요구정보를 턴에 나눠 전달, 이번 논문이 매턴 검색을 추가. 순서무관 가정은 그대로 복제하지 않음 | L4 L5 |
| 2026-09-29 | Handa·Azad (Texas A&M University) | 이번 논문 | 검색입력표현과턴분산을비교하며누적회수율과답변성적을대조 | F5 F6 F17 |

원문 인용 문맥:
- p.2: “Retrieval-augmented generation ... (Lewis et al., 2020; Gao et al., 2023).”
- p.2–3: “recent benchmarks evaluating retrieval and generation over multi-turn interactions ... Cheng et al., 2025”
- p.3: “We extend their setup to retrieval-augmented QA”
- p.3: “Figure 1 ... adapts the multi-turn framework of Laban et al. (2026)”
- p.5: “four graph retrievers (HippoRAG, HippoRAG2, ToG-2, LightRAG)”

저자 교차 확인:
선행 4편 첫 페이지의 전체 명단과 이번 Pranav Handa·Ariful Azad를 대조. 겹치는 저자 없음.
각 기관은 논문 당시 소속으로만 쓰고 현재이직·경력·동기·h-index 등은 해설에서 제외.

후속 연구:
2026-10-04에 직접 인용해 재현·확장한 후속 논문 원문을 확인하지 못함.
Semantic Scholar는 지연 후 피인용목록이 빈것으로 응답. OpenAlex는429.
이것은 후속 연구 부재의 증명이 아님. 공개5일후시점이므로 확인하지못한후속작을이야기에추가하지않음.
자동조회원본은 lineage-api-unverified.md에 보관하며 서술근거로 단독사용하지않음.

판본 주의:
전작 Laban v1은 초록39%,그림35%,서론25점하락 등 집계서술이 서로다름. 이번해설은그숫자들을인용하지않음.
HippoRAG의 웹초록은 비용10~30배,PDF는10~20배. 비용비교서술하지않음.
이번논문의 PoG33.4-31.3 표반올림차2.1과본문하락2.0 불일치로 하락2.0이라는정밀값은원고에넣지않음.
이번논문초록8retrievalsystems는기본검색7종+NONE. 5datasets는원천3종을MuSiQue추론깊이별로분할한5묶음.

원문 링크:
https://arxiv.org/abs/2005.11401v4
https://arxiv.org/abs/2405.14831v3
https://aclanthology.org/2025.findings-naacl.72/
https://arxiv.org/abs/2505.06120v1
https://arxiv.org/abs/2609.36700v1
