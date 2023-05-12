INSERT INTO pizza_tags (name) VALUES('Vegeterian');
INSERT INTO pizza_tags (name) VALUES('Spicy');

INSERT INTO pizza_foodgroup (name) VALUES ('Cheeses');
INSERT INTO pizza_foodgroup (name) VALUES ('Sauces and spices');
INSERT INTO pizza_foodgroup (name) VALUES ('Vegetables');
INSERT INTO pizza_foodgroup (name) VALUES ('Meats');

INSERT INTO pizza_topping (name, price) VALUES('Ham', 299);
INSERT INTO pizza_topping (name, price) VALUES('Pepperoni', 299);
INSERT INTO pizza_topping (name, price) VALUES('Cheese', 299);
INSERT INTO pizza_topping (name, price) VALUES('Mushroom', 299);
INSERT INTO pizza_topping (name, price) VALUES('Bell Pepper', 299);
INSERT INTO pizza_topping (name, price) VALUES('Chilli Flakes', 99);
INSERT INTO pizza_topping (name, price) VALUES('Pepper Cheese', 299);
INSERT INTO pizza_topping (name, price) VALUES('Clay', 0);

INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(4, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(5, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(6, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(6, 2);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(8, 2);

INSERT INTO pizza_product (name, description, pic, pricesmall, pricemedium, pricelarge) VALUES('Margharita', 'The classic pizza', 'https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?s=612x612&w=0&k=20&c=CFDDjavIC5l8Zska16UZRZDXDwd47fwmRsUNzY0Ym6o=', 1800, 1900, 2000);
INSERT INTO pizza_product (name, description, pic, pricesmall, pricemedium, pricelarge) VALUES('Clayo', 'The BEST pizza', 'https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?s=612x612&w=0&k=20&c=CFDDjavIC5l8Zska16UZRZDXDwd47fwmRsUNzY0Ym6o=', 1800, 1900, 2000);
INSERT INTO pizza_product (name, description, pic, pricesmall, pricemedium, pricelarge) VALUES('Spicy Veg', 'Avant Garde', 'https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?s=612x612&w=0&k=20&c=CFDDjavIC5l8Zska16UZRZDXDwd47fwmRsUNzY0Ym6o=', 1800, 1900, 2000);

INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(3, 1);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(8, 2);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(6, 3);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(5, 3);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(4, 3);

INSERT INTO pizza_offer (name, description, price, pic) VALUES('Two for One', 'An exclusive deal where you get to buy two pizzas for the price of one!', 2000, 'https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?s=612x612&w=0&k=20&c=CFDDjavIC5l8Zska16UZRZDXDwd47fwmRsUNzY0Ym6o=');
INSERT INTO pizza_offer (name, description, price, pic) VALUES('Hottest Pizzas', 'Buy the most popular pizzas at a discount', 1500, 'https://media.istockphoto.com/id/1280329631/photo/italian-pizza-margherita-with-tomatoes-and-mozzarella-cheese-on-wooden-cutting-board-close-up.jpg?s=612x612&w=0&k=20&c=CFDDjavIC5l8Zska16UZRZDXDwd47fwmRsUNzY0Ym6o=');

INSERT INTO pizza_includes ("OID_id", "PID_id") VALUES(2, 2)

-- Updating stuff

UPDATE pizza_topping SET foodgroup_id = 4 WHERE id = 1;
UPDATE pizza_topping SET foodgroup_id = 4 WHERE id = 2;
UPDATE pizza_topping SET foodgroup_id = 1 WHERE id = 3;
UPDATE pizza_topping SET foodgroup_id = 3 WHERE id = 4;
UPDATE pizza_topping SET foodgroup_id = 3 WHERE id = 5;
UPDATE pizza_topping SET foodgroup_id = 2 WHERE id = 6;
UPDATE pizza_topping SET foodgroup_id = 1 WHERE id = 7;
UPDATE pizza_topping SET foodgroup_id = 2 WHERE id = 8;

INSERT INTO pizza_topping (name, price, foodgroup_id) VALUES('Pizza Sauce', 0, 2);

INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(10, 1); --Should be 9, but i fucked up some stuff so dw about itttttttttttttttt
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(10, 3);

UPDATE pizza_product SET pricesmall = 2000, pricemedium = 2200, pricelarge = 2400 WHERE id = 3;

INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(3, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(10, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(7, 1);

UPDATE pizza_product SET pricesmall = 1900, pricemedium = 2000, pricelarge = 2200, name='Hawaiian', pic='https://st2.depositphotos.com/1699440/8512/i/600/depositphotos_85123738-stock-photo-hawaiian-pizza.jpg' WHERE id = 2;
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(10, 2);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(3, 2);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(1, 2);

DELETE FROM pizza_hasp WHERE id=2;
DELETE FROM pizza_hast WHERE id=5;
DELETE FROM pizza_topping WHERE id=8;

INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Pineapple', 299, 3);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(11, 2);

INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Bacon Bits', 299, 4);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Salami', 299, 4);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Cream Cheese', 299, 1);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Chili Mayo', 299, 2);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Barbecue', 299, 2);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Black Pepper', 99, 2);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Onion', 299, 3);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Spinach', 299, 3);
INSERT INTO pizza_topping (name, price, "FID_id") VALUES('Dates', 299, 3);

INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(15, 2);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(18, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(19, 1);
INSERT INTO pizza_hast ("TID_id", "TGID_id") VALUES(20, 1);

INSERT INTO pizza_product (name, description, pic, pricesmall, pricemedium, pricelarge) VALUES('Meat Lovers', 'The pizza for the carnivores', 'https://www.perfectitaliano.com.au/content/dam/perfectitaliano-aus/recipe/0_desktop/Desktop-MeatLovers-Pizza.jpg', 2200, 2400, 2600);

INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(12, 4);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(1, 4);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(2, 4);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(3, 4);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(17, 4);
INSERT INTO pizza_hasp ("TID_id", "PID_id") VALUES(10, 4);

UPDATE pizza_product SET pic='https://st2.depositphotos.com/1699440/8512/i/600/depositphotos_85123738-stock-photo-hawaiian-pizza.jpg' WHERE id = 2;
UPDATE pizza_product SET pic='https://cdn.shopify.com/s/files/1/0300/0985/2037/articles/Vegan_BBQ_Tofu_Pizza_600x.jpg?v=1605270116' WHERE id = 3;
