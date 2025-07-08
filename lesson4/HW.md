##7.台灣有多少人在2020確診

```sql
SELECT MAX(總確診數) AS 台灣2020年總確診數
FROM world
WHERE 國家 ='台灣' AND 日期 BETWEEN '2020-01-01' AND '2020-12-31' ;
```
| 台灣2020年總確診數 | 備註 |
| --- | --- |
| 799 |答案 |

##1.查詢亞洲總共有多少人死亡
```sql
SELECT MAX(總死亡數) AS 亞洲總死亡數
FROM world
WHERE 洲名 ='亞洲';
```
| 亞洲總死亡數 | 備註 |
| --- | --- |
| 52,305 |答案 |

##2.查詢全世界2020年的總確診數
```sql
SELECT MAX(總確診數) AS 全世界2020年總確診數數
FROM world
WHERE 日期 BETWEEN '2020-01-01' AND '2020-12-31';
```
| 全世界2020年總確診數 | 備註 |
| --- | --- |
| 83,750,045 |答案 |

##3.查國家名有"阿"字,總死亡數大於10000

```sql
SELECT 國家, MAX(總死亡數) AS 各國總死亡數
FROM world
WHERE 國家 LIKE '阿%'
GROUP BY 國家
HAVING MAX(總死亡數) > 10000;
```

| 國家 | 備註 |
| --- | --- |
| 阿根廷 | 阿字頭的國家死亡人數超過1萬,死亡人數=129,109 |

##4.查詢哪個國家總確診數最多

```sql
SELECT 國家, MAX(總確診數) AS 各國總確診數
FROM world
WHERE 國家 <> '全球'
GROUP BY 國家
ORDER BY 各國總確診數 DESC
LIMIT 1;
```
| 總確診數最多的國家 | 總確診數 |
| --- | --- |
| 美國 | 88,263,393 |

##5.查詢亞洲台灣 2020-06-25 的總確診數

```sql
SELECT 國家, 日期, 總確診數
FROM world
WHERE 國家 = '台灣' AND 日期='2020-06-25';
```

| 國家 |日期 | 總確診數 |
| --- | --- | --- |
| 台灣 | 2020-06-25 | 447 |

##6.總死亡數最高的國家
```sql
SELECT 國家, MAX(總死亡數) AS 各國總死亡數
FROM world
WHERE 國家 <> '全球'
GROUP BY 國家
ORDER BY 各國總死亡數 DESC
LIMIT 1;
```
| 總確診數最多的國家 | 各國總死亡數 |
| --- | --- |
| 美國 | 1,019,083 |

##8.排序各國確診數

```sql
SELECT 國家, MAX(總確診數) AS 各國總確診數
FROM world
GROUP BY 國家
ORDER BY 各國總確診數 DESC;
```
| 國家 | 各國總確診數 |
| 全球 |  552,498,044 |
| 美國 |  88263393 |
| 印度 |  43566739 |
| 巴西 |  32687680 |

##9.查詢每百萬確診人數

```sql
SELECT 國家,MAX(每百萬人確診數) AS 每百萬人確診數,
ROUND(CASE 
      WHEN MAX(總人口數) = 0 OR MAX(總人口數) IS NULL THEN NULL
      ELSE MAX(總確診數) *1000000.0 / MAX(總人口數) END  ,3) AS 每百萬確診人數_算
FROM world
GROUP BY 國家
ORDER BY 每百萬人確診數 DESC;
```

| 國家 |每百萬人確診數 | 每百萬確診人數_算 |
| --- | --- | --- |
| 法羅群島 | 706541.9 | 706541.904 |

##10.台灣哪個月死亡人數最多人

```sql
ALTER TABLE world
ALTER COLUMN 日期 TYPE DATE
USING 日期::DATE;

SELECT 
  TO_CHAR(DATE_TRUNC('month', 日期), 'YYYY-MM') AS 月份,
  SUM(新增死亡數) AS 每月死亡人數
FROM world
WHERE 國家 = '台灣'
GROUP BY DATE_TRUNC('month', 日期)
ORDER BY 每月死亡人數 DESC
LIMIT 1;
```
| 月份 |每月死亡人數 | 
| --- | --- |
| 2022-06 | 4,396 | 

##11.在哪個年度及月分，死亡數達到高峰

```sql
SELECT 
  TO_CHAR(DATE_TRUNC('month', 日期), 'YYYY-MM') AS 月份,
  SUM(新增死亡數) AS 每月死亡人數
FROM world
GROUP BY DATE_TRUNC('month', 日期)
ORDER BY 每月死亡人數 DESC
LIMIT 1;
```
| 月份 |每月死亡人數 | 
| --- | --- |
| 2021-01 | 835,930 | 

