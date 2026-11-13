WITH price_history AS (
    SELECT
        date,
        close,
        LAG(close) OVER (ORDER BY date) AS previous_close
    FROM prices
)

SELECT
    date,
    close,
    previous_close,
    (close / previous_close) - 1 AS daily_return
FROM price_history
ORDER BY date;