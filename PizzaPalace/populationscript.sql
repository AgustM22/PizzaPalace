INSERT INTO pizza_tags (name) VALUES('Vegeterian');
INSERT INTO pizza_tags (name) VALUES('Spicy');

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