

SELECT count(*) AS "台北車站數"
FROM "台鐵車站資訊"
WHERE "stationAddrTw" LIKE '%臺北%';

SELECT count("name" ) AS "台北車站數"
FROM "台鐵車站資訊"
WHERE "stationAddrTw" LIKE '%臺北%';

SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "stationName" = '基隆';

--全省各站點2022年的進站總人數
SELECT "name", count(*) AS 筆數 ,SUM(進站人數) AS "總進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY "name"
ORDER BY "總進站人數" DESC;

--使用日期萃取date_part()，全省各站點2022年的進站總人數
SELECT "name", date_part('year',"日期") AS 年份 ,SUM(進站人數) AS "總進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE date_part('year',"日期") ='2022'
GROUP BY "name","年份"
ORDER BY "總進站人數" DESC;

--全省各站點2022年進站總人數大於500萬的站點
SELECT "name", date_part('year',"日期") AS 年份 ,SUM(進站人數) AS "總進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE date_part('year',"日期") ='2022'
GROUP BY "name","年份"
HAVING SUM(進站人數) > 5000000
ORDER BY "總進站人數" DESC;

--基隆火車站2020,2021,2022每年進站人數
SELECT "name", date_part('year',"日期") AS 年份 ,SUM(進站人數) AS "總進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE "name" = '基隆' AND date_part('year',"日期") BETWEEN '2020' AND '2022'
GROUP BY "name","年份"
ORDER BY "總進站人數" DESC;

--mcp給的語法
SELECT
  EXTRACT(YEAR FROM d."日期") AS 年份,
  SUM(d."進站人數") AS 年進站總人數
FROM
  "台鐵車站資訊" s
JOIN
  "每日各站進出站人數" d
ON
  s."stationCode" = d."車站代碼"
WHERE
  s."stationName" = '基隆'
  AND d."日期" BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY
  年份
ORDER BY
  年份;


--基隆火車站,臺北車站2020,2021,2022每年進站人數
SELECT "name", date_part('year',"日期") AS 年份 ,SUM(進站人數) AS "總進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE "name" IN ('基隆','臺北') AND date_part('year',"日期") IN ('2020','2021','2022')
GROUP BY "name","年份"
ORDER BY "總進站人數" DESC;

--mcp給的語法(臺北、基隆3年的進站人數)
SELECT
  s."stationName" AS 車站名稱,
  EXTRACT(YEAR FROM d."日期") AS 年份,
  SUM(d."進站人數") AS 年進站總人數
FROM
  "台鐵車站資訊" s
JOIN
  "每日各站進出站人數" d
ON
  s."stationCode" = d."車站代碼"
WHERE
  s."stationName" IN ('基隆', '臺北')
  AND d."日期" BETWEEN '2020-01-01' AND '2022-12-31'
GROUP BY
  s."stationName", 年份
ORDER BY
  s."stationName", 年份;

--基隆火車站,臺北車站2020,2021,2022每年進站人數(臺北會出現2019年，where子句內需要一起執行的要用括號包住)
SELECT "name", date_part('year',"日期") AS 年份 ,SUM(進站人數) AS "總進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE date_part('year',"日期") IN ('2020','2021','2022') AND ("name" = '基隆' OR "name" = '臺北' )
GROUP BY "name","年份"
ORDER BY "總進站人數" DESC;

--查詢2022年平均每日進站人數超過2萬人的站點
SELECT "name", date_part('year',"日期") AS 年份 ,AVG(進站人數) AS "平均進站人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "每日各站進出站人數"."車站代碼" = "台鐵車站資訊"."stationCode"
WHERE date_part('year',"日期") = '2022'
GROUP BY "name","年份"
HAVING AVG(進站人數) > 20000
ORDER BY "name" DESC;
