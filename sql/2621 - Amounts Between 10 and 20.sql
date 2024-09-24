SELECT products.name
FROM products
INNER JOIN providers
ON providers.id = products.id_providers
WHERE products.amount between 10 AND 20 AND providers.name like 'P%'
