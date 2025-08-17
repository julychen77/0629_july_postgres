select count(*) as 總筆數
from "每日各站進出站人數"

 SELECT "日期", "車站代碼", "進站人數", "出站人數"
 FROM public."每日各站進出站人數"
 WHERE "日期" = '2023-01-01' AND "車站代碼" = 900;

SELECT s."stationCode",
 		s."stationName" AS station_name,
 		n."日期",
 		n."進站人數",
 		n."出站人數"
FROM public."台鐵車站資訊" s
JOIN public."每日各站進出站人數" n
  ON s."stationCode" = n."車站代碼"
WHERE s."stationName" = '基隆'
  AND n."日期" = '2023-01-01';

SELECT MIN("日期") AS min_date, MAX("日期") AS max_date
        FROM public."每日各站進出站人數";