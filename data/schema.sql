CREATE TABLE meals
(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE,
    healthScore INTEGER NOT NULL,
    ketoPotential BOOLEAN NOT NULL,
    gfPotential BOOLEAN NOT NULL
);


INSERT INTO meals (name, healthScore, ketoPotential, gfPotential)
VALUES
('Chinese Tofu', 3, 0, 1),
('Bosh Chili', 5, 1, 1),
('Cacio y pepe', 1, 0, 1),
('Lentil Lasagna', 3, 0, 1),
('Halloumi and Chickpea with roasted vegetables', 4, 1, 1);

select * from meals