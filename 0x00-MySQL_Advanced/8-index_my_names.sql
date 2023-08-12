-- A script that creates an index on the table and the first letter of the table
CREATE INDEX idx_name_first ON names(name(1));