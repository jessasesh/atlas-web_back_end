-- Create stored procedure to add new correction for a student
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN userID INT, 
    IN projectName VARCHAR(255), 
    IN correctionScore INT
)
BEGIN
    DECLARE projectID INT;
    SELECT id INTO projectID
    FROM projects
    WHERE name = projectName
    LIMIT 1;

    IF projectID IS NULL THEN
        INSERT INTO projects (name) 
        VALUES (projectName);
        SET projectID = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (userID, projectID, correctionScore);
END$$

DELIMITER ;
