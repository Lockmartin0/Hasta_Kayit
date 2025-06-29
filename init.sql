CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad VARCHAR(255),
    soyad VARCHAR(255),
    tc_kimlik_no VARCHAR(11),
    telefon VARCHAR(20),
    bolum VARCHAR(100),
    sikayet TEXT
);
