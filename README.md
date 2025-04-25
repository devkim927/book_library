## 프로젝트 개요
- 도서 정보 등록, 조회, 수정, 삭제가 가능한 도서 관리 웹 애플리케이션입니다
- Django 기반으로 구현되었으며, 사용자 인증 기능과 관심 장르 선택 기능을 포함합니다
- 프로젝트 필수 내용에 따라 회원가입, 로그인, 회원정보 수정 등을 통해 사용자 중심의 기능을 구성했습니다.

## 프로젝트를 통해 배운 점
- 도서 관리 웹 애플리케이션을 Django로 구현하고, 로그인 및 회원정보 수정을 추가하면서 DB에 대한 사용 능력을 키울 수 있었습니다

- Django의 사용자 인증 시스템(Authentication)에 대해 복습하고, 실제 구현을 통해 개념을 보충할 수 있었습니다

- ChoiceField를 이용한 관심 장르 선택 구현을 통해 새로운 input 방식을 접했고, Django 폼에 대해 더 친숙해질 수 있었습니다

## 주요 기능
- 회원가입, 로그인 / 로그아웃, 회원정보 수정

- 도서 CRUD (생성, 조회, 수정, 삭제)

- 관심장르 선택 기능

---

## 추가 구현 기능

### ✅ Thread(독서기록) 기능
- 사용자별로 도서에 대한 독서 기록을 남길 수 있도록 Thread 모델 구현
- Thread 객체는 Book, User와 외래키(ForeignKey)로 연결됨
- 로그인한 사용자가 작성한 게시글만 수정/삭제 가능하도록 권한 분기 처리

### ✅ 좋아요 기능
- Thread 모델에 `likes = ManyToManyField(User)` 필드 추가
- 로그인한 유저가 다른 유저의 독서 기록에 대해 좋아요/취소 가능
- 템플릿에서 `user in thread.likes.all` 조건문을 활용하여 상태에 따라 버튼이 다르게 표시됨

### ✅ 작성자 프로필 페이지
- Thread에 연결된 작성자(nickname)를 클릭하면 `/accounts/profile/<user_id>/`로 이동
- 각 유저의 nickname, 이메일, 팔로워 수 등을 확인할 수 있음
- `get_user_model()`을 통해 유연하게 사용자 모델 가져옴

### ✅ 팔로우 기능
- 사용자 간 팔로우 관계를 표현하기 위해 `following = ManyToManyField('self', symmetrical=False)` 필드를 추가
- 비대칭 관계 설정으로 '내가 팔로우한 사람'과 '나를 팔로우한 사람'을 구분 가능
- 팔로우/언팔로우는 POST 요청으로 처리되며 템플릿에서 실시간 반영됨

---

## 프로젝트를 통해 추가로 배운 점
- ManyToManyField를 활용한 유저 간 관계 표현 (팔로우/좋아요)
- Django 템플릿 언어를 통한 동적 조건 표현 및 UX 반영
- 권한 체크 로직 (`request.user == thread.user`)을 통한 보안 및 기능 분기
- SQLite 마이그레이션 오류(`NOT NULL constraint failed`) 해결을 통해 DB 마이그레이션 구조 심화 이해
- 커스텀 User 모델 구성 및 필드 확장 방식 (nickname, interest, following 등)

---

## 간단 코드 리뷰 (요약)

### accounts/models.py
- AbstractUser를 상속받아 nickname, following 필드를 확장하여 소셜 기능 구현
- following 필드에서 `symmetrical=False` 설정을 통해 일방향 팔로우 관계를 구현함

### accounts/views.py
- 작성자 프로필 페이지(`/accounts/profile/<pk>/`)와 팔로우 토글 뷰 구현
- `request.user.following`을 기준으로 팔로우 여부 판별 및 상태 변경 처리

### books/views.py
- 게시글 생성 시 작성자를 `thread.user = request.user`로 지정
- 삭제 및 수정 시 `request.user == thread.user`로 권한 체크 처리
