# Story Daily

재미있는 논문을 원문 그림과 함께 읽는 한국어 블로그입니다.

- 목록: https://bear2u.github.io/Story-daily-viewer/
- 첫 글: https://bear2u.github.io/Story-daily-viewer/posts/generative-agents.html
- 모바일 읽기 화면, 검색과 주제 필터, 그림 확대, 목차, 읽기 진행 표시, 이미지 보기, RSS를 제공합니다.

## GitHub Pages

저장소의 **Settings → Pages → Build and deployment → Source**에서 **GitHub Actions**를 선택합니다.

`.github/workflows/deploy-pages.yml`은 main 푸시와 수동 실행을 지원합니다. Python으로 글 목록과 본문을 빌드하고, 내부 링크와 RSS를 검사한 뒤 정적 파일만 GitHub Pages에 배포합니다. 설정을 바꾼 뒤 첫 실행이 이미 끝났다면 **Actions → Deploy Story Daily to GitHub Pages → Run workflow**를 누르면 됩니다.

별도의 서버나 Node 빌드는 필요하지 않습니다.

## 글 추가

1. `content/<slug>.md`에 해설을 추가합니다. 파트는 `---`로 구분합니다. 그림 앞뒤에는 빈 줄을 둡니다.
2. `content/<slug>.json`에 제목, 날짜, 요약, 태그, 논문 출처와 목차를 넣습니다. 첫 글의 JSON이 예제입니다.
3. 그림은 `assets/posts/<slug>/`에 넣고 Markdown에서 저장소 루트 기준 상대 경로로 참조합니다.
4. 빌드하고 변경 사항을 푸시합니다.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8000
```

`index.html`, `posts/*.html`, `posts.json`, `feed.xml`, `sitemap.xml`은 빌드 결과입니다. 새 글이 추가될수록 날짜순으로 목록에 쌓입니다. 별도의 계정, 분석 스크립트, 서버 데이터베이스를 사용하지 않습니다.

## 콘텐츠 출처

첫 글은 *Generative Agents: Interactive Simulacra of Human Behavior*, Park 외, UIST 2023, arXiv:2304.03442v2를 해설합니다. 관련 선행 및 후속 연구는 본문의 출처에 연결했습니다. 논문 그림과 연구 결과의 권리는 각 원 저자에게 있으며, 이 저장소는 원 논문에 새로운 재사용 라이선스를 부여하지 않습니다. 출처와 연구 조건을 유지해 주세요.
