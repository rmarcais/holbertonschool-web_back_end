-- Script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for student.
-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT (SUM(corrections.score * projects.weight) / SUM(projects.weight))
    FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END;//

DELIMITER ;
