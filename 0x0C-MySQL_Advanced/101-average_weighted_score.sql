-- Script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and stores the average weighted score for all student.
-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE finished INT DEFAULT 0;
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    OPEN user_cursor;

    user_loop: LOOP
        IF finished = 1 THEN
            LEAVE user_loop;
        END IF;

        FETCH user_cursor INTO user_id;

        SET @average_score = (SELECT (SUM(corrections.score * projects.weight) / SUM(projects.weight))
        FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id);

        UPDATE users SET average_score = @average_score WHERE id = user_id;

    END LOOP;

    CLOSE user_cursor;
END;//

DELIMITER ;
