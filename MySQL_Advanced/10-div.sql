-- Create a function SafeDiv to divide two numbers or return 0 if the second number is 0

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    -- Check if the second argument (b) is zero
    IF b = 0 THEN
        -- Return 0 if b is zero
        RETURN 0;
    ELSE
        -- Return the result of a divided by b
        RETURN a / b;
    END IF;
END$$

DELIMITER ;
