import itertools
import pymysql

# MySQL 연결 정보 설정
db_config = {
    "host": "qqrx224.cgidx97t8k8h.ap-northeast-2.rds.amazonaws.com",
    "user": "BAEKI",
    "password": "qoqorlxo1!",
    "database": "Ezpill"
}


# MySQL 연결
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

query = f"""
    SELECT user_id, price
    FROM {table}
    ORDER BY price DESC
    LIMIT {top_n}
"""
cursor.execute(query)

# 각 테이블에서 상위 3개의 제품을 가져오는 쿼리 예시
tables = ['product_', 'table2', 'table3', 'table4', 'table5']
top_n = 3
result = {}

for table in tables:
    query = f"""
        SELECT product_name, price
        FROM {table}
        ORDER BY price DESC
        LIMIT {top_n}
    """
    cursor.execute(query)
    result[table] = cursor.fetchall()

# 예산 설정
budget = 1000

# 각 테이블에서 하나씩 선택하여 조합 생성
all_combinations = list(itertools.product(*result.values()))

# 최대 가격의 조합 찾기
max_price_combination = None
max_price = 0

for combination in all_combinations:
    total_price = sum(product[1] for product in combination)
    if total_price <= budget and total_price > max_price:
        max_price_combination = combination
        max_price = total_price

# 최대 가격의 조합 출력
print("최대 가격의 조합:", max_price_combination)
print("최대 가격:", max_price)

# 연결 닫기
cursor.close()
connection.close()
