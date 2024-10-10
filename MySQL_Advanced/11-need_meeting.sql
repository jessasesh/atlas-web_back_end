-- Create a view to list students with score under 80
-- and no recent meeting
DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 30 DAY));
