# 팩트 원장: Copy-Paste Language Models
기준일: 2026-10-18 KST. 원문: arXiv 2610.19247v1, PDF 32쪽 전체 정독.
날짜: arXiv 최초 제출 UTC / KST를 구별함. 소속은 논문 작성 당시.
선정: 저장소 기존 18편 제목·arXiv ID 대조, 중복 없음.

## F: 원문 본문
- F1 | p.1 제목·저자 | "COPY-PASTE LANGUAGE MODELS"; "Nathan Godey and Yoav Artzi" | 제목·저자 그대로. 두 저자 모두 Cornell University, New York City, USA.
- F2 | p.1 §1 | "∼60% of the tokens in FineWeb-Edu ... already appear earlier in their 4k-token context" | FineWeb-Edu 4k 문맥 기준 약60%가 앞에 나온 토큰. 모든 언어/모든 문서 일반화 금지.
- F3 | p.2 §2.1 Eq1, p.18 Table4 | "Vocabulary size 49,152"; "Hidden size 576 ... 2,048" | LM head는 상태에서 어휘별 점수를 선형 투사한 뒤 softmax. 135M은 D576,V49152; 1.7B는 D2048,V49152. 어휘차원보다 작은 상태차원으로 표현 및 역전파 경로가 제한됨. 사고력99%손실 같은 해석 금지.
- F4 | p.3 Eq2–3 | "targets are the context positions"; "marginalizing over the positions that emit the same token" | CP는 과거 위치에 확률을 주고 같은 토큰 위치의 확률을 합함. 과거 토큰의 정체성을 복사하며 긴 문자열 통째 복사 아님.
- F5 | p.3 Eq4–7 | "<copy> is never an actual target and only serves as a gate"; "λt = ct (1 − st)" | 실제 예측은 두 분포 가중 혼합. copy확률 c, sink확률 s; 유효복사비중λ=c(1-s). c=.8,s=.25→λ=.6→LM .4+CP .6은 해설용 가상수치, 관측값 아님.
- F6 | p.3 §2.2 | "there is no auxiliary loss and no copy supervision" | 혼합분포의 표준 next-token cross-entropy만으로 end-to-end 학습, 별도복사정답표/보조loss없음.
- F7 | p.4 §3.1; p.18 Table4 | "135M to 1.7B"; "20 B ... 200 B" | 135M,360M 각20B토큰,1.7B200B토큰. 135M=1억3500만,360M=3억6000만,1.7B=17억,200B=2000억. FineWeb-Edu,SmolLM2recipe,양쪽하이퍼파라미터동일. 기본main 1.7B학습문맥4096,SW창256. Full/Hybrid3:1/SW비교.
- F8 | p.4 §3.1; Fig2 p.4 | "reaching the final loss of vanilla models 1.25× faster ... and 2× faster in ... SW" | 같은대조군최종loss도달까지token/step축상최대2배. 고정step처리량2배·실측총시간2배라고쓰지않음. Fig2는LRdecay이전곡선.
- F9 | p.4 Table1 | "Avg. ... Full ... 62.45 ... 63.06"; "SW ... 61.63 ... 62.48"; "Hybrid ... 62.22 ... 62.59" | zero-shot7벤치평균상승은각 .61,.85,.37%p. 종합평균향상≠개별전항목향상.
- F10 | p.6 Table2; p.24 AppD | "Avg ... Full 24.2 26.4 ... Hybrid 24.3 25.5 ... SW 18.9 24.0" | Tulu3로최대16k SFT뒤5벤치평균. 각각+2.2,+1.2,+5.1%p. MATH는861개level1–2/4과목,math pass@4/8samples,temp.7 top-p.9,code pass@10/20samples,temp.8 top-p.95. IFEval은strict/loose,prompt/instruction 평균. 서로다른지표혼합평균이라실서비스성공률로읽지않음. Hybrid MBPP19.0→17.4하락.
- F11 | p.7 §3.3; p.25 Fig13/AppE | "SW (14.3 → 99.4)" | 1.7B base,4k학습,길이1k~64k 7조건×깊이8×셀당200예제,7자리숫자하나,중립문장15개반복,greedy최대16토큰,출력에숫자포함시정답. 전체격자평균14.3%→99.4% =+85.1%p. 64k한조건수치아님. Full49.7→54.8,Hybrid58.2→83.6. Full/Hybrid YaRN×4,SWplainRoPE. k표현은원문사용.
- F12 | p.26 AppE/F; p.28 Table12 | "Both Full models fail completely from 16k on"; SW CPLM BABILong "16k 0.6 ... 64k 0.6" | 단일숫자복사는장문추론일반성능아님. BABILongqa1–5의16k,64k SW CPLM평균각0.6%,Full두모델32k/64k RULER/BABILong0%. YaRN×4한계포함.
- F13 | p.8 §4.1; p.9 Fig6 | "LM heads lose over 99% of the gradient norm"; "conserve up to 85% ... at early positions" | 135M,2048 FineWebEdu에서출력로짓gradient의nullspace성분측정. 학습정보전체99%소실·성능99%손실아님. CP의비교행렬은문맥길이t×D,LM은V×D. t≪V조건에서역투사압축이덜함.
- F14 | p.8 SpamLang,Fig6p.9 | "34% accuracy at 512k" | 한기호반복합성학습,135M,D576,V8k~512k. vanilla V512k에서34%,CPLM모든어휘조건해결. 자연언어복잡추론평가아님.
- F15 | p.30 Table15; p.31 H1 | "Vanilla ... 16.34"; "CPLM ... 15.85"; "stop-gradient ... 16.22" | 135M Full20B토큰단일seed. CP→backbone query/keygradient만차단,head가중치는계속학습,LM경유copygategradient도남음. NLL개선.031→.008nats,비율 .008/.031=.258약1/4. 단일개입전체기전증명아님,해석지지.
- F16 | p.31 H2 Table16;p.32Fig18 | "V = 257"; "D = 576"; "0.6908 ... 0.6918" | byte실험은D576,V257,실제약107M파라미터,20Bbytes약5B토큰상당텍스트,문맥2048bytes;단일seed. vanilla0.6908,CPLM0.6918nats/byte로이득없음. 일반토큰20B와동일텍스트량아님. copygate가활성(.339)이어도개선없음.
- F17 | p.8 §4.2;p.9Fig7 | "Heads scoring above 0.3 count as induction heads"; "4 ... against 13–15" | 1.7B randomsequence반복probe,T128에서임계.3기준CPLM4,대조군13–15. 본체attention부품이줄었다는검출결과,전체attention수감소아님. a→b패턴재현예시는설명용.
- F18 | p.7 §3.4;p.8Fig5 | "200 validation questions"; "n ∼U[5, 50]"; "34–38% EM with 500 distractors" | HotpotQA gold2문단+훈련방해5~50,1epoch lr1e-4 batch32;평가200질문방해5~500. docs dropped는문서를별도encoding후CPkey만접근,질문답변backbone문서KV접근차단. 전혀안읽은문서가아님. 500방해문단34–38%EM,fullKV대비cache약50분의1,가중치포함총메모리아님. 5방해조건정확도90–97%유지와500방해조건범위혼용금지.
- F19 | p.18 AppB;p.19 Table5 | "1.7B ... 55,862 ... 54,113 ... ×0.969"; "125.4 ...137.5" | B3001장,bf16,4k학습문맥,1.7Bbatch8/update포함. 처리량약3.1%감소(1−.969);피크125.4→137.5GB증가12.1GB. 8192위치chunk시+3.4GB(본문) 가능. 9B/30B는미학습구조속도메모리만,품질검증은1.7B까지.
- F20 | p.19 Table6 | "Request ... ×1.008 ... ×1.017" | 1.7B fullcontext,B300,bf16,4k/16k프롬프트+256greedytokens,요청전체지연0.8–1.7%증가. batch및context지정범위이외일반화금지.
- F21 | p.23 Table8 AppC6 | "margins ... small, within about one to two seed standard deviations" | 135M20Bseed42,기존pointer방식적응대조,CPLMFull15.85,shared15.88,sigmoid15.94,vanilla16.34;SW16.02/shared16.09;FinePDFSW13.82동률. 본질신규성은복사발명아님,현대LM사전학습이득과병목기전연결. gate/sink만압승주장금지.
- F22 | p.10Conclusion;p.11Ethics | "experiments stop at 1.7B parameters"; "may also reproduce sensitive or copyrighted content ... more faithfully" | 대형학습·span복사·외부corpus확장추후과제. 안전정렬안된소형연구모델,입력민감/저작권내용재출력위험이있을수있음. 원문가능성수준유지.
- F23 | p.20 Table7 C1 | "seeds 42/43/44" | 135M20B3seed,Full16.33±.03→15.83±.02,모든규모/모든과제3seed아님. H개입단일seed한계와분리.
- F24 | p.10Acknowledgements | "members of the Cornell LIL Lab"; "NG is supported by an Empire AI Postdoctoral Fellowship" | 해당논문감사문근거,NG의논문당시지원사실,현재직함추측없음.
- F25 | p.2 Intro; p.10RelatedWork | "not the adaptation of the copy mechanism itself" | 본논문자신도복사기제적용그자체를신규기여로내세우지않음. 사전학습과gradientpath주장에초점.

## W: 공식 웹과 확인 상태
- W1 | https://arxiv.org/abs/2610.19247v1 (2026-10-18) | "Tue, 13 Oct 2026 22:03:18 UTC" | 최초공개2026-10-13UTC,2026-10-14KST(UTC+9). v1. arXiv공식페이지에학회채택/저널기재없고PDFPre-print표기. 10/18기준심사채택미확인.
- W2 | https://arxiv.org/html/2610.19247v1 ; https://creativecommons.org/licenses/by-sa/4.0/ (2026-10-18) | "License: CC BY-SA 4.0" | 그림과원문CCBYSA4.0. 크롭/크기변경표시,원저자/제목/arxiv/라이선스명시,이번해설기여도동일라이선스. 전작그림은별도권리표시.
- W3 | https://arxiv.org/abs/2610.19247v1 (2026-10-18) | "arXiv-issued DOI ... (pending registration)" | DOI10.48550/arXiv.2610.19247등록대기표시,안정원문링크arxivversion사용.
- W4 | https://yoavartzi.com/pubs ; arXiv정확제목검색 (2026-10-18) | 검색범위기록 | 공개검색에서이논문직접후속/독립재현및학회채택자료확인못함. 부재증명·무인용주장하지않음. S2/OA인용량은조회생략하여싣지않음.

## 해설용 예시
- F26 | F4–F6원리에기댄가상예시 | "order_id" | 같은변수명재사용은독자용가상장면,실측예제/벤치수치아님. 중복order_id위치확률합,문맥에없던토큰은LM경로에서만가능. CP한번에다음토큰한개,여러토큰변수명은차례대로복사함.
- F27 | F10,AppD설명 | pass@k | 샘플k개중하나라도정답인정도를추정하는지표. 단일시도성공률아님. 서로다른pass@k섞인Table2의평균설명필수.
- F28 | p.30Table15, Eq1 p2 표값교차 | "NLL ...2.794 ...PPL ...16.34" | PPL=exp평균NLL. exp(2.794)=16.346로표반올림과일치. 로짓은softmax이전후보점수. 학습량200억=20B환산(20×10억).
- F29 | F8파생 | "1.25× ... 2×" | 동일loss도달학습량은기존대비1/1.25=.8=80%,1/2=.5약절반. 처리량/총시간비율로치환안함.

## L/P: 전작 원문과 저자 맥락
- L1 | sources/prior_pointer_sentinel.pdf pp.1–3 §2.2–2.4,Fig2; https://arxiv.org/abs/1609.07843 (2026-10-18) | "Pointer Sentinel Mixture Models"; "either reproduce a word from the recent context or produce a word from a standard softmax classifier" | Stephen Merity,Caiming Xiong,James Bradbury,Richard Socher,2016-09-26UTC firstarxiv,ICLR2017(본논문참고문헌p14/공식OpenReviewacceptance검색대조). 당시MetaMind/A Salesforce Company. RNN/LSTM문맥pointer와어휘softmax혼합,sentinel로비중조절. CPLM은copygate를LM쪽에서먼저예측,sink는fallback이라는차이.
- L2 | sources/prior_trime.pdf p3/인쇄5659 §2.2–3, p6/5662 §5.3; https://aclanthology.org/2022.emnlp-main.382/ (2026-10-18) | "using local memory during both training and testing can still improve model performance" | Zexuan Zhong,Tao Lei,Danqi Chen,Training Language Models with Memory Augmentation,EMNLP2022. Transformer에서도학습시메모리사용이점선행. 현재CPLM저자들은local-memory변형을가장가까운선행으로분류(p10),기존문맥매칭vs현재토큰pointer/learnedQK/gate차이. 다른데이터/크기라숫자직접우열안함.
- L3 | sources/prior_gradient_bottleneck.pdf p1–4; https://arxiv.org/abs/2603.10145v2 (2026-10-18) | "Published as a conference paper at COLM 2026"; "Nathan Godey, Yoav Artzi" | 동일두저자,Cornell,Lost in Backpropagation: The LM Head is a Gradient Bottleneck. 첫공개2026-03-10UTC,v2 07-10UTC. COLM2026확인. 출력층의역전파병목분석→이번CP설계는동일저자문제의식연속. 전작의심사채택을이번논문으로전이하지않음.
- P1 | F1/F24와L3대조 | "Cornell University" | 소속은현재추측없이두논문당시표기. LILLab감사/EmpireAI지원은연구기여맥락만,검증인증으로이용안함.
