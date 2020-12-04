-- Creates a function SafeDiv that divides and returns the first
-- by the second number or returns 0 if the second number == 0

DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS INT
BEGIN
    IF b=0 THEN
        RETURN 0;
    ELSE
        RETURN a DIV b;
    END IF;
END//
DELIMITER ;
