SELECT * FROM pizza_types;

ALTER TABLE pizza_types
ALTER COLUMN pizza_type_id VARCHAR(30) NOT NULL;
ALTER TABLE pizza_types
ALTER COLUMN name VARCHAR(50);
ALTER TABLE pizza_types
ALTER COLUMN category VARCHAR(30);
ALTER TABLE pizza_types
ALTER COLUMN ingredients VARCHAR(100);
ALTER TABLE pizza_types
ADD CONSTRAINT pk_pizza_type_id PRIMARY KEY (pizza_type_id);


SELECT * FROM pizzas;

ALTER TABLE pizzas
ALTER COLUMN pizza_id VARCHAR(30) NOT NULL;
ALTER TABLE pizzas
ALTER COLUMN pizza_type_id VARCHAR(30);
ALTER TABLE pizzas
ALTER COLUMN size VARCHAR(3);
ALTER TABLE pizzas
ALTER COLUMN price DECIMAL(6,2);
ALTER TABLE pizzas
ADD CONSTRAINT pk_pizza_id PRIMARY KEY (pizza_id);
ALTER TABLE pizzas
add CONSTRAINT fk_pizza_type_id FOREIGN KEY(pizza_type_id) REFERENCES pizza_types(pizza_type_id);

SELECT TOP 100 * FROM orders;

ALTER TABLE orders
ALTER COLUMN order_id INT NOT NULL;
ALTER TABLE orders
ALTER COLUMN date DATE;
ALTER TABLE orders
ALTER COLUMN time TIME;
alter TABLE orders
ADD CONSTRAINT pk_order_id PRIMARY KEY (order_id);



SELECT TOP 100 * FROM order_details;

ALTER TABLE order_details
ALTER COLUMN order_details_id INT NOT NULL;
ALTER TABLE order_details
ALTER COLUMN order_id INT NOT NULL;
ALTER TABLE order_details
ALTER COLUMN pizza_id VARCHAR(30);
ALTER TABLE order_details
ALTER COLUMN quantity INT;
ALTER TABLE order_details
ADD CONSTRAINT pk_order_details_id PRIMARY KEY (order_details_id);
ALTER TABLE order_details
ADD CONSTRAINT fk_order_id FOREIGN KEY(order_id) REFERENCES orders(order_id);
ALTER TABLE order_details
ADD CONSTRAINT fk_pizza_id FOREIGN KEY(pizza_id) REFERENCES pizzas(pizza_id);

