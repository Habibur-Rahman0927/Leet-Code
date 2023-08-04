CREATE FUNCTION getNthHighestSalary
(
    N INT
)
RETURNS INT

BEGIN
    RETURN
    (
        SELECT DISTINCT
               (Salary) AS getNthHighestSalary
        FROM Employee e1
        WHERE N - 1 =
        (
            SELECT COUNT(DISTINCT salary)
            FROM employee e2
            WHERE e2.salary > e1.salary
        )
    );
END
