기본구조 공부

# Django

## 0. settings

- `.gitignore`
- 가상환경 설정
    - $ python -m venv venv
    - $ source venv/Scripts/activate
- `README.md`

## 1. Django 프로젝트

1. Django 설치
```shell
pip install django
```

2. 프로젝트 생성
```shell
$ django-admin startproject <프로젝트 이름> <경로>
```

3. 서버 실행
```shell
python manage.py runserver
```

4. 앱 생성
```shell
django-admin startapp <app이름>
```

5. 앱 등록(`settings.py`에서)
```python
INSTALLED_APPS = [
    ...,
    '<app_이름>',
]
```
## template & views
- urls.py -> views.py -> @@@.html 무한반복

