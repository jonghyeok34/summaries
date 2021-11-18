# 디디의 redis
- remote dictionarh server
  - hash map: key -value
  - 쿠팡
    - 32bit CPU int 최대값 - 21억
    - key 값이 너무 많아져서

## what is redis
- remote dictionary server
- database cache, message broker
- `in memory` data structure

- cache
- 나중의 요청에 대한 결과를 미리 지정했다가 빠르게 사용하기 위함.

- memory hierarchy
  - CPU - 12MB cache memory(SRAM)
  - Main memory - 16GB DRM -적당히 빠르고 비쌈
  - Storage : SSD, HHD
    - 비교적 느리고 비교적 저렴

- HDD, SSD
  - main memory에 접근
  - Database보다 더빠른 메모리에 더 자주 접근하자 

## 자료구조 collection
- memcache와 차이점 : 자료구조(collection 제공)
- String
- List = 자바의 LinkedList
- Set = HashSet of Java
- Sorted Set - Treeset of Java (score라는 숫자값으로 순서)
- Hash

## 그냥 메모리가 아닌 레디스를 쓰는 이유
- 서버가 여러대인 경우 consistency 문제 발생 (세션)
- multi-threaded 환경에서 - race condition 발생
- race condition: 여러 thread가 경합하여 context switching함에 따라 문제 발생

## redis의 특징
  - 기본적으로 single thread
  - atomic crtitical section에 대한 동기화
  - 서로 다른 transaction - read/write를 동기화

## 주의 해야할 점
- single thread 서버이므로, 시간 복잡도를 고려해야 한다.
- in-memory 특성상 
  - 메모리 파편화, 가상 메모리등의 이해가 필요
1. single threaded
  - event driven(비동기)
  - IO-bound Process를 제외하면 비동기를 많이 사용하지 않으므로 
  - single thread이므로 처리를 빠르게 하도록 함
  - 전체를 탐색하는 key, flush, getall 등을 사용에 주의

## memory 관리
- 메모리 파편화
- 가상메모리 swap
- replication - fork

1. 메모리 파편화
  - 메모리 할당 받고 해제하는 과정에서 부분부분 비어있는 게 발생
  - 사용하지 못하는 부분 발생
  - 메모리 적당히 여유있게 사용해야함
2. 가상메모리 swap
  - 프로세스를 올릴때 일부만 올림.
  - 덜쓰는 것 디스크에 저장했다가 필요할 때 올림. - latency가 길어지게 되면 문제 발생 가능성 있음
3. replication
  - 휘발성 가지고 있음 - 데이터 복사하여 replication - fork 할 때  메모리를 여유있게 하지 않으면 문제 발생

# 그외
- redis 는 주기적으로 백업: redis clustering
- 부하 분산 - constant hashing
- 메모리만 사용 Data grid - Spring gemfire


출처 : [https://www.youtube.com/watch?v=Gimv7hroM8A]