# 독립 팩트체크

검수일: 2026-10-13
검수 대상: report.md
대조 자료: paper.pdf 19쪽 전체, text.txt, meta.json, Table 2·3·6·8, Figure 2·5·8·9, 전작·후속 공개 원문

## 수정한 항목

1. 요청식 이미지 baseline의 131개는 두 방식 공동 성공이 아니라 자동 이미지 baseline·요청식 baseline·code 세 구성이 모두 성공한 인스턴스임. 본문과 ledger F26 수정.
2. `0.65 acting primitives`의 분모는 tool call 한 번이 아니라 도구 호출 방식의 LLM 호출 한 번임. 본문과 ledger F27 수정.
3. 무 VLA RoboTwin의 42.8→68.8%는 전체 인스턴스 성공률이고, 1.03M→316k는 두 에이전트 공동 성공 인스턴스의 평균임. 본문과 ledger F32에 모집단 명시.
4. 입력 토큰 감소를 여러 동작 묶기의 단독 인과로 쓰지 않고, 기록 분해가 직접 보인 `호출 수 감소가 더 큰 몫`으로 수정.
5. arXiv `Cited by 2` 표시가 RobotWorld·Embodied Turing Machines 두 편과 정확히 일치한다고 단정하지 않도록 ledger L7 수정. 두 논문의 직접 인용 자체는 각각 원문에서 확인.
6. 논문 표시 제목을 전체 제목으로 복원.

## 최종 판정

- 성공률·토큰·비용·호출 번호·실험 규모·날짜·저자·소속: 원문과 일치.
- 성공률 전체 모집단과 효율 공동 성공 모집단: 구분됨.
- 프리프린트·채택 미확인 표현: 적절함.
- 직접 후속 인용: RobotWorld와 Embodied Turing Machines 원문에서 확인함.
- 차단 오류 없음. PASS.
