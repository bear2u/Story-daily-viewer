# 독립 검토: Trust the Critic More 해설

검토일: 2026-10-05 KST  
검토 대상: `report.md`, `ledger.md`, `lineage.md`, `text.txt`(arXiv:2609.39247v2, 29쪽), 전작 원문, 실제 그림 파일  
검토 기준: paper-report `references/fact-check.md`, `references/rubric.md`, `references/style-guide.md`  

## 종합 판정

**FAIL — 수정 후 재검토 필요.**

핵심 결과인 18.50%, 0.79/1.99×10²⁰ FLOPs, 2.5×, 20.57%, critic 진단 수치, readiness 문턱, 2k confound, 계산량 제외 범위, 버그, single-epoch 한계는 원문과 대체로 맞음. 특히 2.5×를 전체 GPU 비용으로 부풀리지 않았고, 2k 실험이 chunk 길이와 prefix-cut 간격을 함께 바꿨다고 적은 점은 정확함.

다만 다음 항목은 공개 전 반드시 고쳐야 함.

1. 실제 main 설정은 prefix당 16 continuations인데 파트 8에서 “네 갈래”라고 씀.
2. IMO-ProofBench 수치의 단위 `%`가 결과·ablation 전반에서 빠짐.
3. 10k chunk를 “완성 답보다 다섯 배 짧다”고 단정했는데, 50k는 실제 완성 길이가 아니라 총 response budget 상한임.
4. local-readiness 제거 ablation이 `no group & no audit` 조건이며 step 20에서 분기했다는 핵심 조건이 빠짐.
5. `header.png`를 재사용한 파트 11·22의 그림 설명이 실제 이미지 내용과 다름. `algorithm.png`도 전체 알고리즘이라고 해놓고 9행까지만 보임.
6. “3줄 요약”이 실제로 4줄이고, 10k 효과와 심사 상태를 본문보다 강하게 단정함.

## 사실·숫자·조건 검증

| 파트 | 판정 | 문제 문장 또는 항목 | 원문 근거 | 심각도 | 수정 권고 |
|---|---|---|---|---|---|
| 제목 | FAIL | “수학 풀이를 끝까지 안 쓰고 AI를 훈련시킨 방법” | p.1–2는 *every trajectory*를 끝까지 굴릴 필요를 없앤다고 주장하지만, p.5와 p.29에서 unready 문제·audit 문제·refill은 여전히 full rollout을 함. F3·F6·F24 | 과장 | “모든 수학 풀이를 끝까지 쓰지 않고도 AI를 훈련한 방법” 또는 “일부 수학 풀이를 끝까지 쓰지 않고 AI를 훈련한 방법”으로 범위를 드러낼 것. |
| 1 | PASS | GRPO의 동일 advantage와 마지막 계산 실수 예시 | p.2, p.4. F1·F2 | — | 문제 없음. |
| 2 | PASS | 저자·Stanford·공개일·v2·심사 미확인 | p.1, arXiv submission history. P1·W1·W2 | — | “심사 통과·게재처를 확인하지 못했음”이라는 유보가 적절함. |
| 3 | PASS | A3C의 n-step critic bootstrap, 이름 유사성 | 이번 논문 p.10–11, Mnih et al. 2016 p.1–2. L1 | — | 문제 없음. |
| 4 | PASS | GRPO가 value model 없이 group reward mean을 baseline으로 사용 | 이번 논문 p.4·11, DeepSeekMath p.13 Fig.4. F2·L2 | — | 문제 없음. |
| 5 | PASS | Le Critique는 privileged critic을 baseline으로 쓰지만 advantage에 terminal reward 유지 | Le Critique p.2 Fig.1; 이번 논문 p.11. L4 | — | 문제 없음. |
| 6 | PASS | Q-chunking의 action sequence policy·critic | Li et al. 2025 p.1–2. L3 | — | “online 탐색”은 offline-to-online RL 맥락이라는 점만 유지하면 됨. |
| 7 | PASS | replayed prefix에서 chunk를 만들고 endpoint value-group mean으로 advantage 계산 | p.1–2, p.5–6. F3 | — | 문제 없음. |
| 8 | FAIL | “그 뒤를 네 갈래로 조금씩 이어 쓰고” | main 설정은 `g=16 continuations per prefix`임(p.7, Table 4 p.27). Figure 1은 설명용으로 4개만 그린 도식임. F3·F7에는 main group size가 기재되지도 않음. | 오류 | “그 뒤를 여러 갈래로 이어 쓰고 / main 실험에서는 16갈래를 만들었음”으로 수정. |
| 8 | WARN | “같은 길이의 continuation 그룹” | p.2의 이상화 설명은 same length지만 실제 구현은 `at most b`이며 종료·예산 소진 시 더 짧아짐(p.6 Algorithm 1, p.29). | 사소 | “같은 최대 길이 예산의 continuation 그룹”으로 정밀화. |
| 9 | WARN | “그 문제의 직전 오차가 0.18 아래” | p.5는 “prior step it was sampled”, 즉 그 문제가 직전에 **샘플된 때**의 오차임. Appendix p.29도 local threshold 0.18 확인. F5 | 조건 누락 | “그 문제를 직전에 뽑았을 때 오차가 0.18 아래”로 수정. |
| 9 | WARN | “준비된 문제도 1/4은 끝까지 생성” | 실제로는 그 step에서 sampled ready problems `n` 중 `ceil(alpha n)`, alpha=1/4임(p.29, Table 4 p.27). F6 | 사소 | “샘플된 준비 문제의 약 1/4은”으로 완화. |
| 10 | FAIL | “완성 답보다는 다섯 배 짧은 구간” | 50,000은 실제 완성 답 길이가 아니라 prefix까지 포함한 total response budget임. Chunk는 최대 10,000 **new** tokens이고 남은 budget에 따라 더 짧음(p.27·29). F4 | 오류 | “50,000토큰 응답 상한의 1/5인 최대 10,000 새 토큰”으로 수정. |
| 10 | FAIL | “group 16개와 audit 1/4”의 태그가 `F6 F7` | group size 16은 Table 4 p.27에 있으나 F7에는 없음. F6은 audit 1/4만 뒷받침함. | 원장 불일치 | group size 16을 별도 F 항목으로 ledger에 추가하고 그 ID를 붙일 것. |
| 11 | WARN | “문제마다 답 16개를 생성했음”을 F8로 태깅 | 사실 자체는 Table 4 p.27에서 맞음. 다만 ledger F8의 위치는 p.7만 적혀 있고 한국어 요지에도 16 responses가 없음. | 원장 위치 불완전 | F8 위치에 `p.27 Table 4`를 추가하고 요지에도 문제당 16개를 명시. |
| 12 | FAIL | 18.50, 20.57 및 이후 ablation 수치에 `%` 없음 | 원문은 `IMO-ProofBench Score (%)`이고 p.2·7은 18.50%, 20.57%로 표기함. p.8–9의 18.66, 17.90, 16.62, 13.57 등도 모두 %임. F9·F12–F16·F20 | 오류 | 파트 12·14·15·16·17의 모든 benchmark score에 `%`를 붙일 것. 0–7 judge 원점수와 혼동될 수 있음. |
| 12 | WARN | “학습 단계도 120이 아니라 90이 걸렸고” | p.2는 **GRPO peak 18.50%를 넘는 데** AC2 90 steps, GRPO 120 steps라고 함. F9 | 조건 누락 | “그 18.50%를 넘는 데 120단계 대신 90단계가 걸렸고”로 수정. |
| 12 | PASS | 0.79×10²⁰ 대 1.99×10²⁰ decoding FLOPs, 2.5× | p.7. F9 | — | 범위는 파트 18에서 decoding FLOPs로 제한해 둬 정확함. |
| 13 | WARN | critic advantage 진단에서 “2,640개 응답”만 제시 | p.10은 `165 groups containing at least one critic prediction`이라는 표본 조건을 같이 제시함. F18 | 조건 누락 | “critic prediction이 하나 이상 있는 165그룹, 2,640응답”으로 보완. |
| 14 | PASS* | no-audit 18.66% at step 160, stale replay 17.90%, group-1 variant | p.8, Fig.3. F12·F13 | — | 수치는 맞음. 단 `%`는 붙여야 함. |
| 15 | PASS* | 2k: 16.03%/16.62%/13.57%, prefix-cut spacing도 2k로 변경 | p.9, Appendix p.17–18. F14 | — | confound를 정확히 밝혔음. 단 모든 score에 `%`를 붙일 것. |
| 16 | FAIL | local readiness 제거 변형의 비교 조건 누락 | p.9: 이 ablation은 **group과 audit도 없는 설정**이고 main AC2 step-20 checkpoint에서 분기함. 비교 상대 15.33%도 main AC2가 아니라 `AC2 w/o Group & Audit` with local readiness임. F16 원장 요지도 이 조건을 충분히 보존하지 못함. | 조건 누락 | “두 곡선 모두 group·audit가 없고, step 20에서 갈라짐. local readiness만 없앤 쪽…”이라고 먼저 적을 것. F16 ledger에도 조건을 추가. |
| 17 | WARN | “문제마다 16개 답 중 최고를 고르는 best-of-16” | Appendix p.18은 16 validation trajectories에 대한 bootstrap sample에서 max를 취해 best-of-16을 **추정**함. F20 | 사소 | “16개 검증 궤적을 bootstrap해 최고점을 고르는 best-of-16 추정치”로 수정. |
| 18 | PASS | decoding FLOPs 제외 범위, r=0.874, 32 GPUs·196 steps, GRPO 4.01% underestimate | p.25–26. F21–F23 | — | 핵심 조건이 정확함. 가능하면 제외 항목 중 elementwise operations도 함께 적으면 완전함. “2.5배의 분모”는 “2.5배 비교 범위”가 정확한 표현. |
| 19 | PASS | readiness bug가 step 42부터 활성화, 저자 예상임을 명시, scoring failures | p.29. F25·F26 | — | 재실험 결과가 아니라 저자 예상이라고 선을 그어 정확함. |
| 20 | PASS | epoching·complete rollouts·single-epoch future work | p.12. F24 | — | 문제 없음. |
| 21 | WARN | “10k 토큰씩 이어 쓰고” | 실제 chunk는 `at most 10,000 new tokens`이며 남은 response budget에 의해 cap됨(p.29). F3·F4 | 사소 | “최대 10k 새 토큰씩”으로 수정. |
| 22 | PASS* | code 공개·Apache-2.0, arXiv CC BY 4.0, beam search/MCTS는 제안 | 공식 arXiv·GitHub 확인, p.11–12. W3·W4·F28 | — | 본문 표현은 적절함. 아래 요약과 이미지 문제는 별도 수정 필요. |

## 그림·표 대조

**FAIL.** 사용한 본문 Figure 1/2/3/4/7/9, Table 4, 전작 그림, quote crop은 대체로 설명과 일치함. 그러나 아래 세 개는 불일치함.

1. 파트 8 `algorithm.png`: 실제 crop은 Algorithm 1의 1–9행까지만 보이고, 10행 critic error·11행 readiness update·12행 actor/critic update가 잘려 있음. “전체 순서는 아래 알고리즘”이라는 설명과 다름. 알고리즘 전체를 다시 crop하거나 “advantage 계산까지”라고 설명을 줄여야 함.
2. 파트 11 `header.png`: 실제 이미지는 제목·저자·Stanford만 보임. “Qwen3-4B·증명 데이터 조건”은 이미지에 없음. p.1 abstract의 해당 문장을 별도 crop해야 함.
3. 파트 22 `header.png`: 실제 이미지에 코드 링크가 없음. “논문 제목과 공개 코드 링크가 적힌 첫 페이지”라는 설명이 틀림. p.1 하단의 `Code available at ...`까지 포함해 새 crop을 만들거나 설명을 제목·저자 이미지로 고쳐야 함.

나머지 그림 설명은 확인 범위에서 실제 파일 내용과 맞음.

## 3줄 요약 검증

**FAIL.** 제목 아래 “3줄 요약”은 실제로 네 줄임.

- 1행 “준비된 문제에서 … 끝까지 쓰지 않고도 학습”은 F3·F5 범위에서 맞지만, “일부 actor 갱신”이라고 쓰면 더 정확함.
- 2행 “10k 토큰 조각과 문제별 신뢰 검사가 효과를 냈음”은 태그가 없고, 10k 대 2k 비교는 prefix-cut spacing도 함께 바뀌어 chunk 길이의 독립 효과를 입증하지 못함(F14). 본문 파트 15의 유보와 모순됨.
- 3행 “반복 데이터와 완성 rollout도 필요”는 F4가 아니라 주로 F6·F24가 뒷받침함.
- 4행 “공식 심사는 아직임”은 W2의 “확인하지 못했음”보다 강함. 비공개 심사나 미표시 게재를 배제할 수 없으므로 “공식 심사 통과는 확인하지 못했음”을 유지해야 함. “single-epoch 재현”도 아직 수행된 실험이 없으므로 “single-epoch 검증”이 더 정확함.

권장 3줄:

> AC2는 준비된 문제의 일부 actor 갱신을 최대 10k 토큰 조각만으로 수행했음.  
> 18.50%를 넘는 데 decoding FLOPs는 GRPO보다 2.5배 적었지만, 전체 GPU 비용 비교는 아님.  
> 반복 데이터와 완성 rollout이 여전히 필요하며 single-epoch 검증·공식 심사 통과는 확인되지 않았음.

## 흐름·설명 검토

### 경계 판정

- 좋음: 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 7→8, 8→9, 9→10, 10→11, 11→12, 12→13, 13→14, 14→15, 15→16, 18→19, 19→20, 20→21, 21→22
- 약함: 16→17. correct-only/local-readiness ablation에서 best-of-16으로 바로 이동해 왜 지표를 바꾸는지 한 박자 늦게 이해됨. “평균 점수에서 차이를 봤으면, 최고 답 하나를 고를 때도 그런지 확인해야 함”처럼 질문의 이유를 붙일 것.
- 약함: 17→18. best-of-16 다음에 “2.5배의 분모”가 나와 2.5배가 best-of-16 결과인지 잠깐 헷갈림. “계산량 얘기가 나온 김에, 앞의 평균 점수 2.5배가 어디까지 센 값인지 봄”처럼 가리키는 대상을 명시할 것.

### 비약·설명

- 파트 8의 “네 갈래”는 Figure 1의 설명용 가지 수와 main 실험의 g=16을 섞어 초심자에게 잘못된 모델을 만듦.
- 파트 10의 “다섯 배 짧음”은 상한과 실제 길이를 같게 취급함. 장면은 쉬우나 원인 구조가 틀림.
- 파트 13 “전문가용으로”는 왜 이 진단이 필요한지 설명하지 않음. “그럼 terminal reward 없이 critic을 믿어도 되는지 직접 재봄”이 앞 결과와 더 잘 이어짐.
- 파트 16은 no-group/no-audit 공통 조건을 빼서 local readiness 효과를 main AC2와 직접 비교한 듯 보이게 함.

회수는 대체로 잘 됨. 파트 10의 2k 밑밥은 파트 15에서 회수되고, 도입의 마지막 계산 실수는 파트 21에서 다시 답함. 마지막은 코드·검증 과제로 현재와 앞으로를 연결함.

## AI 티·문체 검토

**WARN — 음슴체와 짧은 호흡은 잘 지켰지만 반복 패턴이 보임.**

1. 파트 9 “여기부터 한 파트는 준비도 계산임 / 수식이 싫으면 마지막 세 줄만 보면 됨”은 실제 수식을 제시하지도 않고, 독자 행동을 예고하는 메타 문장이라 지우는 편이 자연스러움.
2. 거의 모든 파트가 “아래…보셈 / …곳을 보셈 / …적혀 있음”으로 그림을 소개함. 그림 안내는 필요하지만 같은 모양이 반복돼 템플릿처럼 읽힘. 핵심 두세 장만 “보셈”을 남기고 나머지는 사실 다음에 곧바로 이미지를 배치하면 됨.
3. checker가 `A가 아니라 B` 대구 6회를 경고함. 모두 잘못은 아니지만 “복사한 실험은 아님”, “숫자 head가 아니라”, “전체 GPU 비용이 … 뜻은 아님”, “도운 게 아니라”, “모든 rollout을 없앴다는 뜻이 아님”이 몰려 있음. 가장 중요한 범위 제한 두세 개만 대비형으로 남길 것.
4. 파트 18 “2.5배의 분모”는 사람 말투라기보다 수사적이면서 수학적으로도 부정확함. “2.5배가 센 건 decoding뿐임”처럼 바로 말하는 편이 좋음.
5. 파트 19 “실험 코드에도 숨은 조건”은 실제 근거가 논문 Appendix C p.29임. “부록에는 숨은 조건 하나가 더 적혀 있음”이 출처와 흐름 모두 자연스러움.

`check_report.py --strict` 재검사 결과는 ERROR 0, WARN 3이었음: `A가 아니라 B` 대구 6회, 파트 16→17 연결 약함, 파트 17→18 연결 약함. 자동 검사로는 잡히지 않은 숫자 단위·그림 설명·요약 문제를 위에서 추가 확인함.

## 원장 검증

**WARN.** 원장 인용 자체는 대부분 원문에서 확인됨. 다만 아래는 보강이 필요함.

- F7은 main group size 16을 뒷받침하지 않음. Table 4 p.27의 `g=16`을 별도 F 항목으로 추가.
- F8 위치에 Table 4 p.27을 추가해 evaluation responses per problem=16을 추적 가능하게 만들 것.
- F14는 2k chunk와 prefix-cut spacing이 함께 바뀐 confound를 잘 보존함. 이 유보를 3줄 요약에도 유지해야 함.
- F16에 “두 비교 run 모두 no group/no audit, step-20 branch” 조건을 넣을 것.
- F22는 selected GRPO steps 161–180에서 4.01% underestimate라는 좁은 범위를 report에도 가능하면 유지할 것.
- W2의 상태는 “심사 전” 확정이 아니라 “공식 심사 통과·게재처 미확인”임. 본문은 이를 지켰지만 요약이 어김.

## 채점 관점의 현재 상태

- 정확성: **1/3** — ERROR 0이지만 위의 사실·단위·그림·요약 오류가 남아 있음.
- 연계성: **2/3** — 두 경계가 약함. 도입 회수와 2k 밑밥 회수는 좋음.
- 재미: **2/3** — 마지막 계산 실수, 2k 역전, step-42 버그가 밑밥 뒤에 배치됨.
- 설명력: **2/3** — 핵심 메커니즘은 따라가기 쉬우나 네 갈래·다섯 배 설명이 잘못된 직관을 만듦.
- 전문성: **2/3** — 핵심 설정·진단·ablation·compute accounting을 다뤘으나 unit과 조건 누락이 있음.
- 사회 맥락: **2/3** — 공개일·코드·프리프린트 상태는 날짜와 함께 제시됨. 저자·기관 맥락은 Stanford 소속 외에는 얕음.
- 말투: **2/3** — 음슴체는 안정적이나 그림 소개와 대구가 반복됨.

위 FAIL 항목을 반영하고 원장 태그를 보강한 뒤 checker를 다시 돌리면 PASS 가능함.

---

## 수정본 재검토 — 2026-10-05

### 재검토 판정

**FAIL — 사실관계 핵심 수정은 통과했으나, 공개 전 고칠 항목 2개가 남음.**

재검토한 파일: 수정된 `report.md`, `ledger.md`, `figures/algorithm.png`, `figures/abstract_conditions.png`, `figures/code_link.png`.

### 통과한 핵심 항목

- 제목이 “일부 수학 풀이…”로 바뀌어 full rollout이 여전히 남는 범위를 보존함.
- main 설정을 prefix당 16 continuations로 바로잡고 F29를 추가함.
- 18.50%, 20.57%와 모든 ablation 점수에 `%` 단위가 붙음.
- 10k를 실제 완성 답의 1/5이라고 하지 않고, prefix 포함 50k response budget 상한의 1/5인 **새 토큰 상한**이라고 고침.
- local-readiness 비교가 no-group/no-audit 공통 조건이며 main AC2 step-20 checkpoint에서 분기했다고 명시함. F16도 같은 조건으로 보강됨.
- best-of-16을 bootstrap 추정치라고 고치고 critic 진단의 165 groups 조건을 보강함.
- 16→17, 17→18 경계가 자연스럽게 연결됨.
- `algorithm.png`는 1–12행 전체가 보임.
- `abstract_conditions.png`에는 Qwen3-4B, FineProofs-RL, IMO-ProofBench 조건이 실제로 보임.
- `code_link.png`에는 GitHub 코드 링크가 실제로 보임.
- 마지막 요약은 정확히 세 줄이고 “심사 통과 미확인”의 유보를 유지함.

### 남은 공개 차단 항목

1. **파트 19 중복 오타**

   현재 문장:

   > 이 버그가 보고된 AC2 성능을  
   > 성능을 해친 방향일 거라고 예상함.

   `성능을`이 두 번 나옴. 아래처럼 한 번만 남겨야 함.

   > 이 버그가 보고된 AC2 성능을  
   > 해친 방향일 거라고 예상함.

   사실 의미는 F19·F25와 맞지만, 현재 상태로는 사람이 읽을 때 즉시 걸리는 편집 오류임.

2. **파트 10의 새 예산 설명에 원장 태그 없음**

   현재 문장:

   > 10k는 prefix까지 포함한  
   > 50k 응답 상한의 1/5인 새 토큰 상한임.

   이는 p.27 Table 4의 “total response budget includes replayed prefixes, with b counting new tokens”에 근거한 사실 주장임. 마지막 줄에 `<!-- F4 -->`를 붙이고, ledger F4 위치도 `p.2, p.27 Table 4, p.29`로 넓혀 prefix 포함·최대 10k new tokens 조건을 명시해야 함.

### 남은 권고 사항

- 3줄 요약 2행 “18.50%를 넘는 decoding FLOPs는 2.5배 적었음”은 비교 대상이 생략됨. standalone 요약으로 읽히게 “GRPO보다”를 넣는 편이 정확함.
- 3줄 요약 3행은 42자로 checker의 40자 권장선을 넘음. “반복 학습·완성 rollout은 남았고 GPU 비용·심사는 미확인임.”처럼 줄이면 됨.
- ledger F9, F12–F15의 숫자 요지에도 `%` 단위를 붙이면 원장만 떼어 읽어도 0–7 judge 원점수와 혼동되지 않음.

### 재검사 결과

`check_report.py --strict`: **ERROR 0, WARN 1**. 남은 WARN은 3줄 요약 3행의 42자 길이임.

위 두 공개 차단 항목을 고친 뒤에는 사실·그림·흐름 기준으로 PASS 가능함.

---

## 최종 재검토 — PASS

**최종 판정: PASS. 새 공개 차단 오류 없음.**

마지막 수정분을 원문과 다시 대조함.

- 파트 19의 `성능을` 중복이 제거됐고, 저자 예상이라는 유보는 그대로 유지됨.
- 파트 10의 50k response budget·최대 10k new-token 설명에 F4 태그가 붙음.
- ledger F4가 p.2, p.27 Table 4, p.29를 가리키며 prefix 포함 총예산과 새 토큰 상한을 정확히 보존함.
- 3줄 요약 2행에 비교 대상 GRPO가 명시됨.
- ledger F9, F12–F16의 IMO-ProofBench 수치에 `%` 단위가 명시됨.
- 제목 범위, main group size 16, local-readiness ablation의 공통 no-group/no-audit 조건과 step-20 branch, decoding-only 2.5× 범위, 2k prefix-cut confound, 심사 미확인 표현이 모두 유지됨.
- algorithm·abstract conditions·code link 크롭의 설명과 실제 이미지가 일치함.
- 3줄 요약은 실제 세 줄이며 본문보다 강하게 단정하지 않음.

최종 `check_report.py --strict` 결과: **ERROR 0, WARN 0**.

따라서 현재 `report.md`와 `ledger.md`는 paper-report의 정확성·그림 대조·원장 추적·흐름 검토 기준에서 공개 가능한 상태로 판정함.
