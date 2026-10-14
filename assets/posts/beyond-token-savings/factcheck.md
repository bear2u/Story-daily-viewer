# 독립 팩트체크 — 2026-10-15

검토자: 집필과 별도로 원문을 대조한 factcheck_1015.
대상: report.md 초안 18파트, ledger.md, 원문 PDF/text.txt, 실제 사용 그림 15종, lineage-audit.md 및 전작 원문.
paper-report SKILL.md와 references/fact-check.md를 읽고 그 지시문을 적용함. report.md와 ledger.md는 수정하지 않았음.

## 총평

핵심 수치·비교 조건에 중대 오류 없음. Qwen의 실측 prefix caching 비활성화, 비용의 가상 입력 과금 및 출력 제외, SWE 100문제 주실험과 25문제 sweep 구분, 시간 초과 제외 규칙, 작은 요약기 시간 비교의 공통 과제 수 10·23이 원문과 맞음. 그림의 축·범례·표 셀을 직접 열어 확인했음.

수정이 필요한 것은 원장 일부의 합성 직접인용과 좁은 위치 표기임. 의미가 맞는 항목도 따옴표 안은 실제 원문으로 바꾸어야 함. 아래 수정안은 보고만 하며 편집자는 원문 재확인 후 반영할 것.

## 발견 사항

| 파트 / 원장 | 문제 문장·표기 | 원문 근거 | 심각도 | 수정안 |
|---|---|---|---|---|
| 2 / F6 | “어느 기록을 남기느냐가 다음 행동을 바꿈” | 선택 논문 p.3 §2.1은 보존되는 정보의 종류를 설명하며 요약이 정보를 누락·변형할 수 있다고 함. p.1도 “can alter the agent’s trajectory”라고 가능성으로 설명함. | 사소한 확신 조정 권고 | “남긴 기록에 따라 다음 행동도 달라질 수 있음”으로 바꾸면 원문 확신 수준에 더 정확함. |
| 7 / F11 | 원장 직접인용 “0.59× ... reduces success by 11.0 pp” | p.6 §4.1: “SU uses a similar 0.59× the tokens but reduces success by 11.0 pp.” | 사소: 원장 인용 정밀성 | 해당 원문 문장으로 대체. 본문 숫자는 맞음. |
| 9 / F14 | 원장 직접인용 “Output tokens ... excluded” | p.19 A.5.2: “Output tokens contribute to token consumption but are excluded from this input-cost metric.” | 사소: 합성 인용 | 실제 문장으로 교체. 본문의 출력 과금 제외 설명은 정확함. |
| 10 / F18 | 원장 “subsets of 25 and 15”의 위치가 p.7·p.19뿐임 | p.4 §3에 “The threshold and depth sweeps use subsets of 25 and 15 of these tasks, respectively.”가 있음. p.7 Figure 3에는 Qwen SWE 25문제 설명, p.19에는 포함 규칙이 있음. | 사소: 위치 | p.4 §3을 추가하고 sweep 표 포함 규칙은 p.7 Figure 3 caption / p.19 A.5로 분리. |
| 12 / F21 | 원장 직접인용 “FC ... 53”, “TRC+SU ...52 ...+7 ...−8” | p.8 §4.2: “TRC+SU solves 52 tasks compared with 53 for full context, but newly solves 7 tasks while losing 8 previously solved tasks.” Figure 4의 셀도 52/+7/−8임. | 사소: 합성 인용 | 실제 문장으로 교체. 본문 산술 53+7−8=52와 2/3 해결 정의는 맞음. |
| 14 / F24 | 수치 위치를 p.29 Figure 13 A.6.3만으로 적음 | SU 53.3/37.3/28.0 및 TRC+SU 68.0/62.7/66.7 서술은 p.28 A.6.3, Figure 13은 p.29. 15K 설정은 p.17 A.3. | 사소: 위치 | pp.17, 28–29로 좁은 근거를 적기. 본문 설정·수치는 맞음. |
| 14 / F25 | “Neither alternative reduces mean end-to-end latency” 위치가 p.29만임 | 문장은 p.28 마지막 줄에서 p.29 첫 문장으로 이어짐. 표본 수 10·23은 p.29 Figure 13 caption. | 사소: 위치 | pp.28–29로 표기. |
| 16 / P1 | 원장 직접인용 “intersection of computer systems and machine learning” | UT Austin 공식 ECE 페이지(2026-10-15 재조회)는 “Most of her research straddles the boundaries of Systems and ML.”라고 적음. Assistant Professor는 같은 페이지에 명시됨. | 사소: 실제로 없는 직접인용 문구 | 해당 실제 문장으로 교체. 본문 ‘시스템과 머신러닝의 접점’ 요지는 맞음. |

## 파트별 확인

검사 항목 수는 해당 파트에서 별도로 대조한 사실 묶음 수임. 위 원장 형식 보완을 제외하면 다음 내용에는 문제 없음.

1. **파트 1 문제 없음 (6항목).** p.1 제목·네 저자·UT Austin 저자란 이미지 확인. 공식 abs/v1의 최초 접수 2026-09-26 21:46:40 UTC 확인. UTC+9 변환으로 한국 9월 27일 맞음. 공식 arXiv에 학술지·학회 채택 표기 없음. ‘심사 채택 미확인’은 ‘미심사 확정’과 구별되어 적절함.
2. **파트 2 문제 없음 (4항목; 가능성 표현 권고 1건).** p.3 §2.1 보호 prefix 및 assistant/tool 압축 대상, p.19 A.5.1 누적 input+output+summary 확인. Figure 1의 파란 기록·압축 시점 설명 맞음. 파일·테스트 장면은 I5 해설 예시로 구분됨.
3. **파트 3 문제 없음 (8항목).** MemGPT 공식 v1 2023-10-12 날짜, v2 §2/Figure 3의 main/external context·함수 호출 확인. Complexity Trap 공식 v1 2025-08-29 및 로컬 v3 p.5 §3.1 관측 마스킹, pp.6–7 비교 결론 확인. 공식 arXiv와 JetBrains 페이지의 DL4C@NeurIPS2025 일치. Copilot 공식 v1 2026-07-30, 원문 §6 Table 6의 7.8% 세션/44.2% 토큰 분모 확인. 압축 호출 자체 비율로 오독하지 않았음.
4. **파트 4 문제 없음 (5항목).** p.3 TR/TRC 개념과 p.15 A.2 구현 대조. 최근 eligible tool responses 세 개 보호, standalone TRC가 목표 미달 시 TR fallback한다는 중요 조건 포함. 그림의 [output cleared] 설명과 일치함.
5. **파트 5 문제 없음 (5항목).** p.3·p.15 SU/SS·부분 요약·추가 모델 호출·기본 동일 요약 모델 확인. quote_summary의 omit or alter가 설명과 일치함. 실패·파일 정보를 요약에 남길 수 있다는 것은 기대/예시로 구별함.
6. **파트 6 문제 없음 (9항목).** pp.3–4 세 축과 D=0.5의 목표, depth-invariant 제외 확인. p.2 65 policies/nearly35,000, pp.4·17 100/40 선택 과제, 세 모델, p.18 mini-swe-agent 2.2.6/로컬 vLLM/서로 다른 GPU 표 확인. 대략 실행 횟수를 확정 정수로 바꾸지 않았음.
7. **파트 7 문제 없음 (8항목).** p.6 §4.1 및 Figure 2/5 직접 확인. Qwen SWE FC53.0/TRC53.7/SU42.0%, TRC tokens0.57·latency0.79, SU tokens0.59, SU−11.0%p 맞음. 두 번째 패널의 token·wall-clock 방향 맞음. 100문제 주실험 조건 있음.
8. **파트 8 문제 없음 (6항목).** p.1 초록 및 p.6 §4.1의 Qwen Terminal-Bench 일부 약 1/3 tokens, 1.2–1.8배 시간 확인. 모든 압축 정책 point estimate의 시간이 FC보다 큼. main_terminal 직접 확인. 저장소 재탐색 vs 일시적 관측은 “We suspect”의 가설이며 원인 입증과 구별함. 모든 모델·모든 작업으로 일반화하지 않았음.
9. **파트 9 문제 없음 (7항목).** p.19 식(1)의 fresh+0.1cached+summary 입력 비용, summary fresh 취급, output 비용 제외 확인. p.20 Qwen prefix caching disabled 및 measured provider bill/cache-hit rate 아님을 그림에서도 확인. 실측 지연을 실제 캐시 손실로 단정하지 않음.
10. **파트 10 문제 없음 (7항목).** p.7 Figure 3c SU 10K·20K, D0.5 셀 50.7→62.7, 1.10→0.92, 653→599 직접 확인. 25문제로 분리하고 p.19 A.5의 all attempts 표 포함 규칙도 맞음.
11. **파트 11 문제 없음 (5항목).** Figure 3c 15K TR D0.3 61.3→D0.7 50.7, SU50.7→60.0 확인. D는 제거 비율 목표임을 p.4 §2.3 식으로 확인. 방향이 primitive별로 다름을 이 조건 안에서만 서술함.
12. **파트 12 문제 없음 (6항목).** p.8 Figure 4/§4.2, p.19 해결 정의 확인. FC53·TRC+SU52·gain7·loss8 모두 그림과 일치. 평균 resolve rate와 majority-task count를 구별함. 산술도 정확함.
13. **파트 13 문제 없음 (6항목).** p.8 Figure 5a OTRC 자기 FC 대비 Qwen0.88/Devstral1.42/GLM0.94 확인. Figure5b SS-p−SS 6.7/8.7/8.0%p 확인. p.9의 모델별 threshold 별도 calibration 및 원인 미분리 한계와 맞음.
14. **파트 14 문제 없음 (9항목).** p.17 A.3의 Qwen 고정·25문제·15K, pp.28–29 A.6.3/Figure13의 두 요약기·두 정책 성공률 6개 확인. figure13의 오른쪽 latency 패널에서 두 대체 요약기가 모두 평균1보다 큼. 시간비율 공통 과제 수 SU10/TRC+SU23을 성공률 표본25와 구별함. 전 작은 모델에 대한 법칙으로 과장하지 않음.
15. **파트 15 문제 없음 (7항목).** p.19 A.5의 시간 제한 제외·step 제한 포함·공통 eligible tasks·성공률 모든 시도·최소 측정 조건 구조 확인. 성공한 실행만 추린 것이 아님을 정확히 적음. 95% task bootstrap은 같은 과제의 모든 시도를 묶어 재표집하는 방식과 일치함.
16. **파트 16 문제 없음 (5항목; P1 직접인용 교정 필요).** p.1 기관, 공식 ECE Assistant Professor와 Systems/ML 연구 분야 확인. 전작 세 편 저자와 선택 논문 네 이름의 교집합 없음. 동일 연구팀의 연속작이나 저자별 담당 역할을 만들어내지 않음. 시스템 연구 관점은 ‘이 글에선 … 읽었음’으로 해설임을 표시함.
17. **파트 17 문제 없음 (6항목).** Figure 5b Terminal-Bench OTRC+SS-p−OTRC 셀 −12.5/−7.5/−12.5 직접 확인. 부분 구조형 요약을 단계별 clearing에 덧붙인 비교라는 범위 맞음. I4 적용 제안과 F27 세 open-weight 모델·두 coding 부분 표본의 일반화 한계를 구분함.
18. **파트 18 문제 없음 (6항목).** 실제 캐시·출력 과금·상태 고정 분기는 I6의 후속 검증 제안이지 완료 실험 주장이 아님. 직접 후속 원문을 ‘확인 못 함’이라고 한정함. PAIR2609.36526 로컬 원문 전체에서 Satish/Beyond Token Savings/2609.32961 미검색을 재확인했으며 계보의 단정적 연결을 피함. arXiv/PDF/DOI URL과 마지막 세 줄 요약의 조건 맞음.

## 독립 재조회한 외부 원문

- 선택 논문 공식 메타데이터: https://arxiv.org/abs/2609.32961v1 (재조회 2026-10-15).
- MemGPT v1 날짜/저자: https://arxiv.org/abs/2310.08560v1 ; v2 방법: https://arxiv.org/html/2310.08560v2 §2, Figure 3.
- The Complexity Trap 공식 날짜/워크숍: https://arxiv.org/abs/2508.21433 ; https://kairos.jetbrains.com/research/publications/complexity-trap ; 로컬 v3 PDF p.5 §3.1·pp.6–7.
- Copilot 최초 공개: https://arxiv.org/abs/2608.00101v1 ; 수치: https://arxiv.org/html/2608.00101v1 §6 Table 6.
- 교수 직책/분야: https://ece.utexas.edu/people/faculty/neeraja-yadwadkar (재조회 2026-10-15).

## 검토 범위 한계

독립 검토가 논문의 실험을 재실행한 것은 아님. 공개 PDF/HTML에 보고된 수치와 원고의 일치·조건·확신 수준을 확인한 것임. 현재 확인되는 공식 채택 표시가 없음을 근거로 ‘미확인’으로만 판정했으며, 실제 비공개 심사 진행 여부나 후속 연구의 절대 부재를 보증하지 않음. 정리 이미지 JSON은 별도 파일이 없고 본문은 원문 그림·표·문단 인용만 사용하므로 해당 없음.

## 최종 수정 재확인

편집자의 수정 후 report.md와 ledger.md를 다시 대조함. F11·F14·P1은 실제 연속 원문 인용으로 교체되었고 F21은 Figure 4의 표 전사값임을 명시하여 합성 직접인용 문제가 해소됨. F18에는 p.4 §3 표본 근거, F24에는 p.17 A.3의 15K 설정 및 pp.28–29 수치 위치, F25에는 pp.28–29 문장과 p.29 표본 수 위치가 추가되어 정확해짐.

파트 2의 단정적 행동 변화 문장은 선행 연구 연결 문장으로 대체되어 확신 수준 지적도 해소됨. 추가된 F30의 토큰 설명은 모델이 텍스트를 처리하는 작은 단위라는 기초 용어 설명이며 단어와 토큰이 일대일이라는 오해를 만들지 않음. SWE-bench의 저장소 오류 수정과 Terminal-Bench의 터미널 작업이라는 추가 설명도 p.4 §3·p.17 A.3와 일치함.

파트 8의 일시적 터미널 관측을 다시 찾기 어려울 수 있다는 문장은 저자 추정으로 남아 있고, 원인을 격리해 입증하지 않았다는 다음 문장을 유지함. 수정된 최종 원고의 숫자·조건·확신·그림 설명에서 추가 오류를 발견하지 못했음. 원고와 원장을 직접 수정하지 않았음.
