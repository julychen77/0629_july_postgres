##更改日期型別，將字串類型更換成為DATE

```sql
ALTER TABLE world
ALTER COLUMN 日期 TYPE DATE
USING 日期::DATE;

```