# sparta_mars
flask app


<br>

## 화성에 땅 사기 미니 app by sparta

- python, flask, mongodb

<br>

**요구**

- 사용자는 땅을 구매할 수 있다.
- 구매 요청된 땅 정보 목록을 조회할 수 있다.


<br>

**api**

- `[GET] /api/mars` : 모든 땅 목록 조회
- `[POST] /api/mars` : 땅 등록



### 과제

- 가격 정보(평당 가격 * 평수)를 같이 보여주는 기능을 추가하고 배포


**endpoint**

- [2022/11/15까지](http://140.238.17.208/)


<br>


### CD

- github actions, docker, ec2

**과정요약**

(1) `master branch` 에 push하면 workflow 실행됨

(2) `Dockerfile` 써서 내 `dockerhub`로 이미지 만들어 넣음

(3) `docker build` 성공했으면 내 인스턴스 ssh 접속해서 `docker-compose.yaml` 넣음

(4) 인스턴스의 `docker-compose` 로 `dockerhub` 이미지 받고 실행시킴 
