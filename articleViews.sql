-- Write your MySQL query statement below
SELECT
    v.author_id as id
FROM
    Views v
WHERE
    v.author_id = v.viewer_id
GROUP BY 
    v.author_id
ORDER BY
    id
