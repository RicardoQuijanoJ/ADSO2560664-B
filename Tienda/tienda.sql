create table Usuario(
idUsuario INTEGER PRIMARY KEY not null,
idRol INTEGER NOT NULL,
usuNombre VARCHAR (100),
usuTipoDocumento VARCHAR (20),
usuNumDocumento VARCHAR (20),
usuDireccion VARCHAR (20),
usuTelefono VARCHAR (20),
usuEmail VARCHAR (50),
usuClave VARCHAR (100),
usuEstado bit
);

create table Venta(
idVenta INTEGER PRIMARY KEY not null,
idCliente INTEGER NOT NULL,
idUsuario INTEGER NOT NULL,
venTipoComprobante VARCHAR (20),
venSerieComprobante VARCHAR (10),
venNumComprobante INTEGER,
venFecha DATETIME
);

create table Rol(
idRol INTEGER PRIMARY KEY not null,
rolNombre VARCHAR (30),
rolDescripcion VARCHAR (255),
rolEstado bit
);

create table Cliente(
idCliente INTEGER PRIMARY KEY not null,
cliNombre VARCHAR (100),
cliTipoDocumento VARCHAR (20),
cliNumDocumento VARCHAR (20),
cliDireccion VARCHAR (20),
cliTelefono VARCHAR (20),
cliEmail VARCHAR (20)
);

Alter table Venta add Column venImpuesto DECIMAL (4,2)
Alter table Venta add add Column venTotal DECIMAL (11,2)
Alter table Venta add add Column venEstado VARCHAR (20)
Alter table Venta add add Constraint FOREIGN KEY (idCliente) REFERENCES Cliente (idCliente)
Alter table Venta add add Constraint FOREIGN KEY (idUsuario) REFERENCES Usuario (idUsuario)

Alter table Usuario add Constraint FOREIGN KEY (idRol) REFERENCES Rol (idRol)

INSERT INTO Rol VALUES (1, "Administrador", "Gerente de la compañia", 1);
INSERT INTO Rol VALUES (2, "Empleado", "Emplead@: Mañana", 1);
INSERT INTO Rol VALUES (3, "Empleado", "Emplead@: Tarde", 1);
INSERT INTO Rol VALUES (4, "Cliente", "Diferente de la compañia", 1);

UPDATE Rol SET rolNombre = "Empleado" WHERE idRol = 4
UPDATE Rol SET rolDescripcion = "Emplead@: Fin Semana" WHERE idRol = 4

INSERT INTO Usuario VALUES (1000, 2, "Ricardo", "Cédula Ciudadania", "1090510168", "cll 2 # 5-68", "330023433", "ricardo@gmail.com", "xcfdsafi343.", 1);
INSERT INTO Usuario VALUES (1001, 3, "Andrea", "Cédula Ciudadania", "2354687", "cll 4 # 6-54", "3006507274", "andrea@gmail.com", "123dfadsraf,,", 1);
INSERT INTO Usuario VALUES (1002, 1, "Marcela", "Cédula Ciudadania", "133434687", "cra 10 # 6-54", "3002504578", "marcela@gmail.com", "facil,,", 1);
INSERT INTO Usuario VALUES (1003, 1, "Juan", "Cédula Ciudadania", "1002354687", "av boyaca # 45-56", "3002651041", "juan@gmail.com", "123dfhghdgfht", 1);
INSERT INTO Usuario VALUES (1004, 4, "Pablo", "Cédula Ciudadania", "1889687", "cll 22 # 66-84", "3006532234", "pablo@gmail.com", "123dfdsafdfadsraf,,", 1);

UPDATE Usuario SET idRol = 1 WHERE usuNombre = "Ricardo" AND usuNumDocumento = "1090510168"
UPDATE Usuario SET idRol = 2 WHERE usuNombre = "Marcela" OR usuNombre = "Juan"

INSERT INTO Cliente VALUES (001, "Pepito Perez", "Cédula Extranjeria", "4876350", "cll sin datos", "601-2343212", "pepito@gmail.com");
INSERT INTO Cliente VALUES (002, "Pablo Constantine", "Cédula Ciudadania", "1002236350", "cll sin datos", "No hay", "pablo@gmail.com");
INSERT INTO Cliente VALUES (003, "Marly Castaño", "Pasaporte", "dfa-12165102", "cll sin datos", " ", "marlycastaño@gmail.com");
INSERT INTO Cliente VALUES (004, "Diana Maria", "Cédula Ciudadania", "1081951025", "cll 5 # 102-34", "3205468799", "diana@gmail.com");

INSERT INTO Venta VALUES (1000, 1090523397, 1, "Ingreso", "ING-001", 12, "2023/03/15", 3.4, 12345,45, "Pagado");
INSERT INTO Venta VALUES (1001, 1090523397, 1, "Egreso", "EGRE-001", 20, "2023/03/16", 4.4, 110000, "en proceso");
INSERT INTO Venta VALUES (1002, 1090542341, 2, "Ingreso", "ING-002", 13, "2023/03/11", 3.4, 200000, "Pagado");
INSERT INTO Venta VALUES (1003, 23445566, 3, "Cheque", "CHE-001", 70, "2023/03/12", 5, 300000, "En proceso");
INSERT INTO Venta VALUES (1004, 88271954, 4, "Ingreso", "ING-003", 14, "2023/03/11", 2, 111000, "Por pagar");
