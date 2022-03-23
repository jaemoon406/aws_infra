# Web Server Infra

## 구현 목적
웹서버 백엔드 인프라을 구축하고, 전체적인 흐름을 확인하는 목적

## 진행 사항
1. AWS(RDS, EC2)배포 환경 구축(22.03.22)
2. uwsgi 배포(22.03.23)
3. NginX 배포- 예정(22.03.24)

## 활용 stack  
- AWS 
 * RDS (MySQL)
 * EC2 (ubuntu)
- uwsgi (Web Server Gateway Interface)
<pre>
<code>
개발환경 uwsgi 실행
uwsgi -i local-uwsgi.ini

운영환경 uwsgi 실행
uwsgi -i employ-uwsgi.ini
</code>
</pre>
- NginX



