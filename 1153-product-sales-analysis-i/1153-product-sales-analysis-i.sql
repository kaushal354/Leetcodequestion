# Write your MySQL query statement below
select pr.product_name, s.year, s.price from Sales as s
inner join Product pr on s.product_id = pr.product_id;