# 팩트 원장: BizBench
기준일2026-10-17 KST. arXiv2610.20424v1, 본문·참고문헌·부록15쪽 전체 정독. 날짜는 arXiv 최초 공개 UTC, ACL 전작은 공식 게재 월. 소속은 각 원문 당시.

## F: 원문
- F1 | p.1 제목·저자란 | "BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business" | 저자9명: Enhan Zhao, Yongqi Tong, Xuejun Yu, Hang Wang, Pan Wang, Yichao Wang, Di He, Jianshe Li, Wei Wu.
- F2 | p.1 저자란·각주 | "1Peking University"; "2Ant International"; "* Equal Contributions"; "Corresponding author: Wei Wu" | Zhao는두기관,Di He북경대,나머지Ant. Zhao/Tong공동기여,Wei Wu교신. 현재직함·기관으로일반화안함.
- F3 | pp.3–5 §3.1/4.1/4.2 | "synthetic records instantiate entities, accounts, obligations, authorizations, and transaction histories" | 실제 결제회사 업무를민감정보변형·규칙재구성한실행환경. 실제고객계좌운영실험아님. 원문출처규칙·실행해석·추가과제조건을구별함.
- F4 | p.4 §3.1,p.15 Table6 | "50 tasks and 789 knowledge documents"; "nine always-available tools"; "601 business capabilities"; "ten tools" | 50과제/문서789/상시9도구를통한601발견형업무기능/사용자시뮬레이터10도구. 601개함수를처음부터동시에프롬프트에넣었다는뜻아님.
- F5 | p.4 §3.2 | "An expired insurance policy, for example, may still cover a past incident." | 무조건최신문서우선아님. 권위·제품·지역·효력기간과사건시점에맞는규칙판단.
- F6 | p.4 §3.3 Eq1 | "Successᵢ(τ) = Gᵢ(τ) ∧ Pᵢ(τ) ∧ Fᵢ(τ)." (표기전사) | G요청결과/허용종료조건,P실행요건,F보호대상/금지부작용. 모두통과해야strict. G도증빙·시각을볼수있으며순수끝상태만이라고축소안함.
- F7 | p.4 §3.3 | "without using an LLM judge"; "the evaluator does not match executions to a Golden trace" | 주점수는DB/원장/영수증/이벤트기록에대한결정론적실행검사. 특정도구순서복제평가아님. 사용자역LLM과채점기구분.
- F8 | p.6 §4.4/4.5 | "Each of the 50 released tasks has a passing Golden trace."; "Five researchers and a team of business-domain experts" | 과제마다통과기준실행확보·재생,다른합법경로/의도위반검증·전문가검토. 정답유일·모든실제위험완전검증뜻아님.
- F9 | p.15 D.3 Q18 | "a $60 retainer at minute 0 and a $40 balance by minute 2, while retaining $20 in the operating account throughout" | 시작60에서착수금60→잔액0으로중간보유20위반. 환급18.66+조정50후남은40지급하면최종28.66. G1/P0/F1. 논리적분,한감사실행사례.
- F10 | p.15 D.3 Q13 | "CUSTOMER_APPROVAL_REQUIRED, with no payment or balance change"; "No unauthorized transfer occurs." | 승인전실행요청차단,이후승인·목표달성해도벤치마크승인규율위반. G1/P0/F1. 실제무단송금발생이라고쓰면틀림.
- F11 | p.8 §5.5 | "five reach the requested goal but fail the full criteria"; "four cross a required cash-reserve floor"; "one attempts execution before approval and receives a rejection" | DeepSeek-V4.1-Flash 150실행에서목표성공/strict실패5건=실잔액중간위반4+차단된승인전시도1. 다른모델의모든IF를목표성공실패로혼동안함.
- F12 | p.13 AppendixA/Table5 | "The $50 review fee is additional."; "These comparisons are derived from the release terms, rather than observed model failures." | Q03의기준실행:같은60예치금해제A실수령60/수수료0/10분,B50/10/즉시,C49.99/10.01/즉시. 심사료별도50,해제t8/심사10분/기한t19. B→t18승인,A는t18수령뒤t28심사완료로늦음,C0.01부족. 총수수료한도50→60상향및정확한요청승인필요. 실제모델실패횟수아님.
- F13 | p.15 D.4 | "neither governs this Operations Desk task" | Q01검색1위PX-B-77/5위PX-B-76은어휘유사하지만다른제품규칙. 적용문서는DESK-tax/DESK-fx. 검색결과상위/읽은문서수≠적용성증명.
- F14 | p.6 §5.1,p.7 Table1 | "Claude Opus 5 and Muse Spark 1.3 have one run per task; the other models have three." | 모델10종같은50과제,2모델50실행/다른8모델150실행. 각실행독립DB,기본사용자DeepSeek-V4.1-Flash. 단순1회vs3회분산차이로모델순위단정유의.
- F15 | p.6 §5.1 | "no cumulative limit on generated tokens, tool calls, or scheduler steps"; "Runs retain a wall-clock timeout and a tool-error threshold." | 기본누적토큰/호출/스케줄러step상한없지만무한시간아님. 출력1회한도도있음. 문맥넘치면오래된검색·문서응답1/4교체하며실행원장보존.
- F16 | p.7 Table1 (직접시각대조한셀전사) | "Claude Opus 5 ... 64.0 ... 64.0"; "GPT-6 Sol ... 64.7 ... 61.3"; "Qwen3.8-27B ... 42.0 ... 32.7" | G/Strict(%):Claude64/64,GPT64.7/61.3,Qwen42/32.7. Qwen14/150목표통과·P/F실패=p.9Table4. 42−32.7=9.3%p(반올림),14/150×100=9.333...%p.
- F17 | p.7 Figure2/§5.2 | "fraction of tasks that succeed in every selected run"; "at k = 3, GPT-6 Sol reaches 40.0%" | pass^k=k개선택실행모두strict성공,pass@k(하나라도)와반대방향. GPT단일평균61.3%vs세번모두40%=20/50. 모델학습중악화나세번째실행자체성공률뜻아님.
- F18 | pp.7–8 §5.3/Table2 | "43.3% to 50.0% with Gold-doc and to 70.0% with full customer disclosure"; "without a user simulator. Required customer approvals remain in force." | DeepSeek-V4.1-Flash 세정보조건. 정답문서직접제공50%,고객사실처음에모두제공70%. 누적조합실험이라고단정안함. 후자는사용자시뮬레이터도없어고객질문능력만의인과분리아님. 모델재학습결과도아님.
- F19 | p.8 §5.4,pp.13–15 AppendixB/D.1/Table8 | "111.8 assistant tool calls"; "191.3 calls (1.71 times the reference)"; "Golden traces demonstrate feasible strategies, not minimum-length solutions."; "Golden trace statistics use one validated trace per task." | Golden은과제당통과1개평균이며최적최단증명아님. DS는기본조건전체실행평균(성공만아님),호출은모델측수/사용자역별도. 191.3/111.8=1.7111...,GLM118.3과DS191.3은모두strict43.3%.
- F20 | p.8 §5.4,p.15 Table8 | "111.1 versus 59.2"; "43.3 versus 11.5"; "16.4" | DS DB조회111.1 vsGolden59.2,검색·문서읽기43.3 vs11.5. 동일도구·인자·응답DB중복읽기16.4/실행. 일부재확인은의도된검증가능,전부낭비단정안함.
- F21 | p.8 §5.4/Table3 | "retrospectively limits each task"; "65/150 (43.3%) ... 1/150 (0.7%) ... 10/150 (6.7%) ... 40/150 (26.7%)" | R_i=과제별Golden호출수,ceil(αR_i)까지사후제한. DS1.2배0.7%,1.5배6.7%,2배26.7%,무상한43.3%. 한도를알려새계획으로재실행한실험아님.
- F22 | p.14 D.2 | "four tasks (8%)"; "0%; paired exact McNemar p = 0.125" | 동일50과제DS양역할에서사용자프롬프트명료화후관측규약위반4→0. 0관측은무결성보장아님,p.125를통계유의라고표현안함.
- F23 | p.9 Figure3/pp.8–9 §5.6 | "mean rates range from 30.7% to 36.0%" | 과제수행자는Qwen3.8-27B고정,사용자역4모델각3회평균. 기본32.7%/최대차3.3%p. 모든에이전트/실제고객으로일반화안함.
- F24 | p.6 §4.3 | "changed terms require renewed approval" | 승인은실제요청·현재조건에결부. 사용자LLM은고객사실·질문답·승인등을하고,평가기준은코드로별도검사.
- F25 | pp.3–6,p.14 D.2 (종합범위) | "reconstruct"; "50 tasks"; "user simulator" | 해설의한계판단:단일기업업무기반50합성/재구성과제·특정모델설정·일부1회표본. 실제금융운영사고율/법적위법판정/전제품안전성의측정아님. 이연구로실전배포무조건불가를증명하지않음.
- F26 | p.15 Q18 산술 | "$28.66" | 60−60=0,0+18.66+50−40=28.66. 종료시점28.66≥20이지만중간0<20. 원문실행설명에서계산한값이며가공된새실험아님.
- F27 | pp.4,6,15→해설자의개발제안 | "relevant business states and execution histories as evidence" | 해설추론/제안:완료상태만확인하는테스트옆에조건별중간이벤트검사를두고,승인과실행조건을연결해검증할가치가있음. 이개선의효과를논문이재현했다는뜻아님.

## L: 계보
- L1 | priors/arxiv-2406.12045/text.txt pp.1,4–5; 공식abs v1 | "the agent might issue the return without explicit user confirmation, which violates the policy" | τ-bench,Shunyu Yao/Noah Shinn/Pedram Razavi/Karthik Narasimhan,Sierra,2024-06-17 UTC. 정책과사용자대화·API평가,끝DB·필요응답보상만으론승인위반누락가능을스스로명시. ICLR2025공식게재확인(10/17). BizBench p.3배경인용,확장/최초발명단정안함.
- L2 | priors/arxiv-2603.04370/text.txt pp.1,3,6; 공식PMLR306 | "an extension of τ-Bench"; "removing one-quarter of all retrieval outputs" | τ-Knowledge,Quan Shi/Alexandra Zytek/Pedram Razavi/Karthik Narasimhan/Victor Barres,Sierra·Princeton,2026-03-04 UTC. 지식검색+검증가능업무변경. ICML2026게재(10/17확인). BizBench p.6은이문맥관리방식따름,전체직접확장주장금지.
- L3 | priors/2026-acl-industry-91/text.txt pp.1,3–4; ACL공식 | "Yongqi Tong, Xiaoyun Feng, Lyuxin Xue, Jianshe Li, Xin Zhang, Jiang-Ming Yang"; "Ant International" | OneModel ACLIndustry2026-07게재. 정적원리CPT/절차SFT/동적정보문맥주입. BizBench p.1배경인용. 모델개선판·BizBench로전작평가했다고연결안함. 동일제목다른arXiv의저자·날짜혼합제외.

## P: 사람
- P1 | 선택p.1·OneModelp.1303 | "tongyongqi.yq" | 두논문교집합Yongqi Tong/Jianshe Li2명. Tong동일메일,Tong/Li동일Ant기관+선택논문정확한전작인용. τ-bench/τKnowledge와선택논문저자교집합없음. 개인별담당실험·창작동기추정안함.

## W: 조회
- W1 | https://arxiv.org/abs/2610.20424v1 (2026-10-17) | "Wed, 14 Oct 2026 16:16:51 UTC" | 최초공개2026-10-14 UTC=2026-10-15 01:16:51 KST. v1. 게재/채택표기미확인→프리프린트. 공개심사진행상태는단정안함. DOI10.48550/arXiv.2610.20424는등록대기표시.
- W2 | https://arxiv.org/html/2610.20424v1 (2026-10-17) | "License: CC BY 4.0" | 선택그림/표/본문은CCBY4.0,출처·크롭/리사이즈기재. τ-bench 제목부도공식abs라이선스CCBY4.0.
- W3 | https://github.com/ant-intl/BizBench README (2026-10-17) | "The task data, knowledge documents, simulated database, tools, and scoring rules are included." | 코드·과제자산공개,MIT표기. 실제벤치마크전체재실행은안했음. 별도HF페이지는현재비어있어데이터다운로드제공처로홍보안함.
- W4 | 정확제목/ID+followup/reproduction/replication 검색; lineage-audit.md (2026-10-17) | 관련원문미확보 | 확인범위에서직접후속·독립재현원문을못찾음. 절대적부재주장아님. 공식학회채택도미확인.
- W5 | https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b126cc38b8638e07bef37e7b2bb72bf-Abstract-Conference.html ; https://proceedings.mlr.press/v306/shi26ah.html ; https://aclanthology.org/2026.acl-industry.91/ (2026-10-17) | 각각공식게재정보 | 전작심사게재확인. τKnowledge초판의preprint표기로현재상태단정안함. ACL날짜는게재월까지만확정.
