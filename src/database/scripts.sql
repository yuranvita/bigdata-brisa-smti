CREATE TABLE vac (
	comunidade VARCHAR(44),
	idade INT,
	data DATE,
	sexo CHAR(1),
	qtd INT
),
CREATE TABLE queimadas (
	data DATE,
	satelite VARCHAR(50),
	pais VARCHAR(20),
	estado VARCHAR(20),
	municipio VARCHAR(20),
	bioma VARCHAR(20),
	diassemchuva INT,
	precipitacao FLOAT,
	riscofogo INT,
	latitude VARCHAR(30),
	longitude VARCHAR(30),
	frp INT
),
CREATE TABLE pecuaria (
	animal VARCHAR(55),
	ano INT,
	municipio VARCHAR(55),
	qtd INT
),
CREATE TABLE umidade_ar (
	data DATE,
	dias_precipitacao_fluvial INT,
	t_max FLOAT,
	t_min FLOAT,
	umi_relativa_p FLOAT,
	velo_vento_m_s FLOAT,
	velo_vento_media_mes_m_s FLOAT,
	latitude VARCHAR(30),
	longitude VARCHAR(30),
	municipio VARCHAR(55)

)