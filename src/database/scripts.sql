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
	latitude FLOAT,
	longitude FLOAT,
	frp INT
)