-- Calculates the average weighted score for a user by summing up the products of the score

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER ##
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(C.score * C.weight) / SUM(C.weight)
        FROM corrections AS C
        JOIN projects AS P ON C.project_id = P.id
        WHERE C.user_id = user_id
    )
    WHERE id = user_id;
END
##