# [우아콘2020] 수십억건에서 QUERYDSL 사용하기
- 출처: https://www.youtube.com/watch?v=zMAX7g6rO_Y
# 테스트 환경

- java : open jdk 1.8
- querydsl-jpa : 4.2.1
- mysql :5.6



# 1. 워밍업 : extends /implements 사용하지 않기

- QuerydslRepositorySupport extends 하지 않고 하기

- `JpaQueryFactory`만 있어도 생성자 주입만 받으면 extends, implements 제거가 가능하다.



```java

@RequiredArgsConstructor
@Repository
public class AcademyQueryRepository {

    private final JPAQUeryFactory queryFactory;

    public List<Academy> findByName(String name){

        return queryFactory.selectFrom(academy)
                           .where(academy.name.eq(name))
                           .fetch();
    }
}

```


- 동적 쿼리 : `BooleanExpression`을 사용하기 - null반환 시 자동으로 조건절에서 제거 된다.

```java

private BooleanExpression eqName(String name){

    if(StringUtils.isEmpty(name)){

        return null;
    }

    return academy.name.eq(name);
}

```



# 2. 성능 개선 - Select

## QueryDsl에서 exist 사용하지 않기
-v exist가 count() > 0으로 실행된다. sql의 exist는 성능이 훨씬 좋다. JPQL은 from 없이 쿼리를 생성할 수 없으므로 직접 구현이 필요하다.

```java

@Transactional(readOnly = true)

public Boolean exist(Long bookId){

    Integer fetchOne = queryFactory.selectOne()
                                   .from(book)
                                   .where(book.id.eq(bookId))
                                   .fetchFirst();

    // 조회 결과가 없으면 null이므로 null 체크
    return fetchOne != null;
}
```



## Cross join 회피한다 
- (묵시적 join을 사용할땐 cross join 발생함)
- 명시적 join을 이용한다. : inner join

```java

public List<Customer> notCrossJoin(){

   return queryFactory.selectFrom(customer)
                      .innerJoin(custome.shop, shop)
                      .where(customer.customerNo.gt(shop.shopNo))
                      .fetch();
}

```

## Entity보다는 Dto를 우선한다.

- Entity 조회시 hibernate 캐시 - 불필요한 컬럼 조회 - OneToOne N+1 쿼리 

- 단순 조회 기능에서는 성능 이슈 요소가 많다. 

### 비교
- entity 조회

  - 실시간으로 entity 변경이 필요한 경우

- dto 조회 

   - 고강도 성능 개선 or 대량의 데이터 조회가 필요한 경우


## 조회 컬럼 최소화 하기

   - 이미 알고 있는 값은 as 표현식으로 대체할 수 있음 : as 표현식은 실제로 select에서 선택하지 않음

```java
public List<BookPagDto> getBooks (int bookNo, int pageNo){

  return queryFactory.select(Projectons.fields(BookPageDto.class,
                                book.name,
                                Expressions.asNumber(bookNo).as("bookNo"),
                                book.id
                            ))
                            .from(book)
                            .where(book.bookNo.eq(bookNo))
                            .offset(pageNo)
                            .limit(10)
                            .fetch();

}

```



## select 컬럼에 entity 자제 - N+1

- Entity의 연관관계를 맺을 때 - 연관된 Entity의 save를 위해서는 반대편 Entity의 id만 있으면 된다. (join column에 들어갈 id만 필요)


## group by 최적화 (mysql )

 - mysql에서 group by 실행 시 file sort 자동
 - order by null을 사용하면 file sort 사용하지 않아, 성능 개선

```java

public class OrderByNull extends OrderSpecifier {

  public static final OrderbyNull DEFAULT = new OrderByNull();

  private OrderByNull(){
    super(Order.ASC, NullExpression.DEFAULT, Default);  
  }
}

```

```java

.orderBy(OrderByNull.DEFAULT)

```
- 페이징이 아닐 때만 추천

## 커버링 인덱스

  - 쿼리를 충족시키는데 필요한 모든 컬럼을 갖고 있는 인덱스

  - JPQL에서는 from 절에 커버링인덱스 사용 x

  - 우회 사용하기 : 커버링 인덱스 나눠서 진행

```java

List<Long> ids = queryFactory
                .select(book.id)
                .from(book)
                .where(book.name.like(name+"%"))
                .orderBy(book.id.desc())
                .limit(pageSize)
                .offset(pageNo *pageSize)
                .fetch();
if (CollectionUtils.isEmpty(ids)){
    return new ArrayList<>();
}

return queryFactory
        .select(Projections.fields(BookPaginationDto.class,
                book.id.as("bookId"),
                book.name,
                book.bookNo,
                book.bookType
        ))
        .from(book)
        .where(book.id.in(ids))
        .orderBy(book.id.desc())
        .fetch();

```
--> 성능 차이 : 기존 페이징 - 26s --> 0.58 sec

# 3. 성능 개선 -  update/ insert

- DirtyChecking
```java
List<Student> students = queryFactory
            .selectFrom(student)
            .where(student.id.loe(studentId))
            .fetch();
for (Student student :students){
    student.updateName(name);
}
```
- Querydsl.update

```java
queryFactory.update(student)
            .where(student.id.loe(studentId))
            .set(student.name, name)
            .execute();
```
- 객체지향을 핑계로 성능을 버리고 무분별한 Dirtychecking을 하고 있는지 확인하자

- 일괄 update 최적화:  하이버 네이트 캐시는 일괄 업데이트 시 캐시 갱신이 안되어, cache eviction(캐시 내용 refresh)이 필요

- 정리
  - dirtyChecking : 실시간 비즈니스 처리, 실시간 단건 처리
  - Querydsl.update : 대량의 데이터를 일괄로 update 처리
  

##  JPA로  bulk insert는 자제한다
- JdbcTemplate을 사용하는 것이 좋다.
- TypeSafe한 개발이 필요한가?

- Querydsl도 Querydsl-SQL을 사용하여 Native SQL을 사용할 수 있다.
  - 그러나 베타 DB 설정이 따로 필요
- EntityQL
  - 단점: gradle 5 이상
    - 어느테이션 name="" ㅣㅍ수
    - primitive type 사용 x
    - querydsl-sql 개선 x
    - @Embedded 미지원
    - @JoinColumn을 지원


# 4. 마무리
- 1. 상황에 따라 ORM/ w-전통적 Query 방식을 골라 사용
- 2. JPA/ querydsl로 발생하는 쿼리 한번 더 확인하기
