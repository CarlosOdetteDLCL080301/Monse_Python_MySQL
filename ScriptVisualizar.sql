CREATE DATABASE monse;
show databases;
use monse;
show tables;
Select * from nyc_arrests;
Select COUNT(OFNS_DESC) FROM nyc_arrests;
Select * from tbl_pd_desc;
select * from tbl_law_code;
select * from tbl_age_group;
select * from tbl_perp_race;
select * from tbl_ofns_desc;

 
-- Genera y ejecuta consultas para eliminar cada tabla
SELECT CONCAT('DROP TABLE IF EXISTS ', table_name, ';') 
FROM information_schema.tables where table_schema = 'monse';

-- Eliminamos las tablas
DROP TABLE IF EXISTS tbl_pd_desc;
DROP TABLE IF EXISTS tbl_law_code;
DROP TABLE IF EXISTS tbl_age_group;
DROP TABLE IF EXISTS tbl_perp_race;
DROP TABLE IF EXISTS tbl_ofns_desc;