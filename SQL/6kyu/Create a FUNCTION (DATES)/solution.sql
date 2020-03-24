CREATE FUNCTION agecalculator (date DATE)
RETURNS integer AS $$
  BEGIN
    RETURN (SELECT EXTRACT(year FROM age(date)))::int;
  END;
$$ LANGUAGE plpgsql;