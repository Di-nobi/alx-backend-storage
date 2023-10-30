-- Calculates the average weighted score for a user by summing up the products of the score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE cal_avg FLOAT;
     SET cal_avg= (SELECT 
    SUM(score * weight) / SUM(weight) 
    FROM users
    JOIN corrections ON users.id = corrections.user_id
    JOIN projects ON corrections.project_id = projects.id
    WHERE users.id = user_id);
    UPDATE users SET average_score = cal_avg WHERE id=user_id;
END$$
DELIMITER ;