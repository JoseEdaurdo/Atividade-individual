CREATE TABLE cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT
);

CREATE TABLE sessao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data_sessao DATE NOT NULL,
    tipo_sessao TEXT NOT NULL,
    local TEXT NOT NULL,
    status TEXT,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id) ON DELETE CASCADE
);
