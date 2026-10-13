# 팩트 원장: Fewer Tokens, Better Action

기준일: 2026-10-13
원문 버전: arXiv 2610.01939v1 (2026-10-01)
검토 범위: 본문·부록 19쪽 전체, 공식 프로젝트 페이지, 공개 코드 저장소, 전작·직접 인용 후속 논문 원문

## F: 이번 논문 원문

- F1 | p.1 저자란 | Ruiyang Si 외 11명. 소속은 Peking University, National University of Singapore, NVIDIA, Impossible Research. 교신저자 Daquan Zhou | 저자·기관
- F2 | arXiv 메타데이터 | 최초 공개 2026-10-01 16:07:49 UTC, v1, cs.CV·cs.RO, 19쪽 | 날짜·버전
- F3 | arXiv·논문 첫 페이지 | 제목 `Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens` | 제목
- F4 | arXiv 메타데이터 | journal_ref와 학회 채택 표기 없음. OpenReview·NeurIPS·PMLR 검색에서도 동일 제목 채택 기록을 확인하지 못함 | 2026-10-13 기준 프리프린트로 취급
- F5 | p.2 Sec.1 | 도구 호출 방식은 앞 도구 결과에 의존하는 다음 동작마다 보통 VLM을 다시 불러야 하고, RPent에서는 움직임 뒤 여러 카메라 이미지가 자동 반환됨 | 문제 설정
- F6 | p.2 Sec.1 | PyRUA-Lean은 로봇 프리미티브와 VLA를 Python 셀에 묶고, 중간 결과를 지속 상태에 남기며, `print`·명시 요청 이미지만 VLM으로 돌려줌 | 핵심 아이디어
- F7 | p.2 Sec.1 | RPent의 로봇 스택과 프리미티브 구현을 그대로 쓰고, 같은 GPT-6 Astra·동결 VLA·과제 인스턴스·LLM 호출 예산으로 RPent 도구 호출과 비교 | 공정 비교 설계
- F8 | p.3 Sec.3 | 예외가 나도 그 전에 만든 변수는 네임스페이스에 남아 다음 셀에서 수정 가능 | 지속 상태
- F9 | p.3 Sec.3 | VLA는 다른 프리미티브처럼 호출 가능하고, 셀 안에서 조건부 재시도·후속 동작을 구성할 수 있음 | 로컬 제어
- F10 | p.4 Fig.2 | 그릇 배치 예시에서 도구 호출 14~17의 네 VLM 턴을 코드 셀 하나가 대체. 성공 셀은 출력 5줄, 이미지 0장 반환 | 구체 장면
- F11 | Appendix A p.11 Fig.6/Table4 | 같은 에피소드 전체에서 도구 방식 20회·1.04M 입력 토큰(성공 시점 call17, 816k, 이미지 33장), 코드 방식 8회·220k(성공 시점 call6, 156k, 요청 이미지 5장) | 대표 에피소드
- F12 | p.4 Sec.4.1 | LIBERO-PRO 40과제×5=200, RoboTwin2.0 50×5=250, RoboCasa365 Target50 50×5=250. 총 140과제, 700 페어 인스턴스, 두 에이전트 합계 1,400회 에피소드 | 규모
- F13 | p.4 Sec.4.1 | 각 에이전트는 task-seed당 한 번만 실행. LLM 호출 한도 40, RoboCasa composite만 100, 에피소드 시간 한도 2시간 | 실험 조건
- F14 | p.4 Sec.4.1 | 두 에이전트 모두 Codex CLI, high reasoning effort, 에피소드 간 기억 없음 | 설정
- F15 | p.4 Sec.4.1 | VLA: LIBERO π0.5, RoboTwin LingBot-VLA, RoboCasa RLDX-1. 세그멘테이션은 SAM3 | 하부 모델
- F16 | p.5 Table2 | 전체 성공률: LIBERO 83.0→94.0(+11.0%p), RoboTwin 60.0→69.2(+9.2%p), RoboCasa atomic 78.9→86.7(+7.8%p), composite 34.4→39.4(+5.0%p) | 성공률
- F17 | p.5 Table2 | 전체 700 인스턴스 성공률 63.1→71.7, +8.6%p. 상대 개선은 8.6/63.1≈13.6%라 제목은 약 14% | 절대·상대 구분
- F18 | p.5 Table2 | 둘 다 성공한 인스턴스에서 에피소드당 LLM 호출 17.0→8.7(49% 감소), 입력 토큰 788k→276k(65% 감소, 2.9배), 비용 $1.63→$0.74(2.2배) | 헤드라인 효율
- F19 | p.5 Table2 캡션 | 성공률은 모든 인스턴스, 호출·토큰·비용은 둘 다 성공한 인스턴스만의 평균. 통합 토큰 배수는 긴 LIBERO 에피소드 영향이 큼 | 모집단 경고
- F20 | p.5 Table2 | LIBERO 1.23M→273k(4.5배), RoboTwin 415k→245k(1.7배), atomic 261k→171k(1.5배), composite 1.22M→603k(2.0배) | 과제별 차이
- F21 | p.5 Sec.4.2 | 코드만 성공 96개, 도구만 성공 36개. 코드만 성공 96개 중 baseline 호출 한도 소진 52, 조기 종료 44 | 추가 성공 분해
- F22 | p.5 Sec.4.2 | 조기 종료 44개 중 약 1/4은 코드 쪽 VLA가 한 번에 되고 baseline 실행에선 안 된 경우여서 복구 로직만으로 차이를 모두 설명할 수 없음 | 확률성 교란
- F23 | p.6 Fig.4 | 기록된 궤적을 토큰 누적량으로 잘라보면 baseline 최종 성공률까지 드는 토큰은 LIBERO 3.18M→564k(5.6배), RoboTwin 2.46M→618k(4.0배), atomic 1.32M→619k(2.1배), composite 5.71M→1.98M(2.9배) | 사후 토큰 곡선
- F24 | p.6 Fig.4 캡션 | 이 곡선은 토큰 예산을 미리 정해 재실행한 게 아니라 기록된 궤적을 사후 절단한 분석 | 한계
- F25 | p.6 Sec.4.3/Fig.5 | LIBERO의 4.48배 토큰 감소는 호출 수 2.55배와 호출당 토큰 1.76배의 곱. atomic은 코드 호출당 프롬프트가 더 큼(0.83배)이지만 호출 수가 줄어 총량 감소 | 원인 분해
- F26 | p.7 Sec.4.3·Appendix Table8 | 이미지 자동 반환만 끈 baseline은 LIBERO 성공률 83.0→68.5로 하락. 자동 이미지 baseline·요청식 baseline·code 세 구성이 모두 성공한 131개에서는 요청식 baseline 총 토큰도 원 baseline과 비슷 | ‘덜 보기만’으로 재현 안 됨
- F27 | Appendix E p.15 Table6 | 700에피소드·11,145셀. 코드 셀당 행동 프리미티브 2.1개(도구 호출 방식은 LLM 호출 1회당 0.65개), 45%가 2개 이상, 19%가 앞 결과에 행동 의존, 14% 루프, 8% VLA 재시도, 30% NumPy 계산 | 실제 사용 습관
- F28 | Appendix E p.15 Table6 | 코드 셀 84%가 이미지를 요청, 20%는 미완료일 때만 요청. 따라서 절약을 ‘거의 안 봄’으로 설명하면 틀림 | 선택적 관찰 뉘앙스
- F29 | Appendix F p.18 Fig.8 | 모카포트가 떨어진 뒤 baseline은 VLA를 반복 호출하고 call32 종료. 코드 에이전트는 뚜껑 점군에 평면을 맞춰 기울기를 구해 세우고 call33 성공 | 복구 장면
- F30 | Appendix F p.18 Fig.8 | 첫 평면 맞춤은 NumPy가 half precision 선형대수를 거부해 TypeError. 다음 셀에서 형변환 후 재실행 | 실패를 유지·수정한 사례
- F31 | Appendix F p.19 Fig.9 | 캐비닛 문에서 baseline은 call40까지 짧게 당겼지만 덜 열림. 코드는 손잡이 세 위치로 원을 맞춰 힌지 궤적을 따라 당겨 call34 성공 | 기하 계산 사례
- F32 | p.8 Table3 | VLA·운영 가이드를 빼도 여러 설정에서 코드가 성공률·토큰 면에서 우세. 예: RoboTwin 무 VLA+가이드의 전체 성공률 42.8→68.8(+26.0%p), 두 방식 공동 성공 인스턴스의 에피소드당 토큰 1.03M→316k(3.2배) | 절제 실험
- F33 | p.8 Table3/Sec.4.4 | 무 VLA RoboTwin에서 가이드 제거가 baseline 성공률을 42.8→60.4로 올림. 가이드는 항상 유익하지 않음 | 예상 밖 결과
- F34 | p.8 Sec.5 | GPT-6 Astra 한 모델, RPent 스택, 시뮬레이션에 한정. 다른 planner·프리미티브·실물 로봇·반복 실행 변동성 미검증 | 핵심 한계
- F35 | p.8 Sec.5 | 비교는 primitive composition·persistent state·selective feedback이 묶인 완성 인터페이스 비교라 각 요소의 독립 효과를 분리하지 못함 | 인과 한계
- F36 | p.8 Sec.5 | 실제 지연시간은 공용 모델 게이트웨이 변동 때문에 측정하지 않고 호출 수를 사용 | 시간 한계
- F37 | p.4 각주·Appendix D | 2026-09 가격표: 입력 $10/M, cached input $1/M, cache write $12.5/M, 출력 $50/M. 캐시 때문에 토큰 2.9배 감소가 비용 2.2배로 작아짐 | 가격 기준
- F38 | Appendix D p.14 | 전체 시도까지 포함한 토큰 비율은 LIBERO 3.1배, RoboTwin 1.8배, composite 1.6배. atomic 추정 비용은 약 1.1배 차이 | 헤드라인 외 회계
- F39 | Appendix D p.14 | 첫 프롬프트는 코드가 더 큼: LIBERO 20k vs 22k, RoboTwin 15k vs 21k, RoboCasa 17k vs 24k | 초기 오버헤드
- F40 | p.6 RoboDojo pilot | 세 과제 파일럿에서 코드 8/30=26.7%, 도구 1/29=3.4%(인프라 실패 1회 제외). 둘 다 버튼 누르기 실패. 작은 파일럿이라 일반화 금지 | 보조 실험

## L: 전작→이번 논문→후속 계보

- L1 | Code as Policies, arXiv:2209.07753v4 p.1, ICRA 2023 | LLM이 로봇 정책 코드를 만들고 피드백 루프·NumPy 같은 라이브러리를 조합. 이번 논문이 로봇 코드 기반 선행으로 직접 인용 | 전작: 코드로 정책 표현
- L2 | CodeAct, arXiv:2402.01030v4 p.1, ICML 2024 | JSON·텍스트 대신 실행 가능한 Python을 통합 행동 공간으로 삼고 새 관찰 뒤 코드를 고쳐 씀. 이번 논문이 일반 에이전트 인터페이스 선행으로 직접 인용 | 전작: 대화형 코드 행동
- L3 | Harness VLA, arXiv:2607.08448v5 p.1 | frozen VLA와 고전 프리미티브를 RPent에서 조합. 이번 논문은 그 RPent 로봇 스택·구현을 기반으로 함 | 직접 기반
- L4 | 이번 논문 p.2~3 | 이전 일들은 코드 생성·피드백·스킬 재사용을 보였고, 이번 논문은 같은 프리미티브에서 도구 호출과 대화형 코드 실행의 성공률·추론비를 비교 | 차별점
- L5 | RobotWorld, arXiv:2610.10409v1 p.2·5, 2026-10-07 | 이번 논문을 “프로그램 조합과 선택적 관찰의 실행 효율” 연구로 직접 인용하고, 84과제·다양한 로봇 체형으로 성공과 피드백 실패를 평가 | 확인 가능한 후속 인용 1
- L6 | Embodied Turing Machines, arXiv:2610.12369v1 p.4, 2026-10-08 | PyRUA-Lean을 “에피소드 중 셀 단위로 코드를 쓰는” 방식으로 분류하고, 모델 호출을 테스트 때 없애는 COAP과 대비 | 확인 가능한 후속 인용 2
- L7 | arXiv 페이지 2026-10-13 | Cited by 2로 표시. 원문 직접 인용은 L5·L6에서 각각 확인했으나, arXiv 표시 두 건의 정확한 구성과 동일하다고 단정하지 않음 | 인용 수는 변동 정보

## P: 저자·기관 맥락

- P1 | 논문 p.1·공식 프로젝트 | 12명 저자, PKU 7명, NUS 겸임 1명, NVIDIA 2명, Impossible Research 2명으로 표기 | 논문 시점 소속
- P2 | PKU 공식 교원 페이지, 2026-10-13 조회 | Daquan Zhou는 Peking University School of Information Engineering의 Assistant Professor·박사 지도교수 | 교신저자 맥락
- P3 | DAGroup GitHub 소개, 2026-10-13 조회 | DAGroup은 Peking University 연구실로 소개되며 PyRUA-Lean 공식 코드를 공개 | 연구실 맥락

## W: 외부 확인

- W1 | https://arxiv.org/abs/2610.01939, 2026-10-13 조회 | v1 제출 기록, 저자·날짜·분야·arXiv DOI 확인 | 서지
- W2 | https://dagroup-pku.github.io/PyRUA-Lean/, 2026-10-13 조회 | 같은 planner·primitive를 두고 인터페이스만 비교, 핵심 수치·데모 확인 | 공식 프로젝트
- W3 | https://github.com/DAGroup-PKU/PyRUA-Lean, 2026-10-13 조회 | 공개 코드 저장소와 Apache-2.0 라이선스 확인 | 코드
- W4 | OpenReview·NeurIPS·PMLR 제목 검색, 2026-10-13 | 확인 가능한 채택 기록 없음 | 심사 여부 판단 보강

## 표현 금지·주의

- 성공률은 “14%p”가 아니라 8.6%p, 상대 약 14%임.
- 토큰 65% 감소는 모든 시도가 아니라 “둘 다 성공한 인스턴스”에서의 에피소드 평균임.
- 인터페이스 전체 비교라 “코드 실행 하나 때문에”라고 인과 단정하면 안 됨.
- VLA 확률성 때문에 코드만 성공한 일부는 복구 설계가 아니라 샘플 운 차이일 수 있음.
- 시뮬레이션·단일 모델·task-seed당 1회라 실물·다른 모델로 일반화 금지.
