# Write your MySQL query statement below
Select name
From Customer
Where (referee_id Is null) or referee_id != "2"