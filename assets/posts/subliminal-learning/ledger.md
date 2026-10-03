# 팩트 원장: Towards Understanding Subliminal Learning
기준일: 2026-10-04 (Asia/Seoul)
원문 버전: arXiv:2509.23886v2 (39쪽)
날짜 기준: arXiv 최초 공개, 판본 날짜 별도

- F1 | p.1 Abstract | "small set of divergence tokens" | 취향 전달에 중요한 일부 분기 토큰을 식별한 발견형 연구
- F2 | pp.2–3 §2 | "initialized from the same base model as the teacher" | 학생은 같은 기반 모델에서 출발하며 취향 지시는 학습 입력에 없음
- F3 | p.13 Appendix A | "No additional characters or formatting are allowed." | 숫자는 0–999의 정수, 구분자·괄호 등 허용 서식만 남김
- F4 | p.3 §2 | "Qwen2.5-7B-Instruct" | Qwen2.5-7B-Instruct와 Gemma 3-4B-it, 다섯 시드 평균
- F5 | p.13 Appendix A | "ten epochs on 10,000 prompt–completion pairs" | 1만 쌍을 10에포크 학습함
- F6 | p.13 Appendix A | "rank-8 LoRA adapters with α = 8" | 전체 층의 지정 가중치에 랭크 8 LoRA, α=8, Adam을 사용함. 전체 가중치 미세조정과 구별함
- F7 | p.13 Appendix A | "percentage of responses containing the target word" | 질문별 200응답을 온도 1로 샘플링해 목표 동물 단어 포함 비율을 평가함
- F8 | p.3 §4 | "always pick the highest-probability token" | greedy는 매번 최고 확률 토큰을 고름. Qwen 고양이·개, Gemma 부엉이 전달 등 관찰
- F9 | pp.3–4 §4 / p.14 Appendix B | "50 most entangled tokens" | 얽힘 상위 50개 숫자를 포함한 샘플을 제외해도 일부 취향 전달이 남음. 모든 얽힘 제거라고 쓰지 않음. Appendix B에서 Qwen/Gemma tokenizer는 digit-based로 명시
- F10 | p.4 Definition 5.1 | "same prefixes" | 사실 스승이 만든 동일 접두 문맥에서 취향만 바꾼 스승의 최고확률 예측이 갈리면 분기 토큰. 숫자 고유 속성이 아닌 위치·문맥별 정의
- F11 | p.5 §5.1 | "retained masked tokens as context in both cases" | 토큰은 문맥에 남기고 학습 손실 계산 대상만 제한함
- F12 | p.5 §5.1 / p.17 Table 1 | "4.7% (Qwen) and 13.2% (Gemma)" | 온도 샘플 데이터 분기 비율 약4.7%,13.2%; 표 평균4.69%,13.18%. greedy는 약7.5%,18.3%
- F13 | p.5 Figure 3 / §5.1 / p.8 Figure 8 | "typically preserved or amplified" | 분기만 학습하면 보통 유지·증폭, 제외하면 보통 억제. Qwen greedy panda·일부 penguin 예외. §5.1·§7 및 Figure8에서 부정렬도 두방향손실 실험에 일관된 패턴 보고
- F14 | p.6 §5.2 | "attribution patching" | 개입을 근사하는 attribution patching+integrated gradients로 중요 층을 조사한 뒤 단일층 LoRA로 검증함
- F15 | p.6 Figure 5 | "layer 0 or 7" | 0 또는7층만 LoRA 학습해도 전달,14·21·27층과 Gemma33층은 미미한 전달
- F16 | p.35 Appendix S / pp.37–39 Figures 39–41 | "first ten or more layers" | Qwen에서 앞10개 이상 동결 시 전달 거의 제거(Figure39 caption: out of28 inQwen). Gemma패널은10개동결에서도일부잔여전달 있어 본문p35의포괄문장범위를좁힘. Qwen 학습수치 유지가 일반화 성능 개선은 아님
- F17 | p.7 §6.1 | "leaving completions unchanged" | 숫자·답을 유지하고 입력 문구만 의미보존 재표현함. 보통 전달 감소
- F18 | p.7 §6.1 / pp.24–26 Appendix J | "biased teacher itself" | Qwen에서는 편향된 스승 자신이 재표현해도 보통 감소. Gemma는 취향을 누설해 같은 조건을 확보 못함
- F19 | p.26 Appendix J / Figure 27 | "paraphrasings surprisingly strengthens preference transmission" | Gemma penguin은 재표현 뒤 전달 강화 예외
- F20 | p.13 Appendix A / p.26 Appendix J | "evaluated on the training set" | Figure6·27 과제성능은 훈련집합 숫자 토큰 재현, Figure28은 held-out. 일반 능력 보존을 증명한 게 아님
- F21 | p.8 §6.2 Figure 7 | "25% nearly eliminates it" | Qwen 본문 그림에서 무편향 교사 데이터10% 혼합 크게 감소,25% 거의 제거. 모든 모델 보장 아님
- F22 | p.8 §6.2 / p.28 Figure30 | "unexpected cross-model transfer" | Gemma→Qwen eagle, Qwen→Gemma penguin 전달 사례 있음. 모델가족 다르면 무조건 안전하다고 쓰지 않음
- F23 | pp.8,27–30 Appendix M | "risky financial advice" | Qwen7B 스승의 위험 금융조언 미세조정 변형에서 숫자 데이터로 부정렬 전달 조사. 취향은 프롬프트, 이 실험은 가중치
- F24 | pp.29–30 Appendix M | "scores less than 30" | Gemma3-27B-it 판정의 정렬점수30미만, 일관성50미만 제외,10단어 이하 답변 접미어 사용
- F25 | pp.31–32 Appendix N | "higher thresholds did not produce subliminal learning" | Qwen32B 수학답 필터 점수50미만 제외,더 높은 문턱은 전달 미관찰. 수학답 실험은 필터조건 민감
- F26 | p.9 Limitations / pp.34–36 | "may not reflect how frontier models convey traits in practice" | 정형화된 증류 실험. 모든 모델·취향 전달 아님. 문맥 있는 사실질문 영향도 제한적
- F27 | pp.14–15 Appendix C | "only as intuition, not as a formal proof" | 독립성·직교 편향방향 등 강한 가정의 수학 설명은 정식 증명 아님
- P1 | p.1 author block | "University of Freiburg" | Schrodi·Kempf 공동기여, 프라이부르크 소속. Brox도 프라이부르크. Barez는 Oxford·WhiteBox·Martian. 논문시점 소속
- P2 | p.10 Acknowledgments | "Alex Cloud, James Chua, and Jan Betley" | 전작 저자 세 명에게 토론 감사. 이번 저자 네명과 전작 여덟명은 이름 목록상 겹치지 않음
- L1 | 1503.02531v1 pp.1–2 | "soft targets" | Hinton·Vinyals·Dean 2015-03-09, Google 표기. 앙상블 지식을 작은 모델로 증류하고 확률분포를 학습 표적으로 사용. 이번 논문 §1에서 방법 배경으로 인용
- L2 | 2507.14805v1 pp.1–4 | "filtered to ensure they match the format" | Cloud·Le·Chua·Betley·Sztyber-Betley·Hilton·Marks·Evans,2025-07-20. 숫자·코드·추론문으로 특성 전달 관찰, 이번 연구가 실험절차 확장
- L3 | 2507.14805v1 pp.9–10 Figure9 | "ICL fails in every setting tested" | GPT4.1nano에서는 같은 숫자데이터를 문맥에 넣는 방식은 효과 재현 못함. 이번 보고는 학습과 대화 읽기를 구별
- L4 | https://owls.baulab.info/ + main p.3 §3 (2026-10-04) | "We hypothesize" | Zur 외 2025 저자 공식 글의 토큰 얽힘·분포누출 가설을 이번 논문이 필요조건으로 검증. 공식 블로그 기준만 사용, 상세 workshop판 PDF는 접근차단
- L5 | 2603.09517v1 p.2 Related Work | "We keep the context fixed" | Gisler·He·Qiu,2026-03-10. 이번논문은 입력문구 변경,후속논문은 문맥을 고정해 출력문장 재표현을 학습; 조작 차이 명시
- L6 | 2603.09517v1 pp.3–5 / p.13 Table8 | "+18.1pp" | GPT4.1nano,1만쌍10epoch. 부정적 돌고래 문장 재표현 학습은 중립교사 대비+18.1%p,독수리+12.8%p. 동물취향만·미세의미차이 배제못함
- L7 | 2606.00995v3 pp.2–5 | "single direction" | Blank·Bhatia·Rajamanoharan·Conmy·Nanda,2026-05-31 최초·06-10v3. 이번논문을 인용해 신호 위치에서 학습 중 활성방향 전달로 설명 확장. Qwen7B/Gemma4B
- L8 | 2606.00995v3 pp.4–5 §3.2–3.3 | "removes over 50%" | 저자들은 학생 활성방향 교체로 특성행동50%이상 감소했다고 보고함,스승방향을 제거한 데이터는 거의 모든 효과제거. 학생효과완전제거라 쓰지 않음
- W1 | https://arxiv.org/abs/2509.23886 (2026-10-04) | "Submitted on 28 Sep 2025" | 최초2025-09-28,v2 2026-03-05,39쪽,arXiv DOI10.48550/arXiv.2509.23886
- W2 | https://proceedings.iclr.cc/paper_files/paper/2026/hash/b51b50262b492dd89bb9cd3105a46702-Abstract-Conference.html (2026-10-04) | "ICLR 2026" | 공식 학회 proceedings로 ICLR2026 게재 확인
- W3 | https://arxiv.org/abs/2606.00831v2 (2026-10-04) | "some of the main claims made in this paper are incorrect" | LoRA Artifact 저자들이09-08 v2에 일부핵심주장 오류 및 대폭수정 준비 공지. 정설로 사용안함, 어느 주장이 틀렸는지 추측안함
- W4 | https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html (2026-10-04) | "non-exclusive license to distribute" | 메인 논문은 arXiv 배포용 비독점 라이선스,CC 재사용허가 아님. 해설용 제한된 그림 인용만 하고 PDF 공개복제 안함
- W5 | https://github.com/lmb-freiburg/divergence-tokens (2026-10-04) | "Official code" | 코드 공개 및 ICLR2026 공식 코드 표기 확인
- W6 | https://arxiv.org/abs/2603.09517 (2026-10-04) | "Accepted for Spotlight presentation" | arXiv 저자기재 EACL2026 SRW Spotlight 승인. 본보고에서 별도공식학회상태는 단정안함
