SELECT c.name
FROM customers AS c
INNER JOIN legal_person as l
ON c.id = l.id_customers

