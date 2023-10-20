-- Esta listo, solo para ser ejecutado el script
USE monse;
-- Agregamos primero las llaves primarias de las diferentes entidades
ALTER TABLE tbl_pd_desc ADD PRIMARY KEY (PD_CD);
ALTER TABLE tbl_law_code ADD PRIMARY KEY (id_LAW_CODE);
ALTER TABLE tbl_age_group ADD PRIMARY KEY (id_AGE_GROUP);
ALTER TABLE tbl_perp_race ADD PRIMARY KEY (id_PERP_RACE);
ALTER TABLE tbl_ofns_desc ADD PRIMARY KEY (id_OFNS_DESC);

-- Agregamos las llaves foraneas en la tabla principal
ALTER TABLE tbl_principal ADD CONSTRAINT fk_pd_desc FOREIGN KEY (PD_CD) REFERENCES tbl_pd_desc (PD_CD);
ALTER TABLE tbl_principal ADD CONSTRAINT fk_law_code FOREIGN KEY (id_LAW_CODE) REFERENCES tbl_law_code (id_LAW_CODE);
ALTER TABLE tbl_principal ADD CONSTRAINT fk_age_group FOREIGN KEY (id_AGE_GROUP) REFERENCES tbl_age_group (id_AGE_GROUP);
ALTER TABLE tbl_principal ADD CONSTRAINT fk_perp_race FOREIGN KEY (id_PERP_RACE) REFERENCES tbl_perp_race (id_PERP_RACE);
ALTER TABLE tbl_principal ADD CONSTRAINT fk_ofns_desc FOREIGN KEY (id_OFNS_DESC) REFERENCES tbl_ofns_desc (id_OFNS_DESC);

-- Para finalizar todas las tablas
Select * from tbl_pd_desc;
select * from tbl_law_code;
select * from tbl_age_group;
select * from tbl_perp_race;
select * from tbl_ofns_desc;
Select * from tbl_principal;