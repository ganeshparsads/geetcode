# Write your MySQL query statement below
select Signups.user_id, COALESCE(
    ROUND(
        (
            sum(
                case when action = 'confirmed' then 1 else 0 end) / count(Confirmations.user_id)),
        2), 0) as confirmation_rate
from Signups
left join Confirmations on
Signups.user_id = Confirmations.user_id
group by Signups.user_id;