# 팩트 원장
기준일: 2026-10-14. 원문: arXiv 2610.12125v1, 33쪽 전체 정독.
날짜 기준: arXiv 최초 공개. 인물 소속은 논문 당시 기준.

## F: 본문
- F1 | p.1 | "The learner who does not learn: when optimizing a pedagogical metric degrades LLM tutoring" | 제목.
- F2 | p.1 | "Daniel Dominguez Figaredoᵃ, Rafael Fernández De la Cruzᵃ"; "ᵃ UNED, Madrid, Spain" | 두 저자, UNED 소속. 이름 악센트는 arXiv 메타데이터 표기 따름.
- F3 | p.1 각주 | "supported by the Tinker Research Program funded by Thinking Machines Lab" | Tinker Research Program 지원. 회사의 독립 검증·보증을 뜻하지 않음.
- F4 | p.4 | "conditions are not fixed properties of a learner" | 학습 과정에서 지식 상태·단계·도움 필요가 달라진다는 이론적 배경.
- F5 | p.5 §3.1 | "scale from −1.0 to +1.0" | 자체 설계 Pedagogical Adaptivity Index, PAI 범위 −1~+1.
- F6 | pp.5–7 §3.1.1 | "Design a sequence of five learning activities"; "25 selections and 25 descriptions" | 사례당 활동 5개×결정 5개. 설명 25개 포함.
- F7 | p.6 | "The index only scores the selections" | 난도, 인지 과제, 지원 구조, 참여 방식, 교과 접근의 선택지만 자동 채점. 설명문은 사람에게 보였지만 점수에 미반영.
- F8 | p.7 | "yielding eleven alignment sub-matrices"; "PAI is equal ... to the mean of its 25 decision scores" | 조건과 선택지 대응표 11개, 25개 결정 점수 단순 평균.
- F9 | p.8 §3.1.3 | "contains no term relating choices across the five activities"; "remain constant throughout the sequence" | 활동 사이 관계 항 없음, 학습자 조건 고정. 범위: 동일 선택지·고정 문맥·독립 점수·평균이라는 구조.
- F10 | pp.9,29 | "2,000 balanced scenarios"; "grok-3-fast" | 합성 사례 2,000개. 실제 학생 2,000명 아님. 다섯 조건의 432칸(3×4×3×4×3)을 반복 표본화한 시나리오.
- F11 | p.9 §3.3 | "Gemini 3.1 Pro Preview"; "Qwen3-32B" | 최초 감사는 Gemini, 모든 미세조정과 가중치 분석은 Qwen. Gemini를 미세조정한 연구 아님.
- F12 | pp.9,29 | "589 cases"; "30 cases with the lowest PAI"; "8 cases with the highest"; "200 cases ... disjoint" | 학습 589, 사람 비교 개입 30은 학습 포함, 불변 비교 8, 학습 제외 행동평가 200.
- F13 | pp.10,30 | "fixed bank of 100 learner-independent phrases"; "three epochs" | greedy 정답은 각 결정 최고점 반복, 문구는 고정 100개 은행. Qwen LoRA 3epoch, lr 1e-4.
- F14 | pp.10,30 | "r ∈ {1, 4, 8, 16}"; "LoRA α 32"; "Random seed Not fixed" | 네 rank, 고정 alpha로 업데이트 크기 동시 변화. 각 조건 1회 학습, seed 고정 안 함.
- F15 | p.10 §3.5 | "Thirty-one educators, out of the 51"; "prior degree in education"; "graduate AI-and-Education program" | 31명은 교육학 학위 보유 대학원생, 현직 교사 표본 아님. 51명 초청, 31명 양쪽 평가 완료.
- F16 | p.10 | "between four and eleven independent ratings, with a mean of 6.5" | 각 사례 평가자 4~11명. 블라인드, 수주 간격 2회, 사례 순서 재무작위.
- F17 | p.12 §4.1 | "mean PAI of +0.29 (SD 0.11)" | Gemini 2,000개 전체 평균. 30개 저점 평균 +0.05와 분모 다름.
- F18 | p.13 §4.2 | "+0.05 to +0.42"; "4.46 to 3.03"; "p < .00001" | 30개 개입 사례, 원 Gemini→greedy r8 Qwen의 PAI +0.37, 사람 1~5점 평균 −1.43. 인과를 반복만으로 단정 안 함.
- F19 | p.13 | "4.39 to 4.51, p = .38" | 원 출력 그대로 보여준 8개 비교 사례, 유의한 변화 확인 안 됨. 미세조정 모델이 통제 사례를 생성한 비교 아님.
- F20 | p.13 | "ρ = −0.15, p = .39"; "α ≈ 0"; "α = 0.27" | 원 점수와 사람평가 상관 유의하지 않음, 초기 평점 천장효과·낮은 평가자 일치도. 변화 크기 상관도 −.24 p=.21, 일반 역상관 법칙 아님.
- F21 | pp.13–14 | "monotony in 19–25%"; "at most 3%" | 코더가 수정 계획 비판 19~25%에서 단조로움 표시. 어휘만 아닌 선택 반복을 지적. 코딩 인과시험 아님.
- F22 | p.14 | "11.9 vs. 16.7 words"; "0.21 to 0.03" | 설명이 짧고 사례 단어와 겹침 낮아짐. 반복 선택과 일반적 문구 영향 분리 못 함.
- F23 | pp.14–15 | "fully monotone sequences in 100%" | 네 rank, 학습 589개에서 모든 계획이 각 결정마다 한 선택 반복. 활동 설명문이 문자 단위로 모두 같다는 뜻 아님.
- F24 | p.15 | "200 cases"; "100% ... mean PAI of 0.42 ... base proxy's ... 0.30" | 학습 제외 200개도 계획 내부 반복 100%, Qwen 전후 PAI .30→.42. 인간 평가는 아님.
- F25 | p.15 Figure 6 | "same option, DP2-b (iterative practice)"; "0.24 to 0.04" | 학습 제외 200명 합성 사례 모두 인지 과제 반복연습 하나. 다른 네 결정은 사례별 변함. DP2 .24→.04, 전체 평균은 오름.
- F26 | p.16 | "+0.37 to +0.07 (0.34 vs. 0.27, p = .047)" | 가상 단계 변화로 기존 출력을 재채점했을 뿐 재학습 아님. 효과 축소, 사람평가와 정렬 안 됨. 스케줄 따라 −.02~+.15.
- F27 | pp.16–17 | "Between 75% and 93%"; "r = 8: 89%" | 업데이트 에너지 중 출력 투영부 비중. 출력 투영은 은닉표현→단어 점수 마지막 선형 변환. 내부 전체 추론 무변화 증명 아님.
- F28 | p.16 | "748 verbatim strings ... out of 750 descriptions" | 개입 30개×25=750, 748개가 100문구 은행과 문자 그대로 일치. 얕은 출력 편집 해석과 일관된 관측.
- F29 | p.18 Table 4 | "Learning stage ... 0.385 ... 0.325 ... 0.395"; κ "0.157 ... 0.046 ... 0.149" | 학습단계 정확도 Gemini38.5%,Qwen32.5%,TFIDF분류39.5%. chance-corrected kappa 낮음. 문장 단서 약함을 시사, 절대 정보 없음 증명 아님.
- F30 | p.20 Table 5 | "Publish the argmax"; "Score sequence-level properties" | 최고점 계획을 공개, 반복·진행·지원 축소를 별도 평가하자는 제안. 유효성 실험으로 보증한 완성 해법 아님.
- F31 | p.21 | "no educators rated the base proxy" | 인간 인과 대조군 빠짐. 수치·다양성 비슷함은 인간 질 동등함 증명 아님.
- F32 | p.21 | "cannot fully apportion ... collapsed selections and generic descriptions" | 낮아진 인간평가를 두 원인에 나눠 설명 못 함.
- F33 | p.21 | "human evaluation is in-sample"; "raters were graduate students rather than in-service teachers"; "case narratives are synthetic" | 실제 학생 학습이득·성적·장기효과 미측정. 사람평가는 학습 포함 사례.
- F34 | p.21 | "each condition was trained once"; "not yet demonstrated that removing ... preserves the gain" | 학습 반복 분산, 다른 모델, 실제 교육과정, 가중치 투영 개입 미검증.

## I: 해설용 계산·추론
- I1 | F8–F9의 구조 | 예시: A1.0,B0.5,C0,D−0.5 | 고정 점수 평균이면 A 다섯 번이 1.0. 합성 설명 예시이며 논문의 실제 점수표가 아님.
- I2 | F18 | 0.42−0.05=.37; 3.03−4.46=−1.43 | 서로 다른 척도라 높이를 직접 비교하지 않음.
- I3 | F25–F26 | 전체 평균과 활동별·사례별 차이를 동시에 보는 개발 체크는 이 글의 적용 제안 | TOPIK·한국어 학습 앱에 직접 검증된 결과라는 주장 안 함.

## W: 공개 상태
- W1 | https://arxiv.org/abs/2610.12125 (2026-10-14) | "[v1] Thu, 8 Oct 2026 15:18:26 UTC" | 최초공개 2026-10-08 UTC, 한국 10-09 00:18. 채택·저널 정보 없음; 동료평가 확인 못 한 프리프린트.
- W2 | arXiv 라이선스 링크 (2026-10-14) | "https://creativecommons.org/licenses/by/4.0/" | CC BY 4.0. 원저자·출처·변경사항 기재.
- W3 | https://github.com/MrEricPraline/pedagogical_adaptivity_in_LLM_tutors; p.1 (2026-10-14) | "Data and code" | 공개 저장소 주소. 논문의 데이터 공개 주장으로 제시, 전수 재현은 안 함.

## L: 계보
- L1 | Gao 외 원 PDF p.1, §2.1; PMLR https://proceedings.mlr.press/v202/gao23h.html | "a fixed gold-standard reward model plays the role of humans" | ICML 2023의 일반 보상 과최적화 연구. 교육실험 아님. 저자 Leo Gao, John Schulman, Jacob Hilton, 당시 OpenAI. arXiv 최초 2022-10-19.
- L2 | Sonkar 외 원 PDF p.1, §3–4; https://aclanthology.org/2024.findings-emnlp.797/ | "constructing a large-scale dataset using synthetic data generation techniques" | EMNLP Findings 2024. 좋은 튜터 행동의 합성 선호쌍 학습. 실제 학생 성적 아닌 선택 정확도 평가. 저자 Shashank Sonkar, Kangqi Ni, Sapana Chaudhary, Richard G. Baraniuk, 주 논문 저자와 겹침 없음.
- L3 | https://link.springer.com/article/10.1007/s10639-025-13857-2 (2026-10-14) | "Published: 15 December 2025"; "Accepted: 20 November 2025" | Explainable pedagogical alignment. Daniel Domínguez Figaredo, José Luis Fernández Vindel, Laura Guerrero Puerta. Daniel만 이번 논문과 겹침. 교육이론으로 모델 출력 감사. 출판사 초록 기준, 구독 본문 미확보여서 세부 수치·그림 제외. 권호 연도2026과 최초 공개2025 구분.
- L4 | 이번 논문 p.2, p.19 | "pedagogical drift"; "shared method could account for part of the convergence" | 전작은 문제제기 맥락, 이번은 평가 지표 최적화의 구조 분석. 같은 Bloom 방법으로 독립 재현 주장 제한.
- W4 | arXiv 공식+제목/ID 검색 두 엔진(2026-10-14), lineage-audit.md | 식별 가능한 직접 후속 연구·독립 재현 찾지 못함 | 0회 전수·후속 없음 단정 안 함.
- W5 | arXiv https://arxiv.org/abs/2610.12125 (2026-10-14) | "arXiv-issued DOI ... (pending registration)" | DOI는 arXiv 발급 DOI 등록 대기 표시. URL https://doi.org/10.48550/arXiv.2610.12125.

- F35 | p.13 Figure4b vs §4.2/초록 | 그림 라벨 "4.45", 본문 "4.46" | 0.01 불일치. 본문값4.46을 사용하고 그림 표시4.45를 명시; 원인을 임의 추정 안 함.

- I4 | F29 Table4 단위 환산 | 0.385×100 = 38.5%; 0.325×100 = 32.5%; 0.395×100 = 39.5% | 정확도를 백분율로 표시.

- F36 | §3.8/AppendixD vs Figure5 | "n = 99" vs "n = 93" 범례 | 두 인간 코더 표본 크기 원문 불일치. 비율19~25%는 인간 코딩 부분표본이며 전체 약점설명 응답률 아님.

- F37 | AppendixB.4, LoRA 설계 해설 | "Epochs 3", "LoRA rank" | epoch=자료 전체 학습 횟수. LoRA는 저랭크 A,B 보정 행렬을 학습하며 rank는 이 내부 폭을 정함.
- F38 | §3.6 | "Frobenius norm" | 에너지는 가중치 업데이트 행렬 크기 기반 비중, 전력 소비량 아님.
