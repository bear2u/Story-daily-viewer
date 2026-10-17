# 계보·저자 맥락 조사

확인일: 2026-10-18 (한국 날짜). 조사자: lineage_1018. 본문 집필자는 메인 에이전트.

## 원문 확보·읽은 범위

선행 연구 세 편의 공개 원문 PDF를 실제 다운로드하고 텍스트로 추출했다. 아래 내용은 초록만이 아니라 각 방법 절과 이번 논문의 Related Work를 대조한 결과다. 선행 PDF 전체 정독을 주장하지 않는다.

| 파일 | 원문 URL | 실제 읽은 관련 범위 |
|---|---|---|
| sources/prior_pointer_sentinel.pdf / .txt | https://arxiv.org/pdf/1609.07843 | PDF pp.1–4, 특히 §2.2–2.6, Fig.1–2, 식(5)–(9) |
| sources/prior_gradient_bottleneck.pdf / .txt | https://arxiv.org/pdf/2603.10145v2 | PDF pp.1–4, §1–2.4, Fig.1, COLM 표지 |
| sources/prior_trime.pdf / .txt | https://aclanthology.org/2022.emnlp-main.382.pdf | PDF pp.1–4 및 p.6; 인쇄 pp.5657–5660, 5662; §2.2–§3, §5.3 |

추출 도구: pdftotext -layout. 파일별 PDF 페이지 수: 13, 29, 17.

## 원장에 옮길 수 있는 검증 사실

### L1. 복사와 어휘 예측을 섞는 발상 자체는 새롭지 않음

- 전작: Stephen Merity, Caiming Xiong, James Bradbury, Richard Socher. *Pointer Sentinel Mixture Models*. arXiv 첫 공개 2016-09-26 04:06:13 UTC. ICLR 2017 논문.
- 원문: https://arxiv.org/abs/1609.07843 ; https://openreview.net/forum?id=Byj72udxe
- PDF p.1 소속 표기는 MetaMind - A Salesforce Company, Palo Alto, CA, USA. 현재 소속으로 전용하면 안 됨.
- PDF pp.2–3 §2.2–2.4: 과거 위치들을 pointer로 점수화하고, 동일한 단어의 여러 위치 확률을 합한다. 어휘 softmax와 pointer 분포를 혼합하고, sentinel이 softmax 쪽에 배정할 확률을 결정한다. 기본 실험 골격은 LSTM/RNN이다.
- 짧은 원문 근거(7단어): “use pointers whenever possible and back-off to” (p.3 §2.4; 뒤를 자른 최소 확인 구절이며 게시 인용문으로 권장하지 않음).
- 이번 논문 p.3 식(7) 뒤에서도 이 전작과 가깝다고 명시한다. 차이는 CPLM의 <copy> 결정이 LM head에서 먼저 나오고, sink는 copy 쪽에서 어휘 예측으로 되돌아가는 역할이라는 점이다. CPLM을 단순히 sentinel 재명명으로 쓰면 틀림.
- 심사 확인: 공식 OpenReview 검색 결과가 ICLR 2017 conference acceptance를 표시함. 직접 포럼 열기는 브라우저 검증벽이 나와 더 진입하지 않았음. 이번 논문 참고문헌 p.14도 ICLR 2017로 기재함. arXiv PDF 메타데이터 Subject의 ICML 2016 문구는 신뢰할 학회 근거로 쓰지 말 것.

### L2. Transformer가 이미 볼 수 있는 과거도 학습 때 명시적으로 쓰면 이득이라는 관찰은 선행함

- 전작: Zexuan Zhong, Tao Lei, Danqi Chen. *Training Language Models with Memory Augmentation* (TRIME). EMNLP 2022, December 7–11, 인쇄 pp.5657–5673.
- 공식 논문/DOI: https://aclanthology.org/2022.emnlp-main.382/ ; https://doi.org/10.18653/v1/2022.emnlp-main.382
- PDF p.3(인쇄5659) §2.2는 local memory를 같은 입력 안의 앞선 context-target 쌍으로 정의함. §3과 식(5)는 메모리를 추론 때만 추가하는 대신 학습 목적함수에도 넣고, 같은 배치에서 만든 메모리 표현까지 역전파한다고 설명함.
- PDF p.6(인쇄5662) §5.3/Table2: WikiText-103의 247M Transformer에서 vanilla perplexity18.70, 추론 시 continuous cache18.26, TRIME local-memory17.76. 이 숫자는 CPLM 실험값이 아니며 직접 우열 비교 불가.
- 원문 짧은 근거(14단어): “using local memory during both training and testing can still improve model performance” (p.6 §5.3).
- 이번 논문 p.10 §5는 TRIME의 local-memory 변형을 가장 가까운 전작으로 지목한다. 다만 TRIME는 과거 context 표현을 맞추는 쪽이고 CPLM은 과거 token을 가리키며, gate 및 학습하는 별도 query/key 투영을 둠. 이 비교는 양쪽 원문을 대조했으나 ‘가장 가까움’은 CPLM 저자들의 분류임.
- 즉 ‘Transformer 시대 첫 복사 모델’이나 ‘학습 중 메모리를 쓰는 첫 모델’이라는 표현은 금지.

### L3. 같은 두 저자가 먼저 LM 출력층의 학습 병목을 분석함

- 전작: Nathan Godey, Yoav Artzi. *Lost in Backpropagation: The LM Head is a Gradient Bottleneck*. arXiv:2603.10145v2.
- 원문: https://arxiv.org/abs/2603.10145 ; https://arxiv.org/pdf/2603.10145v2 ; https://openreview.net/forum?id=PMDKvhbE4x
- 첫 공개 2026-03-10 18:27:01 UTC. 확인한 v2는 2026-07-10 16:51:04 UTC.
- PDF p.1 최상단(10단어): “Published as a conference paper at COLM 2026”. **ICLR가 아니라 COLM 2026**임. arXiv 공식 댓글도 To be presented at COLM'26로 확인됨. OpenReview 직접 열기는 실패했으므로 이 표지와 공식 arXiv 기록을 근거로 삼음.
- PDF pp.1–4: V차원의 출력 오차 신호가 D차원 표현으로 되돌아갈 때의 압축을 최적화 병목으로 분석함. §2.4는 압축이 존재한다는 이론만으로 심각도가 결정되지는 않으며 실험으로 보완한다고 명시함.
- 같은 실험들에서 gradient norm95–99% 억제를 보고함. 이를 ‘학습 정보95–99%가 사라진다’, ‘모든 AI가 학습량99%를 낭비한다’로 일반화하면 부정확함. gradient norm과 정보량·성능 손실은 다른 양임. 본문에 숫자를 넣지 않고 ‘출력층에서 되돌아가는 학습 신호가 압축될 수 있다는 분석’ 정도로 연결하는 편이 안전함.
- 이번 논문 p.9 §4.1 및 p.10 §5는 복사 경로가 이 병목을 일부 줄이는 두 번째 gradient 경로라고 연결함. ‘완전 해결’이 아니라 context 안에 존재하는 token에 한정되는 완화임(p.10 Conclusion).

### P1. 이번 연구 소속과 연구자 이력

- CPLM PDF p.1: Nathan Godey, Yoav Artzi / Cornell University / New York City, USA. 이 논문의 소속은 Cornell로 제시할 것.
- CPLM PDF p.10 Acknowledgements: Cornell LIL Lab 구성원들의 의견에 감사하고, Godey(NG)의 Empire AI Postdoctoral Fellowship 지원을 밝힘. LIL Lab이 모든 실험을 ‘검증’했다는 뜻은 아님.
- 2026-10-18 확인 저자 1차 페이지 https://nathangodey.github.io/ 및 https://nathangodey.github.io/about-me/ : Godey는 Cornell Tech의 Yoav Artzi 연구실 포닥이며 이전 Inria ALMAnaCH 박사과정에서 Benoît Sagot/Éric de la Clergerie 지도를 받았다고 밝힘. 짧은 근거(8단어): “I'm a postdoc in Yoav Artzi's lab at” (홈페이지).
- https://yoavartzi.com/ : Artzi는 Cornell University Computer Science/Cornell Tech Associate Professor라고 표기하고, 연구실 구성원 목록에서도 Godey를 postdoc으로 기재함. 방문연구직 등 글 이해에 필요하지 않은 추가 현직은 생략 권장.
- 이력에서 연구의 품질이나 결과의 진실성을 추론하지 말 것. 유용한 맥락은 ‘같은 두 사람이 병목을 분석한 전작에서 실제 head 설계로 이어졌다’는 연구 연속성임.

### W1. 이번 논문은 프리프린트로 다룰 것

- CPLM PDF 각 페이지 표제는 Pre-print. 공식 arXiv https://arxiv.org/abs/2610.19247 는 v1(2026-10-13 22:03:18 UTC)만 표시하고, 학회 채택/저널 게재 댓글은 보이지 않음.
- 따라서 2026-10-18 확인 기준 ‘프리프린트, 공식 학회·저널 채택 확인 못함’이 정확함. ‘심사에 떨어짐’, ‘심사 안 받음’으로 단정 금지.
- DOI https://doi.org/10.48550/arXiv.2610.19247 는 arXiv-issued DOI / pending registration 상태로 공식 arXiv에 표기됨. 현재 확실히 연결되는 arXiv/PDF 링크를 우선 제공 권장.

### W2. 후속 연구는 확인 범위에서 미확인

- 2026-10-18 검색: 정확한 제목, arXiv ID와 accepted/COLM, extension/replication/followup 조합; arXiv 기록; 저자 홈페이지/출판목록. 확인 가능한 독립 후속 논문이나 재현 결과를 찾지 못했음.
- 저자 Hugging Face 체크포인트 https://huggingface.co/nthngdy/cplm-360M 는 원 연구의 공개 자산이며 후속 연구나 독립 재현으로 세면 안 됨. alphaXiv의 자동 replicate 시작 버튼도 실제 재현 결과가 아님.
- 후속 ‘논문이 없다’는 존재 부정으로 쓰지 말고 ‘이번에 확인한 공개 자료에서는 후속 연구·독립 재현을 확인하지 못했음(2026-10-18)’으로 제한할 것.
- CPLM p.10 Conclusion의 더 큰 모델, span 복사, 외부 corpus 확장은 **저자 제안**이며 완료된 후속 성과가 아님.

### W3. 그림 재사용 라이선스

- CPLM arXiv의 view license 링크를 실제 클릭해 https://creativecommons.org/licenses/by-sa/4.0/ 연결을 확인함. **CC BY-SA4.0**.
- 그림 크롭은 저자/논문 제목/arXiv 버전/그림·표·쪽 위치, 원문 링크 및 라이선스 링크, 크롭·확대 여부를 밝히고 동일조건을 유지해야 함. CC BY로 축약하면 안 됨.
- 선행 논문 PDF들의 재배포 라이선스를 별도로 확정하지 않았으므로 이번 게시글에 원문 통째로 재게시하거나 그림을 무심코 재사용하지 말 것. 메인 논문의 Related Work 크롭으로 계보를 보여줄 수 있음.

## 가장 짧은 서사 제안

1. 예전 LSTM에도 과거 단어를 가리키고 어휘 예측과 섞는 pointer-sentinel이 있었음.
2. Transformer에서도 TRIME는 같은 입력 메모리를 학습 때부터 쓰면 도움이 된다고 관찰했음.
3. Godey·Artzi는 COLM2026 전작에서 출력층의 역전파 병목을 분석했음.
4. 이번에는 학습 초기부터 별도 복사 head와 두 단계 gate를 함께 학습해 그 병목을 일부 우회하려는 설계를 시험함.

이 네 문장이 정확한 계보 연결임. 모든 전작이 순차적으로 직접 개선된 직선 계보라고 그리지는 말 것. pointer/TRIME는 구조적 선행, Lost in Backpropagation은 동일 저자·동기 선행임.
