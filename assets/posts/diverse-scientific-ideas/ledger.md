# 팩트 원장: Training Reasoning Models to Generate Diverse Scientific Ideas

기준일: 2026-10-19. 원문: arXiv:2610.22324v1, PDF 42쪽 전체 정독.
날짜 기준: arXiv 최초 제출 UTC. 독립 채택·후속 재현 확인과 저자 주장을 구분함.
원문 URL: https://arxiv.org/pdf/2610.22324v1
표의 값은 원문 이미지와 대조. 모든 비교는 이 논문의 구현·벤치마크 범위임.

## F: 본문·부록

- F1 | p1 제목·초록, §2 p3 | "set-level reinforcement learning objective" | 개별 아이디어보다 세트 품질·다양성을 함께 학습하는 해결형 연구.
- F2 | p4 §3.2, p14 AppA | "Each source is summarized into a source card" | 입력은 선행 논문의 요약 카드. target 논문의 gold idea는 정책 모델에 보이지 않음. 전체 PDF를 생성 모델에 넣는 방식이 아님.
- F3 | pp3–4 §3, AppA.1 p13 | "problem gap, core claim, method, and inspiration" | 문제·검증 가능한 주장·방법·구체적인 출처 기여의 네 필드. 한 번의 생성에서 K=3. 뒤 아이디어는 앞 내용을 볼 수 있음.
- F4 | p3 Eq2 | "R(U) = ... q(ui) ... min ... d(ui, uj)" | 각 아이디어 품질×앞 아이디어 중 가장 가까운 것과의 거리. 첫 거리는 1. 합산함. 학습 순서는 출력 순서.
- F5 | p2 Fig1 | 그림에 q=(1,0,0.5), d=(1,0.4,0.2), r=(1,0,0.10), 합1.10 | 그림의 설명용 수치. 실측 결과가 아님. 본문 별도 예시 q=1,d=0이면 곱0은 수식으로부터 직접 계산.
- F6 | p4 §3.1 Eq3, p18 C.1 | "long-term scientific impact" | 품질은 숨겨 둔 기존 논문 아이디어와 잠재 장기 영향력을 비교한 심사 결과. 실제 미래 인용수나 참일 확률이 아님. 학습 시 두 순서 비교의 승리 비율로 0/0.5/1.
- F7 | p4 Eq4, pp18–19 C.2 | "problem gap, claim, and method" | 세 필드 유사도1–5를 (5-s)/4로 바꿔 평균. inspiration은 거리에서 제외. 단순 어휘 차이가 아닌 LLM 의미 판정.
- F8 | p4 §3.1, p5 §4 | "SciJudge-30B"; "gpt-oss-120b"; "GPT-5.4-mini"; "Gemini-3.5-Flash" | 학습 품질 SciJudge/거리 gpt-oss, 평가 품질 GPT-5.4-mini/거리·grounding Gemini. 학습과 평가 심사는 구분되지만 모두 대리 지표.
- F9 | p3 §2.2, p20 C.4 | "we drop it for training"; "the order in which the model writes them" | 학습은 할인 없이 출력 순서. 평가는 greedy 순서 선택과 γ=0.9 사용자 인내 할인·정규화. Table1 품질 열은 별도의 길이 보정 strict win rate. 열끼리 단순 곱하여 CU 재계산하면 안 됨.
- F10 | p4 §3.2, p16 B.2 | "7,172"; "hindsight prompting" | SFT 7,172개, 교사 Claude Opus4.8이 먼저 답을 만든 뒤 그 답에 도달하는 탐색문을 사후 작성. 비공개 실제 내부 사고 기록이 아님.
- F11 | pp4–5 §3.3, p17 B.2 | "an empty think block" | think는 합성 탐색문과 답, no-think는 같은 답·빈 think블록. 내부 계산 자체를 제거했다는 뜻이 아님.
- F12 | pp16–17 B.1/B.5, Table7 | "1 epoch (112 steps)"; "600 steps"; "8 NVIDIA H200 GPUs" | Qwen3-8B, SFT1epoch 후 GRPO600step. SFT batch64sequences. GRPO는단계당12prompts×4rollouts. SFT46분·GRPO약10시간/8H200. 외부 심사 호출 비용 별도라 전체 비용 비교 아님.
- F13 | pp15–16 reward implementation, Eq7 | "schema bonus"; "0.05"; "length penalty" | 실제 보상은 핵심 품질×거리 합에 유효 형식 보너스0.05, 길이 벌점 추가. 형식 실패는0. 벌점은 think/inspiration 제외 문제·주장·방법 합 토큰, 기준1000, 기울기1, 상한3.
- F14 | p4 §3.2,p5 §4,pp14–15 A | "1,740"; "16 domains" | 영어 Language영역으로 학습, 2026년 target 논문으로 구성한 16영역 1,740사례 평가. 저자는 contamination-free라 부르지만 모든 모델의 오염 부재가 독립 입증된 것은 아님.
- F15 | p6 Table1 이미지 | "Proposed (no think) 0.64 ... 0.50 ... 0.88" | 제안 no-think CU0.64, 길이보정 품질0.50, 평균거리0.88. think0.51/0.34/0.83. 원문 괄호는 사례 간 SD, 신뢰구간·재학습 seed변동 아님.
- F16 | p6 Table1 이미지 | "Claude Opus 4.8 0.38 ... 0.21 ... 0.80" | 동일 세트생성 프롬프트 Claude CU0.38/품질0.21/거리0.80. GPT-6Astra0.28/0.15/0.86. Qwen3-8B0.03/0.01/0.80.
- F17 | p6 Table1 | "Impact-only RL 0.38 ... 0.43 ... 0.38" | 품질만 보상하면 품질0.43이나 거리0.38, CU0.38. 전체보상 no-think는 품질0.50/거리0.88/CU0.64. 이 ablation은 다양성 보상의 유용성 근거, 모든 설정의 인과 보장 아님.
- F18 | p22 Table12 | Claude sample CU0.34,q0.33,d0.24 / set CU0.38,q0.21,d0.80 | 독립적으로 세 번 생성한 Claude보다 한 번에 세 개를 쓰게 하면 거리가 크게 오르지만 품질 대리 점수는 낮아짐. 프롬프트만으로도 상당한 다양성 변화.
- F19 | p21 Table11 | no-think grounding0.61; think0.81; Claude0.98 | source-dependence 점수. no-think CU0.64vs think0.51의 선택에 반대축 존재. 원문이 말하는 grounding은 사실 정확도 비율이 아님.
- F20 | p42 Prompt8 | "load-bearing head, no source documents" | 심사자는 원본 source문서를 받지 않음. 주장·선언된 inspiration만으로 출처를 제거해도 주장이 버티는지 판정. 실제 인용 내용의 충실성 검증과 구별.
- F21 | p21 Table11 | SFTno0.90→proposedno0.61; SFTthink0.91→proposedthink0.81; noSFT0.19 | RL뒤 source-dependence가 떨어짐. p7의 withSFT0.81은 think를 가리킴. no-think에0.81을 잘못 붙이지 말 것.
- F22 | pp19–20 C.3 | "Spearman ... 0.46"; "weighted ... 0.26" | 100아이디어 source-dependence 검증, 사람-심사 Spearman0.46·weighted κ0.26. 이 지표를 정답률로 해석하지 않음.
- F23 | p7 Table3,p20 D,p24 Table17 | Method Paradigm Hnorm human0.87,Claude0.77,proposedno0.65,think0.73,DARLING0.01 | IdeaSeed500논문에서 각3개. 방법유형 분포의 정규화 엔트로피. 골고루 퍼질수록1에 가까움. 세트 내부 의미 거리와 다른 수준의 다양성. no-think의 방법유형 다양성이 Claude보다 낮음.
- F24 | p8 §6.1,Table4,p24 Table16 | "4 annotators, 15 papers each" | NLP PhD4명,각15사례,본인전문성맞춤,3시스템blind평가. 60사례×3세트×3아이디어=540아이디어. 모든 사례를4명이중복평가한 설계가 아님.
- F25 | p8 Table4 | Claude promising2.20,unique2.72,unique-promising2.03; proposed2.17,2.83,2.05 | 세트당3개 중 평균 개수. 표의 proposed는 no-think. 소규모pilot, Claude와 유사한 유망성·약간 더 많은 unique. 과학자 초월·Claude 통계적 우월 주장 금지.
- F26 | p8 §6.2,Table5,pp25–28 F | "132 ideas"; "90-minute, $30, CPU-only budget"; "a positive result covering most or all of the claim" | ClaudeCode/ClaudeOpus5가 고정아이디어를 조기PoC실행. 각아이디어90분·30달러·CPU, GPU없음. 출처문서는 실행에 미제공. 아이디어생성Claude는Opus4.8로 실행기와 다름. supports는주장대부분/전부를뒷받침하는양성결과에대한실행에이전트자체판정.
- F27 | p8 §6.2 | "instances (15; 14 for think)" | Claude15×3 + no15×3 + think14×3=132. 총135로 쓰면오류. think는 한사례 적음.
- F28 | p8 Table5 | success@3 Claude27%,no33%,think29% | 3개 중 하나이상 supports인 사례율. 실행에이전트의 자체구조화판정. 표반올림과일치하는 수:4/15≈27%,5/15≈33%,4/14≈29%. 27→33%는 +6%p, 통계적 우월·실제발견확률아님.
- F29 | pp27–28 F memoryexample | "the benchmark’s design is worth building", not "the claim is established" | 메모리 평가벤치마크의 supports사례도 핵심가설 확증이 아니라 벤치마크를 만들가치가 있다는뜻으로 읽어야 한다고 저자경고. 실행중검사변경·probe제약도서술.
- F30 | p5§4,p17 B.3 | "without task-specific SFT" | DARLING 재구현은 Qwen3-8B에서 SFT없이GRPO, proposed는SFT후GRPO. 다양성위치만유일차이인 완전통제실험아님. p5의onlydifference요약을 AppB로 제한해야 함.
- F31 | p6 Table1 | "DARLING 0.52 ... 0.38 ... 0.67" | DARLING은이연구의재구현기준CU0.52. 원래논문전체보다보편적으로우수하다고단정불가.
- F32 | pp7,9–10 conclusion/limitations | "grounding"; "diversity across a population"; "instead of focusing on retrieval" | 저자가추후과제로grounding-aware보상·여러세트전체의다양성·더적절한창의탐색trace를제시. 현재영어NLP학습/검색과정미포함·요약문맥과모델지식중심. 결과는아이디어제안평가이며새과학가설의참을확립한연구아님.
- F33 | p7 Thinking helps retain grounding | "the steps might not have enough causal influence on the reward"; "designing thinking traces suitable for creative ideation is an open-problem" | 최종아이디어에만매기는영향력보상이라중간탐색의보상인과영향이약할가능성,적절한창의탐색문설계가미해결이라는두가설. 선행아이디어고착을저자의가설로적으면근거없음. 직접원인분리실험이나모든추론모델일반결론아님.

## L: 계보 (관련절 원문은 filesources/에 보관)

- L1 | CREATE: Testing LLMs for Associative Creativity, arXiv:2603.09970v2 pp1,3–4; 이번논문p3§2 | "Creative Utility" | Wadhwa등5명,최초2026-03-10,연결경로세트의품질×최소거리·인내할인으로평가. 동일제1저자의평가지표를이번논문이보상으로개조. 최초다양성지표라고쓰지않음. https://arxiv.org/abs/2603.09970
- L2 | DARLING: Jointly Reinforcing Diversity and Quality in Language Model Generations, arXiv:2509.02534v1 pp1,3–4 | "multiply the two reward scores" | Li등8명,최초2025-09-02. 별도rollout간의미다양성과품질을함께보상하는선행방법. 이번은단일출력안세트내보상. 전작이품질만봤다는서술금지. https://arxiv.org/abs/2509.02534
- L3 | GIANTS: Generative Insight Anticipation from Scientific Literature, arXiv:2604.09793v1 pp1,3,5–6 | "two parent papers" | He-Yueya등8명,최초2026-04-10. 선행두논문으로후속실제논문통찰재구성. 이번은학습target풀재사용후출처재선별·요약. 데이터그대로혹은동일목표아님. https://arxiv.org/abs/2604.09793
- L4 | AI Can Learn Scientific Taste, arXiv:2603.14473v3 pp1,5–6,13 | "citations are an imperfect form of community feedback" | Tong등23명,최초2026-03-15. 유사시기·분야논문의인용비교로학습한ScientificJudge. 이번은SciJudge30B채택. 인용편향·영향력지연·실험미검증한계. https://arxiv.org/abs/2603.14473

## P: 사람·기관

- P1 | 본논문p1제목·저자란·각주, p10 Acknowledgments | "Work done while at Salesforce AI Research"; "an internship at Salesforce AI Research" | Manya Wadhwa(NYU), Pranav Narayanan Venkit·Hiroaki Hayashi·Yu Li·Chien-Sheng Wu(SalesforceAIResearch), Tuhin Chakrabarty(StonyBrook). Wadhwa의해당연구는Salesforce인턴중수행. 논문당시소속으로한정.
- P2 | CREATE p1 저자란 | Manya Wadhwa first author; Greg Durrett/Junyi Jessy Li coauthors | 평가연구와이번학습연구의동일제1저자맥락은확인. 기관명으로성과신뢰도추론안함.

## W: 발표·상태·웹

- W1 | https://arxiv.org/abs/2610.22324v1 (2026-10-19) | "Thu, 15 Oct 2026 17:52:12 UTC"; "Under Review" | 최초공개2026-10-15 UTC. KST2026-10-16 02:52:12=UTC+9h. 공식게재채택확인안됨. underreview를미심사단정하지않고심사중프리프린트로표기.
- W2 | 같은abs (2026-10-19) | "pending registration" | DOI10.48550/arXiv.2610.22324는당시등록대기. 원문은고정버전arXivURL우선사용.
- W3 | https://creativecommons.org/licenses/by-nc-sa/4.0/ ; 공식arxivlicense링크 (2026-10-19) | "Attribution-NonCommercial-ShareAlike 4.0" | 원문그림·표CCBY-NC-SA4.0. 그림출처·크롭확대변경·동일비영리라이선스표기. 보고서도동일조건배포. 폰트별OFL유지.
- W4 | https://manyawadhwa.github.io/ (2026-10-19) | "Under review"; CREATE별도항목 | 저자도이번논문심사중공개. 당일새소속은본문에혼합안함. 공식PDFp1소속만사용.
- W5 | lineage_research.md 검색로그 (2026-10-19) | 제목/ID + replication/reproduce/follow-up/accepted | 이번조사범위에서독립후속검증·정식채택을확인못함. '없다'고단정안함. 코드URL존재는실행재현검증과별개.
- W6 | https://github.com/ManyaWadhwa/diverge_ideation ; 본논문p1각주 (2026-10-19) | "Code and data" | 저자공개주소. 이보고서에서모델훈련·코드재실행을한것은아님.
- W7 | CREATE arxiv공식license링크 https://creativecommons.org/licenses/by/4.0/ (2026-10-19) | "CC BY 4.0" | CREATE 제목크롭은BY4.0,메인원문과라이선스다름. 각이미지별출처·변경·조건분리명시.

## 집필·선정 감사 기록

기존19편의arxivID/slug와대조해중복없음. 최근cs.CL공식목록에서확인후전체PDF확보되는후보를선정. 원문본문·부록·프롬프트·42쪽끝까지읽음. 연구주장은저자실험조건에한정. 인용수는검증가능한동일출처시계열을확보하지않아제외. DARLING학회근황은저자홈페이지단독이라본문에서제외. 최신모델명은원문실험의명칭이며제품의실시간가용성을주장하지않음.
