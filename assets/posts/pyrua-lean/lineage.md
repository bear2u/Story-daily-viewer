# 계보: 로봇에게 한 동작씩 시킬 것인가, 프로그램을 맡길 것인가

기준일: 2026-10-13

| 시기 | 논문 | 원문에서 확인한 역할 | 이번 논문과 관계 |
|---|---|---|---|
| 2022 공개 / ICRA 2023 | [Code as Policies](https://arxiv.org/abs/2209.07753) | 언어모델이 피드백 루프와 로봇 API를 포함한 정책 코드를 생성. NumPy·Shapely 같은 라이브러리도 조합 | 로봇 정책을 코드로 표현하는 전작 |
| 2024 / ICML 2024 | [Executable Code Actions Elicit Better LLM Agents (CodeAct)](https://arxiv.org/abs/2402.01030) | JSON·텍스트 행동보다 실행 가능한 Python을 행동 공간으로 쓰고, 실행 결과를 보고 코드를 고치는 다중 턴 상호작용 제안 | 일반 에이전트에서 코드 인터페이스의 효용을 보인 전작 |
| 2026-07 공개 | [Harness VLA](https://arxiv.org/abs/2607.08448) | RPent에서 frozen VLA와 고전 로봇 프리미티브를 묶어 복구 가능한 조작기로 사용 | PyRUA-Lean이 직접 이어받은 로봇 스택·프리미티브 기반 |
| 2026-10-01 공개 | [Fewer Tokens, Better Action](https://arxiv.org/abs/2610.01939) | 같은 GPT-6 Astra·프리미티브·VLA·인스턴스에서 RPent 도구 호출과 지속 Python 셀 실행을 비교 | 이번 논문. 성공률과 추론비를 같은 조건에서 함께 측정 |
| 2026-10-07 공개 | [RobotWorld](https://arxiv.org/abs/2610.10409) | PyRUA-Lean을 “프로그램 조합과 선택적 관찰로 실행 효율을 높이는 연구”로 직접 인용. 84과제·다양한 로봇 체형으로 더 넓은 평가를 제안 | 확인 가능한 직접 후속 인용·확장 맥락 |
| 2026-10-08 공개 | [Embodied Turing Machines](https://arxiv.org/abs/2610.12369) | PyRUA-Lean을 매 에피소드 실행 중 모델이 셀 단위 코드를 쓰는 방식으로 분류하고, 테스트 때 모델 호출을 없앤 COAP과 대비 | 확인 가능한 직접 후속 인용·다른 설계 축 |

## 한 줄 관계

Code as Policies가 “로봇 정책을 코드로 쓸 수 있음”을 보였고, CodeAct가 “행동 인터페이스 자체를 Python으로 만들면 에이전트가 더 유연해짐”을 보였음. Harness VLA는 이번 논문이 쓰는 RPent·VLA 혼합 스택을 만들었고, PyRUA-Lean은 그 동일한 스택 위에서 도구 호출과 코드 셀을 정면 비교함. 바로 뒤의 RobotWorld와 Embodied Turing Machines는 각각 더 넓은 평가, 온라인 모델 호출 제거라는 다음 질문으로 이어감.

## 선 긋기

- RobotWorld와 Embodied Turing Machines는 공개일과 참고문헌에서 이번 논문을 직접 인용하는 것을 확인했으나, 둘 다 arXiv 프리프린트임.
- 공개 간격이 6~7일이라 연구가 이번 논문을 보고 새로 시작됐다고 말할 수는 없음. “후속 연구”보다는 “후속 공개·직접 인용”이라고 표현함.
- 저자 겹침은 확인되지 않음. 같은 연구팀의 연속작으로 묶지 않음.
