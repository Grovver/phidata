SELECT year, month, EzorLahatz, Phat_Clali_Miztaber AS Phat_Clali, SUM(SUM_AhuzPhatClali) AS SUM_AhuzPhatClali
FROM MaazanCalcTable
WHERE Merhav='0003' AND EzorLahatz IS NOT NULL
GROUP BY year, month, EzorLahatz, Phat_Clali
LIMIT 20;