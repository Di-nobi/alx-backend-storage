-- A SQL script that decreases the quantity of an item after adding a new order
CREATE TRIGGER d_quantity BEFORE INSERT ON orders
FOR EACH ROW UPDATE items 
SET quantity = quantity - NEW.number
where name = NEW.item_name;