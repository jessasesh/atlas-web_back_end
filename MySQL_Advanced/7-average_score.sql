-- Create stored procedure to compute and store
-- the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN userID INT
)
BEGIN
    DECLARE avgScore DECIMAL(5,2);
    SELECT AVG(score) INTO avgScore
    FROM corrections
    WHERE user_id = userID;

    UPDATE users
    SET average_score = avgScore
    WHERE id = userID;
END$$

DELIMITER ;
