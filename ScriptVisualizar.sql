CREATE DATABASE monse;
show databases;
use monse;
show tables;
Select * from nyc_arrests;
Select * from tbl_principal;
Select ARREST_KEY, ARREST_DATE, PD_CD, PD_DESC, KY_CD, OFNS_DESC, LAW_CODE, LAW_CAT_CD, ARREST_BORO, ARREST_PRECINCT, JURISDICTION_CODE, AGE_GROUP, PERP_SEX, PERP_RACE, X_COORD_CD, Y_COORD_CD, Latitude from nyc_arrests;
Select ARREST_KEY, ARREST_DATE, PD_CD,LAW_CAT_CD, ARREST_BORO, ARREST_PRECINCT, JURISDICTION_CODE, PERP_SEX, X_COORD_CD, Y_COORD_CD, Latitude, Longitude, Lon_Lat from nyc_arrests;

-- Genera y ejecuta consultas para eliminar cada tabla
SELECT CONCAT('DROP TABLE IF EXISTS ', table_name, ';') 
FROM information_schema.tables where table_schema = 'monse';

Select COUNT(OFNS_DESC) FROM nyc_arrests;
Select * from tbl_pd_desc;
select * from tbl_law_code;
select * from tbl_age_group;
select * from tbl_perp_race;
select * from tbl_ofns_desc;

 
-- Genera y ejecuta consultas para eliminar cada tabla
SELECT CONCAT('DROP TABLE IF EXISTS ', table_name, ';') 
FROM information_schema.tables where table_schema = 'monse';

-- Eliminar llaves foraneas
ALTER TABLE tbl_principal DROP FOREIGN KEY fk_pd_desc;
ALTER TABLE tbl_principal DROP FOREIGN KEY fk_age_group;
ALTER TABLE tbl_principal DROP FOREIGN KEY fk_law_code;
ALTER TABLE tbl_principal DROP FOREIGN KEY fk_perp_race;
ALTER TABLE tbl_principal DROP FOREIGN KEY fk_ofns_desc;

-- Eliminamos las tablas
DROP TABLE IF EXISTS tbl_age_group;
DROP TABLE IF EXISTS tbl_law_code;
DROP TABLE IF EXISTS tbl_ofns_desc;
DROP TABLE IF EXISTS tbl_pd_desc;
DROP TABLE IF EXISTS tbl_perp_race;
DROP TABLE IF EXISTS tbl_principal;
-- DROP TABLE IF EXISTS nyc_arrests;