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
WHERE 國家 LIKE '阿%' AND 各國總死亡數 > 10000
GROUP BY 國家
ORDER BY 各國總死亡數 DESC;
```
