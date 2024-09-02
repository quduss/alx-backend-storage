-- creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER //

CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)

BEGIN
  -- Find the project ID based on the project_name
  DECLARE project_id INT DEFAULT NULL;
  SELECT id INTO project_id FROM projects WHERE name = project_name;

  -- Insert project if it doesn't exist
  IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- Insert correction with the retrieved or created project ID
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, project_id, score);

END //

DELIMITER ;
