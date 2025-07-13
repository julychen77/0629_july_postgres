SELECT 
	日期,SUM(新增死亡數) AS 每日死亡人數	
FROM world
GROUP BY 日期
ORDER BY 每日死亡人數 DESC
LIMIT 1;

SELECT MAX(總確診數) AS 全世界2020年總確診數數
FROM world
WHERE 日期 BETWEEN '2020-01-01' AND '2020-12-31';

ALTER TABLE world
ALTER COLUMN 日期 TYPE DATE
USING 日期::DATE;

SELECT 
	洲名,SUM(新增死亡數) AS 死亡人數
FROM world
WHERE 洲名 <> '全球' AND 日期 BETWEEN '2021-01-01' AND '2021-12-31'
GROUP BY 洲名;

SELECT 
	洲名,SUM(新增死亡數) AS 死亡人數
FROM world
WHERE 洲名 = '歐洲' AND 日期 = '2020-06-15'
GROUP BY 洲名;

SELECT 
	日期,SUM(新增確診數) AS 單日確診數
FROM world
GROUP BY 日期
HAVING SUM(新增確診數) > 5;

SELECT 
  洲名,SUM(新增死亡數) AS 死亡數,MAX(總確診數) AS 總確診數,
  round(SUM(新增死亡數)*1.0 / MAX(總確診數),3) AS死亡佔確診數
  FROM world
  GROUP BY 洲名;
--
