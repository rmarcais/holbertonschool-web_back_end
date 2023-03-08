-- Script that creates a stored procedure AddBonus
-- that adds a new correction for a student
-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    SET @existing_project = (SELECT EXISTS(SELECT id FROM projects WHERE name = project_name));
    IF @existing_project = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
    ELSE
        SET @project_id = (SELECT id FROM projects WHERE name = project_name);
    END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END;//

DELIMITER ;
