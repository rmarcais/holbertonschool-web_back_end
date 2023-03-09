-- Script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and stores the average weighted score for student.
-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    SET @weighted_score = (SELECT (SUM(corrections.score * projects.weight) / SUM(projects.weight))
    FROM corrections INNER JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id);
    UPDATE users
    SET average_score = @weighted_score
    WHERE id = user_id;
END;//

DELIMITER ;
