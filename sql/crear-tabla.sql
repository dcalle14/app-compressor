CREATE TABLE palabras_comprimidas (
    id SERIAL PRIMARY KEY,
    palabra_original VARCHAR(255) NOT NULL,
    palabra_comprimida VARCHAR(255) NOT NULL
);