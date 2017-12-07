Create table If Not Exists Customers (Id int, Name varchar(255));
Create table If Not Exists Orders (Id int, CustomerId int);
Truncate table Customers;
insert into Customers (Id, Name) values ('1', 'Joe');
insert into Customers (Id, Name) values ('2', 'Henry');
insert into Customers (Id, Name) values ('3', 'Sam');
insert into Customers (Id, Name) values ('4', 'Max');
Truncate table Orders;
insert into Orders (Id, CustomerId) values ('1', '3');
insert into Orders (Id, CustomerId) values ('2', '1');

-------------------------------------------------------
# One solution

SELECT Name as Customers
  FROM Customers 
  LEFT JOIN Orders
  ON Customers.Id = Orders.CustomerId
  WHERE CustomerId IS NULL;


---------------------------------------------------\
# Better solution

SELECT Name
  FROM Customers
  WHERE Customers.Id NOT IN 
  (
  	SELECT CustomerId FROM Orders
  );