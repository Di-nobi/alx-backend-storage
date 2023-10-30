-- Calculates the average weighted score for a user by summing up the products of the score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER ##
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE cal_avg INT;
    UPDATE users SET cal_avg = (SELECT SUM(score * weight) / SUM(weight) 
    FROM corrections INNER JOIN projects
    ON projects.id = corrections.projects_id 
    WHERE corrections.user_id = user_id) WHERE users.id = user_id 

END
##