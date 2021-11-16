# JVM의 garbage collector

# 용어
## 1. JVM (Java Virtual Machine)
- 운영체제의 메모리 영역에 접근하여 메모리를 관리하는 프로그램

## 2. garbage collector
- 동적 할당된 메모리 영역 중 사용하지 않는 영역을 탐지해 해제하는 기능
## 3. stack, heap
- stack: 정적 할당 메모리 영역
- heap: 동적 할당 메모리 영역
  - 모든 object타입의 데이터가 할당, heap 영역의 object를 가리키는 참조 변수

# garbage collector 과정
- 1. stack의 모든 변수를 스캔하면서 각각 어떤 객체를 참조하기 있는지 찾아서 마킹
- 2. reachable object가 참조하고 있는 객체도 찾아서 마킹
- 3. 마킹되지 않은 객체를 heap에서 제거한다.
- 1,2: mark/ 3: sweep

```
stack --> heap( list-->[String, String])
```

# heap에서 gc가 사용하는 공간
  - new generation
    - `eden`(에덴 동산) : `minor GC`-  새로운 객체가  할당 - 모두 할당 되었을 때 GC 발생--> 모두 찼을 때 mark, sweep
    - `survival 0`, `survival 1` : GC발생시 eden에서 reachable한 객체가 옮겨지고, 나머지(unreachable)는 `mark` & `sweep`
      - 둘중에 하나만 차게 된다.
      - survival 0이 다차면 1로, 옮기고, 1이 다차면 0으로 옮기며 age값이 증가한다.
      - 특정 age가 넘어가면 old generation으로 데이터가 넘어감 `promotion` 
  - `old generation`
    - `major gc`: old generation이 모두 사용되면 gc가 작동됨

# Garbage collector 종류
## serial GC
  - GC 처리하는 스레드가 1개
  - CPU 코어가 1개만 있을 때 사용하는 방식
  - mark, sweep에 compact 과정이 추가됨
## parllel GC
- java 8 기본 GC
  - GC 처리하는 스레드가 여러개이다.
  - 메모리가 충분하고 코어개수가 많을 때 사용
## Concurrent Mark sweep GC(CMS GC)
- deprecated
- Stop-the-world
  - GC를 실행하기 위해 JVM이 애플레이션 실행을 멈추는 것이다
    - stop-the-world가 발생하면 GC 실행하는 스레드를 제외한 나머지 스레드를 모두 멈춘다.
- concurrent mark과정에서
  - intial mark에서 계속해서 마킹
  - remark : 마킹을 한번 다시
  - concurrent sweep - 다른 어플리케이션 sweep과 동시에 sweep
- 장점: stop-the-world 시간이 짧아 애플리케이션 응답 시간이 빨라야 할때 CMS GC를 사용한다. 
-  다른 방식의 GC보다 메모리와 CPU 더 많이 사용.
- compaction 이 없다.
## G1 GC
- java 9부터 기본 GC
- 각 영역을 Region 영역으로 나눈다.

- GC가 일어날 때, 전체 영역(Eden,survival, old generation)을 탐색하지 않는다.
- stop-the-world 시간이 짧다. compaction을 사용한다.


출처: https://www.youtube.com/watch?v=vZRmCbl871I&t=36s