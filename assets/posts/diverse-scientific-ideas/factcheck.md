# 독립 팩트체크

대상: `report.md` 20파트, `ledger.md`, `text.txt`(42쪽), `lineage_research.md`, `filesources/`의 CREATE·DARLING·GIANTS·SciJudge 원문 관련 절, 본문에서 실제 사용하는 그림 17개.

메인 작성자의 정독과 별개로 본문·부록·프롬프트를 대조했음. 보고서와 원장은 직접 수정하지 않았음. 검사 도중 작성자가 반영한 수정은 아래에 따로 표시함. 확인 항목 수는 각 파트에서 대조한 독립 주장·설정 묶음 수임. ‘문제 없음’은 논문의 주장을 외부 실험으로 재현했다는 뜻이 아님.

## 파트별 결과

파트 1 문제 없음 (5항목: 제목, 저자, 연구 목표, 공개일, under-review 상태). arXiv 공식 v1 페이지도 재확인함.

파트 2 문제 없음 (5항목: 한 출력의 세 아이디어, 앞 아이디어 조건화, 품질×거리, Figure 1 수치, 예시와 실측 구분).

파트 3 문제 없음 (6항목: source card 입력, 네 필드, gold idea 비공개, 학습 Language, 영어 한정, 16영역·1,740 평가). 원문 pp3–4, pp13–15와 일치함.

파트 4 문제 없음 (6항목: CREATE 제1저자, 2026년 3월 공개, 연결 경로 과제, CU 품질·거리 결합, DARLING 2025년 9월 공개, rollout 간/단일 출력 내 차이). CREATE 원문 pp1–4와 DARLING 원문 pp1–4를 대조함. 전작이 품질을 무시했다거나 이번 연구가 다양성 RL을 처음 만들었다는 과장은 없음.

파트 5 문제 없음 (5항목: 최근접 선행 답 거리, 첫 거리 1, 중복 답의 0 추가값, 세 필드 의미 비교, 단순 어휘 차이와 구분).

파트 6 문제 없음 (7항목: 상대 영향력 판단, gold 비교, 진실 확률/미래 인용수 실측과 구별, 학습 심사자 둘, 평가 심사자 둘, CU greedy 순서·0.9 할인, LC 품질 집계와 구분).

파트 7 문제 없음 (7항목: Qwen3-8B, 7,172 SFT, SFT→GRPO, 교사 사후 탐색문 생성, 비공개 실제 사고기록과 구별, 같은 답·빈 think 대조, 형식 보너스·길이 벌점). 단, 아래 원장 F12의 배치 설정은 별도 수정 필요.

파트 8 문제 없음 (6항목: Claude Opus 4.8, sampled/set 생성 방식, 거리 0.24→0.80, LC 품질 0.33→0.21, CU 0.34→0.38, 동반 상승이 아님). Table 12 이미지와 일치함.

파트 9 문제 없음 (7항목: 1,740사례, Claude CU0.38, no-think CU0.64, 8B 범위, impact-only 품질0.43·거리0.38, no-think 품질0.50·거리0.88, 다양성 보상 대조의 범위). 전체 과학 능력 서열로 확대하지 않음.

| 파트 | 검사 당시 문제 문장 | 원문 근거 | 심각도 | 수정안·상태 |
|---|---|---|---|---|
| 10 | ‘저자들은 탐색문 품질이나 앞 답에 대한 고착을 / CU 차이의 가능한 이유로 추정함’ | `text.txt` p7: 최종 아이디어만 채점하며 중간 단계의 보상에 대한 인과 영향이 충분하지 않을 가능성, 창의 ideation에 적절한 탐색문 설계가 미해결이라는 두 가설. 앞 답 고착은 이 문단의 가설이 아님. | 오류 | 최종 답 보상이 중간 탐색에 충분한 영향을 못 줄 가능성, 적절한 창의 탐색문 설계의 어려움으로 교체. 작성자가 반영했고 재확인함. F33 위치도 p23→p7로 수정됨. |

파트 10의 나머지 5항목 문제 없음: think CU0.51/no-think0.64, 사후 탐색문 조건, grounding0.81/0.61, Figure 2 축, 추론 일반 무용론을 피한 표현. 수정 후 이 파트의 지적 사항은 해소됨.

파트 11 문제 없음 (7항목: grounding의 source-dependence 의미, 주장·선언된 inspiration 입력, 원문 문서 미제공, 인용 정확도와 구별, 100아이디어 검증, Spearman0.46, no-think0.90→0.61). **Prompt 8 p42의 ‘no source documents’와 실제 입력 자리표시자까지 확인함.**

파트 12 문제 없음 (6항목: 세트 내부와 모집단 수준 다양성 구별, IdeaSeed500논문, 목표 세트 크기3, Method Paradigm축, 정규화 엔트로피 의미, human0.87/Claude0.77/no-think0.65). 전체 500논문에서 모두 형식이 정확히 3개였다고 확장해서 읽지 말 것: 세부 Table 17에는 형식·누락에 따른 유효 개수 차이도 있지만 본문의 시험 설계 요약은 허용 범위임.

| 파트 | 검사 당시 문제 문장 | 원문 근거 | 심각도 | 수정안·상태 |
|---|---|---|---|---|
| 13 | ‘NLP 박사과정 전문가 4명이’ | `text.txt` p8 §6.1: 모집 최소 요건이 NLP PhD 보유 및 최상위 학회 논문 4편 이상이며, 네 참가자가 이를 충족한다고 명시함. | 오류 | ‘NLP 박사 학위 보유자 4명이’. 작성자가 반영했고 재확인함. |

파트 13의 나머지 6항목 문제 없음: 각15사례·총60사례, 전문성 맞춤 배정, 세 시스템 blind, proposed=no-think, 유망성2.20/2.17 및 unique2.72/2.83, 소규모 파일럿 한정. 수정 후 이 파트의 지적 사항은 해소됨.

파트 14 문제 없음 (7항목: Claude Code/Opus5, 고정 아이디어 PoC, 90분, 30달러, CPU-only/no GPU, 총132, think14사례·나머지15). 생성 Claude Opus4.8과 실행 Opus5를 혼동하지 않음.

파트 15 문제 없음 (6항목: success@3 정의, supports 자체 판정, Claude27/no33/think29%, no5/15·Claude4/15, 한 사례 차이, 독립 발견 확률과 구분). 계산: 5/15=33.3%, 4/15=26.7%, 4/14=28.6%.

파트 16 문제 없음 (5항목: 메모리 벤치마크 사례, 실행 중 검사 설계 변경, 저자 해석 경고, 제작 가치와 가설 확립 구분, 추가 검증 필요). 원문 pp25–28와 supportsquote 실제 그림을 대조함.

파트 17 문제 없음 (7항목: DARLING 재구현CU0.52, no-think0.64, no task-specific SFT, proposed SFT→RL, equivalence·quality judge 교체, 다양성 위치 외 설정 차이, 단일 원인 분리 불가). **p5의 ‘only difference’를 그대로 반복하지 않고 p17 B.3의 SFT confound를 정확히 반영함.** 재구현 비교를 원 DARLING 전체 성과에 대한 보편 우열로 확대하지 않음.

파트 18 문제 없음 (7항목: GIANTS의 후속 통찰 재구성, target 풀 재사용, source 재선별·요약, SciJudge 인용 비교 기반 학습, 인용 편향·지연 가치 한계, 저자 6명·기관, Salesforce 인턴십). GIANTS 원문 pp1–3, SciJudge pp5–6·13, 메인 p1·10을 대조함. 단 P1의 인턴십 근거 위치에 p10 추가 필요.

파트 19 문제 없음 (5항목: 평가 내 효과로 범위 제한, 발견 확증과 구별, grounding 역방향, 모집단 방법 다양성 역방향, 미래 과제와 저자 결론 일치).

파트 20 문제 없음 (6항목: under-review 상태, 조사 범위 내 재현/채택 미확인과 부재 단정 구별, 코드 주소와 재실행 구별, 메인 원문 라이선스, CREATE 별도 라이선스, 세 줄 요약의 조건). CREATE 라이선스 태그는 검사 중 W7로 보강됨. arXiv 각 논문의 공식 license 링크를 직접 따라가 메인 CC BY-NC-SA4.0과 CREATE CC BY4.0을 재확인함.

## 원장 자체 지적

| 관련 파트·ID | 문제 | 원문 근거(페이지) | 심각도 | 수정안 |
|---|---|---|---|---|
| 7·F12 | ‘각 단계12prompts×4rollouts’ | 메인 p16 Table7: SFT batch는64 sequences, GRPO만12 prompts×4 rollouts임. | 오류 | ‘SFT batch64 sequences; GRPO12prompts×4rollouts’. 본문에는 이 잘못된 배치 문장이 들어가지 않았음. |
| 7·F12 | compute8H200·SFT46분·GRPO10시간까지 pp15–16로 출처 표시 | 실제 compute 문단은 p17 B.5. | 사소 | 위치를 pp16–17 Table7/B.5로 확장. |
| 3·F3 | AppA.1 p14 | idea schema 정의 AppA.1은 p13. p14는 A.2/A.3. | 사소 | AppA.1 p13으로 수정. |
| 6·F9 | 직접 인용 ‘remove ... patience’ | p3 §2.2 실제 표현은 ‘we drop it for training’. p20에는 generation order 설명이 있음. | 사소 | 따옴표 안을 실제 구절로 교체. 요지 자체는 정확함. |
| 7·F11 | 빈 think 인용의 위치를 p4 §3.3, p16 B.2로만 표시 | 해당 문구는 p5 §3.3, 구체적 같은 답 대조는 p17 B.2 bullet에 있음. | 사소 | pp4–5 §3.3, pp16–17 B.2 또는 p5/p17로 지정. |
| 14–15·F27 | ‘15 instances per system (14 for ... think)’ 위치 p25 F | 15/14사례 명시는 p8 §6.2/Table5 아래 설명. p25는 메모리 사례 설명임. | 사소 | p8 §6.2로 수정하고 그 페이지의 실제 구절을 인용. |
| 18·P1 | 인턴십 사실을 p1 저자란·각주만으로 연결 | p1각주는 재직 중 수행을 말하고, ‘internship’은 p10 Acknowledgments에 명시. | 사소 | p10 Acknowledgments 추가. 사실 자체는 정확함. |
| 10·F33 | 최초 원장의 p23·hypothesize·선행아이디어 고착 | p7의 두 가설과 불일치. | 오류 | 작성자가 p7 실제 두 가설로 수정했고 재확인함. |
| 20·W3/W7 | 최초 CREATE CC BY4.0 문장이 메인 라이선스 W3만 참조 | CREATE 공식 arXiv v2 license 링크는 BY4.0. | 사소 | 작성자가 W7을 신설해 분리했고 재확인함. |

## 직접 연 그림과 정합성

`header.png`, `pipeline.png`, `schema.png`, `prior_create.png`, `reward.png`, `quality.png`, `training.png`, `promptcontrol.png`, `results.png`, `tradeoff.png`, `groundingheading.png`, `population.png`, `human.png`, `executioncaption.png`, `execution.png`, `supportsquote.png`, `darling_sft.png`를 각각 직접 열었음. 캡션·가리키는 열·축·수식·숫자·순서와 본문이 일치함. synthetic summary 그림을 논문 원그림으로 둔갑시킨 사례 없음.

## 판정

본문 확정 오류 2건(박사과정/박사 보유자, 고착 가설)은 검사 중 수정되어 해소됨. 추가 확정 오류 1건은 원장 F12의 SFT 배치 설정이며 본문으로 전파되지는 않았음. 나머지는 근거 위치·직접인용 정확성 보완임. 핵심 수치, 품질 대리 지표의 의미, DARLING 비교 제한, grounding 입력 제한, 실행 판정의 낮은 확증 수준은 원문과 일치함.

## 최종 재확인 — 수정·재배치 후

위 판정은 최초 검사 시점의 기록임. 후속 수정본을 다시 열어 아래 항목을 원문과 재대조했음. 보고서·원장은 수정하지 않고 이 확인 기록만 추가함.

1. F12의 배치 오류 해소 확인: SFT64 sequences와 GRPO 단계당12prompts×4rollouts가 분리됨. compute 위치도 pp16–17로 수정됨. Table7 p16 및 B.5 p17과 일치함.
2. F3 AppA.1 p13, F9 실제 구절 ‘we drop it for training’, F11 pp4–5/p17, F27 p8의15/14사례, P1 p10 인턴십 출처가 모두 반영됨. 기존 위치·직접인용 지적은 해소됨.
3. 파트1로 이동한 저자 명단·당시 기관·Salesforce 인턴십은 메인 p1·10과 일치함. 파트3으로 이동한 GIANTS target 풀 재사용과 입력 source 재선별·요약은 메인 p4 및 GIANTS 원문 pp1–3과 일치함. 파트6으로 이동한 SciJudge의 상대 인용 비교 기반 학습 설명은 선행 원문 pp5–6과 일치함. 이동으로 인한 새 인과 과장 없음.
4. 파트6의 CU 설명 수정은 p20 C.4와 일치함. 최고 품질 답에서 시작한 뒤 다음 한계 기여가 큰 답을 greedy로 고르는 평가임. ‘CU와 길이 보정 품질 열을 단순 곱해 재계산하면 안 됨’도 유지됨.
5. 파트15에 추가한 supports 정의는 p8 §6.2의 ‘positive result covering most or all of the claim’과 일치함. 자체 판정임을 같은 문맥에서 유지하며 독립 확증으로 올리지 않음.
6. 새 파트18의 영어 NLP 학습 한정과 retrieval 미통합은 p10 Limitations에 명시됨. 16영역 평가는 p5이며 전 영역 보편 보장을 주장하지 않음. p17 B.5의8H200·SFT약46분/epoch·GRPO약10시간과 외부 gpt-oss-120b 거리 심사 API 조건도 일치함. 외부 API 비용 금액을 지어내지 않고 보고된 GPU 학습 시간만으로 총비용을 비교할 수 없다고 제한함.
7. 본문 팩트의 신규 오류는 발견하지 못함. 원장 요지까지 완전히 동기화하려면 F32에 영어NLP/검색 미통합 조건, F26에 supports 판정 정의를 추가하면 좋음. F32의 pp9–10 직접인용 ‘population-level’도 그 위치의 실제 표현 ‘diversity across a population’으로 바꿀 것을 전달함. 이는 원문 근거가 없는 본문 주장이 아니라 원장 요지·인용의 추적성 보완 사항임.

최종 재확인 시점: 기존 확정 오류3건(본문2·원장1)은 모두 수정 확인됨. 수정·재배치한 본문에 추가 오류 없음.
